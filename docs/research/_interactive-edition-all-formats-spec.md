---
layer: reference
lastUpdated: 2026-06-28
tags: [research, planning, design, website-launch, epub, audiobook]
title: "Interactive reader's editions — all formats from one source (design)"
---

This is the design for producing **all the reader-facing formats of a work** — the interactive web
edition, a read-along EPUB3, and the synced audiobook — from **one durable marked-up source file**.
It is the worked-out successor to, and supersedes the scope of,
[`_interactive-edition-bundled-text.md`](./_interactive-edition-bundled-text.md) (the June-23 "spec 1",
web-only) and its plan [`_interactive-edition-plan.md`](./_interactive-edition-plan.md). The pilot is
**The Great Sin** (`docs/research/1905-the-great-sin/`), whose audiobook ("A Great Iniquity") is already
built in `projects/audiobook/`.

The goal of this first effort is **to prove a repeatable pipeline**, not to hand-polish one edition.
Success = the path from one source to all three formats is clear enough to repeat on the other dives.

---

## Governing principle — Tolstoy's voice, not the mainstream filter

The reading text, the overview, and the dives present the work **in Tolstoy's own terms** — his voice,
his version — neither softened by mainstream labels nor sharpened past what he wrote
(the dives' existing rule: `corpus-dive-ground-in-primary-not-mainstream`,
`ingestion-accuracy-both-directions`).

## The single source

The **CriticMarkup Markdown** is the one durable thing you edit. One file per *version* of the work,
all sharing the same section anchors:

- `the-great-sin.ru.md` — Russian (the canonical **spine**; the PSS established text)
- `the-great-sin.en-1905.md` — "A Great Iniquity" (Tchertkoff & Mayo, 1905) — the **default** reading version
- `the-great-sin.en-machine.md` — machine English (the neutral comparison version)
- `overview.md` — the reader-facing "about this work" page (distilled from the dive's `index.md`)

These stage in `docs/research/1905-the-great-sin/reader/`, derived from the dive's `dossier.yaml` +
`extracts/`. The Great Sin needs **no transcript cleaning** — its text is already clean digital
(corpus TEI for Russian; Wikisource for the 1905 English).

### `tl` is a tool, not a rival source

The `tl` toolset (`tools/`, a Standard Ebooks fork) does **two separable jobs**: (A) turn messy scans
into clean text (OCR → clean → typography — what the Birukoff biography needed), and (B) package clean
text into a distributable epub (`tl build`). For corpus-sourced works like The Great Sin, **Job A is
irrelevant** (the text is already clean), and for this proof we build the epub with **ebooklib**, not
`tl build` (reason below). The Markdown source sits between `tl`'s two jobs; it is the canonical
enriched source, and `tl` is reached for only when a work's text must be *manufactured* from scans.

## The keystone: a two-layer ID scheme

Everything downstream keys to stable IDs in the text. **IDs are the granularity knob** — a reader
syncs/links at the finest level the markup carries IDs — so we deliberately carry two layers, because
they do different jobs:

- **Paragraph IDs — the shared coordinate across versions.** `id="p-0004"`, zero-padded, stable.
  Paragraphs correspond across Russian/English; sentences usually do not (one English sentence ≠ one
  Russian sentence). So **citations, cross-version alignment, annotations, and deep-links anchor on
  paragraphs.** Stable across re-segmentation.
- **Sentence IDs — within-version, for read-along only.** Each sentence is a `<span id="p-0004-s02">`
  nested inside its paragraph, carrying *that* version's audio sync. Nesting under the paragraph ID
  keeps paragraph anchors stable even when sentences are re-split. (EPUB3 explicitly allows mixing
  granularities.)

This is the single most load-bearing decision: read-along, annotations, alignment, citation, and
deep-linking all ride these IDs.

## Segment once → shared artifacts

A small **segmenter** reads each version's Markdown and writes `segments.json`: per sentence, its
**ID**, its **display text** (faithful, what you read), and its **speech text** (the respelling +
flow rules currently in `flow_preprocess.py` and the build's `SUBS`, applied as a transform). One
segmentation feeds everything:

```
 already-clean sources ──► CriticMarkup .md ──segment once──►  segments.json
                                  │                                  │
        ┌─────────────────────────┼───────────────┐                 │
        ▼                         ▼                ▼                 │
   serve.py / web          ebooklib EPUB3      audiobook build ◄─────┘
   (renders the .md,       (display text +     (synth per sentence,
    annotations)            <span id> + SMIL    already tracks each
        │                   read-along)         sentence's start/end)
        │                        ▲                    │
        │                        └──── timing.json ◄──┘
```

`segments.json` is the clean hand-off between the main project and the separate `projects/audiobook/`
repo: JSON in, `timing.json` (sentence ID → start/end ms) out. No shared code across the two repos.

## The three derivations

### Web (serve.py / later Eleventy)
serve.py already renders the marked-up `.md` (CriticMarkup, footnotes, `[[wikilinks]]`; commit
`9d21bd94`). No new rendering engine. The web edition is where **interactivity lives** — toggleable
cut-reveals, wikilink modals, version switching, annotations. Default reading state stays bare.

### Audiobook
Rewire `build_audiobook.py` to read `segments.json` (instead of `chapters_flow/`) and emit
`timing.json`. The build **already tracks** each sentence's cumulative start/end time (it uses them for
chapter markers), so emitting the map is a handful of lines. Voice (`bm_daniel`), pauses, and mastering
are unchanged. The existing per-sentence WAV cache is preserved.

### EPUB3 (ebooklib + hand-built read-along)
A new builder. Clean reading text, each sentence wrapped `<span class="sentence" id="p-0004-s02">`, with
a SMIL Media-Overlay file (one `<par>` per sentence, `clipBegin/clipEnd` straight from `timing.json`)
that gives real **highlight-as-it-reads in Apple Books**. Key facts from the research:

- **Sentence-level sync is the sweet spot** — free given per-sentence TTS, no forced alignment, renders
  well in Apple Books + Thorium. Word-level needs forced alignment and reads "jumpy" — skip.
- **ebooklib does not generate SMIL** — it is a packager only (`EpubSMIL` is a content carrier). We
  hand-assemble the SMIL string and the metadata; ebooklib zips a valid container.
- **EPUBCheck is strict**: `media-overlay` attribute on the content item; SMIL as
  `application/smil+xml`; `media:duration` **per content document and a total**.
- **Apple gotcha**: Apple Books ignores `media:active-class` and applies its own CSS-controllable
  highlight — declare the class for Thorium/Readium, but verify the look on-device.

### The split rule: epub = resolved/static, web = interactive
In the **epub**, CriticMarkup is rendered **resolved and static** — cuts shown as styled deletions or
moved to endnotes, variants/softenings as notes — **not** live toggles. In-epub JavaScript is a trap
(most readers disable it; you'd build the static fallback anyway; it breaks screen-reader flow). The
live toggles stay on the **website**. CSS-only styling of deletions/additions in the epub is fine.

## EPUB3 features to include

**Build first** (well-supported; the source already mostly carries the data):

1. **Popup footnotes / endnotes** — `noteref` + `<aside epub:type="footnote">` + a backlink (↩). This
   is how **editorial notes, cut-explanations, and the work's own footnotes** appear in the epub.
   *Load-bearing rule:* Apple only pops up an `<aside>`; a `<div>`/`<p>` shows the note inline *and* in
   the popup. Two visually-distinct streams: editorial vs the work's own.
2. **Page-list with real PSS vol/page** — invisible `epub:type="pagebreak"` anchors + a
   `<nav epub:type="page-list">`, labelled "PSS 36:218". On-screen display is mostly Apple-only, but
   it's the correct machine-readable provenance regardless, and exactly the scholarly feature we have
   data for.
3. **Accessibility metadata** — mandatory in EPUB 3.3 and a public-good obligation (schema.org
   `accessMode`/`accessibilityFeature`/`accessibilityHazard`, `dcterms:conformsTo`). Read-along counts
   as `synchronizedAudioText`.
4. **Landmarks nav** — trivial; jump-points to the notes section and an "About this edition" page.
5. **`dc:source` / Dublin Core** — cite the PSS edition, translator, dates.

**Defer / skip:**

- **In-epub scripting** — skip (the split rule above).
- **Formal Dictionaries & Glossaries spec** — near-zero adoption; later, build a wiki-entity glossary
  via the same `noteref`/`aside` pattern instead.
- **Switchable bilingual in one file** — the Multiple-Rendition container is effectively unsupported.
  Instead: **separate per-language epubs**, or (later) a paragraph-interleaved study epub — feasible
  because the paragraph IDs align across versions.

**Validation gate:** every generated epub runs through **EPUBCheck** + **ACE by DAISY** (both free,
scriptable).

## Annotations (web)

serve.py already has a working annotation system saving to `localStorage` per document, so annotations
*do* persist across sessions in the same browser. Two upgrades, no backend:

- **Anchor to paragraph IDs**, not fuzzy text-matching — so annotations stop silently vanishing when the
  underlying text is edited, and become portable/shareable (the same anchor works in web and epub, and
  two readers' sets can merge). This reuses the keystone ID scheme.
- **Finish export/import** — "Copy annotations" → save to a file you can commit and reload; add the
  import side. `localStorage` stays the store.

## The encoding vocabulary

CriticMarkup (an existing plain-text standard) + the project's `[[wikilinks]]`, plus two small carries:

| Mark | CriticMarkup | Encodes |
|---|---|---|
| Excision | `{--…--}` | A passage cut before print (censor / editor / self-revision — named in the note) |
| Insertion | `{++…++}` | A passage added in a later draft/proof |
| Softening / edition diff | `{~~old~>new~~}` | A word/phrase changed between draft and print, or between editions |
| Note | `{>>…<<}` | The editorial fact (who, when, why); carry a **note-type** (editorial vs the work's own) |
| Highlight | `{==…==}` | Translation diagnostic (e.g. dropped from the 1905 English) |
| Wikilink | `[[Entity]]` | A person/place/concept |

Plus: **paragraph + sentence IDs** (assigned by the segmenter, not hand-written) and **PSS
page-boundary markers** (vol/page, from the dossier/extracts).

## What our setup additionally unlocks (opportunities, not first-build scope)

Because every paragraph/sentence has a stable, version-shared ID plus a timing map, several things
become cheap later:

1. **IDs fix annotations** (above) — robust, portable, shareable.
2. **Cross-version alignment** — click an English paragraph, jump to the same Russian paragraph.
3. **The timing map is more than read-along** — trivially also yields WebVTT subtitles (web read-along
   *and* a shareable text+narration video), resume-across-formats (stop the audio at `p-0004`, open the
   reader there), and per-paragraph permalinks (`…/#p-0004`) for "cite this passage".
4. **Citations as a feature** — IDs + PSS page data → *"A Great Iniquity, §IV — PSS 36:218"* with a
   stable deep link.
5. **"Watch the text grow"** — the CriticMarkup cuts/insertions keyed to IDs render the textual history.
6. **Wiki entities → in-book glossary** — via the noteref/aside pattern.

## Fidelity & guardrails

- `primary-sources/**` and the dive's `extracts/**` are untouched; the reader text is openly a derived
  edition. The Russian version's prose, with marks stripped, must match the source extract exactly.
- `verify_quotes.py` still guards every locked quote against the extracts.

## Outputs & layout

- Source Markdown → `docs/research/1905-the-great-sin/reader/`
- Generated artifacts (`segments.json`, `timing.json`, per-chapter audio, `.epub`) →
  `_generated/reader/the-great-sin/` (audio gitignored; regenerates).
- Later promotion: the source files move to `website/src/works/.../text/` at ingestion (the existing
  research → human-in-the-loop discipline). **CLAUDE.md fix needed** when that lands: `works/**/text/`
  is an *enriched reader's edition* edited on purpose — reword "source text, do not modify" to "don't
  corrupt the words."

## Scope of the proof

Prove the full chain end-to-end on a **vertical slice** (chapter I of The Great Sin) across all three
outputs: overview + the three versions, marked from the dossier, a sentence-timed read-along EPUB3 that
highlights in Apple Books, and the rewired audiobook emitting `timing.json`. Finishing the remaining
chapters is mechanical repetition (the whole audiobook already exists, so it's cheap).

## Out of scope (later)

- The bespoke Eleventy/PWA web reader, web read-along, "My Library", reading progress, PWA offline,
  reader comments. (The IDs + timing map leave them ready to build.)
- The `tl build` SE-imprint epub (library-grade clean edition; complementary to the read-along epub).
- Corpus-wide machine-translation or read-along as a batch job.
- The cross-dive generator that emits the version files + marks from a dossier at scale (build after
  this pilot is reviewed).

## Settled in this design

- **Goal** = prove a repeatable pipeline (generators over hand-polish).
- **One source** = CriticMarkup Markdown; `tl` is a tool (cleaning + epub-build), not a rival source.
- **Two-layer IDs** = paragraph (shared coordinate) + sentence (within-version read-along).
- **Spine** = the Russian PSS established text; **default version** = the 1905 English; **default state**
  = bare.
- **Read-along** = sentence-level; SMIL hand-built from `timing.json`; ebooklib packages.
- **EPUB build** = ebooklib (not `tl build`) for this proof.
- **epub = resolved/static, web = interactive.**
- **EPUB feature first-build** = popup notes/endnotes, PSS page-list, a11y metadata, landmarks,
  `dc:source`.
- **Annotations** = paragraph-ID anchoring + export/import; localStorage, no backend.
- **Validation** = EPUBCheck + ACE.

## Left for the implementation plan

- The segmenter's exact shape and `segments.json` schema.
- The Markdown→XHTML generator (sentence spans, note `noteref`/`aside`, pagebreak anchors).
- The SMIL builder + the package metadata (`media:duration` arithmetic).
- ebooklib wiring (set `.media_overlay`, add `media:*` and a11y meta by hand).
- serve.py annotation rework (paragraph-ID anchors; import side).
- Period-English sourcing/cleanup (fetch + clean the Wikisource 1905 text).

## Sources (research, June 2026)

- W3C: [EPUB 3.3](https://www.w3.org/TR/epub-33/), [Media Overlays 3.2](https://www.w3.org/publishing/epub32/epub-mediaoverlays.html),
  [Accessibility 1.1](https://www.w3.org/TR/epub-a11y-11/),
  [Multiple-Rendition 1.1](https://www.w3.org/TR/epub-multi-rend-11/)
- Apple: [Pop-up Footnotes](https://help.apple.com/itc/booksassetguide/en.lproj/itccf8ecf5c8.html),
  [Media Overlays Structure](https://help.apple.com/itc/booksassetguide/en.lproj/itcf373ff8f8.html)
- [Standard Ebooks Manual of Style](https://standardebooks.org/manual/1.8.8/single-page)
- DAISY KB: [Media Overlays](https://kb.daisy.org/publishing/docs/sync-media/overlays.html),
  [Page list](https://kb.daisy.org/publishing/docs/navigation/pagelist.html),
  [Landmarks](https://kb.daisy.org/publishing/docs/navigation/landmarks.html)
- [Thorium MO implementation notes](https://github.com/edrlab/thorium-reader/wiki/Implementation-notes:-EPUB3-Media-Overlays,-Readium-WebPub-Manifest-and-W3C-%22Sync-Narration%22),
  [Pettarin: Audio-eBooks with Media Overlays](https://www.albertopettarin.it/blog/2014/07/22/audio-ebooks-using-media-overlays-in-reflowable-epub-3-ebooks.html)
- [ebooklib source](https://github.com/aerkalov/ebooklib/blob/master/ebooklib/epub.py)
- Tools: EPUBCheck, [ACE by DAISY](https://daisy.github.io/ace/)
