# Interactive Reader's Editions — the go-forward workflow (design)

> Approved design from the 2026-06-30 brainstorm. It wraps the machinery plan [`2026-06-29-interactive-reader-editions.md`](../plans/2026-06-29-interactive-reader-editions.md) with the *workflow* around it: what runs unattended, where files live, how translation and annotation work, and what the "re-dive" actually produces. Execution is a separate session.

## Context

The pipeline **machinery is already built** (`reader/` at the repo root — `segment.py`, `speech.py`, `build_xhtml.py`, `build_epub.py`, `validate.py`, `ids.py`, `paragraph_ids.py` + a full test suite; reported green on fixtures). But it has **never run end-to-end on a real work** — there's no built edition output and no audio yet.

Johan wants a repeatable, mostly-unattended way to turn **each Tolstoy prophet-period work** into a reader's edition (web + read-along EPUB + synced audiobook), then read it to form his editorial voice, then feed that voice into the site's content. This brainstorm settled the workflow and corrected several things the single-work machinery plan missed.

**The biggest reframe:** the corpus dives were always a *förstudie* (pre-research) whose real purpose was helping Johan find his editorial voice before LLM ingestion. The reader editions change *where* that voice forms — now it forms by **reading the actual work**, not research about it. So the dive drops to *cited substrate*, and **Phase 3 becomes the front door of the wiki/works ingestion**, not a separate research step.

---

## The three-phase loop (run per work)

### Phase 1 — Build (light prep, then unattended)

- **Phase 1a — light human prep (Johan, before the machine):** pick the work; pull the authoritative Russian from the corpus TEI; **declare which English translation is canonical** when several exist; set the section structure. This is **batchable** — prep several works ahead, then let the machine work through them.
- **Phase 1b — unattended machine build:** machine-translate Russian→English (Claude, a *faithful, readable one-pass* rendering), then build the formats from the one segmented source. The **web edition is `serve.py` rendering the bundle's markdown live** (interactive); the **read-along EPUB** and **synced audiobook** are the built artifacts. 1b is the part the nightly queue automates (see *Industrializing* below).
- **Three text layers per work:**
  - **Russian PSS** — the spine. Canonical. Paragraph IDs, structure, and every editorial mark anchor to it. Always present.
  - **Published English** (Maude etc.) — what the reader opens by default, where one exists. Johan picks the canonical one when there are several.
  - **Machine English** — faithful one-pass, always generated. The default reading text *only* when no published translation exists; everywhere else it's the neutral fidelity ruler.
- **Fidelity check (no burden on Johan):** an automated diff of the published English against the literal machine English flags where the translation softened or dropped Tolstoy → `{==clause==}{>>dropped from the … English<<}` marks (the "translation diagnostic" already designed in `_interactive-edition-bundled-text.md`). The machine translation is **not proofed** — it stays raw by design.

### Phase 2 — Read & annotate (Johan, present)

- Read the default English while listening to the synced audiobook.
- **One annotation stream**, every note free-form. An **optional "needs a text fix" flag** marks notes that point at a source change (typo, OCR slip, audio/text mismatch, rough MT patch).
- Nothing is forced into bins (an edit can carry editorial meaning too):
  - *All* notes feed Phase 3.
  - The *flagged* ones **also** form a fix-list that loops back to correct the source and rebuild.
  - A single note can be both a fix and a reflection. The flag colors it in the reader (a small wrench) for visual distinction — it is not a wall between two kinds.

### Phase 3 — Reconcile = the front door of ingestion (Johan + LLM)

- Reading the work *is* the förstudie now. The academic dive becomes **cited substrate** (genesis, textology, dates, provenance) reconciled against — backstage, not reader-facing as-is, retained for its citations.
- Reconciling Johan's reflections (collected in the dive's `annotations.md`) against the dive **produces the real content**: the work's overview page + the steer for the paired wiki entities. **Per-work judgment call** — no rigid output rule; the pattern is set by doing the first one together.
- **Voice:** minimal editorializing made concrete — *prefer his words; own the unavoidable choices* (selection, ordering, grounding in his terms over the academy's); *flag genuine judgment calls for Johan*. ("Editing" is unavoidable and his to own; "editorializing" — imposing opinion — is what's minimized.) This is the existing **Voice target** rule.
- "Re-dive" and "LLM ingestion editorial steer" are **the same moment**.

> Scope boundary: this design defines the **handoff into** ingestion (what Phase 3 produces and in whose voice). The full LLM-ingestion mechanics are their own design — fed by this, not specified here.

---

## How works and wiki pair up

- The work's **overview page IS the work's node** — there is no separate wiki article for a work (`website/src/works/<cat>/<subcat>/<Title>.md` is canonical for it). During development the overview lives in the work's bundle as `overview.md` and **graduates** to `website/src/works/...` on publish.
- The **entities** the work touches (persons, places, concepts) are the wiki — one shared `[[wikilink]]` namespace across both.
- The reader edition's `[[wikilink]]` marks become the **entity work-list** for ingestion: reading the work surfaces exactly which entities matter. Phase 3 covers the overview page + those marked entities, in one voice.

---

## Directory structure — three tiers, self-contained work folder

The produced editions are **durable content**, not throwaway output, and not immutable primary sources either. Three tiers:

1. **Immutable primary** — the TEI/XML. Stays in `primary-sources/` (organized by provenance, never touched, not bundled per work).
2. **Produced editions (durable content)** — the markdown editions + overview, **bundled per work**.
3. **Regenerable build artifacts** — segments.json, timing.json, the `.epub`, audio. Derived from tier 2; gitignored.

The per-work bundle is **self-contained**, mirroring the site's `/works/<category>/<subcat>/<id>/`:

```
docs/reader/<category>/<subcat>/<id>/      ← the work's bundle (tracked content)
   <id>.ru.md                              ← Russian reading text (the spine)
   <id>.en-machine.md                      ← machine translation (faithful one-pass)
   <id>.en-<translator>.md                 ← published translation(s), wikilinks infused
   overview.md                             ← the work's overview page (→ graduates to website/src/works/)
   annotations.json                        ← Phase 2 notes (one stream + fix flag)
   build/                                  ← gitignored: segments.json, timing.json, .epub, audio/
```

- The **engine stays at root** (`reader/`) — it's an imported package; `serve.py` already imports it; `projects/` is gitignored separate-repos so the engine can't live there.
- `serve.py` serves all of `docs/`, so it **previews straight from the bundle** (renders the `.md` editions live; serves the `.epub`/audio from `build/` for the read-along).
- The **audiobook repo** (`projects/audiobook/`) writes the per-section audio into the work's `build/audio/` via the segments.json↔timing.json contract.
- Reflections also land in the dive's `annotations.md` (the existing per-dive seam) as Phase 3 input.

---

## The works tracker (generated sortable table)

A master table of every prophet-period work, built **from the works metadata** (schema sidecar `.data.yaml`) **+ the dives** (PSS location, dates) **+ a lightweight per-work status** — rendered as a **sortable HTML table** (like the research index), viewable in `serve.py`, exportable to CSV. It's the run-list *and* the progress board.

- **Columns:** title · type (novel · essay · treatise · play · story…) · date-period written · PSS location (vol:page) · available English translation(s) · canonical translation · where in the loop (dived · built · read · re-dived · ingested) · ready-for-ingestion.
- **Status** derives from artifact presence where it can (e.g. a `build/` exists → built) plus a small per-work status field for the human-judgment stages.
- It also **surfaces gaps** — which works still lack a schema record — so the run-list stays honest.

---

## Small additions (status — the plumbing landed 2026-06-30)

Everything else was already built; these were the gaps. The first four landed this session:

1. **Self-contained bundle + gitignore** — ✓ done. `docs/reader/<cat>/<subcat>/<id>/` is the tracked bundle; `docs/reader/**/build/` is ignored (regenerable artifacts). The audiobook now writes timing + per-section audio into the bundle's `build/` (derived from the segments-file path, so audio → `build/audio/`).
2. **Canonical-translation flag** — ✓ done. Added `translationEditions[].readerDefault` (boolean) to the works schema §8 (v10), Johan-approved. *Correction to this spec:* the schema defines the translation arrays as a `.data.yaml` sidecar, but **no sidecars exist yet** — so the flag is live in the schema and the tracker reads it, but it stays blank until a work's sidecar is first authored in light-prep.
3. **Annotation fix flag** — ✓ done. `serve.py` annotations carry an optional `needsFix` boolean (the wrench): a checkbox in the popover, a dashed underline + wrench on the mark, carried through the existing export/import. Backward-compatible, no migration.
4. **Works tracker generator** — ✓ done. `docs/reader/lib/build_works_tracker.py` → `docs/reader/index.html`: a sortable, searchable, CSV-exportable table built from the dives + works records + the hand-kept `docs/reader/status.yaml`. Auto-runs in `serve.py`; it surfaces the gap (53 of 68 works have no record yet). *Note:* it lists every dived work, not only prophet-period ones — the Period column marks which belong.
5. **Update the existing plan + spec** — ✓ done. This status block, plus a "superseded paths" banner on `docs/superpowers/plans/2026-06-29-interactive-reader-editions.md` and on the all-formats spec, both pointing here as the source of truth.

---

## Pilot and order

- **Finish The Great Sin first** — it's furthest along (dive done; the *A Great Iniquity* audiobook exists). The pieces left: run the web + read-along build to **prove sentence-sync in Apple Books**, and the **Phase 3 re-dive** with Johan's reflections on the existing dive.
- **Then A Confession** — the first work through the *full* unattended loop from scratch, so the real test of "repeatable."
- **Then one by one**, sequenced off the works tracker — once the loop is proven, the machine build (1b) runs as a queue (see below); run order seeded from `docs/research/_prophet-period-nonfiction-dives.md`.

---

## Industrializing Phase 1 — the nightly build queue (once proven)

Once The Great Sin and A Confession prove the loop, the **machine build (1b) becomes a queue**: it picks the next *prep-done, build-pending* work off the tracker and builds it — **one work per run, gated by the available token budget** (the MT leg spends Claude tokens; the run stops when the budget is spent). It can run **as a nightly cron** (precedent: the overnight `docs/research/lib/corpus-dive-queue.sh`). The human prep (1a) is batched ahead, so the cron only ever touches works Johan has already prepped — nothing unattended runs without his structural decisions in place. The tracker is the queue's source of truth: what's prepped, what's built, what's left.

---

## Verification (how we know the loop holds)

- **Phase 1:** `python3 -m pytest reader/tests/ -v` green; build The Great Sin → its `build/` holds segments.json, timing.json, `.epub`, per-section audio; `verify_quotes.py` passes on the Russian; EPUB validates (EPUBCheck/ACE skip-with-warn).
- **Read-along proof:** the EPUB highlights sentence-by-sentence in sync in **Thorium Reader** (the EPUB3 media-overlay reference reader), with the *recorded* voice firing — not Thorium's silent TTS fallback. *Correction (2026-06-30, pilot): the original target was Apple Books, but Apple Books renders media-overlay read-along **only for fixed-layout books** (per Apple's Books Asset Guide: "read aloud content is supported only in fixed-layout books") — a reflowable prose edition gets no narration control there, on Mac or device, by design. We keep the edition reflowable (resizable type, accessibility) and treat **Thorium / Readium / Kobo and the web edition** as the read-along surfaces. EPUBCheck-clean confirms the file itself is correct; a fixed-layout Apple-only variant is possible but deliberately out of scope.*
- **Phase 2:** annotations save with the fix flag; the fix-list exports; reflections land in `annotations.md`.
- **Phase 3:** The Great Sin taken from reflections → overview page + entity steer, in Johan's voice, with the dive as cited substrate.
- **Tracker:** renders as a sortable table, columns correct, status reflects the real state of at least The Great Sin and A Confession.

---

## What this is NOT

- Not building all ~30 editions at once — prove the loop on The Great Sin, shake it out on A Confession, then go one by one.
- Not re-running the 33 existing dives — they become cited substrate; Phase 3 runs per work as it enters the reader pipeline.
- Not proofing the machine translation — raw by design.
- Not moving the engine or rewriting the green machinery for cosmetics.

---

## Working constraints (Johan)

- Plain language, no engineering jargon, in every doc and commit message.
- Commit freely as work lands; **never `git push`** — provide the exact push commands instead.
- The audiobook repo (`projects/audiobook/`) commits/pushes separately from the parent.
