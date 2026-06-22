---
layer: reference
lastUpdated: 2026-06-22
tags: [research, planning, design, website-launch]
title: "Interactive reader's editions — bundling each dive's text (design)"
---

This is the design for bundling the **text of the work** into each corpus-dive folder as an
enriched, marked-up Markdown file — so a finished dive carries not just the research index and
dossier, but a draft of the **work's overview page** and a draft of the **work itself**, ready
to become an interactive reader's edition on the site.

It is the worked-out successor to the deferred brainstorm note (`project_dive_bundled_text_brainstorm`,
2026-06-22). The pilot is **The Great Sin** (`docs/research/1905-the-great-sin/`).

---

## The split: this is spec 1 of 2

The conversation produced two clearly separable pieces. **This spec covers only the first.**

- **Spec 1 — dive-side content (this file).** What a dive produces on disk: the marked-up text
  file, the overview-page draft, the machine-translation pass, and the small `serve.py` changes
  that let us *see* the reading page in the research preview. This is the durable thing. Build it first.
- **Spec 2 — the e-reader website UI (later).** Focus mode, the docked settings rail, theming,
  table of contents, bookmarks, highlights, persistence. A website-launch build on top of spec 1's
  files. Mocked during brainstorm, not designed here.

The reason the split is safe: **one durable file, two renderers.** Everything the e-reader does is
*rendering*. Underneath sits one thing the dive produces — the marked-up text plus the dossier. Two
renderers read it: `serve.py` today (research preview) and the Eleventy e-reader later. The reader UI
can grow for years and **the content is never redone.** So what we design and produce per dive is that
one file, not the e-reader.

## The north star (context, not scope)

`tolstoy.life` becomes a **new interactive edition of Tolstoy's works**: a clean e-reader by default,
with toggleable layers summoned from a side rail — wikilinks, the passages Tolstoy or his editors or
the censor cut, edition and translation differences, modal info boxes on the entities. Spec 1 produces
the content those layers render; spec 2 builds the reader.

## Where the text lives — `works/`, not `wiki/`

The site already has the destination in skeleton:

```
website/src/works/<mainCategory>/<subcategory>/<work-slug>/
        ├─ Work-Title.md     ← the record + overview page (big schema frontmatter)
        └─ text/             ← the work's enriched text (CLAUDE.md already reserves works/**/text/)
```

`wiki/` is for the **entities the text points at** — persons, concepts, places. The work itself is
never a wiki page. The dive folder is a **staging area**: we draft the overview body and the text
markdown inside `docs/research/<dive>/`, then promote both into `works/.../` at ingestion — the same
research → human-in-the-loop ingest discipline the dives already use.

**Fix needed:** CLAUDE.md currently calls `works/**/text/` "source text, do not modify." That wording
is wrong for this design — the reading text is an **enriched reader's edition**, edited on purpose
(wikilinks, cut-markers). The unaltered archive is `primary-sources/`. Reword the CLAUDE.md line to
"don't corrupt the words," not "no markup," when this lands.

## What a dive additionally produces

Three deliverables, staged in the dive folder:

1. **The enriched text** — the work's text as a reader's edition: one reading spine in **English**
   (the period translation where one exists in the public domain; otherwise the machine pass), marked
   up with the encoding below, wikilinks embedded. The mission is an English-language resource, so
   English is the default spine; the Russian is always available as a switchable edition.
2. **The overview-page draft** — the reader-facing "about this work" body for the future
   `works/.../Work-Title.md` record. The dossier's `workRecord` already supplies the schema frontmatter;
   this is the prose around it (significance, a short genesis summary, links to the key entities).
3. **The machine-translation pass** — a one-pass English translation, labelled "machine, unverified,"
   serving as the **Machine EN** edition and as the neutral third reference for the translation
   diagnostic. Optional per work; see Machine translation below.

## The encoding vocabulary

The marks are **CriticMarkup** — an existing plain-text standard for editorial change-tracking (deleted /
inserted / changed / commented text) — plus the project's existing `[[wikilink]]`. Nothing invented.
The marks map one-to-one onto the textual facts the dive already extracts into the dossier.

| Mark | CriticMarkup | Encodes | Renders as |
|---|---|---|---|
| Excision | `{--…--}` | A passage cut before print (Tolstoy, an editor, or the censor) | Ghost block at the seam |
| Insertion | `{++…++}` | A passage added in a later draft/proof | Revealed addition (the text growing) |
| Softening / edition diff | `{~~old~>new~~}` | A word/phrase changed between draft and print, **or** between two editions | Dotted printed word; reveal shows the other reading |
| Note | `{>>…<<}` | The editorial fact — who, when, why | The modal/info card |
| Wikilink | `[[Entity]]` | A person/concept/place | Toggleable link → entity modal |

Three conventions on top:

- **One mark, three stories.** A `{--cut--}` means different things depending only on who the note
  names — the **state censor**, an **editor** (e.g. Chertkov), or **Tolstoy revising himself**. The
  reader UI can color them (red = censored, amber = edited, blue = self-revised); the encoding is one
  mechanism carrying the whole textual life of the work.
- **Notes inline, for now.** The note text sits in the `{>>…<<}` comment — no second file to keep in
  sync. If drift between the text and the dossier ever bites, move notes to a dossier reference id later.
  (Lazy first; known upgrade path.)
- **Translation diagnostic = a highlight + note.** Where the period English dropped or blunted
  something versus the Russian/machine reading: `{==clause==}{>>dropped from the 1905 English<<}`. The
  machine-translation thread rides the *same* encoding as the cuts.

Worked example (real Great Sin material; English wording illustrative):

```markdown
The poverty of the masses {~~springs from~>is connected with~~}{>>Chertkov softened this,
8 Jul 1905: the evil itself springs from a deeper evil, human egoism<<} this one cause.

{--Just as the slave-owner of old re-enacted his crime each day he held men as property, so the
landowner renews this sin each day he holds the earth.--}{>>var. 8, cut at Chertkov's suggestion<<}

the single tax that [[Henry George]] proposed.
```

## The `serve.py` render pass

`serve.py` uses Python-Markdown, so the rendering is mostly off-the-shelf extensions, not custom parsing:

- **CriticMarkup** → `pymdownx.critic` (from `pymdown-extensions`). Renders the four marks to
  `<ins>` / `<del>` / `<mark>` with classes we can style and toggle. Confirm the package is available;
  if not, a ~30-line inline pattern covers the four marks.
- **Footnotes** → the built-in `footnotes` extension. This closes the long-standing "serve.py renders
  no `[^n]`" gap. Keep `{>>…<<}` for *editorial/variant* notes; use real footnotes for the work's own
  authorial/translator footnotes (e.g. the ones in "A Great Iniquity").
- **Wikilinks** `[[ ]]` → the built-in `wikilinks` extension (or a small inline pattern) pointed at the
  `works/`/`wiki/` URL scheme. Dangling links (entity page not yet created) are fine — they mark future
  ingestion work, same as the vault tolerates today.

Plus a **minimal focus-mode reading template** and CSS so the layers are visible and toggleable in the
preview. This is preview-grade only — the real rail, theming, and bookmarks are spec 2.

## Machine translation

- **Rides the dive.** When a work's text is bundled, generate its machine pass then. Never a
  corpus-wide batch — that's huge and pointless; do the works you're already touching.
- **Cheap per work.** A ~14k-word essay is ~35k tokens in + ~18k out — one context window. Roughly
  $2 at Opus / $0.40 at Sonnet via the API, or ~$0 marginal via the subscription `claude-cli` path
  (the graphify spike already proved a session can wrap `claude-cli`).
- **Two quality tiers.** One pass, labelled "machine, unverified," for the comparison column (cheap).
  Reserve the late-voice two-pass draft-then-audit only for passages promoted to finished translation.
- **Differently biased, not unbiased.** The machine reading has no stake in Chertkov's cuts, Free Age
  Press house-softening, or Victorian propriety — which is exactly what makes a period translator's
  softening *visible*. That is its job in the edition switcher.

## Fidelity and guardrails

- `primary-sources/**` and the dive's `extracts/**` (byte-faithful originals) are **untouched**. The
  enriched text is openly a reader's edition, derived from them.
- `verify_quotes.py` still guards every locked quote against the extracts — the existing gate is unchanged.
- The reading text is **English-spine + Russian-available**; the Russian column is the corpus text, not
  a re-typing.

## How it's built and run

- **A separate post-dive step, not a change to the `corpus-dive` skill.** The dive skill is heavily
  validated; leave its internals alone. A companion step (a small skill or a `--bundle-text` mode) reads
  a *finished* dive folder — dossier + extracts — fetches the public-domain period English (Wikisource /
  Gutenberg / archive.org) where it exists, generates the machine pass, and writes the enriched text +
  overview draft. This also lets us run it **retroactively on the ~14 dives already shipped.**
- **Pilot: The Great Sin.** Its period English ("A Great Iniquity," trans. Tchertkoff & Mayo, *The Times*
  1905) is public-domain and identified on Wikisource; its cut/variant data is the richest in the corpus.

## Wiki scope (the question you flagged)

Settled: the reader edition **embeds** `[[wikilinks]]` (toggleable) and the dive **proposes** the
`works/` record (as it already does). It does **not** itself create wiki entity pages — those stay the
separate human-in-the-loop ingestion step. Embedded wikilinks may point at not-yet-created pages; that's
expected and marks future work.

## Out of scope (spec 2 or beyond)

- The full e-reader UI: focus mode polish, the docked rail, theming, TOC, **bookmarks, highlights,
  personal annotations, persistence**. (Drawn in the rail from day one, built last.)
- Corpus-wide machine translation as a batch job.
- The reader's *own* highlights/bookmarks baked into source files — that's browser state, not text.
- Editorial "this is important" highlighting — fights the bare-voice rule.
- Changes to `corpus-dive` internals beyond adding the companion step.

## Open questions to confirm before/within the plan

1. **Overview draft origin** — author the reader-facing overview fresh, or distill it from the existing
   research `index.md`? (They overlap; `index.md` is dense and cited, the overview is lighter.)
2. **Per-edition file mechanics** — one file per edition (`<slug>.en-period.md`, `<slug>.en-machine.md`,
   `<slug>.ru.md`) that the switcher loads, vs. one spine file with the others referenced. The marks
   live on the spine; alternate editions are parallel reference texts.
3. **Do cuts/softenings show in every edition or only the spine?** A cut is an edition fact (it lives in
   the Russian variants); decide whether the Russian column shows its own marks or only the spine does.
4. **Period-English sourcing/cleanup** — fetching and cleaning the PD translation (footnotes, section
   numbering) is real per-work work; budget for it.
