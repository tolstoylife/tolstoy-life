---
name: corpus-dive
description: "Primary-source research on one theme across the local Tolstoy corpus (tolstoydigital TEI + Jubilee Edition PDFs). Produces a cited index.md (+ a rendered index.html), a machine-readable dossier.yaml (evidence + entity + visuals layers), and a draft dev-blog note — ingestion-ready. Use when asked to research a theme/concept across the corpus/PSS/TEI, or to run such research unattended."
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
- **`--model <tier>`** — informational (the CLI already set the baseline); record the effective tier in the run-report.
- **slug** = kebab-case of the theme (lowercase, non-alphanumeric → `-`).

## Hard boundaries

- **READ freely:** `primary-sources/**` (TEI corpus + PSS PDFs); anywhere under `website/` (read-only).
- **WRITE only to:** `docs/research/<slug>/` (and everything under it — `extracts/`, `visuals/`,
  `dossier.yaml`, `index.md`, `index.html`, `run-report.md`, `session-log.md`), `docs/research/lib/`,
  `docs/research/_batch-<date>.md`, and `website/src/posts/notes/`.
- **NEVER write/modify:** `primary-sources/**`, or anything under `website/` except
  `website/src/posts/notes/`. **No vault writes** — ingestion is a separate human step.

## Mode

- **Interactive (default):** confirm the scoping contract at Phase 0; escalate genuine editorial
  judgment to the user.
- **Autonomous (`--auto`):** auto-derive the scope and proceed; **never call `AskUserQuestion`**;
  any decision needing a human goes to the dossier's `needsReview` and the run is not blocked;
  honor the time-box; save progress incrementally; terminate cleanly; write `run-report.md`.
  `--confirm-scope` adds exactly one approval (the contract) before detaching. An autonomous run
  must never publish: the note is always written with `draft: true` (never flipped to published),
  no vault writes, licence-gated downloads only.

## Model routing

Delegate sub-steps to subagents with the right tier (Agent tool `model` param). Baseline from
`--model`. **Optimize cost on mechanical steps, never on fidelity or judgment.**

| Phase / task | Tier |
|---|---|
| Grep sweep, `extract_tei.py`, `pdftoppm`, `serve.py --build-only` (HTML), file/vault checks, dedup, image download | no-model / haiku |
| Candidate-hit relevance triage; visual-archive web triage | sonnet |
| Scoping contract | sonnet/opus |
| Working-English translations · synthesis (index.md + dossier) · verify pass | opus |

**Escalate-on-low-confidence:** if a cheaper-tier subagent returns low confidence / high
ambiguity, re-run that step on opus. Escalating the model buys quality, not a fabrication licence —
findings still unresolved after escalation go to `needsReview`, never into the prose unanchored.

## Phase 0 — Scope (front-gate)

Draft a **scoping contract**: (1) restate the precise question; (2) corpus surface — genres
(diaries / letters / works / notebooks / commentary) + date-range, **defaulting to the post-1880
"Prophet" period with letters/correspondence first-class**; (3) layered **Russian** keyword set —
high-confidence anchors → broader combinable terms, with orthographic / pre-reform variants;
(4) stop-condition / time-box; (5) sweep mode — inline (narrow) vs fan-out (broad).
Interactive: show the contract and confirm. `--auto`: record the scope contract (written in full to
`docs/research/<slug>/run-report.md` at Phase 5) and proceed.

## Phase 1 — Sweep (scale-aware)

- **Inline:** grep `primary-sources/tolstoydigital-TEI/texts/` with the keyword set; capture
  candidate hits with their TEI id (the filename encodes Tom — the PSS volume number — and, for
  diaries, the entry date).
- **Fan-out (broad themes):** partition the corpus — diaries by decade, **letters by Tom-range
  with a dedicated Prophet-period pass**, works — and dispatch parallel subagents that each return
  structured candidate hits (TEI id, snippet, why-relevant). Dedupe/rank in the main context.
- A **post-1880 letter pass always runs**, regardless of mode.

## Phase 2 — Extract & verify finalists

- Run `python3 docs/research/lib/extract_tei.py <xml>` on each finalist → clean verbatim Russian
  to `docs/research/<slug>/extracts/<tei-id>.txt`.
- Cross-check finalists against the printed PSS PDF (`pdftoppm` @ 220 dpi); if the PDF for the
  relevant Tom is not held locally, note the gap in `needsReview` and proceed. For the **single
  keystone citation**, save the page image to `extracts/`.
- Produce **working-English** translations, explicitly labelled "(working English)".
- Run the **visual-materials sweep** (below) in parallel.

### Visual-materials sweep

Check, in order: local `primary-sources/`; State Tolstoy Museum collection
(tolstoy-iss.kamiscloud.ru) + Goskatalog (web.goskatalog.ru); **Wikimedia Commons** (many
late-period Tolstoy photographs are PD, including Chertkov's own); tolstoy.ru; émigré scan
archives (vtoraya-literatura.com, imwerden.de). For each item record provenance, holding,
access, rights, `licence`, and `usable`.

**Two image channels (the rights gate is at *publication*, not download):**
- `docs/research/<slug>/visuals/` is **git-ignored** (a local research cache — see `docs/.gitignore`).
  Download freely into it for local viewing and embedding — PD *or* rights-uncertain — since the
  public repo never redistributes it. Always record `licence` + source `url` + `usable` in the
  dossier anyway: that metadata is the gate for the *separate* step of publishing an image to
  `website/src/` (the actually-public surface). Never put a rights-reserved/unknown image into
  `website/src/` without cleared rights.
- `docs/research/<slug>/extracts/` **is committed** — put only PD material there: facsimiles you
  render yourself from the local PSS PDFs (`pdftoppm`), which are PD (Tolstoy's own text).

Robust Commons fetch: resolve the real `File:` page (don't guess filenames) — the Commons API
`generator=search`/`categorymembers` + `prop=imageinfo&iiprop=url|extmetadata` returns the direct
URL *and* the licence in one call; download via `Special:FilePath/<file>?width=N`. Embed fetched
images in `index.md` with a `<figure><img src="visuals/…"><figcaption>…</figcaption></figure>`
block (raw HTML passes through; serve.py styles `main img`/`figcaption`). If web tools are
unavailable (headless), degrade gracefully: document provenance, download nothing.

## Phase 3 — Synthesize the outputs

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
3. **`website/src/posts/notes/<YYYY-MM-DD>-<slug>.md`** — frontmatter `title` / `description` / `date` /
   `tags` / `draft: true`. A short recap in the project voice (simple, factual, minimal editorial),
   linking to `index.md`. Stays `draft: true` until the user publishes.
4. **`docs/research/<slug>/index.html`** — generated from `index.md`, never hand-written. The docs
   tree has one canonical generator: `python3 docs/serve.py --build-only` converts every
   `docs/**/*.md` to a sibling `.html` (house CSS, breadcrumb header, per-document annotation UI) and
   rebuilds `docs/INDEX.html` so the new dive is listed. Run it after `index.md` is final. The `.html`
   files are **git-ignored** (`docs/.gitignore`: `*.html`) and regenerated on demand — so `index.md`
   is the sole source of record: don't hand-edit or commit the HTML, just re-run `serve.py` after edits.

## Phase 4 — Verify (separate pass; never self-approve)

Dispatch a **verifier subagent (opus)** in a fresh context. It checks: a sample of citations
re-derived from TEI/PDF for **byte-fidelity**; every `index.md` claim is source-anchored; dossier
entities resolve to valid wiki types with accurate `vaultStatus`; translations are labelled; no
editorializing voice; `extracts/` holds only PD facsimiles, `visuals/` is git-ignored, and **no
rights-reserved/unknown image was committed or placed in `website/src/`** (downloads into the
git-ignored `visuals/` cache are fine; each carries a `licence` in the dossier). Iterate until
the verdict is clean; in `--auto`, if it cannot converge after a few iterations, record the open
items in `needsReview` and conclude the run rather than blocking indefinitely.

## Phase 5 — Handoff

Produce a summary: what was covered, the `notCovered` queue, the **entity work-order** (which wiki
pages this dive feeds), the **visuals work-order** (images/facsimiles to acquire or request), and
the draft note path. Remind that wiki ingestion is a separate, human-in-the-loop step — the
dossier is the pointer, not the writer. **Interactive:** print it. **`--auto`:** write it to
`docs/research/<slug>/run-report.md` (scope contract, coverage, `notCovered`, `needsReview`,
models used + rough cost note, output paths).

## Multi-session dives

A broad theme may exceed one session. At the start of any dive, if `docs/research/<slug>/`
already exists, **resume** from its `session-log.md` and the dossier's `notCovered` queue rather
than re-sweeping. For such dives, keep an append-only `docs/research/<slug>/session-log.md`
(what each session covered) and treat `notCovered` as the resume queue.

## Voice & language

`index.md` and the note in English; cited foreign titles kept verbatim; working-English
translations labelled; minimal editorial. Interactive → escalate genuine editorial judgment to the
user; `--auto` → defer to `needsReview`.
