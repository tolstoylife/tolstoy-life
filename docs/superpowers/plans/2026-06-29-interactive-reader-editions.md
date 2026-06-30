# Interactive Reader's Editions — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

> **Superseded paths (2026-06-30):** the go-forward workflow moved the outputs into a self-contained per-work bundle. Source markdown now lives in `docs/reader/<cat>/<subcat>/<id>/` (not `docs/research/<slug>/reader/`); the regenerable artifacts — `segments.json`, `timing.json`, audio, `.epub` — live in that bundle's gitignored `build/` (not `_generated/reader/<work>/`). The machinery below is unchanged and green (32 tests pass); only the file destinations moved, and the audiobook build now derives its output dir from the segments-file path. See the wrapping workflow in [`2026-06-30-interactive-reader-editions-workflow-design.md`](../specs/2026-06-30-interactive-reader-editions-workflow-design.md) — the source of truth for where files live and how the loop runs.

**Goal:** From one marked-up Markdown source per version of *The Great Sin*, produce all three reader formats — the interactive web edition (serve.py), a read-along EPUB3 that highlights as it reads in Apple Books, and the synced audiobook — proving a repeatable pipeline end-to-end on Chapter I.

**Architecture:** One **segmenter** reads each version's Markdown and writes `segments.json` (per sentence: stable ID, display text, speech text). That one file is the shared contract: the **audiobook build** reads it and emits `timing.json` (segment → start/end); the **EPUB builder** reads `segments.json` + `timing.json` to write XHTML + a hand-built SMIL media overlay and packages with ebooklib; **serve.py** keeps rendering the Markdown but re-anchors annotations to the same paragraph IDs. Everything keys to a two-layer ID scheme (paragraph = public citable coordinate; sentence = read-along plumbing).

**Tech Stack:** Python 3.12 · python-markdown + pymdownx (already used by serve.py) · ebooklib 0.20 (already installed) · pytest 9 · ffmpeg/ffprobe + kokoro-tts-tool (audio, existing) · EPUBCheck + ACE by DAISY (external validation gates).

## Global Constraints

Every task's requirements implicitly include this section. Values are copied verbatim from `docs/research/_interactive-edition-all-formats-spec.md`.

- **No new Python dependencies.** Use stdlib, `markdown`/`pymdownx` (serve.py already imports them), `ebooklib` (installed), `pytest` (installed). EPUBCheck and ACE are external CLI tools — gate on them but **skip-with-warning if not installed** (do not hard-fail the build for a missing validator).
- **New pipeline code lives in `reader/`** at the repo root — NOT in `tools/` (that is the `tl` Standard Ebooks fork) and NOT in `docs/` (serve.py's home). Tests in `reader/tests/`.
- **Two-layer IDs:** paragraph `p-{section}-{n}` (e.g. `p-1-12`) is the public, citable coordinate; sentence `p-{section}-{n}-s{k}` (e.g. `p-1-12-s2`) is read-along plumbing only. Headings use the section anchor `sec-{n}`. Typed counters per element (`fig-`, `tbl-`, `bq-`, `li-`, `note-`) each scoped to the section.
- **Number by element type, not flow position.** Each block type has its own per-section counter.
- **Never renumber after publishing.** Split → append (`p-1-12a`/`p-1-12b`); never shift later numbers.
- **The spine (Russian PSS) defines the coordinate.** Process `the-great-sin.ru.md` first; each translation maps onto the spine's paragraph IDs. For this proof, translations are assumed paragraph-parallel to the spine and **validated** (a paragraph-count mismatch per section is a hard error, not a silent mis-alignment).
- **epub = resolved/static, web = interactive.** No JavaScript inside the EPUB. CriticMarkup in the EPUB renders resolved (insertions kept, deletions removed/endnoted, changes → new word); live toggles stay on the website only.
- **Read-along = sentence-level.** SMIL hand-built; ebooklib packages only.
- **Accessibility = WCAG 2.1 AA.** EPUB Accessibility 1.1 metadata + ACE gate; web inherits pa11y-ci (new interactive parts deferred to spec 2).
- **Fidelity:** `primary-sources/**` and `docs/research/1905-the-great-sin/extracts/**` are untouched. The Russian reading text with marks stripped must match the source extract exactly; `verify_quotes.py` gates every locked quote.
- **Outputs:** source Markdown → `docs/research/1905-the-great-sin/reader/`; generated artifacts (`segments.json`, `timing.json`, audio, `.epub`) → `_generated/reader/the-great-sin/` (audio gitignored).
- **Working style:** plain language in all docs/commit messages (no engineering jargon). Commit freely as tasks land; **never `git push`** — provide push commands instead. Branch is `docs/research-index`.

---

## File map

| Path | Responsibility | Phase |
|---|---|---|
| `reader/ids.py` | The one ID-numbering rule, shared by segmenter + serve.py | 0 |
| `reader/speech.py` | Display-text → speech-text transform (ported flow_preprocess + SUBS) | 1 |
| `reader/segment.py` | Markdown → `segments.json` (the contract) | 1 |
| `reader/build_xhtml.py` | `segments.json` (+ Markdown notes) → EPUB XHTML with typed-ID sentence spans | 3 |
| `reader/build_epub.py` | XHTML + `timing.json` → SMIL + packaged `.epub` (ebooklib) | 4 |
| `reader/validate.py` | EPUBCheck + ACE subprocess gates (skip-with-warn) | 4 |
| `reader/tests/*.py` | pytest for the above | 0–4 |
| `projects/audiobook/build_audiobook.py` | Rewired: reads `segments.json`, emits `timing.json` + per-section audio | 2 |
| `projects/audiobook/test_timeline.py` | pytest for the timing math (no synthesis) | 2 |
| `docs/serve.py` | Annotation rework: paragraph-ID anchoring + import; `<p>` gets IDs | 5 |
| `docs/research/1905-the-great-sin/reader/*.md` | The authored source (human-present) | 6 |
| `_generated/reader/the-great-sin/` | Generated artifacts | 2,4,7 |

**The `segments.json` schema** (one file per version; the keystone contract):

```json
{
  "work": "the-great-sin",
  "version": "en-1905",
  "spine": "ru",
  "sections": [
    {
      "id": "sec-1",
      "heading": "Part I",
      "headingSpeech": "Part One.",
      "paragraphs": [
        {
          "id": "p-1-1",
          "pss": "36:206",
          "sentences": [
            {"id": "p-1-1-s1", "display": "The other day I was walking along the high road to Tula.", "speech": "The other day I was walking along the high road to Tula."},
            {"id": "p-1-1-s2", "display": "It was on the Saturday of Holy Week.", "speech": "It was on the Saturday of Holy Week."}
          ]
        }
      ]
    }
  ],
  "notes": [
    {"id": "note-1", "label": "1", "html": "Henry Labouchère, the radical MP."}
  ]
}
```

- `pss` is optional (a PSS vol:page boundary that *opens* in this paragraph; from the dossier/extracts). Omitted when none.
- `display` keeps inline footnote markers `[^1]`; `speech` strips them (notes are skippable in audio).
- `headingSpeech` is what the audiobook speaks at the section start ("Part One." not "Part I").

**The `timing.json` schema** (emitted by the audio build, one per version, times in seconds **relative to that section's audio file**):

```json
{
  "audio": {"sec-1": "the-great-sin.sec-1.m4a"},
  "clips": {
    "sec-1":      {"section": "sec-1", "begin": 0.0,  "end": 1.10},
    "p-1-1-s1":   {"section": "sec-1", "begin": 1.55, "end": 4.97},
    "p-1-1-s2":   {"section": "sec-1", "begin": 5.42, "end": 7.10}
  }
}
```

---

## Phase 0 — Shared ID rule + fixtures

### Task 0: The ID-numbering rule (`reader/ids.py`)

The single source of truth for how paragraph/sentence/heading IDs are formed. Both the segmenter and serve.py import this so they can never drift.

**Files:**
- Create: `reader/__init__.py` (empty)
- Create: `reader/ids.py`
- Create: `reader/tests/__init__.py` (empty)
- Test: `reader/tests/test_ids.py`

**Interfaces:**
- Produces:
  - `section_id(n: int) -> str` → `"sec-1"`
  - `paragraph_id(section: int, n: int) -> str` → `"p-1-12"`
  - `sentence_id(paragraph_id: str, k: int) -> str` → `"p-1-12-s2"`
  - `typed_id(prefix: str, section: int, n: int) -> str` → `typed_id("fig", 4, 1) == "fig-4-1"`
  - `note_id(n: int) -> str` → `"note-1"`; `noteref_id(n: int) -> str` → `"noteref-1"`

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_ids.py
from reader import ids

def test_id_shapes():
    assert ids.section_id(1) == "sec-1"
    assert ids.paragraph_id(1, 12) == "p-1-12"
    assert ids.sentence_id("p-1-12", 2) == "p-1-12-s2"
    assert ids.typed_id("fig", 4, 1) == "fig-4-1"
    assert ids.typed_id("bq", 4, 2) == "bq-4-2"
    assert ids.note_id(1) == "note-1"
    assert ids.noteref_id(1) == "noteref-1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_ids.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'reader.ids'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/ids.py
"""The one ID-numbering rule, shared by the segmenter and serve.py so they never drift.
Spec: paragraph p-{section}-{n} is the public citable coordinate; sentence
p-{section}-{n}-s{k} is read-along plumbing; typed counters are per-section."""

def section_id(n): return f"sec-{n}"
def paragraph_id(section, n): return f"p-{section}-{n}"
def sentence_id(paragraph_id, k): return f"{paragraph_id}-s{k}"
def typed_id(prefix, section, n): return f"{prefix}-{section}-{n}"
def note_id(n): return f"note-{n}"
def noteref_id(n): return f"noteref-{n}"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_ids.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/__init__.py reader/ids.py reader/tests/__init__.py reader/tests/test_ids.py
git commit -m "feat(reader): shared ID-numbering rule for reader pipeline"
```

### Task 1: Fixtures — a tiny two-version source

A small synthetic Markdown pair the machinery is built against, so Phases 1–5 don't wait on the human-present content authoring (Phase 6).

**Files:**
- Create: `reader/tests/fixtures/mini.ru.md`
- Create: `reader/tests/fixtures/mini.en-1905.md`

**Interfaces:**
- Produces: two fixture files used by later tests. One section (`## Part I`), two paragraphs; paragraph 2 carries one footnote and one CriticMarkup deletion + a `[[wikilink]]`.

- [ ] **Step 1: Write the Russian spine fixture**

```markdown
<!-- reader/tests/fixtures/mini.ru.md -->
## Часть I

Иду в вербную субботу по большой дороге в Тулу. Народ обозами едет на базар.

Сморщенная старушка ведёт корову.[^1] Я знаю {--эту--} старуху.

[^1]: Корова без молока.
```

- [ ] **Step 2: Write the English fixture (paragraph-parallel)**

```markdown
<!-- reader/tests/fixtures/mini.en-1905.md -->
## Part I

The other day I was walking along the high road to Tula. The people were driving to market.

A wrinkled old woman was leading a cow.[^1] I knew the [[old woman]].

[^1]: A cow without milk.
```

- [ ] **Step 3: Commit**

```bash
git add reader/tests/fixtures/mini.ru.md reader/tests/fixtures/mini.en-1905.md
git commit -m "test(reader): mini two-version fixture for the pipeline"
```

---

## Phase 1 — The segmenter (`segments.json`)

### Task 2: Speech transform (`reader/speech.py`)

Port the TTS-phrasing rules (currently `projects/audiobook/flow_preprocess.py`) and the pronunciation respellings (currently `build_audiobook.py` `SUBS`) into one pure function. This is what turns *display* text into *speech* text. After this, the audio repo no longer owns these rules — `segments.json` carries the final speech.

**Files:**
- Create: `reader/speech.py`
- Test: `reader/tests/test_speech.py`

**Interfaces:**
- Produces: `to_speech(text: str) -> str` — applies ellipsis/semicolon/dash flow fixes + pronunciation respellings + strips `[^n]` footnote markers.

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_speech.py
from reader.speech import to_speech

def test_semicolon_before_conjunction_becomes_comma():
    assert to_speech("pahать time; and the horse is gone") == "pahать time, and the horse is gone"

def test_bare_semicolon_becomes_full_stop():
    assert to_speech("one thing; another follows") == "one thing. Another follows"

def test_respell_known_words():
    assert "Labooshair" in to_speech("the MP Labouchere spoke")
    assert "Yasnaya Polyahna" in to_speech("near Yasnaya Poliana")

def test_strips_footnote_marker():
    assert to_speech("leading a cow.[^1] I knew her.") == "leading a cow. I knew her."

def test_ellipsis_normalised():
    assert to_speech("well... maybe") == "well… maybe"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_speech.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'reader.speech'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/speech.py
"""Display text -> speech text. Ported from projects/audiobook/flow_preprocess.py
(phrasing fixes) and build_audiobook.py SUBS (pronunciation respellings), so the
segmenter owns these rules and segments.json carries final speech text.
The display text stays faithful; we only reshape what the TTS hears."""
import re

_CONJ = r"(?:and|but|or|nor|yet|so|for)\b"

# Pronunciation respellings for Kokoro's g2p (verbatim from build_audiobook.py SUBS).
_SUBS = [
    (r"\blive\b", "liv"),
    (r"\bLabouchere\b", "Labooshair"),
    (r"\bRadischeff\b", "Rahdeeshef"),
    (r"Yasnaya Poliana", "Yasnaya Polyahna"),
    (r"\(Matt[.,] xxiii\. 27, 28\)",
     "Matthew twenty-three, verses twenty-seven and twenty-eight"),
]

def _fix_ellipsis(t):
    t = t.replace("...", "…")
    return re.sub(r"\.\s*\.\s*\.", "…", t)

def _fix_semicolons(t):
    t = re.sub(rf";\s+({_CONJ})", r", \1", t)            # "; and" -> ", and"
    return re.sub(r";\s+([a-zA-Z])", lambda m: ". " + m.group(1).upper(), t)

def _fix_dashes(t):
    t = t.replace("—", " — ")
    return re.sub(r"\s{2,}", " ", t)

def _respell(t):
    for pat, rep in _SUBS:
        t = re.sub(pat, rep, t)
    return t

def to_speech(text):
    text = re.sub(r"\[\^\w+\]", "", text)                # drop footnote markers (skippable in audio)
    text = _fix_ellipsis(text)
    text = _fix_semicolons(text)
    text = _fix_dashes(text)
    text = _respell(text)
    return text.strip()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_speech.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/speech.py reader/tests/test_speech.py
git commit -m "feat(reader): speech transform (flow + respellings) ported from audiobook"
```

### Task 3: CriticMarkup resolver + sentence splitter (`reader/segment.py`, part 1)

The two pure helpers the segmenter needs: resolve CriticMarkup/wikilinks to plain reading text, and split a paragraph into sentences (ported from `build_audiobook.py` `split_sents`, which handles decimals and quotes).

**Files:**
- Create: `reader/segment.py`
- Test: `reader/tests/test_segment_helpers.py`

**Interfaces:**
- Produces:
  - `resolve_reading_text(md: str) -> str` — `{++x++}`→x, `{--x--}`→removed, `{~~a~>b~~}`→b, `{>>n<<}`→removed, `{==x==}`→x, `[[Entity]]`→Entity; keeps `[^n]` markers.
  - `split_sentences(text: str) -> list[str]`

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_segment_helpers.py
from reader.segment import resolve_reading_text, split_sentences

def test_resolve_criticmarkup():
    assert resolve_reading_text("I knew {--this--} the woman") == "I knew the woman"
    assert resolve_reading_text("a {++very ++}old woman") == "a very old woman"
    assert resolve_reading_text("the {~~horse~>cow~~}") == "the cow"
    assert resolve_reading_text("text {>>editor cut this<<}here") == "text here"
    assert resolve_reading_text("a {==dropped==} word") == "a dropped word"

def test_resolve_keeps_wikilink_label_and_footnote():
    assert resolve_reading_text("the [[old woman]] spoke") == "the old woman spoke"
    assert resolve_reading_text("a cow.[^1] I knew her.") == "a cow.[^1] I knew her."

def test_split_sentences_basic():
    out = split_sentences("First one. Second one! Third?")
    assert out == ["First one.", "Second one!", "Third?"]

def test_split_protects_decimals():
    out = split_sentences("It cost 1.40 rubles. That is dear.")
    assert out == ["It cost 1.40 rubles.", "That is dear."]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_segment_helpers.py -v`
Expected: FAIL — `ImportError: cannot import name 'resolve_reading_text'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/segment.py
"""Markdown (one version of a work) -> segments.json (the shared contract).
Each sentence gets a stable two-layer ID, its faithful display text, and its
speech text. The spine (Russian) defines the paragraph coordinate; translations
are validated as paragraph-parallel."""
import re, json, sys, argparse
from pathlib import Path
from reader import ids
from reader.speech import to_speech

# ── CriticMarkup → reading text ────────────────────────────────────────────────
def resolve_reading_text(md):
    md = re.sub(r"\{>>.*?<<\}", "", md, flags=re.S)         # notes: drop
    md = re.sub(r"\{--(.*?)--\}", "", md, flags=re.S)       # deletions: drop
    md = re.sub(r"\{\+\+(.*?)\+\+\}", r"\1", md, flags=re.S)# insertions: keep
    md = re.sub(r"\{~~(.*?)~>(.*?)~~\}", r"\2", md, flags=re.S)  # change: keep new
    md = re.sub(r"\{==(.*?)==\}", r"\1", md, flags=re.S)    # highlight: keep
    md = re.sub(r"\[\[([^\]]+)\]\]", r"\1", md)             # wikilink: keep label
    return re.sub(r"[ \t]{2,}", " ", md).strip()

# ── Sentence split (ported from build_audiobook.split_sents) ───────────────────
def split_sentences(text):
    text = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", text)        # protect 1.40
    parts = re.split(r'(?<=[.!?"])\s+(?=["“(A-ZА-Я])', text)
    return [p.replace("<DOT>", ".").strip() for p in parts if p.strip()]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_segment_helpers.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/segment.py reader/tests/test_segment_helpers.py
git commit -m "feat(reader): CriticMarkup resolver + sentence splitter"
```

### Task 4: Markdown → sections/paragraphs/notes parser (`reader/segment.py`, part 2)

Parse the Markdown structure: split on `## ` headings into sections, blank-line into paragraphs, collect `[^n]:` note definitions. Heading-spoken form ("Part I" → "Part One.") ported from `build_audiobook.spoken_header`.

**Files:**
- Modify: `reader/segment.py`
- Test: `reader/tests/test_segment_parse.py`

**Interfaces:**
- Consumes: `resolve_reading_text`, `split_sentences` (Task 3); `ids`, `to_speech`.
- Produces:
  - `heading_speech(heading: str) -> str` → `"Part One."` for "Part I", else the heading + "."
  - `parse(md: str) -> dict` — returns `{"sections": [...], "notes": [...]}` with the `segments.json` shape minus the top-level `work`/`version`/`spine`.

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_segment_parse.py
from reader.segment import parse, heading_speech

MD = open("reader/tests/fixtures/mini.en-1905.md").read()

def test_heading_speech():
    assert heading_speech("Part I") == "Part One."
    assert heading_speech("Part IV") == "Part Four."
    assert heading_speech("Introduction") == "Introduction."

def test_parse_structure():
    doc = parse(MD)
    assert len(doc["sections"]) == 1
    sec = doc["sections"][0]
    assert sec["id"] == "sec-1"
    assert sec["heading"] == "Part I"
    assert sec["headingSpeech"] == "Part One."
    assert [p["id"] for p in sec["paragraphs"]] == ["p-1-1", "p-1-2"]

def test_parse_sentence_ids_and_text():
    sec = parse(MD)["sections"][0]
    s = sec["paragraphs"][0]["sentences"]
    assert [x["id"] for x in s] == ["p-1-1-s1", "p-1-1-s2"]
    assert s[0]["display"] == "The other day I was walking along the high road to Tula."

def test_parse_resolves_marks_in_display():
    sec = parse(MD)["sections"][0]
    p2 = sec["paragraphs"][1]["sentences"]
    # wikilink label kept, footnote marker kept in display, stripped in speech
    assert "[[old woman]]" not in p2[1]["display"]
    assert "old woman" in p2[1]["display"]
    assert "[^1]" in p2[0]["display"]
    assert "[^1]" not in p2[0]["speech"]

def test_parse_collects_notes():
    notes = parse(MD)["notes"]
    assert notes == [{"id": "note-1", "label": "1", "html": "A cow without milk."}]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_segment_parse.py -v`
Expected: FAIL — `ImportError: cannot import name 'parse'`

- [ ] **Step 3: Write minimal implementation** (append to `reader/segment.py`)

```python
# ── Heading spoken form (ported from build_audiobook.spoken_header) ────────────
_ROMAN = {"I":"One","II":"Two","III":"Three","IV":"Four","V":"Five",
          "VI":"Six","VII":"Seven","VIII":"Eight","IX":"Nine"}

def heading_speech(heading):
    m = re.match(r"Part ([IVX]+)\s*$", heading.strip())
    if m and m.group(1) in _ROMAN:
        return f"Part {_ROMAN[m.group(1)]}."
    return heading.strip().rstrip(".") + "."

# ── Structure parse ────────────────────────────────────────────────────────────
def _note_defs(md):
    """Pull '[^label]: text' definitions out; return (body_without_defs, notes)."""
    notes, n = [], 0
    def repl(m):
        nonlocal n
        n += 1
        notes.append({"id": ids.note_id(n), "label": m.group(1),
                      "html": m.group(2).strip()})
        return ""
    body = re.sub(r"^\[\^(\w+)\]:[ \t]*(.+)$", repl, md, flags=re.M)
    return body, notes

def parse(md):
    body, notes = _note_defs(md)
    # split into sections on '## ' headings; text before the first heading is ignored here
    chunks = re.split(r"^##\s+(.+)$", body, flags=re.M)
    sections = []
    # chunks = [pre, heading1, body1, heading2, body2, ...]
    sec_n = 0
    for i in range(1, len(chunks), 2):
        sec_n += 1
        heading = chunks[i].strip()
        sec = {"id": ids.section_id(sec_n), "heading": heading,
               "headingSpeech": heading_speech(heading), "paragraphs": []}
        paras = [p.strip() for p in re.split(r"\n\s*\n", chunks[i + 1]) if p.strip()]
        for pn, raw in enumerate(paras, start=1):
            pid = ids.paragraph_id(sec_n, pn)
            reading = resolve_reading_text(raw)
            sentences = []
            for sk, sent in enumerate(split_sentences(reading), start=1):
                sentences.append({"id": ids.sentence_id(pid, sk),
                                  "display": sent, "speech": to_speech(sent)})
            sec["paragraphs"].append({"id": pid, "sentences": sentences})
        sections.append(sec)
    return {"sections": sections, "notes": notes}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_segment_parse.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/segment.py reader/tests/test_segment_parse.py
git commit -m "feat(reader): parse Markdown into sections/paragraphs/sentences/notes"
```

### Task 5: Spine alignment check + CLI (`reader/segment.py`, part 3)

The top-level `segment()` that assembles the full `segments.json`, plus the cross-version guard: a translation must have the same paragraph count per section as the spine (else the IDs would mis-align). Plus a `main()` CLI.

**Files:**
- Modify: `reader/segment.py`
- Test: `reader/tests/test_segment_align.py`

**Interfaces:**
- Consumes: `parse` (Task 4).
- Produces:
  - `segment(md_path, version, work, spine="ru", spine_doc=None) -> dict` — full `segments.json` dict; if `spine_doc` is given (the parsed spine), raises `ValueError` on per-section paragraph-count mismatch.
  - `main()` — CLI: `python3 -m reader.segment <md> --version en-1905 --work the-great-sin [--spine-json path] -o out.json`

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_segment_align.py
import json, subprocess, sys
import pytest
from reader.segment import segment, parse

def test_segment_full_shape():
    doc = segment("reader/tests/fixtures/mini.en-1905.md",
                  version="en-1905", work="the-great-sin")
    assert doc["work"] == "the-great-sin"
    assert doc["version"] == "en-1905"
    assert doc["spine"] == "ru"
    assert doc["sections"][0]["paragraphs"][0]["id"] == "p-1-1"

def test_alignment_passes_when_parallel():
    spine = parse(open("reader/tests/fixtures/mini.ru.md").read())
    # should not raise — both fixtures have 1 section, 2 paragraphs
    segment("reader/tests/fixtures/mini.en-1905.md",
            version="en-1905", work="the-great-sin", spine_doc=spine)

def test_alignment_fails_on_mismatch():
    fake_spine = {"sections": [{"id": "sec-1", "paragraphs": [{"id": "p-1-1"}]}],
                  "notes": []}  # only 1 paragraph
    with pytest.raises(ValueError, match="paragraph count"):
        segment("reader/tests/fixtures/mini.en-1905.md",
                version="en-1905", work="the-great-sin", spine_doc=fake_spine)

def test_cli_writes_json(tmp_path):
    out = tmp_path / "seg.json"
    subprocess.run([sys.executable, "-m", "reader.segment",
                    "reader/tests/fixtures/mini.en-1905.md",
                    "--version", "en-1905", "--work", "the-great-sin",
                    "-o", str(out)], check=True)
    doc = json.loads(out.read_text())
    assert doc["version"] == "en-1905"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_segment_align.py -v`
Expected: FAIL — `ImportError: cannot import name 'segment'`

- [ ] **Step 3: Write minimal implementation** (append to `reader/segment.py`)

```python
def segment(md_path, version, work, spine="ru", spine_doc=None):
    doc = parse(Path(md_path).read_text(encoding="utf-8"))
    if spine_doc is not None:
        for s_sec, t_sec in zip(spine_doc["sections"], doc["sections"]):
            if len(s_sec["paragraphs"]) != len(t_sec["paragraphs"]):
                raise ValueError(
                    f"paragraph count mismatch in {t_sec['id']}: spine has "
                    f"{len(s_sec['paragraphs'])}, {version} has {len(t_sec['paragraphs'])}")
        if len(spine_doc["sections"]) != len(doc["sections"]):
            raise ValueError("section count mismatch between spine and " + version)
    return {"work": work, "version": version, "spine": spine, **doc}

def main():
    ap = argparse.ArgumentParser(description="Markdown -> segments.json")
    ap.add_argument("md")
    ap.add_argument("--version", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--spine", default="ru")
    ap.add_argument("--spine-json", help="segments.json of the spine, to align against")
    ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    spine_doc = json.loads(Path(a.spine_json).read_text()) if a.spine_json else None
    doc = segment(a.md, version=a.version, work=a.work, spine=a.spine, spine_doc=spine_doc)
    Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {a.out}: {len(doc['sections'])} sections, "
          f"{sum(len(s['paragraphs']) for s in doc['sections'])} paragraphs")

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_segment_align.py -v`
Expected: PASS

- [ ] **Step 5: Run the whole reader suite + commit**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/ -v`
Expected: all PASS

```bash
git add reader/segment.py reader/tests/test_segment_align.py
git commit -m "feat(reader): segment() with spine-alignment guard and CLI"
```

---

## Phase 2 — Audiobook rewire (`segments.json` → `timing.json`)

> **Separate git repo** (`projects/audiobook/`). The JSON files are the only cross-repo contract — no shared code. Commit in that repo, not the parent.

### Task 6: Pure timeline math (`projects/audiobook/build_audiobook.py` refactor, part 1)

Factor the cumulative-time bookkeeping into one pure function that takes a list of clips + their durations and the gap sizes, and returns `timing.json`'s `clips` map plus the concat order. This is the only logic with arithmetic worth a test; synthesis/ffmpeg stay untested I/O as before.

**Files:**
- Modify: `projects/audiobook/build_audiobook.py`
- Test: `projects/audiobook/test_timeline.py`

**Interfaces:**
- Produces:
  - `iter_clips(seg: dict) -> list[dict]` — flatten one version's `segments.json` into ordered clips: `{"id","speech","gap_after","section","is_section_start"}`. Heading first per section (`id`=`sec-N`, `speech`=`headingSpeech`); each sentence with `gap_after` = `PARA_GAP` if last in paragraph else `SENT_GAP`; `CHAP_GAP` is inserted *between* sections by the builder, not as a clip's gap.
  - `build_timeline(clips: list[dict], duration_of) -> dict` — `duration_of(clip_id) -> float` (seconds); returns `{"clips": {id: {"section","begin","end"}}}` with `begin`/`end` **relative to that clip's section audio file** (each section's audio resets to 0).

- [ ] **Step 1: Write the failing test**

```python
# projects/audiobook/test_timeline.py
from build_audiobook import iter_clips, build_timeline

SEG = {
  "version": "en-1905", "sections": [
    {"id": "sec-1", "headingSpeech": "Part One.", "paragraphs": [
      {"id": "p-1-1", "sentences": [
        {"id": "p-1-1-s1", "speech": "First."},
        {"id": "p-1-1-s2", "speech": "Second."}]}]},
    {"id": "sec-2", "headingSpeech": "Part Two.", "paragraphs": [
      {"id": "p-2-1", "sentences": [
        {"id": "p-2-1-s1", "speech": "Third."}]}]}]}

def test_iter_clips_order_and_heading():
    clips = iter_clips(SEG)
    assert [c["id"] for c in clips] == ["sec-1", "p-1-1-s1", "p-1-1-s2", "sec-2", "p-2-1-s1"]
    assert clips[0]["speech"] == "Part One."
    assert clips[0]["is_section_start"] is True
    # last sentence of a paragraph gets the paragraph gap
    assert clips[2]["gap_after"] > clips[1]["gap_after"]

def test_build_timeline_resets_each_section():
    clips = iter_clips(SEG)
    timing = build_timeline(clips, duration_of=lambda _id: 1.0)  # every clip 1.0s
    c = timing["clips"]
    # sec-1: heading 0-1, then SENT_GAP, then s1, then PARA_GAP, then s2
    assert c["sec-1"] == {"section": "sec-1", "begin": 0.0, "end": 1.0}
    assert c["p-1-1-s1"]["begin"] == round(1.0 + 0.45, 3)   # after heading + SENT_GAP
    assert c["p-1-1-s2"]["begin"] > c["p-1-1-s1"]["end"]
    # section 2 audio file resets to 0
    assert c["sec-2"] == {"section": "sec-2", "begin": 0.0, "end": 1.0}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy/projects/audiobook && python3 -m pytest test_timeline.py -v`
Expected: FAIL — `ImportError: cannot import name 'iter_clips'`

- [ ] **Step 3: Write minimal implementation** (add to `build_audiobook.py`; keep existing constants `SENT_GAP=0.45`, `PARA_GAP=0.85`, `CHAP_GAP=2.0`)

```python
import json

def iter_clips(seg):
    """Flatten one version's segments.json into ordered synth clips."""
    clips = []
    for sec in seg["sections"]:
        clips.append({"id": sec["id"], "speech": sec["headingSpeech"],
                      "gap_after": SENT_GAP, "section": sec["id"],
                      "is_section_start": True})
        for para in sec["paragraphs"]:
            sents = para["sentences"]
            for i, s in enumerate(sents):
                clips.append({"id": s["id"], "speech": s["speech"],
                              "gap_after": PARA_GAP if i == len(sents) - 1 else SENT_GAP,
                              "section": sec["id"], "is_section_start": False})
    return clips

def build_timeline(clips, duration_of):
    """Per-section relative begin/end. Each section's audio file restarts at 0;
    the gap *after* a clip is silence that lives inside that section's file."""
    out = {}
    cur_section = None
    cum = 0.0
    for c in clips:
        if c["section"] != cur_section:
            cur_section, cum = c["section"], 0.0
        begin = round(cum, 3)
        end = round(cum + duration_of(c["id"]), 3)
        out[c["id"]] = {"section": c["section"], "begin": begin, "end": end}
        cum = end + c["gap_after"]
    return {"clips": out}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy/projects/audiobook && python3 -m pytest test_timeline.py -v`
Expected: PASS

- [ ] **Step 5: Commit** (in the audiobook repo)

```bash
cd /Volumes/Graugear/Tolstoy/projects/audiobook
git add build_audiobook.py test_timeline.py
git commit -m "feat: pure timeline math reading segments.json"
```

### Task 7: Wire synthesis to `segments.json` + emit `timing.json` + per-section audio

Replace the `chapters_flow/` reading and the old `units_for`/`split_sents`/`merge_short`/`respell` path with: read `segments.json`, synth each clip's `speech` (cache keyed by segment ID), write one mastered audio file per section, write `timing.json` with real `ffprobe` durations, and keep producing the standalone `.m4b`.

**Files:**
- Modify: `projects/audiobook/build_audiobook.py`

**Interfaces:**
- Consumes: `iter_clips`, `build_timeline` (Task 6).
- Produces: writes `_generated/reader/the-great-sin/timing.en-1905.json` and `…/audio/the-great-sin.sec-N.m4a` per section; cache dir `wav_full_{VOICE}/` now keyed by segment ID.

> **Flagged simplification (ponytail):** the old `merge_short` glued tiny dialogue clips (e.g. "How much have you?") into a neighbour for better TTS cadence. That changed sentence *count*, which would break the 1:1 sentence↔SMIL-par mapping the read-along needs. For the proof we drop merging — **one segment = one clip = one SMIL `<par>`**. Add back later as an audio-only `speechGroup` field in `segments.json` if short-clip cadence proves audibly weak on Chapter I (it has a few short dialogue lines). The known ceiling: a 2–4 word clip synthesized alone can rise instead of fall.

- [ ] **Step 1: Replace the input + main loop**

Replace the file-list/`units_for`/main-build section (`FILES`, `TITLES`, the `if DRY:` block, and the `for i, f in enumerate(FILES)` loop) with a `segments.json`-driven build. Keep `SUBS`/`respell`/`split_*`/`merge_short`/`spoken_header`/`units_for` **deleted** (now in `reader/`), and keep `dur()`, `make_sil()`, `run()`, the mastering constants, and the muxing tail. New core:

```python
SEG_PATH = os.environ.get("SEG_JSON",
    "../../_generated/reader/the-great-sin/segments.en-1905.json")
OUT_DIR  = "../../_generated/reader/the-great-sin"
AUDIO_DIR = f"{OUT_DIR}/audio"
TIMING   = f"{OUT_DIR}/timing.en-1905.json"

seg = json.load(open(SEG_PATH, encoding="utf-8"))
clips = iter_clips(seg)

os.makedirs(CACHE, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

def wav_for(clip):
    wav = f"{CACHE}/{clip['id']}.wav"
    if not os.path.exists(wav):
        print(f">> synth {clip['id']}: {clip['speech'][:50]!r}")
        run(["kokoro-tts-tool", "synthesize", "--stdin", "--output", wav,
             "--voice", VOICE], input=clip["speech"] + "\n")
        norm = wav + ".n.wav"
        run(["ffmpeg", "-y", "-i", wav, "-ar", str(SR), "-ac", "1",
             "-c:a", "pcm_s16le", norm]); os.replace(norm, wav)
    return wav

# 1) synth every clip so durations are known, then compute the timeline
for c in clips:
    wav_for(c)
timing = build_timeline(clips, duration_of=lambda cid: dur(f"{CACHE}/{cid}.wav"))

# 2) per-section mastered audio: concat clip wavs + their gap silences
sil = {}
for g in {SENT_GAP, PARA_GAP, CHAP_GAP}:
    sil[g] = f"{CACHE}/_sil_{int(g*1000)}.wav"; make_sil(sil[g], g)

timing["audio"] = {}
sections = {s["id"]: s for s in seg["sections"]}
by_section = {}
for c in clips:
    by_section.setdefault(c["section"], []).append(c)

for sec_id, sec_clips in by_section.items():
    listfile = f"{CACHE}/_concat_{sec_id}.txt"
    with open(listfile, "w") as f:
        for c in sec_clips:
            f.write(f"file '{os.path.abspath(CACHE)}/{c['id']}.wav'\n")
            if c["gap_after"] > 0:
                f.write(f"file '{os.path.abspath(sil[c['gap_after']])}'\n")
    out_audio = f"{AUDIO_DIR}/{seg['work']}.{sec_id}.m4a"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
         "-af", MASTER, "-ar", "44100", "-c:a", "aac", "-b:a", BITRATE,
         "-movflags", "+faststart", out_audio])
    timing["audio"][sec_id] = f"audio/{seg['work']}.{sec_id}.m4a"

json.dump(timing, open(TIMING, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f">> wrote {TIMING} ({len(timing['clips'])} clips, {len(timing['audio'])} sections)")
```

- [ ] **Step 2: Keep the standalone `.m4b` build (optional for the proof)**

The existing whole-book M4B mux + chapter markers can stay below, now fed by the per-section concat lists chained with `CHAP_GAP` between them. For the **Chapter-I proof slice** the per-section `.m4a` + `timing.json` are what the EPUB needs; the full `.m4b` is unchanged value and may be left as-is or run separately. Leave a one-line `# ponytail:` note that the M4B path is independent of the read-along contract.

- [ ] **Step 3: Smoke-run on the real segments (after Phase 6/7 produce it)**

Run (once `segments.en-1905.json` exists): `cd /Volumes/Graugear/Tolstoy/projects/audiobook && SEG_JSON=<path> python3 build_audiobook.py`
Expected: `wrote …/timing.en-1905.json (N clips, M sections)`; `_generated/reader/the-great-sin/audio/*.m4a` present.

> Until Phase 7, this step has no real input — the **timeline math is already covered by `test_timeline.py`**. Do not block this task on real audio.

- [ ] **Step 4: Commit** (audiobook repo)

```bash
cd /Volumes/Graugear/Tolstoy/projects/audiobook
git add build_audiobook.py
git commit -m "feat: build from segments.json, emit per-section audio + timing.json"
```

---

## Phase 3 — EPUB XHTML generator

### Task 8: `segments.json` (+ notes) → one XHTML chapter document

Render a section's `segments.json` into an EPUB-ready XHTML string: a heading carrying `id="sec-N"`, each paragraph `<p id="p-N-k">`, each sentence `<span class="sentence" id="p-N-k-sK">…</span>`, inline footnote markers turned into `noteref` links, and a notes section of `<aside epub:type="footnote">` with backlinks. This is the resolved/static reading text (the split rule).

**Files:**
- Create: `reader/build_xhtml.py`
- Test: `reader/tests/test_build_xhtml.py`

**Interfaces:**
- Consumes: `segments.json` dict; `ids` (Task 0).
- Produces:
  - `render_section_xhtml(seg: dict, section_id: str, title: str, lang: str) -> str` — a full XHTML doc string for one section, with `<html xmlns:epub>`, the sentence spans, noterefs, and the asides for any notes referenced in that section.
  - `noteref_html(label: str) -> str` and `aside_html(note: dict) -> str` (helpers).

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_build_xhtml.py
import re
from reader.build_xhtml import render_section_xhtml
from reader.segment import segment

def _seg():
    return segment("reader/tests/fixtures/mini.en-1905.md",
                   version="en-1905", work="the-great-sin")

def test_sentence_spans_have_typed_ids():
    html = render_section_xhtml(_seg(), "sec-1", "The Great Sin", "en")
    assert '<span class="sentence" id="p-1-1-s1">' in html
    assert 'id="p-1-2"' in html            # paragraph id
    assert 'id="sec-1"' in html            # heading anchor

def test_footnote_becomes_noteref_and_aside():
    html = render_section_xhtml(_seg(), "sec-1", "The Great Sin", "en")
    assert 'epub:type="noteref"' in html
    assert '<aside epub:type="footnote"' in html
    assert 'A cow without milk.' in html
    # marker text [^1] must NOT survive literally
    assert "[^1]" not in html

def test_is_wellformed_xml():
    import xml.dom.minidom as m
    html = render_section_xhtml(_seg(), "sec-1", "The Great Sin", "en")
    m.parseString(html)   # raises on malformed XML
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_build_xhtml.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'reader.build_xhtml'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/build_xhtml.py
"""Render one section of a version's segments.json into EPUB-ready XHTML.
Resolved/static reading text (the split rule): footnotes become popup asides,
sentences carry stable IDs for the SMIL read-along. No JavaScript."""
import re, html
from reader import ids

_DOC = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}" xml:lang="{lang}">
<head><meta charset="utf-8"/><title>{title}</title>
<link rel="stylesheet" type="text/css" href="../styles/reader.css"/></head>
<body epub:type="bodymatter chapter">
<section aria-labelledby="{sec}">
<h2 id="{sec}">{heading}</h2>
{paras}
{notes}
</section>
</body></html>"""

def noteref_html(label):
    nid = ids.note_id(int(label)) if label.isdigit() else f"note-{label}"
    rid = ids.noteref_id(int(label)) if label.isdigit() else f"noteref-{label}"
    return (f'<a epub:type="noteref" id="{rid}" href="#{nid}" '
            f'role="doc-noteref"><sup>{html.escape(label)}</sup></a>')

def aside_html(note):
    rid = note["id"].replace("note-", "noteref-")
    return (f'<aside epub:type="footnote" id="{note["id"]}" role="doc-footnote">'
            f'<p>{note["html"]} '
            f'<a href="#{rid}" epub:type="backlink" role="doc-backlink">↩</a></p></aside>')

def _render_sentence(text):
    # turn [^label] markers into noterefs, escape the rest
    parts = re.split(r"(\[\^\w+\])", text)
    out = []
    for p in parts:
        m = re.fullmatch(r"\[\^(\w+)\]", p)
        out.append(noteref_html(m.group(1)) if m else html.escape(p))
    return "".join(out)

def render_section_xhtml(seg, section_id, title, lang):
    sec = next(s for s in seg["sections"] if s["id"] == section_id)
    referenced = set(re.findall(r"\[\^(\w+)\]",
                     " ".join(s["display"] for p in sec["paragraphs"] for s in p["sentences"])))
    paras = []
    for p in sec["paragraphs"]:
        spans = " ".join(
            f'<span class="sentence" id="{s["id"]}">{_render_sentence(s["display"])}</span>'
            for s in p["sentences"])
        paras.append(f'<p id="{p["id"]}">{spans}</p>')
    notes = [aside_html(n) for n in seg.get("notes", []) if n["label"] in referenced]
    return _DOC.format(lang=html.escape(lang), title=html.escape(title),
                       sec=section_id, heading=html.escape(sec["heading"]),
                       paras="\n".join(paras),
                       notes=("\n".join(notes)))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_build_xhtml.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/build_xhtml.py reader/tests/test_build_xhtml.py
git commit -m "feat(reader): segments.json -> EPUB XHTML with sentence spans + popup notes"
```

---

## Phase 4 — SMIL + ebooklib packaging

### Task 9: SMIL builder + media-duration arithmetic

Hand-build the SMIL media overlay (one `<par>` per clip, `clipBegin`/`clipEnd` from `timing.json`) and the `media:duration` figures EPUBCheck demands (per content document **and** a total, in SMIL clock format `H:MM:SS.mmm`).

**Files:**
- Create: `reader/build_epub.py`
- Test: `reader/tests/test_smil.py`

**Interfaces:**
- Consumes: `timing.json` dict (Task 7 shape).
- Produces:
  - `clock(seconds: float) -> str` → `"0:00:01.100"`
  - `build_smil(section_id, xhtml_href, audio_href, timing) -> str` — SMIL XML; one `<par>` per clip in that section, in `timing` order, `text` ref = `xhtml_href#clipId`, `audio` ref = `audio_href` with clipBegin/clipEnd.
  - `section_duration(section_id, timing) -> float` — last clip's `end` in that section.

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_smil.py
from reader.build_epub import clock, build_smil, section_duration

TIMING = {
  "audio": {"sec-1": "audio/the-great-sin.sec-1.m4a"},
  "clips": {
    "sec-1":    {"section": "sec-1", "begin": 0.0,  "end": 1.10},
    "p-1-1-s1": {"section": "sec-1", "begin": 1.55, "end": 4.97}}}

def test_clock_format():
    assert clock(1.1) == "0:00:01.100"
    assert clock(3661.5) == "1:01:01.500"

def test_section_duration_is_last_end():
    assert section_duration("sec-1", TIMING) == 4.97

def test_smil_has_par_per_clip_with_clips():
    smil = build_smil("sec-1", "text/sec-1.xhtml", "audio/the-great-sin.sec-1.m4a", TIMING)
    assert smil.count("<par") == 2
    assert 'epub:textref="text/sec-1.xhtml#p-1-1-s1"' in smil or \
           'src="text/sec-1.xhtml#p-1-1-s1"' in smil
    assert 'clipBegin="0:00:01.550"' in smil
    assert 'clipEnd="0:00:04.970"' in smil
    import xml.dom.minidom as m; m.parseString(smil)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_smil.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'reader.build_epub'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/build_epub.py
"""Package a version's XHTML + timing.json into a read-along EPUB3.
ebooklib only zips the container; the SMIL media overlay and the media:* metadata
are hand-built (ebooklib's EpubSMIL is a content carrier only)."""
from reader import ids   # noqa: F401 (kept for parity; ids used by callers)

def clock(seconds):
    h = int(seconds // 3600); m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:06.3f}"

def section_duration(section_id, timing):
    ends = [c["end"] for c in timing["clips"].values() if c["section"] == section_id]
    return max(ends) if ends else 0.0

_SMIL = """<?xml version="1.0" encoding="utf-8"?>
<smil xmlns="http://www.w3.org/ns/SMIL" xmlns:epub="http://www.idpf.org/2007/ops" version="3.0">
<body>
<seq id="seq-{sec}" epub:textref="{xhtml}" epub:type="chapter">
{pars}
</seq>
</body></smil>"""

def build_smil(section_id, xhtml_href, audio_href, timing):
    pars = []
    clips = [(cid, c) for cid, c in timing["clips"].items() if c["section"] == section_id]
    for cid, c in clips:
        pars.append(
            f'<par id="par-{cid}">'
            f'<text src="{xhtml_href}#{cid}"/>'
            f'<audio src="{audio_href}" clipBegin="{clock(c["begin"])}" '
            f'clipEnd="{clock(c["end"])}"/></par>')
    return _SMIL.format(sec=section_id, xhtml=xhtml_href, pars="\n".join(pars))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_smil.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/build_epub.py reader/tests/test_smil.py
git commit -m "feat(reader): SMIL builder + media-duration clock arithmetic"
```

### Task 10: ebooklib packaging with media overlay + a11y metadata

Assemble the `.epub`: add each section's XHTML, attach its SMIL via `media_overlay`, add the per-doc + total `media:duration` and `media:active-class` metadata by hand, write accessibility metadata (schema.org + `dcterms:conformsTo`), `dc:source`, landmarks + a page-list nav, and the audio files. ebooklib zips it.

**Files:**
- Modify: `reader/build_epub.py`
- Create: `reader/tests/test_epub_package.py`

**Interfaces:**
- Consumes: `render_section_xhtml` (Task 8), `build_smil`/`clock`/`section_duration` (Task 9).
- Produces:
  - `build_epub(seg, timing, out_path, meta) -> str` — writes the `.epub`, returns `out_path`. `meta` = `{"title","author","lang","source","translator","date","pss_pages"}` where `pss_pages` maps `section_id -> "PSS 36:206"`.

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_epub_package.py
import zipfile
from reader.build_epub import build_epub
from reader.segment import segment

TIMING = {
  "audio": {"sec-1": "audio/the-great-sin.sec-1.m4a"},
  "clips": {"sec-1": {"section":"sec-1","begin":0.0,"end":1.1},
            "p-1-1-s1": {"section":"sec-1","begin":1.55,"end":4.97},
            "p-1-1-s2": {"section":"sec-1","begin":5.4,"end":7.1},
            "p-1-2-s1": {"section":"sec-1","begin":7.5,"end":9.0},
            "p-1-2-s2": {"section":"sec-1","begin":9.4,"end":11.0}}}
META = {"title":"A Great Iniquity","author":"Leo Tolstoy","lang":"en",
        "source":"PSS vol. 36","translator":"V. Tchertkoff & I. Mayo","date":"1905",
        "pss_pages":{"sec-1":"PSS 36:206"}}

def test_epub_is_written_and_has_overlay(tmp_path):
    seg = segment("reader/tests/fixtures/mini.en-1905.md",
                  version="en-1905", work="the-great-sin")
    # the test audio file need not exist for packaging; create a stub
    (tmp_path / "audio").mkdir()
    (tmp_path / "audio" / "the-great-sin.sec-1.m4a").write_bytes(b"\x00")
    out = build_epub(seg, TIMING, str(tmp_path / "out.epub"), META,
                     audio_root=str(tmp_path))
    z = zipfile.ZipFile(out)
    names = z.namelist()
    assert any(n.endswith(".smil") for n in names)
    opf = next(n for n in names if n.endswith(".opf"))
    content = z.read(opf).decode()
    assert "media:duration" in content
    assert "media:active-class" in content
    assert "schema:accessMode" in content or "accessMode" in content
    assert "dcterms:conformsTo" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_epub_package.py -v`
Expected: FAIL — `ImportError: cannot import name 'build_epub'`

- [ ] **Step 3: Write minimal implementation** (append to `reader/build_epub.py`)

```python
import os
from ebooklib import epub
from reader.build_xhtml import render_section_xhtml

_A11Y = [   # schema.org accessibility metadata (EPUB Accessibility 1.1 / WCAG 2.1 AA)
    ("schema:accessMode", "textual"), ("schema:accessMode", "auditory"),
    ("schema:accessModeSufficient", "textual"),
    ("schema:accessModeSufficient", "textual,auditory"),
    ("schema:accessibilityFeature", "synchronizedAudioText"),
    ("schema:accessibilityFeature", "readingOrder"),
    ("schema:accessibilityFeature", "structuralNavigation"),
    ("schema:accessibilityFeature", "displayTransformability"),
    ("schema:accessibilityHazard", "none"),
    ("schema:accessibilitySummary",
     "Read-along edition with sentence-level synchronized narration."),
]

def build_epub(seg, timing, out_path, meta, audio_root="."):
    book = epub.EpubBook()
    book.set_identifier(f"tolstoy-life-{seg['work']}-{seg['version']}")
    book.set_title(meta["title"]); book.set_language(meta["lang"])
    book.add_author(meta["author"])
    book.add_metadata("DC", "source", meta["source"])
    book.add_metadata("DC", "contributor", meta["translator"], {"role": "trl"})
    book.add_metadata("DC", "date", meta["date"])
    book.add_metadata(None, "meta", "EPUB Accessibility 1.1",
                      {"property": "dcterms:conformsTo"})
    for prop, val in _A11Y:
        book.add_metadata(None, "meta", val, {"property": prop})
    book.add_metadata(None, "meta", "-epub-media-overlay-active",
                      {"property": "media:active-class"})

    spine, total = ["nav"], 0.0
    for sec in seg["sections"]:
        sid = sec["id"]
        x = render_section_xhtml(seg, sid, meta["title"], meta["lang"])
        item = epub.EpubHtml(title=sec["heading"], file_name=f"text/{sid}.xhtml",
                             lang=meta["lang"]); item.content = x
        audio_href = "../" + timing["audio"][sid]
        smil = build_smil(sid, f"{sid}.xhtml", audio_href, timing)
        smil_item = epub.EpubSMIL(uid=f"smil-{sid}", file_name=f"smil/{sid}.smil",
                                  content=smil.encode("utf-8"))
        item.media_overlay = smil_item.get_id()
        dur = section_duration(sid, timing); total += dur
        book.add_metadata(None, "meta", clock(dur),
                          {"property": "media:duration",
                           "refines": f"#{smil_item.get_id()}"})
        # audio file as an EpubItem
        ap = os.path.join(audio_root, timing["audio"][sid])
        audio_bytes = open(ap, "rb").read() if os.path.exists(ap) else b"\x00"
        book.add_item(epub.EpubItem(uid=f"audio-{sid}",
            file_name=timing["audio"][sid], media_type="audio/mp4",
            content=audio_bytes))
        book.add_item(smil_item); book.add_item(item)
        spine.append(item)
    book.add_metadata(None, "meta", clock(total), {"property": "media:duration"})

    book.toc = [epub.Link(f"text/{s['id']}.xhtml", s["heading"], s["id"])
                for s in seg["sections"]]
    book.add_item(epub.EpubNcx()); book.add_item(epub.EpubNav())
    book.spine = spine
    epub.write_epub(out_path, book)
    return out_path
```

> **Note for the executor:** `EpubNav` gives the landmarks/toc nav. The **page-list** nav (`epub:type="page-list"` with real PSS pages) and on-page `pagebreak` anchors are a small follow-on — add them in Task 11 once the base package validates, so a validation failure is easy to localise.

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_epub_package.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/build_epub.py reader/tests/test_epub_package.py
git commit -m "feat(reader): package read-along EPUB3 with media overlay + a11y metadata"
```

### Task 11: PSS page-list nav + pagebreak anchors

Add the scholarly provenance feature the project has data for: invisible `epub:type="pagebreak"` anchors at PSS page boundaries (from each paragraph's `pss` field) and a `<nav epub:type="page-list">`.

**Files:**
- Modify: `reader/build_xhtml.py` (emit a pagebreak span when a paragraph carries `pss`)
- Modify: `reader/build_epub.py` (build the page-list nav)
- Test: `reader/tests/test_pagelist.py`

**Interfaces:**
- Consumes: paragraph `pss` field in `segments.json`.
- Produces:
  - In XHTML: `<span epub:type="pagebreak" id="page-36-206" role="doc-pagebreak" aria-label="PSS 36:206"></span>` at the start of the paragraph whose `pss` is set.
  - `page_list_nav(seg) -> str` — XHTML `<nav epub:type="page-list">` listing those anchors.

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_pagelist.py
from reader.build_xhtml import render_section_xhtml
from reader.build_epub import page_list_nav

SEG = {"work":"the-great-sin","version":"en-1905","spine":"ru","notes":[],
  "sections":[{"id":"sec-1","heading":"Part I","headingSpeech":"Part One.",
    "paragraphs":[{"id":"p-1-1","pss":"36:206","sentences":[
        {"id":"p-1-1-s1","display":"A.","speech":"A."}]}]}]}

def test_pagebreak_anchor_in_xhtml():
    html = render_section_xhtml(SEG, "sec-1", "The Great Sin", "en")
    assert 'epub:type="pagebreak"' in html
    assert 'aria-label="PSS 36:206"' in html

def test_page_list_nav():
    nav = page_list_nav(SEG)
    assert 'epub:type="page-list"' in nav
    assert "PSS 36:206" in nav
    assert "#page-36-206" in nav
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_pagelist.py -v`
Expected: FAIL — `ImportError: cannot import name 'page_list_nav'` (and the XHTML assertion fails)

- [ ] **Step 3: Write the implementation**

In `reader/build_xhtml.py`, change the paragraph loop in `render_section_xhtml` to prepend a pagebreak span when `pss` is present:

```python
    for p in sec["paragraphs"]:
        spans = " ".join(
            f'<span class="sentence" id="{s["id"]}">{_render_sentence(s["display"])}</span>'
            for s in p["sentences"])
        pb = ""
        if p.get("pss"):
            anchor = "page-" + p["pss"].replace(":", "-")
            pb = (f'<span epub:type="pagebreak" id="{anchor}" role="doc-pagebreak" '
                  f'aria-label="PSS {p["pss"]}"></span>')
        paras.append(f'<p id="{p["id"]}">{pb}{spans}</p>')
```

In `reader/build_epub.py`, add:

```python
def page_list_nav(seg):
    items = []
    for sec in seg["sections"]:
        for p in sec["paragraphs"]:
            if p.get("pss"):
                anchor = "page-" + p["pss"].replace(":", "-")
                items.append(f'<li><a href="text/{sec["id"]}.xhtml#{anchor}">'
                             f'PSS {p["pss"]}</a></li>')
    return ('<nav epub:type="page-list" hidden="hidden"><ol>'
            + "".join(items) + "</ol></nav>")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_pagelist.py reader/tests/test_build_xhtml.py -v`
Expected: PASS (the existing XHTML test still passes — paragraphs without `pss` get no anchor)

- [ ] **Step 5: Commit**

```bash
git add reader/build_xhtml.py reader/build_epub.py reader/tests/test_pagelist.py
git commit -m "feat(reader): PSS page-list nav + pagebreak anchors"
```

### Task 12: Validation gates (EPUBCheck + ACE), skip-with-warning

Wrap the two external validators. They run as a build gate but degrade gracefully if not installed (the proof can be produced on a machine without them; CI/Johan runs the real gate).

**Files:**
- Create: `reader/validate.py`
- Test: `reader/tests/test_validate.py`

**Interfaces:**
- Produces:
  - `epubcheck(path) -> tuple[bool, str]` — `(passed, output)`; `(True, "skipped: epubcheck not found")` if the binary is absent.
  - `ace(path, out_dir) -> tuple[bool, str]` — same contract for `ace`.

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_validate.py
from reader import validate

def test_skips_gracefully_when_absent(monkeypatch):
    monkeypatch.setattr(validate.shutil, "which", lambda _: None)
    ok, msg = validate.epubcheck("nonexistent.epub")
    assert ok is True and "skipped" in msg
    ok, msg = validate.ace("nonexistent.epub", "/tmp/ace")
    assert ok is True and "skipped" in msg
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_validate.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'reader.validate'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/validate.py
"""EPUBCheck + ACE by DAISY gates. Skip-with-warning if the tool isn't installed
(don't hard-fail the proof build for a missing validator)."""
import shutil, subprocess

def epubcheck(path):
    exe = shutil.which("epubcheck")
    if not exe:
        return True, "skipped: epubcheck not found (install: brew install epubcheck)"
    p = subprocess.run([exe, path], capture_output=True, text=True)
    return p.returncode == 0, (p.stdout + p.stderr)

def ace(path, out_dir):
    exe = shutil.which("ace")
    if not exe:
        return True, "skipped: ace not found (install: npm i -g @daisy/ace)"
    p = subprocess.run([exe, "-o", out_dir, path], capture_output=True, text=True)
    return p.returncode == 0, (p.stdout + p.stderr)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_validate.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add reader/validate.py reader/tests/test_validate.py
git commit -m "feat(reader): EPUBCheck + ACE validation gates (skip-with-warning)"
```

---

## Phase 5 — serve.py annotation rework (paragraph-ID anchoring + import)

### Task 13: Paragraph IDs in the rendered web HTML

For annotations to anchor to paragraph IDs, serve.py's rendered `<p>` must carry them — using the **same rule** as the segmenter (`reader/ids.py`), so web and EPUB share coordinates. Add a small markdown treeprocessor.

**Files:**
- Modify: `docs/serve.py` (register a treeprocessor on the `MD` instance)
- Create: `reader/paragraph_ids.py` (the treeprocessor; importable + testable)
- Test: `reader/tests/test_paragraph_ids.py`

**Interfaces:**
- Consumes: `reader.ids` (Task 0).
- Produces:
  - `add_paragraph_ids(html_fragment: str) -> str` — a pure post-processor that walks `<h2>`/`<p>` in document order, increments the section on each `<h2>`, and adds `id="p-{section}-{n}"` to each `<p>` that lacks an id. (A post-processor on the HTML string is simpler and dependency-free vs a markdown treeprocessor, and equally testable — **ponytail**.)

- [ ] **Step 1: Write the failing test**

```python
# reader/tests/test_paragraph_ids.py
from reader.paragraph_ids import add_paragraph_ids

def test_numbers_paragraphs_per_section():
    html = "<h2>Part I</h2><p>One.</p><p>Two.</p><h2>Part II</h2><p>Three.</p>"
    out = add_paragraph_ids(html)
    assert 'id="p-1-1"' in out
    assert 'id="p-1-2"' in out
    assert 'id="p-2-1"' in out

def test_preamble_paragraph_before_first_heading_is_section_0():
    html = "<p>Intro.</p><h2>Part I</h2><p>Body.</p>"
    out = add_paragraph_ids(html)
    assert 'id="p-0-1"' in out      # before any heading
    assert 'id="p-1-1"' in out

def test_leaves_existing_ids_alone():
    html = '<p id="keep">x</p>'
    assert add_paragraph_ids(html) == '<p id="keep">x</p>'
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_paragraph_ids.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'reader.paragraph_ids'`

- [ ] **Step 3: Write minimal implementation**

```python
# reader/paragraph_ids.py
"""Add p-{section}-{n} ids to rendered HTML <p> elements, numbered per <h2>
section, matching reader.ids so web annotations share the EPUB's coordinates.
A regex post-processor over the HTML string — no extra dependency."""
import re
from reader import ids

def add_paragraph_ids(html_fragment):
    section = [0]; n = [0]
    def repl(m):
        tag = m.group(0)
        if tag.lower().startswith("<h2"):
            section[0] += 1; n[0] = 0
            return tag
        if "id=" in tag:                       # leave explicit ids alone
            return tag
        n[0] += 1
        return f'<p id="{ids.paragraph_id(section[0], n[0])}"' + tag[2:]
    return re.sub(r"<h2\b[^>]*>|<p\b[^>]*>", repl, html_fragment)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/test_paragraph_ids.py -v`
Expected: PASS

- [ ] **Step 5: Wire it into serve.py**

In `docs/serve.py`, in `render_body`, pass the converted HTML through the post-processor. Add the import near the top (after the `sys.path` is set so `reader` is importable — serve.py runs from repo root, so `reader` imports cleanly):

```python
from reader.paragraph_ids import add_paragraph_ids

def render_body(text: str) -> str:
    """Convert a Markdown string (CriticMarkup, footnotes, [[wikilinks]]) to an HTML fragment."""
    MD.reset()
    return add_paragraph_ids(MD.convert(text))
```

- [ ] **Step 6: Smoke-check serve.py still renders**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -c "import sys; sys.path.insert(0,'.'); sys.argv=['serve']; import importlib.util, pathlib; spec=importlib.util.spec_from_file_location('serve','docs/serve.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.render_body('## Part I\n\nHello there. A second sentence.'))"`
Expected: output contains `<p id="p-1-1">`

- [ ] **Step 7: Commit**

```bash
git add reader/paragraph_ids.py reader/tests/test_paragraph_ids.py docs/serve.py
git commit -m "feat(serve): paragraph IDs in rendered HTML (shared coordinate with EPUB)"
```

### Task 14: Re-anchor annotations to paragraph IDs + import side

Change the annotation JS so anchors store the enclosing paragraph's ID (plus the quote for in-paragraph location), scope the find/wrap to that paragraph, and add an **Import** button (paste/upload the exported JSON, merge into `localStorage`).

**Files:**
- Modify: `docs/serve.py` (the `<script>` block, lines ~605–820, and the `#ann-bar` markup ~600–602)

**Interfaces:**
- Consumes: paragraph IDs now present in the DOM (Task 13).
- Produces: anchors of shape `{paraId, text, before, after}`; an importable JSON round-trip with the existing **Copy annotations** export.

> The export format today is human-readable Markdown (Task reads serve.py ~792–809). For a clean round-trip, **change Copy annotations to emit JSON** (the same `{DOC_KEY: [...]}` slice) and add Import that reads it back. The Markdown export was never re-importable; JSON is the lazy-correct portable format.

- [ ] **Step 1: Update the anchor capture**

In the selection listener (`getContext`), capture the enclosing paragraph id. Replace `getContext` with:

```javascript
  function getContext(range) {{
    const selected = range.toString();
    let el = range.commonAncestorContainer;
    if (el.nodeType === 3) el = el.parentNode;
    const para = el.closest('[id^="p-"]');
    if (!para) return null;
    const full = para.textContent || '';
    const start = full.indexOf(selected);
    if (start === -1) return null;
    return {{
      paraId: para.id,
      text: selected,
      before: full.slice(Math.max(0, start - 30), start),
      after: full.slice(start + selected.length, start + selected.length + 30)
    }};
  }}
```

- [ ] **Step 2: Scope find/wrap to the paragraph**

Replace `findAndWrap` so it searches only within the anchored paragraph (robust when text elsewhere repeats, and stable across edits to other paragraphs):

```javascript
  function findAndWrap(ann, index) {{
    const para = ann.anchor.paraId ? document.getElementById(ann.anchor.paraId) : null;
    const scope = para || document.querySelector('main');
    if (!scope) return;
    const walker = document.createTreeWalker(scope, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {{
      const idx = node.textContent.indexOf(ann.anchor.text);
      if (idx === -1) continue;
      const before = node.textContent.slice(0, idx);
      const after = node.textContent.slice(idx + ann.anchor.text.length);
      const mark = document.createElement('mark');
      mark.className = 'annotation';
      mark.dataset.index = index;
      mark.textContent = ann.anchor.text;
      const afterNode = document.createTextNode(after);
      node.textContent = before;
      node.parentNode.insertBefore(mark, node.nextSibling);
      node.parentNode.insertBefore(afterNode, mark.nextSibling);
      attachTooltip(mark, ann, index);
      break;
    }}
  }}
```

- [ ] **Step 3: Make export emit JSON + add the Import button**

In the `#ann-bar` markup, add an import control next to export:

```html
<div id="ann-bar">
  <button id="ann-export">Copy annotations</button>
  <button id="ann-import">Import…</button>
  <input id="ann-import-file" type="file" accept="application/json" hidden>
  <button class="danger" id="ann-clear">Clear all</button>
</div>
```

Replace the export handler to emit JSON and wire import:

```javascript
  document.getElementById('ann-export').addEventListener('click', () => {{
    const anns = loadDoc();
    if (!anns.length) return;
    const payload = JSON.stringify({{ [DOC_KEY]: anns }}, null, 2);
    navigator.clipboard.writeText(payload).then(() => {{
      const btn = document.getElementById('ann-export');
      const orig = btn.textContent; btn.textContent = 'Copied!';
      setTimeout(() => {{ btn.textContent = orig; }}, 1800);
    }});
  }});

  function mergeImported(obj) {{
    const incoming = obj[DOC_KEY] || [];
    if (!incoming.length) return;
    const anns = loadDoc();
    const seen = new Set(anns.map(a => a.anchor.paraId + '|' + a.anchor.text + '|' + a.comment));
    incoming.forEach(a => {{
      const key = (a.anchor.paraId||'') + '|' + a.anchor.text + '|' + a.comment;
      if (!seen.has(key)) {{ anns.push(a); seen.add(key); }}
    }});
    saveDoc(anns); renderAll();
  }}

  document.getElementById('ann-import').addEventListener('click', () => {{
    const pasted = prompt('Paste exported annotations JSON:');
    if (pasted) {{ try {{ mergeImported(JSON.parse(pasted)); }} catch {{ alert('Not valid JSON.'); }} }}
  }});
  document.getElementById('ann-import-file').addEventListener('change', e => {{
    const f = e.target.files[0]; if (!f) return;
    f.text().then(t => {{ try {{ mergeImported(JSON.parse(t)); }} catch {{ alert('Not valid JSON.'); }} }});
  }});
```

- [ ] **Step 4: Verify in the browser (preview)**

Start serve.py against a reader page, select text in a paragraph, save an annotation, Copy annotations, Clear all, Import (paste) — the annotation reappears anchored to the same paragraph.

Run: `cd /Volumes/Graugear/Tolstoy && python3 docs/serve.py` then use the preview tools to load a `reader/*.md` page, exercise select→save→export→clear→import, and screenshot the restored highlight.
Expected: annotation persists and re-anchors after an edit to a *different* paragraph.

- [ ] **Step 5: Commit**

```bash
git add docs/serve.py
git commit -m "feat(serve): paragraph-ID annotation anchoring + JSON export/import"
```

---

## Phase 6 — Content authoring (human-present, dive discipline)

> This phase is **human-in-the-loop**, grounded in the dossier/extracts — not codegen. Follow `corpus-dive` discipline: ground in Tolstoy's own words, loose-match vault titles before writing `[[wikilinks]]`, and gate locked quotes with `verify_quotes.py`. Do this **with Johan present**; it is not an `--auto` job.

### Task 15: Author the Chapter-I reader source files

**Files:**
- Create: `docs/research/1905-the-great-sin/reader/the-great-sin.ru.md`
- Create: `docs/research/1905-the-great-sin/reader/the-great-sin.en-1905.md`
- Create: `docs/research/1905-the-great-sin/reader/overview.md`
- (machine-English `the-great-sin.en-machine.md` is **optional** for the proof — skip unless Johan wants the third version in the slice)

**Steps:**

- [ ] **Step 1: Russian spine (Chapter I)** — from `extracts/v36_206_230_Velikij_greh.txt`, the `[head] I.` section. Author `## Часть I` + paragraphs, blank-line separated, dialogue em-dashes preserved. Add CriticMarkup only where the dossier's `Varianty`/commentary document a real cut/change; carry PSS page boundaries as paragraph `pss` data (recorded in a sidecar or as an HTML comment the segmenter can read — for the proof, a leading `<!-- pss: 36:206 -->` line per paragraph, parsed in a later refinement, OR set `pss` by hand in the generated JSON). **Marks-stripped Russian must byte-match the extract** — `verify_quotes.py` gate.

- [ ] **Step 2: 1905 English (Chapter I)** — fetch "A Great Iniquity" (Tchertkoff & Mayo, 1905) Chapter I from Wikisource; clean to the same paragraph structure as the spine (paragraph-parallel — the alignment guard in Task 5 enforces equal counts). Add the translator's footnotes as `[^1]` + definitions. Add `[[wikilinks]]` for the people/places Tolstoy names (loose-match vault titles first — `reference_vault_transliteration_gotcha`).

- [ ] **Step 3: overview.md** — distil the reader-facing "about this work" from the dive's `index.md` (the "What the work says" / "Why this matters" sections), in the project's plain factual voice.

- [ ] **Step 4: Verify quotes**

Run: `cd /Volumes/Graugear/Tolstoy && python3 <path-to>/verify_quotes.py docs/research/1905-the-great-sin/reader/the-great-sin.ru.md` (use the dive's existing verify_quotes path/invocation).
Expected: all locked quotes match the extracts.

- [ ] **Step 5: Commit**

```bash
git add docs/research/1905-the-great-sin/reader/
git commit -m "content(the-great-sin): Chapter I reader source — ru spine, 1905 English, overview"
```

---

## Phase 7 — End-to-end integration on Chapter I

### Task 16: Run the full chain and validate

Drive the real pilot through every stage and confirm the read-along highlights in Apple Books — the proof's success condition.

**Files:**
- Create: `reader/build_all.py` (a thin orchestrator wiring Tasks 5→7→8–12 for one work)

**Interfaces:**
- Consumes: everything above.
- Produces: `python3 -m reader.build_all the-great-sin` → `_generated/reader/the-great-sin/{segments.*.json, timing.en-1905.json, audio/, the-great-sin.en-1905.epub}` + a validation report line.

- [ ] **Step 1: Write the orchestrator**

```python
# reader/build_all.py
"""End-to-end: author Markdown -> segments -> (audio handled separately) -> EPUB.
Audio is a separate repo; run projects/audiobook/build_audiobook.py between
segment and epub. This wires the main-repo stages."""
import sys, json
from pathlib import Path
from reader.segment import segment
from reader.build_epub import build_epub
from reader import validate

WORKS = {
  "the-great-sin": {
    "dir": "docs/research/1905-the-great-sin/reader",
    "out": "_generated/reader/the-great-sin",
    "versions": ["ru", "en-1905"],
    "meta": {"title": "A Great Iniquity", "author": "Leo Tolstoy", "lang": "en",
             "source": "Полное собрание сочинений, vol. 36 (1936), pp. 206–230",
             "translator": "V. Tchertkoff & I. F. Mayo", "date": "1905",
             "pss_pages": {"sec-1": "PSS 36:206"}}}}

def main():
    work = sys.argv[1]
    cfg = WORKS[work]; outdir = Path(cfg["out"]); outdir.mkdir(parents=True, exist_ok=True)
    # 1) segment spine first, then each translation against it
    spine = segment(f"{cfg['dir']}/{work}.ru.md", version="ru", work=work)
    (outdir / "segments.ru.json").write_text(
        json.dumps(spine, ensure_ascii=False, indent=2), encoding="utf-8")
    for v in cfg["versions"]:
        if v == "ru": continue
        doc = segment(f"{cfg['dir']}/{work}.{v}.md", version=v, work=work, spine_doc=spine)
        (outdir / f"segments.{v}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(">> segmented. Now run the audiobook build to produce timing.en-1905.json:")
    print(f"   cd projects/audiobook && SEG_JSON=../../{cfg['out']}/segments.en-1905.json python3 build_audiobook.py")
    # 2) EPUB (needs timing.json from the audio repo)
    timing_path = outdir / "timing.en-1905.json"
    if not timing_path.exists():
        print(">> timing.en-1905.json not found — run the audiobook build, then re-run."); return
    seg = json.loads((outdir / "segments.en-1905.json").read_text())
    timing = json.loads(timing_path.read_text())
    epub_path = build_epub(seg, timing, str(outdir / f"{work}.en-1905.epub"),
                           cfg["meta"], audio_root=str(outdir))
    ok1, m1 = validate.epubcheck(epub_path)
    ok2, m2 = validate.ace(epub_path, str(outdir / "ace"))
    print(f">> EPUB: {epub_path}")
    print(f">> EPUBCheck: {'PASS' if ok1 else 'FAIL'} — {m1.splitlines()[-1] if m1 else ''}")
    print(f">> ACE: {'PASS' if ok2 else 'FAIL'} — {m2.splitlines()[-1] if m2 else ''}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Segment the real content**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m reader.build_all the-great-sin`
Expected: `segments.ru.json` + `segments.en-1905.json` written; the alignment guard passes (equal paragraph counts). If it raises a paragraph-count mismatch, fix the English source's paragraph breaks (Task 15) to match the spine — **do not** edit the guard.

- [ ] **Step 3: Build the audio + timing**

Run: `cd /Volumes/Graugear/Tolstoy/projects/audiobook && SEG_JSON=../../_generated/reader/the-great-sin/segments.en-1905.json python3 build_audiobook.py`
Expected: `_generated/reader/the-great-sin/audio/the-great-sin.sec-1.m4a` + `timing.en-1905.json` written.

- [ ] **Step 4: Build + validate the EPUB**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m reader.build_all the-great-sin`
Expected: `the-great-sin.en-1905.epub` written; EPUBCheck PASS (or "skipped"); ACE PASS (or "skipped").

- [ ] **Step 5: On-device read-along check (manual, the proof's success condition)**

Open `the-great-sin.en-1905.epub` in **Apple Books** and **Thorium**. Confirm: it opens; the audio plays; the **highlight advances sentence-by-sentence** in sync; popup footnotes work; the page-list shows PSS pages (Apple). Note the Apple `media:active-class` caveat — verify the highlight look on-device, not just in the markup.

- [ ] **Step 6: Run the whole main-repo test suite**

Run: `cd /Volumes/Graugear/Tolstoy && python3 -m pytest reader/tests/ -v`
Expected: all PASS.

- [ ] **Step 7: Commit**

```bash
git add reader/build_all.py
git commit -m "feat(reader): end-to-end orchestrator; Chapter-I read-along EPUB proven"
```

- [ ] **Step 8: Provide push commands to Johan (do not push)**

Per the push protocol, hand Johan the exact sequence:
```bash
# submodule first (if website changed — it didn't here), then parent:
git -C /Volumes/Graugear/Tolstoy push -u origin docs/research-index
# audiobook repo (separate):
git -C /Volumes/Graugear/Tolstoy/projects/audiobook push origin main
```

---

## Self-review against the spec

**Spec coverage:**
- One CriticMarkup source per version → Tasks 15 (authoring), 3 (resolver). ✓
- Two-layer typed IDs, spine defines coordinate, never renumber → Tasks 0, 4, 5 (alignment guard). ✓
- Segment once → `segments.json` (ID/display/speech) → Tasks 2–5. ✓
- Audio rewire reads `segments.json`, emits `timing.json` → Tasks 6, 7. ✓
- Web renders the `.md`, interactivity stays → unchanged serve.py rendering; annotations Tasks 13–14. ✓
- EPUB via ebooklib, hand-built SMIL, sentence sync → Tasks 8–11. ✓
- epub = resolved/static (no JS) → Task 8 renders resolved text; flagged deferral of styled-visible deletions. ✓
- EPUB first-build features: popup notes (Task 8), page-list (Task 11), a11y metadata + landmarks + `dc:source` (Task 10). ✓
- Annotations = paragraph-ID anchoring + export/import, localStorage → Tasks 13–14. ✓
- Validation = EPUBCheck + ACE → Task 12, run in Task 16. ✓
- Accessibility WCAG 2.1 AA (EPUB metadata + ACE gate) → Tasks 10, 12. ✓
- Wiki-ingestion alignment (dangling `[[wikilinks]]`, loose-match titles) → Task 15 guidance. ✓
- Fidelity / `verify_quotes.py` → Task 15. ✓
- Outputs & layout paths → File map + Tasks 7, 16. ✓

**Deferred by the spec, not built here (correctly absent):** bespoke Eleventy/PWA reader, `tl build` SE-imprint epub, corpus-wide MT/read-along, the cross-dive generator, in-epub scripting, switchable-bilingual single file. The machine-English version is optional for the slice.

**Known flagged simplifications (ponytail, each with an upgrade path):**
1. Audio `merge_short` dropped to keep 1 sentence = 1 SMIL `<par>`; re-add as a `speechGroup` if Chapter I's short dialogue lines read poorly (Task 7).
2. EPUB shows resolved reading text; styled-visible CriticMarkup deletions deferred (Task 8).
3. `pss` page data is hand-supplied in the orchestrator's `meta`/segments for the proof; a per-paragraph `<!-- pss: -->` parse is a later refinement (Task 15 Step 1).
4. EPUBCheck/ACE skip-with-warning if absent — the real gate runs where they're installed (Task 12).

**Type consistency:** `segments.json`/`timing.json` shapes are fixed in the File map and reused verbatim across Tasks 5–11, 16; `reader.ids` helpers are the single ID source for segmenter (Task 4), XHTML (Task 8), and serve.py (Task 13). `iter_clips`/`build_timeline`/`build_smil`/`build_epub`/`render_section_xhtml`/`add_paragraph_ids` names are consistent between their defining task and every caller.
