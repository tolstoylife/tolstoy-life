---
layer: reference
lastUpdated: 2026-06-14
tags: [research, planning, tooling]
title: "An interactive index for docs/research — the handoff plan"
---

The goal: a single **interactive landing page for `docs/research/`** that links to every dive, embeds the project's research visualizations, and **regenerates itself** so it never has to be hand-rebuilt as new dives ship. This file is the plan for the next session to execute. The visual style is settled — reuse and expand the dark editorial theme from the Prophet-essays visualization (see [Artifacts already made](#artifacts-already-made)).

This is a **plan only.** Two decisions were deliberately left open (below) to settle at run time; nothing has been built yet beyond the coverage-map visualization itself.

## Why this is easy here — the pattern already exists

The project already generates committed HTML by scanning the dives. The next session does **not** need to invent machinery — it follows what's already here:

- **`docs/serve.py`** has a `build_index(docs)` function (around line 958) that walks every `docs/**/*.md`, reads its frontmatter (`title`, `date`, `layer`, `description`), and writes the committed top-level **`docs/INDEX.html`** — a dated feed of everything, rebuilt on every `serve.py --build-only`. This is the *global* index; it is **not** a research landing page (it's a flat chronological list across all doc folders). That's the gap this plan fills.
- **`docs/research/lib/build_evidence_index.py`** already reads **every dive's `dossier.yaml`** and writes the committed `docs/research/evidence-index/index.html`. This is the direct precedent for "scan the dossiers → emit one HTML page → re-run on demand." Read this script first; the new generator mirrors it.
- **`docs/.gitignore`** ignores `*.html` but lists explicit committed exceptions (`!/INDEX.html`, `!/research/evidence-index/index.html`, …). So a generated-but-committed `docs/research/index.html` is an established move — just add the exception.

## The manifest is already there — `dossier.yaml`

Every dive carries a `topic:` block the generator can read with zero extra bookkeeping:

```yaml
topic:
  slug: 1879-1882-a-confession
  title: "A Confession (Исповедь)"
  question: >- …one-line scope…
  date: "2026-06-06"
  period: "Prophet period (post-1880); composition 1879–1882 (Old Style)"
  corpusSurface: "PSS Tom 23 …; diaries Tom 48–49; letters Tom 62–63 …"
  dateRange: "1877–1906 …"
```

`index.md` frontmatter (`title`, `date`, `lastUpdated`, `tags`) is a fallback for the handful of older surveys without a dossier. As of 2026-06-14 there are ~47 dive/research folders; the generator should discover them, not hard-code a list.

## Two open decisions (settle at run time)

### Decision 1 — how the index stays current

- **A. Generator + auto-run (recommended).** A small `docs/research/lib/build_research_index.py` reads every `dossier.yaml` and writes `docs/research/index.html`; call it from `serve.py`'s `build_all()` so it regenerates on every docs build. Never hand-edited; new dives appear automatically. Mirrors `build_evidence_index.py`. This is what "dynamic, not redone each session" means in practice here.
- **B. Generator, run by hand.** Same script, run on demand (like a dive's `serve.py --build-only` step). No change to `serve.py`; one extra command per session.
- **C. Client-side JSON.** Ship a static page that loads a generated `manifest.json` and renders dive cards in the browser. Most "live", but more moving parts than this project needs.

*Recommendation: A* — it reuses the existing build, so the page is correct by construction. B is the low-risk fallback if touching `serve.py` feels heavy.

### Decision 2 — where the visualizations live

The visualizations currently sit under `_generated/`, which the repo **deliberately does not track**. To embed them in a committed research index they need a permanent home.

- **A. Promote into the docs tree (recommended).** Copy the coverage map + the 2026-06-12 Prophet-essays viz into a committed `docs/research/visualizations/` folder; the index embeds them (iframe or thumbnail-link). Permanent, works on a fresh clone. Add the `.gitignore` exceptions. (These two stop being throwaway session artifacts and become permanent index components — a deliberate promotion, consistent with the artifact policy's split between session work and curated docs.)
- **B. Embed inline in the index.** Fold the charts directly into the index HTML. Self-contained single file, but larger and it duplicates the viz code.
- **C. Keep in `_generated`, link out.** No copy — but `_generated` isn't tracked and sits outside the docs server root, so links break on a clean clone. (Not viable for a committed index.)

*Recommendation: A.*

## What the page should contain

1. **A featured visual** up top — the [Jubilee-Edition coverage map](#artifacts-already-made) (90-volume dive-coverage shelf).
2. **The dive list, generated and grouped** — each entry links to its `index.html`, with title, date, period, and one-line scope from the dossier. Suggested grouping:
   - *Work-dives* (single work; slug carries a composition-year prefix) — chronological by that year.
   - *Theme-dives* (multi-work; bare slug) — e.g. the death-penalty, break-with-the-Church, folk-tales, late-voice dives.
   - *Reference & method* — the corpus/PSS reference dives (`jubilee-edition-tei-corpus`, `pss-volume-mapping`, `tolstoydigital-tei-reference`, the evidence-index).
   - A light filter/hover (by type / period) keeps it "interactive" without new machinery.
3. **The remaining backlog** — the 11 queued Prophet-period non-fiction dives (see [`_prophet-period-nonfiction-dives.md`](_prophet-period-nonfiction-dives.md)).
4. **The Prophet-essays viz** (timeline / translation-lag / correspondence) embedded or linked.

## Build outline (once decisions are made)

1. Read `build_evidence_index.py` to match its conventions (YAML loading, HTML templating, house CSS).
2. Write `docs/research/lib/build_research_index.py`: discover `*/dossier.yaml` (+ `*/index.md` fallback), parse `topic`, classify work-dive vs theme-dive vs reference, sort, render the dark-theme page with the embedded/linked visualizations and the backlog.
3. If Decision 2 = A: copy the two viz into `docs/research/visualizations/`; add `.gitignore` exceptions for `!/research/index.html` and the viz HTML.
4. If Decision 1 = A: call the new generator from `serve.py`'s `build_all()`; otherwise document the manual command.
5. Run it, then `python3 docs/serve.py --build-only`; verify in the browser. Commit (do **not** push).

## Artifacts already made

- **The coverage map** — `_generated/research/session-pss-coverage-map-2026-06-14/index.html` (+ `README.md`). Dark editorial theme; the first visualization to feature. This is the file to promote under Decision 2.
- **The Prophet-essays viz** — `_generated/research/session-prophet-essays-viz-2026-06-12/index.html` (timeline, translation-lag, share-translated, correspondence ridgeline). The style source to reuse and the second viz to embed.

Both live in untracked `_generated/`; Decision 2 governs how they reach the committed index.
