---
layer: reference
title: "Interactive Reader — prototype (v1) design"
lastUpdated: 2026-07-03
tags: [reader, interactive-edition, spec, pwa, the-great-sin]
---

# Interactive Reader — prototype (v1)

The reading surface for tolstoy.life: a clean e-reader by default, with
read-along audio, and annotation that works on **any** text in the project —
the work, the corpus dive, the works overview page. Built by expanding
`docs/serve.py` (which already renders every `docs/` file and already has a
select→comment→export annotation layer), so the prototype grows out of what
runs today rather than starting fresh.

**Pilot:** The Great Sin, whose reader-edition is already built — the 1905
English edition, the paragraph-aligned Russian spine, and the read-along audio
(`docs/reader/non-fiction/essays-and-criticism/the-great-sin/`,
`segments.*.json` + `timing.en-1905.json` + per-section `.m4a`).

**Visual reference:** the four UI drafts + the locked decisions —
[The Reader — UI drafts](https://claude.ai/code/artifact/a22a1f08-b163-4abf-9615-ca87ccaef765)
(private Artifact, 3 July 2026 brainstorm).

---

## How this fits the existing plans

This is **"spec 2 — the e-reader website UI"**, which the earlier docs
deliberately parked (see `_interactive-edition-bundled-text.md` "Out of scope"
and `_interactive-edition-plan.md` §"Spec 2"). Rather than wait for the
Eleventy build, we pull it forward into `serve.py` as a working prototype, then
port to the site later. The other docs are unchanged and remain authoritative
for what they cover:

- **Content pipeline** (one source → web + EPUB + audio): `_interactive-edition-all-formats-spec.md`.
- **Reader-editions loop** (build → read+annotate → re-dive): `2026-06-30-interactive-reader-editions-workflow-design.md`.
- **PWA architecture** (offline, storage, sync): `docs/pwa/` — this spec pulls in only the *data-shape* decisions from it and leaves the infrastructure for later (see §Later).

---

## Scope

### In v1 (the prototype)

- The full **reading experience** below: focus mode, Zen fullscreen, one scroll, the top bar, the Tools overlay (Display / Layers / Version), the audio transport, the hairline progress, the return-to-overview affordance.
- **Read-along** for The Great Sin (English), driven by the existing `segments`/`timing` data.
- **Annotation** on every doc, saved in the portable open-standard shape (below).
- The **web table of contents** (upper-left, from the chapter headings) — newly designed here; it never existed.
- Wired to render both **works** (rich: read-along, layers, version switch) and **plain docs** (the reading shell + annotation only).

### Left for later — the `docs/pwa/` stages

Deferred, and safe to defer because the v1 annotation *shape* (below) is the only expensive-to-change decision, and we make it now:

- Offline download of a work + install-to-home-screen (Cache API / Workbox, install guide).
- The larger local database (IndexedDB) and the no-DOM-mutation highlight rendering (CSS Custom Highlights API).
- Cross-device **sync + QR pairing** (Yjs/CRDT relay).
- Content-addressed **version stamping** + the note **re-anchoring** engine.
- Bookmarks · in-text search · reading-progress (1%→100%) · per-work update log · reader comments.
- "My Library" — the **works tracker** (`docs/reader/index.html`, already built) is the de-facto library/home for now; reconcile the two later.
- The **PSS page-list** as a second TOC axis (the data is already in `segments.json` as per-paragraph `pss`).
- The Thorium bug where **clicking a paused narration restarts it** — v1 keeps read-along control explicit; the finer "don't resume on select/click" polish is a later refinement (Johan's call).

---

## The reading experience

All of this is one **universal reading shell** wrapping every `docs/` page.
Plain docs (the dive, notes, specs) get the shell + annotation. Works
additionally light up read-along, the editorial layers, and the version switch.

### Focus mode is the default; Zen is the fullscreen toggle

The page opens **bare** — good type, the text alone, every enrichment off.
**Focus / Zen mode** (our name for Thorium's "Zen") is the fullscreen toggle
(the corner icon): it hides all chrome and centers the column. Chrome fades
when idle and returns on mouse-move, so the gear stays reachable *inside* focus
mode.

### One continuous scroll — never paginated

A single scrolling column. No pages. This removes a whole class of Thorium
bugs at the root (the marker jumping to the wrong page). Reading position *is*
the scroll, shown as a **hairline** at the top edge — not a fat progress bar.

### Top bar — minimal

Four affordances only: **Contents** (list icon, upper-left) · **Notes** ·
**Tools** (gear) · **Focus** (fullscreen). The standalone `Aa` is gone — type
lives in Tools.

### Tools — an overlay, not a reflow

The gear opens Tools as an **overlay** that floats above the page: in the empty
margin on a wide screen, over the text on a narrow one. The reading column
**never moves** (no reflow → your line breaks and scroll position stay put).
Closable with `×`; reachable in focus mode.

- **Display** — text size · **line length** (in `ch`, default **66**, range ~48–82, with a live "NN ch" readout) · theme (paper / sepia / dark). All remembered between visits.
- **Layers (opt-in, works only)** — wikilinks · editorial cuts (CriticMarkup) · footnotes. Off until summoned; `serve.py` already renders all three marks.
- **Version (works only)** — RU / EN / MT, single column. Split view is drawn but **deferred**.

### Bottom audio transport + return affordance

A **slim** bar, shown only while read-along is on: play/pause, seek, elapsed/total, and the **speed** switch (kept — Johan values it). A **Home/back** affordance returns to the work's **overview page** and the **works tracker** (the library) — the "close the book, see where it sits" move.

### Fluid type — good without tweaking

Size and measure adapt to the viewport via `clamp()`, so the reader is
well-set on a laptop *or* a 27″ display **without touching a setting** — the
Apple Books failure (no measure control in fullscreen → unreadable long lines),
fixed. The `ch` unit ties the column to the actual font. The manual controls
fine-tune a good default; they don't rescue a broken one.

---

## Read-along

**Data (already exists):** `segments.en-1905.json` (sections → paragraphs →
sentences, each with a stable id + display + speech text), `timing.en-1905.json`
(`clips[sentenceId] = {section, begin, end}`, section-relative), and per-section
`the-great-sin.sec-N.m4a`.

**Behaviour:** load the current section's audio; on `timeupdate`, highlight the
sentence whose `[begin, end]` spans `currentTime` and keep it in view
(auto-scroll follow); click a sentence to seek to its `begin`; play/pause/speed
on the transport. Vanilla JS, no library. English only (it's the version with
audio); switching to RU/MT hides the transport.

**Coexistence with annotation (the Thorium fix):** the two highlights use
**different visual channels** so neither hides the other — read-along is a
yellow **background wash**; an annotation is an **underline + margin marker**.
On a sentence that is both, you see the wash *and* the underline.

---

## Annotations (universal)

The reason for the build: mark up the work *and* other texts (the dive, the
overview) in one comfortable reader.

- **Making a note** — select text → a small popover to write it (carried from `serve.py`). A margin marker shows an annotated line; hover/click shows the note; the optional 🔧 "needs a text fix" flag stays.
- **Seeing notes back** — the **Notes** panel (its own top-bar icon → slide-in list), scannable, jump-to, with export/import.
- **Works on every doc** — the shell is universal, so the same annotation UI covers the work, the dive, and the overview page.

### The saved shape — portable open standard (decided for v1)

`serve.py` already stores each note as `{paraId, text, before, after}` — which
is essentially the W3C Web Annotation model's **TextQuoteSelector** (exact +
prefix + suffix) already. v1 formalises this into the portable shape so notes
are **yours forever** and exportable to tools like Hypothes.is / Readwise —
nearly free, since it's mostly renaming what we already capture:

- **target** = the doc/work **URI** (`serve.py`'s existing `doc_key`, e.g. `docs/reader/…/the-great-sin` + `#sec-N`) — a stable identifier to anchor to.
- **selectors** = `TextQuoteSelector {exact, prefix, suffix}` (from the current anchor) **+** `TextPositionSelector {start, end}` (character offsets, added for robustness).
- **body** = the note text (+ the optional needs-fix flag).
- **export** = W3C-shaped **JSON-LD**; keep a plain-Markdown export as a convenience.

**Storage:** the browser's simple local storage (`localStorage`) for v1 —
enough for text notes on a single device, and trivially migratable to the
larger local database (IndexedDB) when the PWA stages land. We build the durable
*shape* now, not the durable *machinery*.

---

## Architecture — how `serve.py` becomes this

`serve.py` already: rglobs every `docs/**/*.md`, renders Markdown +
CriticMarkup + footnotes + `[[wikilinks]]`, calls `add_paragraph_ids`, and
injects the annotation UI + CSS into a full page. v1 adds:

1. **The reading shell** — the top bar (Contents/Notes/Tools/Focus), the Tools overlay, focus/Zen mode, fluid type, theming, and the settings store — applied to **every** rendered page. Mostly CSS + one vanilla-JS module; the annotation layer already present is folded into it.
2. **The work-reader render path** — when a page is a reader-edition (has a `segments.*.json`), render the body from **`segments.json`** so each sentence is a `<span class="sentence" id="…">` inside `<p id="…">` — exactly the markup `reader/build_xhtml.py` already produces for the EPUB, so `timing.json` lines up. Reuse `build_xhtml.py`'s sentence-span rendering (adapt the EPUB footnote asides to web popovers). This is the lazy reuse — the EPUB path already solved sentence segmentation.
3. **Read-along JS** — loads `segments`/`timing`/`.m4a`, does the highlight-follow + click-to-seek + transport described above.
4. **Version switch** — swaps which single edition file renders (`.ru` / `.en-1905` / `.en-machine`), by the shared `{#sec-N}` section anchors.
5. **TOC + return affordance** — Contents drawer from the section headings; Home/back links to the overview page + the works tracker.

Plain docs skip 2–4 and just get the shell + annotation.

**Boundaries respected:** `primary-sources/**` and the dive `extracts/**` stay
untouched; the reader-edition `.md` files are the enriched source of truth;
`build/` stays gitignored/regenerable.

---

## Navigation, overview, TOC

- **TOC** — newly designed (a web TOC never existed). Upper-left **Contents** drawer, built from the work's chapter headings (`## {#sec-N}`); left-side, separate from the right-side Tools so navigation and settings don't fight. PSS page-list is a later second axis.
- **Overview page** — the work's own page (`type: work`, homed in `works/`, distilled from the dive); `[[The Great Sin]]` resolves there and backlinks collect there. The reader **embeds** its `[[wikilinks]]` (toggleable) and links **back** to it.
- **Library / home** — the **works tracker** (`docs/reader/index.html`, already generated by `build_works_tracker.py`) is the reader's home surface; the reader links back to it.

---

## Verification

Observable in the `serve.py` preview, so verify there:

- **Read-along sync** — for a sample section, the highlighted sentence's `[begin,end]` contains `currentTime` throughout playback; clicking a sentence seeks to its `begin`. (Guard: reuse the existing words-per-second sanity check that already catches out-of-sync timing.)
- **Highlight coexistence** — a sentence that is both under the wash and annotated shows *both* (wash + underline), on any theme.
- **Annotation shape** — an exported note validates as W3C Web Annotation JSON-LD (target URI + TextQuote + TextPosition selectors) and re-imports/re-anchors on reload.
- **Fluid type** — at a narrow and a wide viewport, the measure stays within ~48–82 ch with no setting changed.
- **Universal shell** — the dive (`docs/research/1905-the-great-sin/index.md`) and the overview render with the shell + annotation but **no** transport/version chrome.

Keep tests lean: one runnable check for the read-along sync mapping and one for
the annotation round-trip (save → export → import → re-anchor); no framework.

---

## Later — the PWA stages (deferred, and why it's safe)

Everything in §Scope "left for later" comes from `docs/pwa/` and is genuinely
staged there. It's safe to defer because the **one** expensive-to-reverse
decision — the annotation record shape and its stable target URI — is made in
v1. Offline caching, IndexedDB, CSS Custom Highlights, Yjs sync + QR pairing,
version stamping, bookmarks, search, reading-progress, and the public
annotation layer all layer on top of that shape without redoing the notes made
in the prototype.

---

## Non-goals / open questions

- **Split view** (two columns RU/EN) — drawn in the rail, not built in v1.
- **Machine-translation edition** — the MT version slot exists in the switch, but generating the MT pass for The Great Sin is separate work (the reader just renders a file if present).
- **Read-along for RU** — no Russian audio exists; the transport hides on RU/MT.
- Whether the work body renders from `segments.json` display text directly or re-runs the Markdown/CriticMarkup per sentence is an implementation detail for the build session (both preserve the sentence IDs `timing.json` needs).

---

## References

- Build assets: `docs/reader/non-fiction/essays-and-criticism/the-great-sin/{segments.*.json, build/timing.en-1905.json, build/audio/*.m4a}`
- Reader engine: `reader/{segment.py, paragraph_ids.py, build_xhtml.py, ids.py, speech.py}`
- Doc server: `docs/serve.py` (current render + annotation layer)
- Earlier design: `docs/research/_interactive-edition-{all-formats-spec,bundled-text,plan}.md`; `docs/superpowers/specs/2026-06-30-interactive-reader-editions-workflow-design.md`
- PWA architecture: `docs/pwa/{local-first-architecture, yjs-schema-and-sync, tl-pipeline-integration, wiki-integration}.md`
- UI drafts (visual): https://claude.ai/code/artifact/a22a1f08-b163-4abf-9615-ca87ccaef765
