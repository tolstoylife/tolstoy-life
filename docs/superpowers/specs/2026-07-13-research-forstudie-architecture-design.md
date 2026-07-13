# The research folder (förstudie) architecture — one entity, one page (design)

> Approved design from the 2026-07-13 brainstorm. It settles how `docs/research/` — the förstudie — is organised, and how people and concepts are shared across dives. It grew out of the entity-steer step of **The Great Sin** re-dive and continues the reader-editions workflow ([`2026-06-30-interactive-reader-editions-workflow-design.md`](2026-06-30-interactive-reader-editions-workflow-design.md)), which named Phase 3 as "the front door of ingestion". This brainstorm starts to specify the ingestion *feedstock* — the shape the dives graduate *from*.
>
> **This is a design only.** The actual folder move + link-rewrite is a separate later session (the "plan, then execute separately" rule).

## Context

`docs/research/` is currently **flat** — every dive is a sibling folder, mixed with infra folders and loose planning files. Three different kinds of thing live side by side:

- **Work-dives**, named `<date-range>-<work-slug>/` (e.g. `1905-the-great-sin/`, `1889-1899-resurrection/`) — ~33 of them.
- **Theme / concept / person / group dives**, bare-name folders (e.g. `tolstoyanism/`, `doukhobors/`, `free-age-press/`, `gospel-translation/`).
- **Infra and planning** — `evidence-index/`, `visualizations/`, `lib/`, `jubilee-edition-tei-corpus/`, and many top-level `_*.md` plans.

Two forces make this an architecture question rather than a tidy-up:

1. **Mimic the live site.** The reader-editions already live under `docs/reader/<genre>/<subgenre>/<work>/`, mirroring `website/src/works/`. The research tree does not — it speaks dates, not genres. Bringing it into the site's shape makes **graduation to the live site a *move*, not a rewrite**.
2. **The shared-entity problem.** Henry George recurs across many dives (the land-question cluster, the George prefaces, *Three Days in the Country*). If each dive describes George only inside its own folder, you get many drifting copies. Johan wants **one page per person/concept that every dive updates** — the single-source property the live vault has — but kept in the förstudie until ingestion.

**Correction that reframes everything:** `docs/` is **public on GitHub by design** (the repo is fully open — memory `project_open_source_policy`). So keeping entity work out of the live vault is **editorial** — förstudie voice-forms before ingestion — **not secrecy**. Any "staging = private" reasoning is void.

---

## The decisions

### 1. Three homes under `research/`, plus infra

```
docs/research/
  works/                         ← work-dive bundles, mirroring the live site's genres
    non-fiction/essays-and-criticism/1905-the-great-sin/
    non-fiction/treatises/1890-1893-the-kingdom-of-god-is-within-you/
    fiction/novels/1889-1899-resurrection/
    plays/drama/1886-the-power-of-darkness/
    ...
  themes/                        ← concept / person / group dive bundles
    tolstoyanism/  doukhobors/  free-age-press/  gospel-translation/  ...
  wiki/                          ← flat, shared accreting entity pages (one per person/concept)
    Henry George.md   Isabella Fyvie Mayo.md   Tolstoyanism.md   ...
  _meta/                         ← infra + planning, out of the dive namespace
    evidence-index/  visualizations/  lib/  jubilee-edition-tei-corpus/  _prophet-period-*.md  ...
```

**Naming, per home:**

- `works/<genre>/<subcat>/<date-range>-<slug>/` — **keep the date prefix** on work-dive bundles (`1905-the-great-sin/`). It self-labels the förstudie layer (distinct from the live site's dateless slug), preserves chronology within a genre, and costs nothing at graduation: the *bundle folder* never becomes the live folder — its `overview.md` graduates to a fresh dateless `website/src/works/…/the-great-sin/`, so the date is never stripped.
- `themes/<theme-slug>/` — **bare name** (`tolstoyanism/`), no date; a theme isn't pinned to a single date.
- `wiki/<Entity>.md` — **Title Case, dateless**, mirroring the live wiki (and keeping Obsidian wikilinks working).

Rejected alternatives: a **pure two-folder mirror** (`works/` + `wiki/` only, theme-dives nesting under their entity page) — cleanest mirror, but `wiki/` would hold both single files and sub-bundles and a theme-dive would lose its standalone identity; and a **minimal** version (add only `wiki/`, leave dives where they are) — least disruption, but drops the genre-nesting that makes work-dive graduation mechanical.

### 2. Bundle and entity page are two different layers

- A **dive** is a multi-file **bundle** — `index.md` + `dossier.yaml` + `extracts/` + `annotations.md` + visuals/reports. It is a research *act* with substrate.
- A **wiki entity page** is a **single accreting file** — one `Henry George.md` that many dives keep adding to.

These are not the same file. A dive *about* Tolstoyanism is a bundle in `themes/tolstoyanism/`; the entity page `wiki/Tolstoyanism.md` is a separate single file that this dive — and any other dive touching the concept — feeds.

The parallel that makes graduation mechanical:

| Dive kind | Lives in | Graduates its… | To live site |
|---|---|---|---|
| Work-dive | `works/<genre>/<subcat>/<dive>/` | `overview.md` | `website/src/works/…` |
| Theme-dive | `themes/<theme>/` | `wiki/<Entity>.md` | `website/src/wiki/…` |

Both kinds *also* feed the shared `wiki/` entity pages for every person/concept they touch. Everything else in a bundle (dossier, extracts, annotations, reports) **stays backstage, cited** — never reader-facing as-is.

### 3. One entity, one page — even for already-live people

> Every person/concept a dive touches has **exactly one** `research/wiki/<Entity>.md` that accretes across all dives. A frontmatter flag says what it becomes:
> - `liveStatus: new` → graduates to a fresh `website/src/wiki/<Entity>.md`.
> - `liveStatus: enriches-live` → the entity is **already live**; this file holds **only the förstudie additions** and merges into the existing live page at ingestion — never a full duplicate.

So Chertkov (already live) gets a `research/wiki/Vladimir Chertkov.md` marked `enriches-live`, carrying just the new material (e.g. the *A Great Iniquity* co-translation), not a copy of his live page. This resolves the handoff's #3 (what graduates), #4 (the per-dive steer), and #5 (don't duplicate live entities) with one uniform rule.

Before creating any `wiki/<Entity>.md`, **loose-match the existing pages first** — a wrong "new" makes ingestion duplicate a page that already exists under a different transliteration (memory `reference_vault_transliteration_gotcha`).

### 4. Per-dive `entity-steer.md` is a thin pointer

Each dive keeps a small `entity-steer.md`: "this dive touched `[[Henry George]]`, `[[Vladimir Chertkov]]`" — an audit trail of which entities the dive fed and the one-line gist of what it added. The **substance lives in the shared `wiki/` page**, not scattered across dive folders. At ingestion you read the shared pages; the per-dive steer is the "who contributed what" record behind them.

### 5. `research/wiki/` page frontmatter — full schema *shape*, relaxed fields (option C)

Pages carry the **live `wiki-schema` v1.4 shape** from the start, so graduation is a **move + final review**, not a convert. But unverified fields (Wikidata QIDs, exact dates) may carry `<!-- NEEDS PRIMARY SOURCE -->` placeholders rather than block on verification — the pattern the live `Christian Anarchism.md` already uses. This keeps the pure-move payoff without forcing premature fact-checking in the förstudie.

Rejected: full verified schema now (too much upfront burden; forces QID/date checks early) and a lighter förstudie-only header (makes graduation a convert, and the two headers drift).

### 6. `_meta/` for infra and planning

`evidence-index/`, `visualizations/`, `lib/`, `jubilee-edition-tei-corpus/`, `tolstoy-in-art/`, `tolstoy-in-photographs/`, and the top-level `_*.md` / `_*.html` planning docs move under `research/_meta/`, out of the dive namespace so `works/`, `themes/`, and `wiki/` contain only dives and entity pages.

---

## Out of scope for this design (flagged for the later move-session)

Moving folders **breaks paths**, and the execution session must budget a link-rewrite pass:

- Reader "Around this work" links point at `/research/<slug>/index.html`.
- `docs/INDEX.html` (the docs feed) and `serve.py` routing assume the current flat layout.
- Cross-dive references in existing `index.md` / `dossier.yaml` files use the flat paths.

The <abbr title="Polnoe sobranie sochinenii — the 90-volume Jubilee complete works">PSS</abbr>-cited substrate inside each bundle does not change — only where the bundle sits.

## Scope boundary

This design defines **how the förstudie is organised and how entities are shared** — the feedstock ingestion draws from. It does **not** specify the LLM-ingestion mechanics (how a graduated page is reconciled and written into the live vault); that is its own design, fed by this. And it does not build anything into `website/src/wiki/` — that is the ingestion phase, out of scope here.
