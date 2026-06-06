# corpus-dive Work-Focused Refinement — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Strengthen the theme-shaped `corpus-dive` skill so a single-work dive (*A Confession* first) yields more — richer standing spine, a work-record field-fill, a folded-in pre-reform extractor fix, and a coverage ledger — then run *A Confession* as the live proof.

**Architecture:** Additive enrichment, no new unit/mode (work-ness lives in the Phase-0 scope contract; every addition scales to evidence and degrades back to a pure theme dive). One real code change (`extract_tei.py` `--choice` flag, TDD); the rest are precise edits to `.claude/skills/corpus-dive/SKILL.md`; the proof is a real `/corpus-dive` run verified by the existing gates.

**Tech Stack:** Python 3 + lxml (`extract_tei.py`); bash regression tests; PyYAML (`verify_quotes.py`, `build_evidence_index.py`); the `corpus-dive` skill; `serve.py` for HTML render.

**Spec:** `docs/superpowers/specs/2026-06-06-corpus-dive-work-dives-design.md`

---

## File structure

- **Modify** `docs/research/lib/extract_tei.py` — add the `--choice=reg|orig|both` flag (default `legacy` = current behaviour) + a stderr nudge when legacy mode drops pre-reform `<choice>` pairs.
- **Create** `docs/research/lib/test-fixtures/prereform-choice.xml` — a minimal TEI fixture with `<choice><orig>/<reg>` pairs.
- **Modify** `docs/research/lib/test-extract-tei.sh` — add reg/orig/legacy assertions against the fixture.
- **Modify** `docs/research/lib/README.md` — document `--choice`; note it supersedes the per-dive `_reg_extract.py` helper.
- **Modify** `.claude/skills/corpus-dive/SKILL.md` — Phase 0/1/2/4/5/6 additions, dossier `workRecord:` + `coverage:` blocks.
- **Modify** `/Users/johanedlund/.claude/projects/-Volumes-Graugear-Tolstoy/memory/reference_extract_tei_prereform_choice_gap.md` + `MEMORY.md` pointer — record the fix.
- **Create** `docs/research/a-confession/` (by running the dive) — `index.md`, `dossier.yaml`, `extracts/`, `visuals/` (if any), dev-blog note under `website/src/posts/notes/`.

---

## PART A — `extract_tei.py` `--choice` flag (TDD)

### Task A1: Create the pre-reform fixture

**Files:**
- Create: `docs/research/lib/test-fixtures/prereform-choice.xml`

- [ ] **Step 1: Write the fixture**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <fileDesc>
      <titleStmt><title type="main">Pre-reform choice fixture</title></titleStmt>
      <publicationStmt><p>test fixture</p></publicationStmt>
      <sourceDesc><p>synthetic — for test-extract-tei.sh</p></sourceDesc>
    </fileDesc>
  </teiHeader>
  <text>
    <body>
      <p>Молитва <choice><orig>стараго</orig><reg>старого</reg></choice> образца и <choice><orig>новаго</orig><reg>нового</reg></choice> завета.</p>
    </body>
  </text>
</TEI>
```

Expected resolutions: `--choice=reg` → "Молитва старого образца и нового завета."; `--choice=orig` → "Молитва стараго образца и новаго завета."; default (legacy) → "Молитва образца и завета." (pairs dropped) + a stderr nudge.

- [ ] **Step 2: Commit**

```bash
git add docs/research/lib/test-fixtures/prereform-choice.xml
git commit -m "test: add pre-reform <choice> TEI fixture for extract_tei"
```

---

### Task A2: Write the failing test

**Files:**
- Modify: `docs/research/lib/test-extract-tei.sh` (append before the final `echo "PASS"` on line 46)

- [ ] **Step 1: Add the assertions**

Insert this block immediately before the final `echo "PASS"` line:

```bash
# --- 6. Pre-reform <choice><orig>/<reg> resolution (the --choice flag) ---
FIX="$HERE/test-fixtures/prereform-choice.xml"

# reg mode resolves to the regularized (modern) reading and does NOT leak orig
REGOUT="$(python3 "$EXTRACT" "$FIX" --choice=reg)"
printf '%s\n' "$REGOUT" | grep -q 'старого' \
  || { echo "FAIL: --choice=reg did not resolve <reg> (старого missing)"; exit 1; }
printf '%s\n' "$REGOUT" | grep -q 'нового' \
  || { echo "FAIL: --choice=reg did not resolve the second <reg> (нового missing)"; exit 1; }
if printf '%s\n' "$REGOUT" | grep -q 'стараго'; then
  echo "FAIL: --choice=reg leaked the <orig> reading (стараго)"; exit 1
fi

# orig mode resolves to the pre-reform reading
ORIGOUT="$(python3 "$EXTRACT" "$FIX" --choice=orig)"
printf '%s\n' "$ORIGOUT" | grep -q 'стараго' \
  || { echo "FAIL: --choice=orig did not resolve <orig> (стараго missing)"; exit 1; }

# legacy default stays backward-compatible: it DROPS the pair (neither reading appears) ...
LEGOUT="$(python3 "$EXTRACT" "$FIX" 2>/dev/null)"
if printf '%s\n' "$LEGOUT" | grep -Eq 'старого|стараго'; then
  echo "FAIL: legacy default unexpectedly kept a pre-reform <choice> reading"; exit 1
fi
# ... but it must NOT be silent — a stderr nudge points at --choice=reg
LEGERR="$(python3 "$EXTRACT" "$FIX" 2>&1 >/dev/null)"
printf '%s\n' "$LEGERR" | grep -qi 'choice=reg' \
  || { echo "FAIL: legacy mode dropped pre-reform pairs without nudging about --choice=reg"; exit 1; }
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `bash docs/research/lib/test-extract-tei.sh`
Expected: FAIL — the first new assertion fires (`--choice=reg did not resolve <reg>`), because `--choice` isn't implemented yet (the flag is treated as a positional path → parse/usage behaviour), and legacy currently drops pairs without a nudge.

---

### Task A3: Implement the `--choice` flag

**Files:**
- Modify: `docs/research/lib/extract_tei.py`

- [ ] **Step 1: Replace the `<choice>` handling in `normalise_paragraph`'s `walk()`**

Find this block (lines ~56–62):

```python
        if tag == "note":
            return
        if tag == "choice":
            corr = node.find("t:corr", NS)
            if corr is not None:
                walk(corr)
            return
        if tag == "sic":
            return  # sibling of <corr>, already handled above
```

Replace it with (adds `<reg>/<orig>` handling, controlled by `choice_mode` from the enclosing scope):

```python
        if tag == "note":
            return
        if tag == "choice":
            # Editorial sic/corr: always prefer the corrected reading (unchanged).
            corr = node.find("t:corr", NS)
            if corr is not None:
                walk(corr)
                return
            # Orthographic orig/reg: pre-reform spelling pairs. Legacy mode drops
            # them (the historical gap); reg/orig/both resolve them per --choice.
            reg = node.find("t:reg", NS)
            orig = node.find("t:orig", NS)
            if reg is not None or orig is not None:
                if choice_mode == "reg":
                    walk(reg if reg is not None else orig)
                elif choice_mode == "orig":
                    walk(orig if orig is not None else reg)
                elif choice_mode == "both":
                    if reg is not None:
                        walk(reg)
                    if orig is not None:
                        text.append(" [")
                        walk(orig)
                        text.append("]")
                # choice_mode == "legacy": drop (preserve historical behaviour)
                return
            return
        if tag == "sic":
            return  # sibling of <corr>, already handled above
```

- [ ] **Step 2: Thread `choice_mode` into `normalise_paragraph`**

Change the signature on line ~36 from:

```python
def normalise_paragraph(p):
```

to:

```python
def normalise_paragraph(p, choice_mode="legacy"):
```

- [ ] **Step 3: Pass `choice_mode` through `recover_note_body`**

Change its signature (line ~107) from `def recover_note_body(body):` to `def recover_note_body(body, choice_mode="legacy"):`, and its inner call from `txt = normalise_paragraph(p)` to `txt = normalise_paragraph(p, choice_mode)`.

- [ ] **Step 4: Thread `choice_mode` through `extract`, count dropped pairs**

Change the `extract` signature (line ~134) from:

```python
def extract(path, notes_mode="auto"):
```

to:

```python
def extract(path, notes_mode="auto", choice_mode="legacy"):
```

Inside the body-iteration loop, change `txt = normalise_paragraph(el)` to `txt = normalise_paragraph(el, choice_mode)`, and change the recovery call `note_paras = recover_note_body(body)` to `note_paras = recover_note_body(body, choice_mode)`.

Then, just before the `return` of `extract`, count the pairs legacy mode drops (a `<choice>` with a `<reg>` child but no `<corr>` child):

```python
    prereform_pairs = sum(
        1
        for ch in body.iter("{http://www.tei-c.org/ns/1.0}choice")
        if ch.find("t:reg", NS) is not None and ch.find("t:corr", NS) is None
    )
    return file_id, title_text, bibl_text, paragraphs, recovered, prereform_pairs
```

(The early `return file_id, title_text, bibl_text, [], 0` on the empty-body path must also become `return file_id, title_text, bibl_text, [], 0, 0`.)

- [ ] **Step 5: Parse `--choice` in `main()` and emit the legacy nudge**

In `main()`, add `choice_mode = "legacy"` next to `notes_mode = "auto"`, add an arg branch, validate, unpack the new return value, and warn on stderr in legacy mode. The argument loop becomes:

```python
    notes_mode = "auto"
    choice_mode = "legacy"
    positional = []
    for arg in sys.argv[1:]:
        if arg.startswith("--notes="):
            notes_mode = arg.split("=", 1)[1]
        elif arg == "--no-notes":
            notes_mode = "off"
        elif arg.startswith("--choice="):
            choice_mode = arg.split("=", 1)[1]
        else:
            positional.append(arg)
    if not positional:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    if notes_mode not in ("auto", "off", "force"):
        print(f"invalid --notes mode: {notes_mode!r} (use auto|off|force)", file=sys.stderr)
        sys.exit(2)
    if choice_mode not in ("legacy", "reg", "orig", "both"):
        print(f"invalid --choice mode: {choice_mode!r} (use legacy|reg|orig|both)", file=sys.stderr)
        sys.exit(2)
```

Change the extract call and unpacking from:

```python
    file_id, title, bibl, paragraphs, recovered = extract(path, notes_mode)
```

to:

```python
    file_id, title, bibl, paragraphs, recovered, prereform_pairs = extract(
        path, notes_mode, choice_mode
    )
    if choice_mode == "legacy" and prereform_pairs:
        print(
            f"# warning: dropped {prereform_pairs} pre-reform <choice><orig>/<reg> "
            f"pair(s) — re-run with --choice=reg to resolve them to modern orthography",
            file=sys.stderr,
        )
```

- [ ] **Step 6: Update the module docstring**

In the top docstring, under the usage lines, add a `--choice` line and a short paragraph. Insert after the `--notes=MODE` usage line:

```
  extract_tei.py <xml> [--choice=MODE]    # resolve pre-reform <choice><orig>/<reg>
```

and after the `--notes=force` paragraph, add:

```
--choice controls pre-reform <choice><orig>/<reg> orthographic pairs:
  --choice=legacy (default)  drop the pair (historical behaviour); warns on stderr
                             so a forgetful run is not silently gutted.
  --choice=reg               resolve to the <reg> (modern-orthography) reading —
                             recommended for any pre-1918 text (all Prophet-period works).
  --choice=orig              resolve to the <orig> (pre-reform) reading.
  --choice=both              emit the <reg> reading with the <orig> in [brackets].
Editorial <choice><sic>/<corr> pairs are unaffected (always resolved to <corr>).
```

---

### Task A4: Run the tests to verify they pass

- [ ] **Step 1: Run the extractor regression test**

Run: `bash docs/research/lib/test-extract-tei.sh`
Expected: `PASS` (all six checks, including the new reg/orig/legacy assertions).

- [ ] **Step 2: Confirm no regression in the sibling test**

Run: `bash docs/research/lib/test-verify-quotes.sh`
Expected: `PASS` (unchanged — verify_quotes is untouched, but confirm the lib still imports cleanly).

- [ ] **Step 3: Smoke-test on a real 1880s text**

Run: `python3 docs/research/lib/extract_tei.py primary-sources/tolstoydigital-TEI/texts/letters/$(ls primary-sources/tolstoydigital-TEI/texts/letters | grep -m1 '^v63_') --choice=reg | head -20`
Expected: clean modern-orthography Russian prose (no gutted words); running the same file without `--choice` prints the stderr `# warning: dropped N pre-reform …` nudge if that file carries pairs. (If no `v63_` file exists, substitute any letter from PSS Tom 63; the point is a real pre-reform document.)

- [ ] **Step 4: Commit**

```bash
git add docs/research/lib/extract_tei.py docs/research/lib/test-extract-tei.sh
git commit -m "feat(extract_tei): --choice=reg|orig|both resolves pre-reform <choice> pairs

Folds the lords-prayer one-off _reg_extract.py into the canonical extractor.
Default stays legacy (drop) for backward-compat but now warns on stderr so a
forgetful 1880s extraction is no longer silently gutted. reg = modern orthography."
```

---

### Task A5: Document the flag and update memory

**Files:**
- Modify: `docs/research/lib/README.md`
- Modify: `/Users/johanedlund/.claude/projects/-Volumes-Graugear-Tolstoy/memory/reference_extract_tei_prereform_choice_gap.md`
- Modify: `/Users/johanedlund/.claude/projects/-Volumes-Graugear-Tolstoy/memory/MEMORY.md`

- [ ] **Step 1: Document `--choice` in the README**

In `docs/research/lib/README.md`, change the `extract_tei.py` usage line (line ~6) from:

```
  Usage: `python3 extract_tei.py <path-to-xml> [substring] [--notes=auto|off|force]`.
```

to:

```
  Usage: `python3 extract_tei.py <path-to-xml> [substring] [--notes=auto|off|force] [--choice=legacy|reg|orig|both]`.
```

Then add a new sub-bullet after the "Note-encoded body recovery" sub-bullet (before the `verify_quotes.py` entry):

```markdown
  - **Pre-reform orthography (`--choice`).** Pre-1918 texts encode old/new spelling as
    `<choice><orig>стараго</orig><reg>старого</reg></choice>`. The default `legacy` mode
    **drops** these pairs (the historical gap that gutted Tom 58 / 1880-era diaries and
    letters) — but now prints a `# warning:` to stderr naming the count so a run is never
    silently gutted. `--choice=reg` resolves to the modern-orthography `<reg>` reading and
    is **recommended for every Prophet-period (pre-1918) extraction**; `--choice=orig`
    keeps the pre-reform reading; `--choice=both` emits `reg [orig]` for collation.
    Editorial `<sic>/<corr>` pairs are always resolved to `<corr>`, independent of this
    flag. This supersedes the per-dive `_reg_extract.py` helper (e.g.
    `lords-prayer/extracts/_reg_extract.py`), which is left in place only as that dive's
    provenance record.
```

- [ ] **Step 2: Update the memory note**

Overwrite `reference_extract_tei_prereform_choice_gap.md` body (keep the frontmatter, update `description` to past tense) so it records the fix:

```markdown
---
name: extract-tei-prereform-choice-gap
description: extract_tei.py --choice=reg resolves pre-reform <choice><orig>/<reg> pairs (was a silent-drop gap)
metadata:
  type: reference
---

`extract_tei.py` used to silently drop pre-reform `<choice><orig>/<reg>` word-pairs
(Tom 58 / 1880-era diaries and letters gutted out). **Fixed 2026-06-06:** the canonical
extractor takes `--choice=legacy|reg|orig|both`. Use **`--choice=reg`** for any pre-1918
text — it resolves to the regularized (modern-orthography) `<reg>` reading. The default
`legacy` mode still drops the pairs (backward-compat) but now prints a stderr nudge naming
the dropped count, so a forgetful run is no longer silent. For `verify_quotes`, still pick
ё-free substrings; for ingestion, still PDF-collate. The per-dive `_reg_extract.py` helper
is superseded. See [[corpus-dive-research-prototypes]].
```

- [ ] **Step 3: Update the MEMORY.md pointer**

In `MEMORY.md`, change the existing line for this memory to reflect the fix (find the `[extract_tei pre-reform gap]` line and update its hook):

```markdown
- [extract_tei pre-reform gap](reference_extract_tei_prereform_choice_gap.md) — FIXED: extract_tei.py `--choice=reg` resolves pre-reform `<choice><orig>/<reg>` pairs to modern orthography; default `legacy` still drops but warns on stderr; recommended for all pre-1918 (Prophet-period) extraction
```

- [ ] **Step 4: Commit**

```bash
git add docs/research/lib/README.md
git commit -m "docs(lib): document extract_tei --choice flag; supersedes per-dive _reg_extract"
```

(Memory files under `~/.claude/` are outside this repo — no git add needed; the Write persists them.)

---

## PART B — `corpus-dive` SKILL.md refinement

All edits are to `.claude/skills/corpus-dive/SKILL.md`. Direct write is permitted for `.claude/**`. After each task, verify with the grep in its final step.

### Task B1: Phase 0 work-subject scope + Phase 1 composition-years/interlocutors sweep

**Files:**
- Modify: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Add work-subject fields to Phase 0**

At the end of the `## Phase 0 — Scope (front-gate)` section (immediately before `## Phase 1 — Sweep (scale-aware)`), insert:

```markdown
**Work-subject dives.** When the subject is a *single work* (not a scattered theme), the
scope contract additionally pins: the **PSS Tom(s)** holding the work and each of its
**redactions**; the **composition window** (writing start→finish, from the `works/` record +
corpus); and the path to the work's `works/` record. These drive the composition-years sweep
(Phase 1), the deep read (Phase 2), the standing spine (Phase 4), and the `workRecord:` fill
(dossier). Everything below degrades gracefully for a pure theme: a spine section with no
evidence is dropped and logged in the `coverage` ledger.
```

- [ ] **Step 2: Add the composition-years sweep to Phase 1**

At the end of the `## Phase 1 — Sweep (scale-aware)` section (immediately before `## Phase 2 — Extract & verify finalists`), insert:

```markdown
**Composition-years witness sweep (high priority — work dives).** Once the writing window is
known, always sweep that window's diaries + letters for two things, not one: (1) **Tolstoy's
own genesis & reaction** — the strain, urgency, and self-understanding while writing; (2) **the
people around the work** — whom he met, corresponded with, and talked to during composition
(visitors, key correspondents, conversation partners, named draft-readers). Diaries name the
visits and conversations; letters name the correspondence network — sweep both for *people*,
surfacing each as a `person` entity (with `ingestionPriority`) in the dossier routing map. This
runs alongside the always-on post-1880 letter pass and feeds the Genesis section (Phase 4).
```

- [ ] **Step 3: Verify**

Run: `grep -c "Work-subject dives\|Composition-years witness sweep" .claude/skills/corpus-dive/SKILL.md`
Expected: `2`

---

### Task B2: Phase 2 deep-read + `--choice=reg` standard

**Files:**
- Modify: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Add the two bullets to Phase 2**

In `## Phase 2 — Extract & verify finalists`, immediately after the bullet that begins `- Run \`python3 docs/research/lib/extract_tei.py …\``, insert these two bullets:

```markdown
- **Read the work's own text deeply (work dives).** The subject text is known — read its TEI
  in the holding Tom(s) as the primary source: a structural pass for the keystone passages,
  chapter by chapter, not only a grep for theme hits. This is the raw material for the *What the
  work says* section.
- **Pre-reform orthography:** run `extract_tei.py` with **`--choice=reg`** on any pre-1918 text
  (every Prophet-period work qualifies) — it resolves `<choice><orig>/<reg>` spelling pairs to
  modern orthography. Without the flag the legacy default drops those pairs and guts the text (it
  now warns on stderr). Use `--choice=orig`/`both` only for deliberate orthographic collation.
  This supersedes the per-dive `_reg_extract.py` helper.
```

- [ ] **Step 2: Verify**

Run: `grep -c "Read the work's own text deeply\|--choice=reg" .claude/skills/corpus-dive/SKILL.md`
Expected: `2` or more.

---

### Task B3: Phase 4 standing-spine sections

**Files:**
- Modify: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Add the standing-sections paragraph**

In `## Phase 4 — Synthesize the outputs`, item `1.` (the `index.md` spine), immediately after the sentence ending `Close with a link to the dev-blog note.` and before the `**Cross-link contested labels (don't scrub).**` paragraph, insert:

```markdown
   **Work-dive standing sections (evidence-scaled).** When the subject is a work, the spine
   additionally carries these — inserted where they fit the narrative, each present *only when
   the corpus supports it* and otherwise dropped and logged in the `coverage` ledger (never
   padded to fill the template): **Genesis & composition** (how/when/why it was written, from
   the composition-year diaries+letters, *including the people around the work* — visitors,
   correspondents, conversation partners — each carried into `entities`); **What the work says**
   (a structural map of keystone passages read from the work's own TEI); **Redactions & textual
   history** (the variants, which Tom holds each, what differs); **Publication, censorship &
   translation** (first publication, ban, foreign first edition, Russian first legal printing,
   translation lineage); **Reception & afterlife — the Russian society & church reaction first**
   (critical/public debate, censorship, clergy and the Holy Synod, the 1901 excommunication where
   the work bears on it; then wider influence); **Place in the cluster** (sibling works + prior
   dives, via the cross-link rule below); and **The author's later verdict** (Tolstoy's own later
   judgment on the work). Keep them bare and in the project voice.
```

- [ ] **Step 2: Verify**

Run: `grep -c "Work-dive standing sections\|The author's later verdict" .claude/skills/corpus-dive/SKILL.md`
Expected: `2`

---

### Task B4: Dossier `workRecord:` + `coverage:` blocks

**Files:**
- Modify: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Add the two blocks to the dossier schema fence**

In `## Phase 4 — Synthesize the outputs`, item `2.` (the `dossier.yaml` schema, inside the ```yaml fence), immediately before the `   contradictions:` line, insert:

```yaml
   workRecord:      # proposed fills for the works/ frontmatter — READ-ONLY to works/; human ingestion applies
     recordPath:    # path to the works/<…>/<Title>.md record
     workId:        # the record's id field
     fields:        # one entry per field the dive can source; omit fields it cannot determine
       - { field, value, oldStyle, approximate, evidenceRefs, source, confidence, note }
   coverage:        # surfaces × status — derives index.md "Material not covered"; resume reads this
     - { surface, status, note }   # status ∈ covered | partial | not-covered
```

- [ ] **Step 2: Add legend entries**

Immediately after the existing `   - \`relation\` ∈ confirms | complicates | contradicts | extends …` legend bullet (within the same item-2 prose), add:

```markdown
   - `workRecord.fields[].field` mirrors a `works/` frontmatter key (no new schema — it reflects
     `website/schema/` + the record itself). The dive never writes `works/`; it *proposes*.
     `confidence` ∈ high | medium | low. `oldStyle`/`approximate` mirror the record's date fields.
   - `coverage[].status` ∈ covered | partial | not-covered — the structured surface map the
     "Material not covered" section is derived from and that multi-session resume reads first.
```

- [ ] **Step 3: Update the skill description frontmatter**

Change the `description:` field (line 3) substring `(evidence + entity + visuals + scholarship layers)` to `(evidence + entity + visuals + scholarship + work-record + coverage layers)`.

- [ ] **Step 4: Verify**

Run: `grep -c "workRecord:\|coverage:\|work-record + coverage layers" .claude/skills/corpus-dive/SKILL.md`
Expected: `3` or more.

---

### Task B5: Phase 5 verifier + Phase 6 handoff + multi-session resume

**Files:**
- Modify: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Extend the Phase 5 verifier checklist**

In `## Phase 5 — Verify (separate pass; never self-approve)`, at the end of the paragraph describing what the verifier checks (immediately before `Iterate until the verdict is clean`), insert:

```markdown
For **work dives** it additionally checks: `workRecord` proposals are evidence-anchored (no
fabricated dates/venues) and their `field` names match the `works/` record schema; the
`coverage` ledger is honest (no `covered` the evidence shows is really `partial`); and the
standing spine sections obey the bare-voice / attribute-don't-assert rules.
```

- [ ] **Step 2: Extend the Phase 6 handoff summary**

In `## Phase 6 — Handoff`, in the sentence listing what the summary contains, after `the **visuals work-order** (images/facsimiles to acquire or request),` insert:

```markdown
the **work-record work-order** (the `workRecord` proposed fills grouped by confidence, for human ingestion into the `works/` record), the **coverage ledger** (covered / partial / not-covered surfaces),
```

- [ ] **Step 3: Make multi-session resume read the coverage ledger**

In `## Multi-session dives`, first paragraph, change `**resume** from its \`session-log.md\` and the dossier's \`notCovered\` queue rather than re-sweeping.` to:

```markdown
**resume** from its `session-log.md`, the dossier's `coverage:` ledger (the structured surface map — read this first), and the `notCovered` queue (free-text overflow) rather than re-sweeping.
```

- [ ] **Step 4: Verify and commit**

Run: `grep -c "work-record work-order\|coverage ledger\|coverage. ledger" .claude/skills/corpus-dive/SKILL.md`
Expected: `2` or more.

```bash
git add .claude/skills/corpus-dive/SKILL.md
git commit -m "feat(corpus-dive): work-focused spine, workRecord + coverage dossier blocks

Standing sections (genesis incl. interlocutors, what-the-work-says, redactions,
publication/censorship, Russian society & church reception, cluster, author's
later verdict); workRecord field-fill proposal; coverage ledger; --choice=reg
standard for pre-1918 extraction; verifier + handoff + resume updates."
```

---

## PART C — *A Confession* proof dive + evaluation gate

### Task C1: Run the dive

- [ ] **Step 1: Invoke the refined skill, interactively**

Run `/corpus-dive A Confession (Исповедь)` (slug `a-confession`; work id `confession`; PSS Tom 23). At Phase 0, confirm the work-subject scope contract: PSS Tom 23; redactions of Исповедь; composition window ≈1879–1882; record path `website/src/works/non-fiction/personal-papers/confession/Confession.md`. Let it run all six phases, using `extract_tei.py --choice=reg` for extraction.

Expected outputs in `docs/research/a-confession/`: `index.md` (with the work-dive standing sections, evidence-scaled), `dossier.yaml` (with `workRecord:` + `coverage:` blocks populated), `extracts/`, `visuals/` (only if an open-licensed image was found), and a `draft: true` dev-blog note under `website/src/posts/notes/`.

- [ ] **Step 2: Confirm the new blocks are present**

Run: `grep -c "workRecord:\|coverage:" docs/research/a-confession/dossier.yaml`
Expected: `2` (both blocks present and populated).

---

### Task C2: Mechanical byte-fidelity gate

- [ ] **Step 1: Run verify_quotes**

Run: `python3 docs/research/lib/verify_quotes.py docs/research/a-confession/dossier.yaml`
Expected: `PASS` (exit 0) — every `quoteRu` is verbatim in its extract. Fix any mismatch (or re-extract with the right `--choice` mode) until it passes.

---

### Task C3: Human-judgment verifier pass

- [ ] **Step 1: Dispatch the verifier subagent (opus, fresh context)**

Dispatch a verifier per Phase 5: sample citations re-derived from TEI/PDF for byte-fidelity; every primary `index.md` claim source-anchored; scholarly claims attributed (not asserted); `workRecord` proposals evidence-anchored with valid `works/` field names; `coverage` ledger honest; entities resolve to valid wiki types with accurate `vaultStatus`; translations labelled; no editorializing voice; `extracts/` PD-only, `visuals/` git-ignored, no rights-reserved image committed.
Expected: a clean verdict (iterate until clean; unresolved items go to `needsReview`).

---

### Task C4: Aggregator + HTML render

- [ ] **Step 1: Confirm the new dossier doesn't break cross-dive aggregation**

Run: `python3 docs/research/lib/build_evidence_index.py --check`
Expected: exit 0 (no broken links introduced by the new blocks). If the aggregator errors on the new `workRecord:`/`coverage:` keys, that's a regression — it should ignore keys it doesn't consume; fix only if it crashes.

- [ ] **Step 2: Render HTML**

Run: `python3 docs/serve.py --build-only`
Expected: `docs/research/a-confession/index.html` generated and `docs/INDEX.html` lists the new dive. (HTML is git-ignored; do not commit it.)

---

### Task C5: Evaluation gate (the pilot retrospective)

- [ ] **Step 1: Run the six-point check with the reader**

Per spec §4 "Evaluation gate," produce a brief findings note covering: (1) did the composition-years sweep surface *the people around the work* as usable `person` entities, not just Tolstoy's reactions? (2) is the Russian society & church reception genuinely covered and source-confirmed? (3) did `workRecord:` populate `Confession.md`'s empty fields with provenance + confidence, accurate against the schema? (4) does the `coverage` ledger read honestly and work as a resume queue? (5) did `--choice=reg` extract cleanly with verify_quotes passing? (6) did the richer spine stay *bare* and evidence-scaled?
Expected: a short note + any skill adjustments folded back into `SKILL.md`/`extract_tei.py` **before** the canon proceeds.

- [ ] **Step 2: Capture the reader's steer**

If the reader annotates the dive, save the interpretive steer to `docs/research/a-confession/annotations.md` (per the dive-annotations→ingestion convention) — guidance for later wiki ingestion, kept out of the bare dive.

---

### Task C6: Commit the dive

- [ ] **Step 1: Commit (no push)**

```bash
git add docs/research/a-confession website/src/posts/notes
git commit -m "Add corpus-dive: A Confession (Исповедь) — work-focused pilot

First work-focused dive on the refined skill: genesis incl. interlocutors,
structural map, redactions, publication/censorship, Russian society & church
reception, cluster, author's later verdict; workRecord fill against the empty
Confession.md + coverage ledger. Byte-verified (verify_quotes PASS)."
```

(Leave the `M website` submodule pointer and any HTML alone; do not push — Johan pushes.)

---

## Self-review

**Spec coverage:**
- Lever 1 (richer standing spine) → Tasks B1 (composition-years/interlocutors), B3 (standing sections). ✔
- Lever 2 (work-record field-fill) → Task B4 (`workRecord:` block + legend). ✔
- Lever 3 (pre-reform extractor fix) → Tasks A1–A5 (fixture, test, impl, docs, memory). ✔
- Lever 4 (coverage ledger) → Task B4 (`coverage:` block), B5 (resume reads it). ✔
- Composition-years interlocutors + Russian church/society reception (round-2 feedback) → B1, B3, and the A Confession test (C1, C5). ✔
- Evaluation gate (round-3 feedback) → Task C5. ✔
- Acceptance test (run A Confession) → Tasks C1–C6. ✔
- Boundaries (no `works/` write) → B4 wording ("READ-ONLY to works/; proposes"), C3 verifier check, C6 commit note. ✔

**Placeholder scan:** No TBD/TODO; every code step shows the code; every edit step shows the exact insert text and anchor; every command has an expected result. ✔

**Type/identifier consistency:** `extract()` returns a 6-tuple everywhere it returns (both the empty-body path and the normal path updated); `normalise_paragraph(p, choice_mode)` / `recover_note_body(body, choice_mode)` signatures match their call sites; `choice_mode` values `legacy|reg|orig|both` are consistent across docstring, walk, validation, and tests; dossier keys `workRecord:`/`coverage:` are spelled identically in SKILL.md, the dive (C1/C2), and the grep checks. ✔
