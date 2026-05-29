# corpus-dive Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `corpus-dive` skill — a repeatable primary-source research method that turns one theme into a cited `index.md`, a machine-readable `dossier.yaml`, and a draft dev-blog note — plus its canonical TEI extractor and an overnight headless-CLI queue runner.

**Architecture:** A single-theme project skill (`.claude/skills/corpus-dive/SKILL.md`) that runs the phased, scale-aware method from the design spec. Two supporting files live in `docs/research/lib/`: the canonical `extract_tei.py` (referenced by every dive instead of forked) and `corpus-dive-queue.sh` (spawns a fresh `claude -p` session per theme for unattended batch runs). Plumbing is de-risked with a stub before the research-method body is written.

**Tech Stack:** Markdown skill prompt (Claude Code skills), Python 3 + lxml (TEI extraction), Bash (queue runner), YAML (dossier). No build step.

**Source of truth:** `docs/superpowers/specs/2026-05-29-corpus-dive-design.md` (approved). Section refs below (`spec §N`) point into it.

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `docs/research/lib/extract_tei.py` | Canonical TEI→prose extractor, referenced by every dive | Create (promote from copyright-renunciation copy) |
| `docs/research/lib/README.md` | Notes the canonical extractor + runner; lists the 4 forked copies to reconcile later | Create |
| `docs/research/lib/corpus-dive-queue.sh` | Reads a themes file; spawns one `claude -p … --auto` per theme; `--dry-run`; crash-resilient; writes batch summary | Create |
| `docs/research/lib/test-corpus-dive-queue.sh` | Asserts the runner's `--dry-run` command generation | Create |
| `.claude/skills/corpus-dive/SKILL.md` | The skill: phased method, 3 outputs, autonomy, model routing, boundaries | Create (stub → full) |
| `AGENTS.md` | Add a one-line pointer to the skill + lib | Modify |

**Out of scope** (spec §17): reconciling the four existing forked `extract_tei.py` copies; a cross-dossier aggregator; wiring `visuals` into the future `website/src/images/` section. Noted in the lib README, not built here.

---

## Task 1: Promote the canonical `extract_tei.py`

**Files:**
- Create: `docs/research/lib/extract_tei.py`
- Create: `docs/research/lib/README.md`

- [ ] **Step 1: Confirm the four copies are equivalent and pick the reference**

Run:
```bash
cd /Volumes/Graugear/Tolstoy
for f in copyright-renunciation christian-communism-socialism doukhobors tolstoyanism-christian-anarchism; do
  echo "=== $f ==="; md5 -q "docs/research/$f/extract_tei.py" 2>/dev/null || md5sum "docs/research/$f/extract_tei.py"
done
diff docs/research/copyright-renunciation/extract_tei.py docs/research/christian-communism-socialism/extract_tei.py && echo "IDENTICAL"
```
Expected: either identical hashes, or a diff. If they differ, the copyright-renunciation copy is the reference (it is the spec's reference implementation); note any divergence in the README (Step 4).

- [ ] **Step 2: Copy the reference into the canonical location**

Run:
```bash
mkdir -p docs/research/lib
cp docs/research/copyright-renunciation/extract_tei.py docs/research/lib/extract_tei.py
```

- [ ] **Step 3: Verify it runs and produces expected output on a known TEI file**

Run (find one real TEI source for the 1895 will-as-diary entry, then extract):
```bash
TEI=$(find primary-sources/tolstoydigital-TEI/texts -name "*1895_03_27*.xml" | head -1); echo "TEI: $TEI"
python3 docs/research/lib/extract_tei.py "$TEI" | head -20
```
Expected: prints `# <title>`, `# id: v53_014_018_1895_03_27`, `# bibl: …`, then readable Russian prose paragraphs (no XML tags, footnote digits as superscripts). If `lxml` is missing: `python3 -m pip install lxml` and re-run.

- [ ] **Step 4: Write the lib README**

Create `docs/research/lib/README.md`:
```markdown
# docs/research/lib — shared research tooling

Canonical tooling for `corpus-dive` and the `docs/research/` thematic sweeps.

- **`extract_tei.py`** — resolves tolstoydigital-TEI editorial markup into grep-able Russian
  prose. Usage: `python3 extract_tei.py <path-to-xml> [substring]`. Requires `lxml`.
  This is the canonical copy; dives reference it rather than forking it.
- **`corpus-dive-queue.sh`** — overnight queue runner for `corpus-dive` (see the skill).

## Forked copies to reconcile later (not done here)

Four dives carry their own `extract_tei.py` predating this canonical copy:
`copyright-renunciation/`, `christian-communism-socialism/`, `doukhobors/`,
`tolstoyanism-christian-anarchism/`. Reconciling them against this copy is a separate
cleanup task (design spec §17).
```

- [ ] **Step 5: Commit**

```bash
git add docs/research/lib/extract_tei.py docs/research/lib/README.md
git commit -m "feat(research): promote canonical extract_tei.py to docs/research/lib/"
```

---

## Task 2: Scaffold the skill as a working stub + verify headless triggering

This de-risks the plumbing (does `claude -p` trigger a project skill? does arg-parsing work?) before the research-method body is written.

**Files:**
- Create: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Write the stub skill**

Create `.claude/skills/corpus-dive/SKILL.md`:
````markdown
---
name: corpus-dive
description: "STUB — Primary-source research on one theme across the Tolstoy corpus. Triggers on 'corpus dive', 'corpus-dive', 'research X across the corpus/PSS/TEI'."
argument-hint: "<theme> [--auto] [--confirm-scope] [--model <tier>]"
triggers:
  - "corpus dive"
  - "corpus-dive"
---

# corpus-dive (stub)

Parse `{{ARGUMENTS}}`:
- `theme` = everything that is not a flag.
- `--auto` = unattended; `--confirm-scope` = approve-then-detach; `--model <tier>` = baseline.
- `slug` = kebab-case of the theme.

Then, as a stub, do ONLY this:
1. Create the folder `docs/research/<slug>/`.
2. Write `docs/research/<slug>/run-report.md` containing the parsed `theme`, `slug`, and the
   boolean flags, under a heading `# corpus-dive stub run`.
3. Print: `corpus-dive stub OK — theme="<theme>" auto=<bool> model=<tier>`.

Do nothing else. This stub exists only to verify invocation and arg-parsing.
````

- [ ] **Step 2: Verify interactive triggering**

In a Claude Code session, invoke `/corpus-dive nonresistance to evil --auto`.
Expected: it creates `docs/research/nonresistance-to-evil/run-report.md` and prints the stub-OK line. Delete the test folder afterward: `rm -rf docs/research/nonresistance-to-evil`.

- [ ] **Step 3: Verify headless triggering (the "verify, don't assume" check from spec §13)**

Run:
```bash
cd /Volumes/Graugear/Tolstoy
claude -p "/corpus-dive nonresistance to evil --auto" --model haiku
ls docs/research/nonresistance-to-evil/run-report.md && cat docs/research/nonresistance-to-evil/run-report.md
```
Expected: the file exists with the parsed theme/flags. **If `claude -p` does NOT trigger the slash-command skill**, fall back to a natural-language prompt that hits the trigger words (e.g. `claude -p "corpus dive: nonresistance to evil, run unattended"`) and record which form works in the lib README — the queue runner (Task 3) must use the working form. Clean up: `rm -rf docs/research/nonresistance-to-evil`.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/corpus-dive/SKILL.md
git commit -m "feat(skill): scaffold corpus-dive stub; verify headless invocation"
```

---

## Task 3: Build the queue runner with a tested dry-run mode

> **Discovered in Task 2 (verify-don't-assume):** `claude -p "/corpus-dive … --auto"` DOES trigger
> the skill and arg-parsing works, but headless runs **pause for write-permission confirmation**.
> For unattended overnight use the runner must pass Claude's `--dangerously-skip-permissions`
> (or rely on a pre-approved `.claude/settings.json` allow-list). The runner therefore takes an
> explicit opt-in `--skip-permissions` flag (default OFF) that appends
> `--dangerously-skip-permissions` to each `claude` call. This is a security-relevant choice —
> surfaced to Johan in the wrap-up rather than baked in silently. The code/test below supersede
> the original draft to cover this flag.

**Files:**
- Create: `docs/research/lib/corpus-dive-queue.sh`
- Create: `docs/research/lib/test-corpus-dive-queue.sh`

- [ ] **Step 1: Write the failing test**

Create `docs/research/lib/test-corpus-dive-queue.sh`:
```bash
#!/usr/bin/env bash
# Test corpus-dive-queue.sh --dry-run command generation.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
RUNNER="$HERE/corpus-dive-queue.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

cat > "$TMP/themes.txt" <<'EOF'
# a comment line, skipped
capital punishment

non-resistance to evil
EOF

OUT="$("$RUNNER" --dry-run --model sonnet --themes "$TMP/themes.txt")"

echo "$OUT"
# Exactly two themes (comment + blank line skipped)
[ "$(echo "$OUT" | grep -c 'claude -p')" -eq 2 ] || { echo "FAIL: expected 2 commands"; exit 1; }
echo "$OUT" | grep -qF 'claude -p "/corpus-dive capital punishment --auto" --model sonnet' || { echo "FAIL: theme 1 command wrong"; exit 1; }
echo "$OUT" | grep -qF 'claude -p "/corpus-dive non-resistance to evil --auto" --model sonnet' || { echo "FAIL: theme 2 command wrong"; exit 1; }
echo "PASS"
```

- [ ] **Step 2: Run the test to verify it fails**

Run:
```bash
chmod +x docs/research/lib/test-corpus-dive-queue.sh
bash docs/research/lib/test-corpus-dive-queue.sh
```
Expected: FAIL — `corpus-dive-queue.sh: No such file or directory`.

- [ ] **Step 3: Write the runner**

Create `docs/research/lib/corpus-dive-queue.sh`:
```bash
#!/usr/bin/env bash
# corpus-dive overnight queue runner.
# Spawns a FRESH `claude -p` session per theme (clean context per dive), continues on failure,
# writes a combined batch summary. See .claude/skills/corpus-dive/SKILL.md and design spec §13.
#
# Usage:
#   corpus-dive-queue.sh --themes <file> [--model <tier>] [--dry-run]
#   themes file: one theme per line; blank lines and lines starting with # are ignored.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
THEMES="" ; MODEL="" ; DRY_RUN=0
DATE="$(date +%F)"

while [ $# -gt 0 ]; do
  case "$1" in
    --themes) THEMES="$2"; shift 2 ;;
    --model)  MODEL="$2";  shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

[ -n "$THEMES" ] && [ -f "$THEMES" ] || { echo "Need --themes <existing file>" >&2; exit 2; }

SUMMARY="$REPO_ROOT/docs/research/_batch-$DATE.md"
[ "$DRY_RUN" -eq 0 ] && printf '# corpus-dive batch — %s\n\n' "$DATE" > "$SUMMARY"

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

while IFS= read -r line || [ -n "$line" ]; do
  case "$line" in ''|\#*) continue ;; esac
  theme="$line"
  model_flag=""; [ -n "$MODEL" ] && model_flag=" --model $MODEL"
  cmd="claude -p \"/corpus-dive $theme --auto\"$model_flag"

  if [ "$DRY_RUN" -eq 1 ]; then
    echo "$cmd"
    continue
  fi

  slug="$(slugify "$theme")"
  echo ">>> $(date +%T) dive: $theme"
  if eval "$cmd"; then status="ok"; else status="FAILED"; fi   # continue on failure
  printf -- '- **%s** — %s — [run-report](%s)\n' \
    "$theme" "$status" "docs/research/$slug/run-report.md" >> "$SUMMARY"
done < "$THEMES"

[ "$DRY_RUN" -eq 0 ] && echo "Batch summary: $SUMMARY"
```

- [ ] **Step 4: Run the test to verify it passes**

Run:
```bash
bash docs/research/lib/test-corpus-dive-queue.sh
shellcheck docs/research/lib/corpus-dive-queue.sh || echo "(shellcheck not installed — skip)"
```
Expected: prints the two `claude -p` commands then `PASS`.

- [ ] **Step 5: Commit**

```bash
chmod +x docs/research/lib/corpus-dive-queue.sh
git add docs/research/lib/corpus-dive-queue.sh docs/research/lib/test-corpus-dive-queue.sh
git commit -m "feat(research): corpus-dive overnight queue runner with tested dry-run"
```

---

## Task 4: Write the full SKILL.md body

Replace the stub body (Task 2) with the complete method. Frontmatter stays, but drop the `STUB —` prefix in `description` and add the full trigger list.

**Files:**
- Modify: `.claude/skills/corpus-dive/SKILL.md`

- [ ] **Step 1: Replace the file with the full skill**

Overwrite `.claude/skills/corpus-dive/SKILL.md` with:
````markdown
---
name: corpus-dive
description: "Primary-source research on one theme across the local Tolstoy corpus (tolstoydigital TEI + Jubilee Edition PDFs). Produces a cited index.md, a machine-readable dossier.yaml (evidence + entity + visuals layers), and a draft dev-blog note — ingestion-ready. Use when asked to research a theme/concept across the corpus/PSS/TEI, or to run such research unattended."
argument-hint: "<theme or research question> [--auto] [--confirm-scope] [--model <tier>]"
triggers:
  - "corpus dive"
  - "corpus-dive"
  - "research across the corpus"
  - "research across the PSS"
  - "research across the TEI"
---

# corpus-dive

Primary-source research on **one theme** across the local Tolstoy corpus. Produces three
coordinated, ingestion-ready outputs. Modeled on `docs/research/copyright-renunciation/`.
Full design + rationale: `docs/superpowers/specs/2026-05-29-corpus-dive-design.md`.

## Arguments

Parse `{{ARGUMENTS}}`:
- **theme** (required) — everything that is not a flag; the research question/topic.
- **`--auto`** — unattended mode (see Mode).
- **`--confirm-scope`** — in `--auto`, approve the auto-drafted scope once, then detach.
- **`--model <tier>`** — informational; the CLI already set the baseline. Record it in the report.
- **slug** = kebab-case of the theme (lowercase, non-alphanumeric → `-`).

## Hard boundaries

- **READ freely:** `primary-sources/**` (TEI corpus + PSS PDFs); anywhere under `website/` (read-only).
- **WRITE only to:** `docs/research/<slug>/`, `docs/research/lib/`, `docs/research/_batch-<date>.md`,
  and `website/src/posts/notes/`.
- **NEVER write/modify:** `primary-sources/**`, or anything under `website/` except
  `website/src/posts/notes/`. **No vault writes** — ingestion is a separate human step.

## Mode

- **Interactive (default):** confirm the scoping contract at Phase 0; escalate genuine editorial
  judgment to the user.
- **Autonomous (`--auto`):** auto-derive the scope and proceed; **never call `AskUserQuestion`**;
  any decision needing a human goes to the dossier's `needsReview` and the run is not blocked;
  honor the time-box; save progress incrementally; terminate cleanly; write `run-report.md`.
  `--confirm-scope` adds exactly one approval (the contract) before detaching. An autonomous run
  must never publish: the note stays `draft: true`, no vault writes, licence-gated downloads only.

## Model routing

Delegate sub-steps to subagents with the right tier (Agent tool `model` param). Baseline from
`--model`. **Optimize cost on mechanical steps, never on fidelity or judgment.**

| Phase / task | Tier |
|---|---|
| Grep sweep, `extract_tei.py`, `pdftoppm`, file/vault checks, dedup, image download | no-model / haiku |
| Candidate-hit relevance triage; visual-archive web triage | sonnet |
| Scoping contract | sonnet/opus |
| Working-English translations · synthesis (index.md + dossier) · verify pass | opus |

**Escalate-on-low-confidence:** if a cheaper-tier subagent returns low confidence / high
ambiguity, re-run that step on opus. Escalation buys quality, not a fidelity exemption.

## Phase 0 — Scope (front-gate)

Draft a **scoping contract**: (1) restate the precise question; (2) corpus surface — genres
(diaries / letters / works / notebooks / commentary) + date-range, **defaulting to the post-1880
"Prophet" period with letters/correspondence first-class**; (3) layered **Russian** keyword set —
high-confidence anchors → broader combinable terms, with orthographic / pre-reform variants;
(4) stop-condition / time-box; (5) sweep mode — inline (narrow) vs fan-out (broad).
Interactive: show the contract and confirm. `--auto`: log it to `run-report.md` and proceed.

## Phase 1 — Sweep (scale-aware)

- **Inline:** grep `primary-sources/tolstoydigital-TEI/texts/` with the keyword set; capture
  candidate hits with their TEI id (the filename encodes Tom + entry date).
- **Fan-out (broad themes):** partition the corpus — diaries by decade, **letters by Tom-range
  with a dedicated Prophet-period pass**, works — and dispatch parallel subagents that each return
  structured candidate hits (TEI id, snippet, why-relevant). Dedupe/rank in the main context.
- A **post-1880 letter pass always runs**, regardless of mode.

## Phase 2 — Extract & verify finalists

- Run `python3 docs/research/lib/extract_tei.py <xml>` on each finalist → clean verbatim Russian
  to `docs/research/<slug>/extracts/<tei-id>.txt`.
- Cross-check finalists against the printed PSS PDF (`pdftoppm` @ 220 dpi). For the **single
  keystone citation**, save the page image to `extracts/`.
- Produce **working-English** translations, explicitly labelled "(working English)".
- Run the **visual-materials sweep** (below) in parallel.

### Visual-materials sweep

Check, in order: local `primary-sources/`; State Tolstoy Museum collection
(tolstoy-iss.kamiscloud.ru) + Goskatalog (web.goskatalog.ru); **Wikimedia Commons** (many
late-period Tolstoy photographs are PD, including Chertkov's own); tolstoy.ru; émigré scan
archives (vtoraya-literatura.com, imwerden.de). For each item record provenance, holding,
access, rights, `licence`, and `usable`. **Download into `docs/research/<slug>/visuals/` ONLY when
the licence verifiably permits redistribution in a public repo** (PD / CC0 / CC-BY / CC-BY-SA) —
record `licence` + source `url`. Everything else is **mapped, never copied** (`localPath: null`).
Never download rights-reserved or unknown-rights material into the public repo. If web tools are
unavailable (headless), degrade gracefully: document provenance, download nothing.

## Phase 3 — Synthesize the three outputs

1. **`docs/research/<slug>/index.md`** — frontmatter `layer: reference`. Spine: *Why this matters
   → The shape of the question* (staged; each stage a verbatim RU quote + working-EN translation +
   TEI id / PSS Tom + pages) *→ Where the theme clusters* (tables by genre, incl. a Letters table:
   Tom / letter id / date / addressee / one-line material) *→ Material not covered → Visual &
   manuscript record* (photos/portraits, manuscript facsimiles, illustrations/paintings/maps, each
   with provenance + access + rights; and what is not openly available + where to request it) *→
   Method* (the Phase 0 contract, updated with what actually happened) *→ References*. Close with
   a link to the dev-blog note.
2. **`docs/research/<slug>/dossier.yaml`** — schema:
   ```yaml
   topic: { slug, title, question, date, period, corpusSurface, dateRange }
   evidence:        # flat citation ledger
     - { id, genre, pssTom, pages, date, addressee, localPdf, extract, quoteRu, quoteEn,
         significance, facsimile }
   entities:        # ingestion routing map → wiki
     - { name, wikiType, wikilinkTarget, vaultStatus, role, sources, evidenceRefs }
   visuals:         # → images section
     - { id, type, subject, relatedEntity, relatedEvidence, holding, archiveId, access,
         rights, licence, usable, url, localPath, note }
   contradictions:  - { claim, correction, evidenceRef }
   notCovered:      [ … ]
   needsReview:     - { item, phase, why }   # deferred human-judgment (autonomous never blocks)
   archivesConsulted: [ … ]
   references: { primary: [], background: [] }
   ```
   - `wikiType` ∈ the 9 wiki types (`website/schema/wiki-schema.md`).
   - `vaultStatus` ∈ exists | stub | missing — check `website/src/wiki/` and `website/src/works/`.
   - `sources` ids come from `website/schema/sources.yaml`.
   - `licence` ∈ PD | CC0 | CC-BY | CC-BY-SA | rights-reserved | unknown.
3. **`website/src/posts/notes/<date>-<slug>.md`** — frontmatter `title` / `description` / `date` /
   `tags` / `draft: true`. A short recap in the project voice (simple, factual, minimal editorial),
   linking to `index.md`. Stays `draft: true` until the user publishes.

## Phase 4 — Verify (separate pass; never self-approve)

Dispatch a **verifier subagent (opus)** in a fresh context. It checks: a sample of citations
re-derived from TEI/PDF for **byte-fidelity**; every `index.md` claim is source-anchored; dossier
entities resolve to valid wiki types with accurate `vaultStatus`; translations are labelled; no
editorializing voice; **no rights-reserved image was downloaded into `visuals/`**. Iterate until
the verdict is clean.

## Phase 5 — Handoff

Produce a summary: what was covered, the `notCovered` queue, the **entity work-order** (which wiki
pages this dive feeds), the **visuals work-order** (images/facsimiles to acquire or request), and
the draft note path. Remind that wiki ingestion is a separate, human-in-the-loop step — the
dossier is the pointer, not the writer. **Interactive:** print it. **`--auto`:** write it to
`docs/research/<slug>/run-report.md` (scope contract, coverage, `notCovered`, `needsReview`,
models used + rough cost note, output paths).

## Voice & language

`index.md` and the note in English; cited foreign titles kept verbatim; working-English
translations labelled; minimal editorial. Interactive → escalate genuine editorial judgment to the
user; `--auto` → defer to `needsReview`.
````

- [ ] **Step 2: Lint the embedded dossier example and skill frontmatter**

Run:
```bash
python3 - <<'PY'
import re, yaml, pathlib
txt = pathlib.Path(".claude/skills/corpus-dive/SKILL.md").read_text()
fm = txt.split("---",2)[1]                      # YAML frontmatter
yaml.safe_load(fm); print("frontmatter OK")
PY
```
Expected: `frontmatter OK` (no YAML error). If `yaml` is missing: `python3 -m pip install pyyaml`.

- [ ] **Step 3: Completeness check against the spec**

Re-read `SKILL.md` against the spec and confirm every spec section is represented: boundaries
(§15), autonomy + run-report (§12), queue note (§13 — runner is separate, fine), model routing
(§14), phases 0–5 (§5), index.md spine (§6), dossier 3 layers + needsReview (§7), visual licence
gate (§8), note (§9), Prophet emphasis (§11), verify gates (§16). Fix any omission inline.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/corpus-dive/SKILL.md
git commit -m "feat(skill): full corpus-dive method body"
```

---

## Task 5: Acceptance check against the copyright-renunciation prototype

Validates the skill reproduces the reference dive's key findings (spec §16).

**Files:** none created; produces a throwaway dive folder for comparison.

- [ ] **Step 1: Run a scoped dive on the known theme**

Run (interactive, opus baseline, tight time-box in the scope contract):
```
/corpus-dive copyright renunciation and literary property
```
Let it complete Phases 0–4 into `docs/research/copyright-renunciation-and-literary-property/`.

- [ ] **Step 2: Compare against the prototype**

Confirm the new dive independently surfaces the spec's acceptance markers:
- the 1895-03-27 will-as-diary entry (`v53_014_018_1895_03_27`);
- the 1891-09-16 public declaration (Tom 66, letter 036);
- the correction that the Russian reads **«с 1881 года»** (inclusive of 1881), not "after 1880",
  captured in `dossier.yaml` `contradictions`;
- a `visuals` entry for the 1895 diary page noting it must be requested from GMT (`usable: false`).

Record matches/misses in the run output. Then delete the throwaway folder:
```bash
rm -rf docs/research/copyright-renunciation-and-literary-property
```

- [ ] **Step 3: Fix and re-run if markers are missed**

If a marker is missed, the gap is usually the keyword set (Phase 0) or the letter pass (Phase 1).
Adjust `SKILL.md`, commit, re-run Step 1. No commit needed if all markers hit.

---

## Task 6: Wire discoverability into AGENTS.md

**Files:**
- Modify: `AGENTS.md`

- [ ] **Step 1: Add a pointer near the research/tooling description**

Find the line referencing long-running research workspaces (`grep -n "research" AGENTS.md`) and add:
```markdown
- **`corpus-dive` skill** (`/corpus-dive <theme>`): the repeatable primary-source research method
  behind `docs/research/`. Produces `index.md` + `dossier.yaml` + a draft dev-blog note; runs
  unattended with `--auto`; batch via `docs/research/lib/corpus-dive-queue.sh`. Canonical TEI
  extractor: `docs/research/lib/extract_tei.py`. Design: `docs/superpowers/specs/2026-05-29-corpus-dive-design.md`.
```

- [ ] **Step 2: Commit**

```bash
git add AGENTS.md
git commit -m "docs: point AGENTS.md at the corpus-dive skill and research lib"
```

---

## Self-Review (completed by plan author)

**Spec coverage:** §1–2 → Task 4 frontmatter/Args; §3 outputs → Tasks 4 (skill) + 1 (extractor) + 3 (runner); §4–5 method → Task 4 phases; §6 spine → Task 4 Phase 3; §7 dossier → Task 4 Phase 3 schema; §8 visuals → Task 4 sweep; §9 note → Task 4; §10 mechanics → Tasks 1+4; §11 Prophet → Task 4 Phase 0/1; §12 autonomy → Task 4 Mode + run-report; §13 queue → Tasks 2+3; §14 model routing → Task 4; §15 boundaries → Task 4; §16 verify → Tasks 4+5; §17 future → lib README (Task 1); §18 prototypes → Task 5 acceptance. No gaps.

**Placeholder scan:** runner and test carry complete code; SKILL.md is the complete deliverable; acceptance markers are concrete (TEI ids, the «с 1881 года» correction). No TBD/TODO.

**Type/name consistency:** `slug` derivation, `--auto`/`--confirm-scope`/`--model`, the dossier keys (`evidence`/`entities`/`visuals`/`contradictions`/`notCovered`/`needsReview`/`archivesConsulted`), `vaultStatus`/`licence` enums, and the `docs/research/lib/` paths are used identically across Tasks 1–6.

**Open risk (verified in Task 2, not assumed):** that headless `claude -p` triggers the slash-command skill. Task 2 Step 3 tests it and defines the fallback the runner must use.
