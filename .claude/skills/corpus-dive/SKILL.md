---
name: corpus-dive
description: "Primary-source research on one theme across the local Tolstoy corpus (tolstoydigital TEI + Jubilee Edition PDFs). Produces a cited index.md (+ a rendered index.html), a machine-readable dossier.yaml (evidence + entity + visuals + scholarship + work-record + coverage layers), and a draft dev-blog note — ingestion-ready. Use when asked to research a theme/concept across the corpus/PSS/TEI, or to run such research unattended."
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
For **work dives**, `--auto` is the preferred way to run a dive while the reader is away: the
composition/interlocutor sweep, the `workRecord:` fill, the standing sections, and the
`coverage:` ledger all run with no human in the loop; any uncertain field, attribution, or
judgment call goes to `needsReview`, never into the prose. The post-pilot **evaluation gate is
not run live under `--auto`** — the dive instead writes a **self-assessment** of its checks
(did the interlocutor sweep yield people; is the Russian society/church reception covered; is
the `workRecord` fill accurate + provenanced; is `coverage` honest; did `--choice=reg` extract
cleanly; did the spine stay bare) into `run-report.md`, each self-scored, with concerns routed
to `needsReview`. The human retrospective is deferred to the reader's return; the
self-assessment never blocks the run.

## Model routing

Delegate sub-steps to subagents with the right tier (Agent tool `model` param). Baseline from
`--model`. **Optimize cost on mechanical steps, never on fidelity or judgment.**

| Phase / task | Tier |
|---|---|
| Grep sweep, `extract_tei.py`, `verify_quotes.py`, `pdftoppm`, `serve.py --build-only` (HTML), file/vault checks, dedup, image download | no-model / haiku |
| Candidate-hit relevance triage; visual-archive web triage | sonnet |
| Scholarship + gap-filling web search & relevance triage; factual lookups | sonnet / haiku |
| Scoping contract | sonnet/opus |
| Working-English translations · synthesis (index.md + dossier) · scholarship triangulation · verify pass | opus |

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
`docs/research/<slug>/run-report.md` at Phase 6) and proceed.

**Don't let the gate become a wall.** If the user's framing already answers the scope (they named the
angle, period, or emphasis), confirm the contract in prose and proceed — don't re-block on
`AskUserQuestion`. Use the picker only for genuinely open scope choices, and if the question UI
misfires or returns duplicate/empty answers, fall back to the framing the user already gave rather
than re-firing it. The contract still gets written down; it just isn't gated behind a flaky picker.

**Work-subject dives.** When the subject is a *single work* (not a scattered theme), the
scope contract additionally pins: the **PSS Tom(s)** holding the work and each of its
**redactions**; the **composition window** (writing start→finish, from the `works/` record +
corpus); and the path to the work's `works/` record. These drive the composition-years sweep
(Phase 1), the deep read (Phase 2), the standing spine (Phase 4), and the `workRecord:` fill
(dossier). Everything below degrades gracefully for a pure theme: a spine section with no
evidence is dropped and logged in the `coverage` ledger.

## Phase 1 — Sweep (scale-aware)

- **Inline:** grep `primary-sources/tolstoydigital-TEI/texts/` with the keyword set; capture
  candidate hits with their TEI id (the filename encodes Tom — the PSS volume number — and, for
  diaries, the entry date).
- **Fan-out (broad themes):** partition the corpus — diaries by decade, **letters by Tom-range
  with a dedicated Prophet-period pass**, works — and dispatch parallel subagents that each return
  structured candidate hits (TEI id, snippet, why-relevant). Dedupe/rank in the main context.
- A **post-1880 letter pass always runs**, regardless of mode.

**Composition-years witness sweep (high priority — work dives).** Once the writing window is
known, always sweep that window's diaries + letters for two things, not one: (1) **Tolstoy's
own genesis & reaction** — the strain, urgency, and self-understanding while writing; (2) **the
people around the work** — whom he met, corresponded with, and talked to during composition
(visitors, key correspondents, conversation partners, named draft-readers). Diaries name the
visits and conversations; letters name the correspondence network — sweep both for *people*,
surfacing each as a `person` entity (with `ingestionPriority`) in the dossier routing map. This
runs alongside the always-on post-1880 letter pass and feeds the Genesis section (Phase 4).

## Phase 2 — Extract & verify finalists

- Run `python3 docs/research/lib/extract_tei.py <xml>` on each finalist → clean verbatim Russian
  to `docs/research/<slug>/extracts/<tei-id>.txt`.
- **Read the work's own text deeply (work dives).** The subject text is known — read its TEI
  in the holding Tom(s) as the primary source: a structural pass for the keystone passages,
  chapter by chapter, not only a grep for theme hits. This is the raw material for the *What the
  work says* section.
- **Pre-reform orthography:** run `extract_tei.py` with **`--choice=reg`** on any pre-1918 text
  (every Prophet-period work qualifies) — it resolves `<choice><orig>/<reg>` spelling pairs to
  modern orthography. Without the flag the legacy default drops those pairs and guts the text (it
  now warns on stderr). Use `--choice=orig`/`both` only for deliberate orthographic collation.
  This supersedes the per-dive `_reg_extract.py` helper.
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

**Intensity (scale to the Phase-0 scope, like the text sweep).** *Light* — find the keystone image
plus a handful per major entity, single channel (usually Commons); the default for a narrow theme.
*Heavy* (when the scope asks for "a lot of visuals" or a broad relationship) — fan out one subagent
per source channel, each told to *err toward more*, then dedup. Record the chosen intensity in the
Method section / run-report.

**Dedup contract (when fanning out).** Give each channel a **non-overlapping territory** so they
don't re-fetch the same picture — e.g. by *holding* (Commons vs Canadian archives vs Russian
museums) and by *subject area*, and tell each channel which subjects another owns. Filename prefixes
(`commons-`, `canada-`, `russia-`) prevent path collisions but **not content duplication**; so after
the channels return, run a **dedup-by-subject pass in the main context** before writing the dossier
`visuals` block — one canonical entry per distinct image, noting cross-channel overlap rather than
listing the same photo twice. (A heavy sweep can easily land 2× the files for 1× the subjects.)

**Two image channels (the rights gate is at *publication*, not download):**
- `docs/research/<slug>/visuals/` is **git-ignored** (a local research cache — see `docs/.gitignore`).
  Download freely into it for local viewing and embedding — PD *or* rights-uncertain — since the
  public repo never redistributes it. On a fresh clone the cache is empty — `python3
  docs/fetch_visuals.py [slug]` repopulates it from the dossier `url:` fields. Always record
  `licence` + source `url` + `usable` in the
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

## Phase 3 — Scholarly context & gap-filling

After the primary evidence is locked (Phase 2), add a *secondary* layer: web-search conventional
Tolstoy scholarship + related facts, triangulate the dive's findings against the received view, and
fill knowledge gaps. **Research-prototype rigor:** primary-source citations stay byte-faithful;
secondary/scholarly claims are drafted from knowledge + web and **cited only when there is a clear
source** (inline attribution + a References-list entry — see Synthesize; serve.py renders no Markdown
`[^n]` footnotes), with genuine uncertainty sent to `needsReview`. No adversarial citation gate.

**Ground in the project before the mainstream.** The dive's spine is the primary record — the words
of Tolstoy and the people he trusted (Biryukov, Chertkov) — and the project's **own prior dives**
(scan `docs/research/` for the relevant ones, e.g. `tolstoyanism`, `crisis`). Mainstream and academic
scholarship is a **contrast to read critically**, never a baseline the dive "confirms": treat it with
skepticism, attribute it, and watch for the subtle framing/word-choice that softens or inverts
Tolstoy's message — the Sofia-centred "moralistic dogmatist who tried to impoverish his family" frame
(Popoff; *The Last Station*) is the worked example. Don't let contested movement-labels ("Tolstoyan")
or villain framings ("Chertkov the antagonist") stick in the dive's own voice; attribute them to the
outside. §5 "Scholarly context" is a divergence map, not corroboration. (Memory:
`corpus-dive-ground-in-primary-not-mainstream`.)

1. **Assemble claims & gaps.** List the dive's main findings from the evidence ledger. Collect the
   open gaps from the dossier: `needsReview` items, `notCovered` candidates worth a quick check,
   entities with `vaultStatus: missing | stub`, and factual unknowns (identities, dates, event
   context) flagged during extraction.
2. **Web sweep — scholarship + related facts.** Scholarship scope is **English-first** (major
   biographers + academic Tolstoy studies), Russian-language when authoritative or decisive. Two
   intents: (a) the **received view** on the theme and on the specific findings — key voices, the
   consensus, whether mainstream work addresses them; (b) **gap-filling facts** to resolve the
   assembled unknowns + related context the corpus lacked. Capture each source as
   `author, year, work/title, url`. Lightweight fan-out (the search-and-triage shape of the
   `deep-research` skill) — **not** its full adversarial harness. Distinct from Phase 2's
   *visual-materials* sweep (images), which is unchanged.
3. **Triangulate.** Classify each major finding against the conventional view: `confirms`
   (scholarship agrees), `complicates` (nuance / partial), `contradicts` (the primary source pushes
   back on the received narrative), `extends` (scholarship does not reach this — the corpus supplies
   primary grounding for a point scholars argued only thematically, or addresses one the literature
   leaves open). `contradicts` and `extends` are the high-value cases. Each entry ties to its primary
   `evidenceRef` and, *where there is a clear source*, an inline-attributed secondary citation (a
   References-list entry — not a `[^n]` footnote).
4. **Completeness loop (bounded, once).** Ask what scholars treat as central that the corpus sweep
   missed. If a real gap emerges (a key text, letter, episode, sub-theme), loop back for **one**
   targeted Phase 1→2 mini sweep+extract for it, then return. A gap that can't be resolved in-scope
   — or one that is central in the scholarship but lies *outside the dive's declared scope* (e.g.
   wrong period) — goes to `notCovered` with a pointer, **not** a forced loop. Run the loop once,
   not open-endedly.

Writes the dossier `scholarship:` block (see Synthesize), adds secondary sources to
`references.background`, and updates `notCovered` / `needsReview` / `entities`. The "Scholarly
context" prose section of `index.md` is composed in Synthesize.

## Phase 4 — Synthesize the outputs

1. **`docs/research/<slug>/index.md`** — frontmatter `layer: reference`. Spine: *Key findings* (the first section — a tight bulleted exec-summary of the dive's own conclusions, reusing its own figures; no new claims) *→ Why this matters
   → The shape of the question* (staged; each stage a verbatim RU quote + working-EN translation +
   TEI id / PSS Tom + pages) *→ Where the theme clusters* (tables by genre, incl. a Letters table:
   Tom / letter id / date / addressee / one-line material) *→ Scholarly context* (the received
   scholarly view, and where the corpus evidence confirms / complicates / contradicts / extends it —
   **attribute, don't assert**: "Bartlett (2010) describes… ; the diary shows…"; cite clear secondary
   sources inline + in References — serve.py renders no `[^n]` footnotes) *→ Material not covered → Visual &
   manuscript record* (photos/portraits, manuscript facsimiles, illustrations/paintings/maps, each
   with provenance + access + rights; and what is not openly available + where to request it) *→
   Method* (the Phase 0 contract, updated with what actually happened) *→ References*. Close with
   a link to the dev-blog note.
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
   **Cross-link contested labels (don't scrub).** Wherever a contested mainstream label appears —
   most often in *Scholarly context*, but anywhere it surfaces — link its first prominent occurrence
   to the project's dedicated dive on that term (`../<slug>/index.html`, the rendered sibling; a bare
   `.md` link serves as raw text). The link keeps the label visible as the *mainstream's* word while
   pointing at the dive that interrogates it — it does **not** license asserting the badge as fact in
   the dive's own voice (that is Phase 3's "ground in the project before the mainstream" rule, which
   this complements). Interlink sibling dives the same way, via a short *Links* line in Method.
   Worked example: `biryukov-sofia-relationship` §5 (the `tolstoyanism` link) + §8 (sibling links);
   memory `corpus-dive-ground-in-primary-not-mainstream`. Never link `tolstoyanism-christian-anarchism`
   as authoritative — it is the superseded combined survey.
2. **`docs/research/<slug>/dossier.yaml`** — schema:
   ```yaml
   topic: { slug, title, question, date, period, corpusSurface, dateRange }
   evidence:        # flat citation ledger
     - { id, genre, pssTom, pages, date, addressee, localPdf, extract, quoteRu, quoteEn,
         significance, facsimile }
   entities:        # ingestion routing map → wiki
     - { name, wikiType, wikilinkTarget, vaultStatus, role, sources, evidenceRefs,
         ingestionPriority, dependsOn }   # last two optional — turn the map into a plan
   visuals:         # → images section
     - { id, type, subject, relatedEntity, relatedEvidence, holding, archiveId, access,
         rights, licence, usable, url, localPath, note }
   scholarship:                 # secondary layer — conventional scholarship (Phase 3)
     summary:                   # short prose: the received view on this theme (English-first)
     triangulation:             # one entry per major finding vs scholarship
       - { evidenceRef, conventionalView, relation, source }
   workRecord:      # proposed fills for the works/ frontmatter — READ-ONLY to works/; human ingestion applies
     recordPath:    # path to the works/<…>/<Title>.md record
     workId:        # the record's id field
     fields:        # one entry per field the dive can source; omit fields it cannot determine
       - { field, value, oldStyle, approximate, evidenceRefs, source, confidence, note }
   coverage:        # surfaces × status — derives index.md "Material not covered"; resume reads this
     - { surface, status, note }   # status ∈ covered | partial | not-covered
   contradictions:  - { claim, correction, evidenceRef }   # intra-corpus (primary-vs-primary) only — distinct from scholarship
   notCovered:      [ … ]
   needsReview:     - { item, phase, why }   # deferred human-judgment (autonomous never blocks)
   archivesConsulted: [ … ]
   references: { primary: [], background: [] }
   ```
   - `wikiType` ∈ the 9 wiki types (`website/schema/wiki-schema.md`).
   - `vaultStatus` ∈ exists | stub | missing — check `website/src/wiki/` and `website/src/works/`.
   - `sources` ids come from `website/schema/sources.yaml`.
   - `licence` ∈ PD | CC0 | CC-BY | CC-BY-SA | rights-reserved | unknown.
   - `relation` ∈ confirms | complicates | contradicts | extends — scholarship triangulation
     (`extends` = the corpus reaches below the scholarship's resolution); clear secondary sources
     also go in `references.background` (`source` omitted when there is no clear one).
   - `workRecord.fields[].field` mirrors a `works/` frontmatter key (no new schema — it reflects
     `website/schema/` + the record itself). The dive never writes `works/`; it *proposes*.
     `confidence` ∈ high | medium | low. `oldStyle`/`approximate` mirror the record's date fields.
   - `coverage[].status` ∈ covered | partial | not-covered — the structured surface map the
     "Material not covered" section is derived from and that multi-session resume reads first.
   - `ingestionPriority` (optional) ∈ 1 | 2 | 3 — the order the wiki pages should be written:
     **1** = central, write first (the entities the dive is *about*); **2** = supporting; **3** =
     peripheral / mentioned. `dependsOn` (optional) lists the `name`s of entities that should exist
     first (e.g. an `event` page reads better once its key `person`/`concept` pages exist). Together
     they turn the flat routing map into a sequenced ingestion plan; the Phase-6 entity work-order
     should present the `missing`/`stub` entities in priority-then-dependency order.
3. **`website/src/posts/notes/<YYYY-MM-DD>-<slug>.md`** — frontmatter `title` / `description` / `date` /
   `tags` / `draft: true`. A short recap in the project voice (simple, factual, minimal editorial),
   linking to `index.md`. Stays `draft: true` until the user publishes.
4. **`docs/research/<slug>/index.html`** — generated from `index.md`, never hand-written. The docs
   tree has one canonical generator: `python3 docs/serve.py --build-only` converts every
   `docs/**/*.md` to a sibling `.html` (house CSS, breadcrumb header, per-document annotation UI) and
   rebuilds `docs/INDEX.html` so the new dive is listed. Run it after `index.md` is final. The `.html`
   files are **git-ignored** (`docs/.gitignore`: `*.html`) and regenerated on demand — so `index.md`
   is the sole source of record: don't hand-edit or commit the HTML, just re-run `serve.py` after edits.

## Phase 5 — Verify (separate pass; never self-approve)

**First, run the mechanical gate:** `python3 docs/research/lib/verify_quotes.py
docs/research/<slug>/dossier.yaml`. It asserts every `evidence[].quoteRu` appears verbatim in its
named `extract` file (and that declared `facsimile:` files exist). This must exit 0 (PASS) before
the human-judgement verifier runs — it turns byte-fidelity from a sampled LLM check into a complete
deterministic one. Fix any mismatch (or, if the divergence is a genuine source variant, re-extract)
until it passes.

Then dispatch a **verifier subagent (opus)** in a fresh context for the judgement-level checks the
script cannot make. It checks: a sample of citations re-derived from TEI/PDF for **byte-fidelity**
(belt-and-braces on top of `verify_quotes.py`); every **primary** `index.md` claim is source-anchored; **scholarly/secondary claims are
*attributed* (not asserted) and a named source / References-list entry backs every claim — no
byte-fidelity is demanded on secondary sources (prototype rigor); `scholarship.triangulation`
entries reference valid `evidenceRef`s and use a valid `relation`**; dossier
entities resolve to valid wiki types with accurate `vaultStatus`; translations are labelled; no
editorializing voice; `extracts/` holds only PD facsimiles, `visuals/` is git-ignored, and **no
rights-reserved/unknown image was committed or placed in `website/src/`** (downloads into the
git-ignored `visuals/` cache are fine; each carries a `licence` in the dossier).

For **work dives** it additionally checks: `workRecord` proposals are evidence-anchored (no
fabricated dates/venues) and their `field` names match the `works/` record schema; the
`coverage` ledger is honest (no `covered` the evidence shows is really `partial`); and the
standing spine sections obey the bare-voice / attribute-don't-assert rules.

Iterate until
the verdict is clean; in `--auto`, if it cannot converge after a few iterations, record the open
items in `needsReview` and conclude the run rather than blocking indefinitely.

## Phase 6 — Handoff

Produce a summary: what was covered, the `notCovered` queue, the **entity work-order** (which wiki
pages this dive feeds — present the `missing`/`stub` entities in `ingestionPriority`-then-`dependsOn`
order so it reads as a plan, not a flat list), the **visuals work-order** (images/facsimiles to
acquire or request), the **work-record work-order** (the `workRecord` proposed fills grouped by confidence, for human ingestion into the `works/` record), the **coverage ledger** (covered / partial / not-covered surfaces), and the draft note path. Remind that wiki ingestion is a separate, human-in-the-loop step — the
dossier is the pointer, not the writer. **Interactive:** print it. **`--auto`:** write it to
`docs/research/<slug>/run-report.md` (scope contract, coverage, `notCovered`, `needsReview`,
models used + rough cost note, output paths, the **evaluation self-assessment** (work dives)).

## Multi-session dives

A broad theme may exceed one session. At the start of any dive, if `docs/research/<slug>/`
already exists, **resume** from its `session-log.md`, the dossier's `coverage:` ledger (the structured surface map — read this first), and the `notCovered` queue (free-text overflow) rather than re-sweeping. For such dives, keep an append-only `docs/research/<slug>/session-log.md`
(what each session covered) and treat `notCovered` as the resume queue.

**Resuming a *completed* dive to add Phase 3** (enrich, not re-sweep): when the primary layer is
already locked, the existing `index.md` narrative + the dossier `evidence` ledger **are** the
Phase 2 inputs Phase 3 reads — there is no live Phase 2 handoff. Leave the primary evidence and
voice untouched; add only the `scholarship:` block, the "Scholarly context" section, and the
secondary references, then re-verify.

**Retrofitting a pre-corpus-dive survey** (the `index.md` predates this skill — e.g. an early
`docs/research/<slug>/` written in the hand-authored copyright-renunciation style, with `extracts/`
but **no `dossier.yaml`**): treat the existing prose as **locked Phase-2 output**, not raw material.
Do **not** re-sweep, re-translate, or rewrite the narrative — its quotes are already byte-faithful
and its voice is already settled. Instead:
1. **Back-fill the structured layers from what's there.** Build `dossier.yaml` by reading the
   existing `extracts/` and the narrative's citations into `evidence` rows (run `verify_quotes.py`
   to confirm each `quoteRu` you transcribe is verbatim), then derive `entities`, `scholarship`,
   `contradictions`, `notCovered`, `needsReview` from the prose.
2. **Add only what the original lacked** — typically the visuals sweep (+ the "Visual & manuscript
   record" section), the dossier, and the draft note. Make targeted *additive* edits to `index.md`
   (a new section, embedded figures, dossier/note pointers); do not touch the frozen quotes.
3. **Re-derive evidence from the existing extract files, don't re-translate** — if a working-English
   line already exists in the prose, port it; only translate text the original never rendered.
4. Bump `lastUpdated`, add a `session-log.md` entry recording the retrofit, then run Phase 5.
This is distinct from the two resume modes above: there is no `notCovered` queue to resume from and
no Phase-3 handoff — the *whole structured apparatus* is being added under a finished narrative.

## Voice & language

`index.md` and the note in English; cited foreign titles kept verbatim; working-English
translations labelled; minimal editorial. Interactive → escalate genuine editorial judgment to the
user; `--auto` → defer to `needsReview`.

**Unwrapped prose (nl2br).** serve.py renders Markdown with the `nl2br` extension, so every source
newline *inside* a block becomes a literal `<br>` in the HTML — a hard-wrapped paragraph renders as a
ragged column of `<br>`s. Write each paragraph, blockquote, and list-item as **one source line** (do
not hard-wrap); make the `Date:` / `Context:` preamble two separate paragraphs (blank line between);
keep a blank line before every list (and after a bold/italic label that precedes one). Headings,
frontmatter, tables, fenced code, and raw `<figure>` HTML are unaffected.
