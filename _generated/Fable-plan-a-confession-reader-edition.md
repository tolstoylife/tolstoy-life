# Plan: A Confession — the first from-scratch reader's edition

> **For agentic workers:** execute top to bottom. This plan has a hard human gate between Stage A and Stage B — do Stage A, present the decision sheet, STOP. Stage B runs in a later session after Johan decides. Written 2026-07-07.

**Goal:** Run A Confession («Исповедь», PSS Tom 23) through Phase 1 of the reader-editions loop — the first work to go from nothing to a full bundle (Russian spine + published English + machine English + synced audio + read-along EPUB) using only the established machinery. The Great Sin proved each piece; this proves the *loop is repeatable*, which is the stated gate before the nightly build queue gets industrialized (`docs/superpowers/specs/2026-06-30-interactive-reader-editions-workflow-design.md`, "Pilot and order").

**Why A Confession:** the design names it explicitly as the second work. The dive exists (`docs/research/1879-1882-a-confession/`), the works record exists (`website/src/works/non-fiction/personal-papers/confession/Confession.md`, id `confession`), and the TEI source is known: `primary-sources/tolstoydigital-TEI/texts/works/v23_001_059_Ispoved.xml` (16 chapters, I–XVI).

## Global constraints

- Never write under `website/src/` (one gated exception in Stage B Task 8), never touch `primary-sources/**` or `website/src/_staging/`.
- Do not push — either repo. The audiobook repo (`projects/audiobook/`) is its own git repo and commits separately.
- Plain language everywhere Johan reads.
- Bundle path mirrors the works record: `docs/reader/non-fiction/personal-papers/confession/`. The work id everywhere is `confession`.

---

## Stage A — preparation and decision sheet (agent, unattended)

### Task A1 — Fresh Russian extraction

The dive's extract (`docs/research/1879-1882-a-confession/extracts/v23_001_059_Ispoved.txt`) **predates the extractor's note-tail fix of 2026-06-07** — extracts from before that fix silently dropped prose that followed inline footnotes. Do not build the spine from it. Re-extract:

```bash
cd /Volumes/Graugear/Tolstoy
python3 docs/research/lib/extract_tei.py --help   # confirm current flags first
python3 docs/research/lib/extract_tei.py \
  primary-sources/tolstoydigital-TEI/texts/works/v23_001_059_Ispoved.xml \
  --choice=reg --notes=auto > /tmp/ispoved-fresh.txt
```

(`--choice=reg` resolves pre-reform spelling pairs; `--notes=auto` recovers text stored in note elements — both are the recommended settings on record.) Then diff the fresh extract against the dive's old one; differences beyond spelling normalization are exactly the note-tail recoveries — list them in the decision sheet as proof the re-extraction mattered (or note that it didn't).

Confirm the `# bibl` header line inside the extract says Tom 23 — the filename is not trusted for bibliographic facts in this project; the bibl line is.

### Task A2 — Pin the structure

From the fresh extract: confirm the chapter count and numbering (expected: 16 chapters, I–XVI). Two structural questions for the sheet:

1. Does the TEI carry anything outside the 16 chapters (an untitled opening, the closing 1882 dream passage as a separate block)? A Confession famously ends with a later-added postscript describing a dream — determine from the TEI + the dive's commentary extract whether it is inside ch. XVI or its own unit, and propose the section structure accordingly (16 sections, or 16 + a closing unit).
2. Proposed section = chapter (1:1), which matches how the Great Sin used its Parts. State it as the default.

### Task A3 — Translation candidates

Assemble the published-English options with provenance, public-domain status, and — the real constraint — **whether a clean digitized text exists to build from**. Known lineage from the dive (dossier line ~690): 1885 first translations → Wiener 1904 → Maude 1921.

For each candidate record: translator, year, edition, PD status (all pre-1930 publications are US-PD; note UK status), where a clean source text lives (Project Gutenberg, Internet Archive, Wikisource — give the exact URL), and one sentence on the translation's character. Expected candidates: Leo Wiener (1904, the Complete Works edition) and Aylmer Maude (1921, Oxford World's Classics "A Confession and What I Believe"). Include any 1885-era translation only if a digitized text actually exists.

Recommend one (likely Maude, the standard) but the pick is Johan's — this is his Phase-1a role by design ("declare which English translation is canonical").

### Task A4 — The decision sheet, then STOP

Write `_generated/research/session-confession-prep-2026-07-XX/decision-sheet.html` (self-contained HTML, per the artifact conventions in `AGENTS.md`; use the run date). Contents: the two decisions Johan must make (canonical translation; section structure), your recommendation for each, the re-extraction findings from A1, and a one-paragraph preview of Stage B. Plain language, no jargon.

**STOP here.** Present the sheet. Stage B needs the two decisions.

---

## Stage B — the build (after Johan's decisions)

### Task B1 — Author the Russian spine

Create `docs/reader/non-fiction/personal-papers/confession/confession.ru.md` from the fresh extract. Mirror the Great Sin spine's format exactly — open `docs/reader/non-fiction/essays-and-criticism/the-great-sin/the-great-sin.ru.md` and copy its conventions: title heading (the work self-titles in its own language: «Исповедь»), section heading form, paragraph spacing.

Quality gates while authoring:

- OCR homoglyph sweep — Latin letters hiding inside Cyrillic words:
  ```bash
  grep -nP '[а-яА-ЯёЁ]+[a-zA-Z]+|[a-zA-Z]+[а-яА-ЯёЁ]+' docs/reader/non-fiction/personal-papers/confession/confession.ru.md
  ```
  Expected: zero hits (investigate every hit; The Great Sin had 5 of these).
- Spot-verify 3 random paragraphs against the local PSS facsimile PDF for Tom 23 (the jubilee-edition directory names are offset from the real Tom numbers — find the right volume by its title page, not the folder name).
- Do not silently "improve" the text — the spine is faithful; oddities you believe are source defects go in `alignment-notes.md`, and only clear OCR/transmission defects get fixed (each one recorded).

### Task B2 — Author the published-English edition

Create `confession.en-<translator>.md` (e.g. `confession.en-maude.md` — the version suffix is Johan's chosen translation, lowercase). Source: the clean text identified in A3. Align it paragraph-for-paragraph to the Russian spine **by hand**: where the translation merges or splits Tolstoy's paragraphs, adjust *paragraph breaks only* (never wording) and record every such decision in `alignment-notes.md` (the Great Sin's `alignment-notes.md` is the worked example of tone and format).

Create `meta.ru.json` and `meta.en-<translator>.json` mirroring the Great Sin meta shape (title, author, lang, source "PSS vol. 23, pp. 1–59 (Исповедь, 1879–82)", translator, date).

### Task B3 — Machine-translation leg

Follow the method in `_generated/Fable-plan-great-sin-machine-translation.md` Tasks 2–5, transposed to this bundle: `confession.en-machine.md`, `meta.en-machine.json`, `translation-diagnostic.md`. Same rules: translate from the `.ru.md` spine, paragraph-for-paragraph, faithful one-pass, unproofed, no marks in other files.

### Task B4 — Segment everything

```bash
cd /Volumes/Graugear/Tolstoy
B=docs/reader/non-fiction/personal-papers/confession

python3 -m reader.segment $B/confession.ru.md --version ru --work confession -o $B/build/segments.ru.json
python3 -m reader.segment $B/confession.en-<translator>.md --version en-<translator> --work confession \
  --spine-json $B/build/segments.ru.json -o $B/build/segments.en-<translator>.json
python3 -m reader.segment $B/confession.en-machine.md --version en-machine --work confession \
  --spine-json $B/build/segments.ru.json -o $B/build/segments.en-machine.json
```

All three exit 0. Alignment failures name the section/paragraph — fix the markdown.

One check before this: `grep -n "MERGE_FORWARD" reader/speech.py` and confirm the merge list is keyed by full segment IDs (which embed the work slug) — Great Sin's entries must not leak into this work. If the list is not work-scoped, stop and flag rather than building audio with wrong merges.

### Task B5 — Audio (long-running; background it)

The audiobook builder lives in the separate repo `projects/audiobook/` and reads the bundle's segments file via the `SEG_JSON` environment variable (it defaults to the Great Sin path — `projects/audiobook/build_audiobook.py:104` — so the variable is mandatory here):

```bash
cd /Volumes/Graugear/Tolstoy/projects/audiobook
SEG_JSON=/Volumes/Graugear/Tolstoy/docs/reader/non-fiction/personal-papers/confession/build/segments.en-<translator>.json \
  python3 build_audiobook.py
```

- Voice is settled: `bm_daniel` (the default) — do not re-audition.
- A Confession is roughly 2–3× The Great Sin's length; expect hours of synthesis. Run in the background and verify by the outputs, not the wall clock.
- Output lands in the bundle's `build/`: one `.m4a` per section + `timing.en-<translator>.json`. The build is resumable (cached WAVs skip).
- Requires `kokoro-tts-tool`, `ffmpeg`, `ffprobe`, `espeak-ng` on PATH — check before starting, report if missing rather than half-running.
- Audio is built for the **published English only** — not for `ru` (no Russian voice in the pipeline), not for `en-machine` (never a listening edition).

### Task B6 — Read-along EPUB

```bash
cd /Volumes/Graugear/Tolstoy
B=docs/reader/non-fiction/personal-papers/confession
python3 -m reader.build_epub --seg $B/build/segments.en-<translator>.json \
  --timing $B/build/timing.en-<translator>.json \
  --meta $B/meta.en-<translator>.json \
  --audio-root $B/build/audio \
  -o $B/build/confession.en-<translator>.epub
```

(Confirm flags with `python3 -m reader.build_epub --help`; `--audio-root` may want the exact audio folder the audiobook build produced — check where the `.m4a` files landed.) If `epubcheck` is installed, run it and require clean; if not installed, say so in the report — skip-with-warn is the accepted posture.

### Task B7 — Regression + preview

```bash
python3 -m pytest reader/tests/ -v        # all green, same count as before you started
```

Then preview: kill any stale :7877 server, start `docs/serve.py`, open the bundle page, confirm the editions list and that the read-along loads (the works tracker at `/reader/` regenerates automatically and should now show `confession` as **built**). Note for Johan's later reading session: the web reader is the proof surface — no Thorium step needed.

### Task B8 — The sidecar (GATED — needs Johan's nod)

The canonical-translation flag lives in the works schema (v10, `translationEditions[].readerDefault`) in a `.data.yaml` sidecar next to the works record — and **no sidecar exists yet for any work**, so this would be the first. Because vault writes follow the wiki-operations protocol (read source → discuss with Johan → write), do not create it silently. Prepare the exact proposed content in your report:

```yaml
# website/src/works/non-fiction/personal-papers/confession/confession.data.yaml (PROPOSED)
translationEditions:
  - translator: "<chosen translator>"
    year: <year>
    title: "<edition title>"
    readerDefault: true
```

…and write it only if Johan approves in-session; otherwise leave the proposal in the report. (Validate afterwards with `node .github/scripts/validate-frontmatter.mjs` from `website/` if written.)

### Task B9 — Commit (two repos)

```bash
cd /Volumes/Graugear/Tolstoy
git add docs/reader/non-fiction/personal-papers/confession/
git commit -m "reader: A Confession bundle — spine, two English editions, alignment notes"
```

`build/` is gitignored — nothing from it gets committed. If `projects/audiobook/` needed any code change (it shouldn't — `SEG_JSON` exists for this), commit that separately inside that repo. Do not push either repo.

## Edge cases a weaker model would miss

1. **The dive's extract is quietly incomplete** — it predates the note-tail fix, so text after inline footnotes may be missing. Re-extract; never build the spine from the old file.
2. **The audiobook builder defaults to the wrong work** — without `SEG_JSON` it happily rebuilds The Great Sin. Also do not edit its default path; the env var is the designed seam.
3. **The WAV cache is keyed by clip ID, not text** — if you re-author any paragraph after a synthesis run, the changed clips keep their old audio silently. Diff the segments file and delete the affected WAVs from `wav_full_bm_daniel/` before re-running.
4. **`chapters/`, `chapters_flow/`, `flow_preprocess.py` in the audiobook repo are decoys** — leftovers not read by the build. Editing them does nothing; the bundle's `.md` is the source of truth.
5. **The Tom-23 facsimile folder may be mislabeled** — jubilee-edition directory names are offset from the real PSS Tom numbers; verify by title page or the extract's `# bibl` line.
6. **The closing dream postscript** may be a separate textual unit — deciding its section placement *before* segmenting avoids re-cutting audio later (the Great Sin learned this: late text repairs forced a partial audio rebuild).
7. **The sidecar is a schema precedent, not a formality** — it is the first `.data.yaml` in the vault and sets the pattern; that's why it's gated on Johan even under an otherwise green light.
8. **Fixing translation wording is out of bounds** — the published English is a historical text; alignment adjusts paragraph *breaks* only.
9. **The 1885 translation is only a real candidate if its text is digitized** — a bibliographically interesting edition with no clean source text would stall the build; don't recommend it for sentiment.

## Acceptance criteria

**Stage A:**
- [ ] Fresh extract produced with `--choice=reg --notes=auto`; diff vs. the dive extract summarized; `# bibl` confirms Tom 23.
- [ ] Decision sheet exists at the session-folder path, self-contained HTML, states both decisions with recommendations, and names the clean source text URL for each translation candidate.
- [ ] Nothing outside `_generated/` was written; no commit made in Stage A (working artifacts only).

**Stage B:**
- [ ] Bundle holds 3 editions + 3 meta files + `alignment-notes.md` + `translation-diagnostic.md` + `overview.md` scaffold (a stub noting Phase 3 comes after reading — copy the pattern the Great Sin used before its real overview).
- [ ] All three segmenter runs exit 0 against the spine; homoglyph grep returns zero.
- [ ] `build/` holds per-section `.m4a` (one per section), `timing.en-<translator>.json`, the `.epub`; epubcheck clean or explicitly skip-warned.
- [ ] `python3 -m pytest reader/tests/ -v` green.
- [ ] Works tracker shows `confession` as built; the web reader plays read-along on at least section I (manual check by Johan or via the preview tools).
- [ ] One commit in the parent repo, none pushed; audiobook repo untouched or separately committed.
- [ ] The sidecar either written-with-approval + validator green, or left as a proposal in the report.
