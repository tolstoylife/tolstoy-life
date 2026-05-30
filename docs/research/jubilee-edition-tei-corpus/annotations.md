---
layer: reference
lastUpdated: 2026-05-30
tags: [research, annotations]
---

# Annotations — Jubilee Edition + tolstoydigital TEI corpus

Reader annotations by Johan on [index.md](index.md), 2026-05-30. These are interpretive steer / open questions for a follow-up session — kept out of the bare dive. They do not change the dive's verified findings.

---

## A. Open questions raised against the dive's `needsReview`

### A1. No native wiki type for an "edition" — **investigate** (Johan: "Yes, this needs investigation.")

The Jubilee Edition and the TEI corpus are currently routed as `wikiType: concept` / `institution` because the schema's nine types have no `edition`. Decide: add an `edition` type to `website/schema/wiki-schema.md`, or settle `concept` as the home. Affects the dossier entity rows "The Jubilee Edition (Полное собрание сочинений)" and "Tolstoy Digital / «Слово Толстого»".

### A2. Is `sources.yaml` updated, or is that for the ingestion phase? (Johan's question)

**Status:** NOT updated. The corpus-dive skill's write boundaries exclude `website/schema/sources.yaml` (it writes only to `docs/research/**` and `website/src/posts/notes/`), so the dive did **not** add a source id. Adding a `tolstoydigital-tei` source id is therefore an **ingestion-phase decision**, not something the dive did. `sources.yaml` already holds the related ids `jubilee-edition`, `tolstoy-museum-moscow`, `rgb-tolstoy-fond`, `yasnaya-polyana-archive`, `wikidata`. Suggested new entry: `id: tolstoydigital-tei`, type `database`/`primary`, CC BY-SA (header-scoped).

---

## B. Annotations on index.md

### B1. The free-reproduction notice → possible SDG (Soli Deo Gloria) dedication use

Against: *"The edition carries its own free-reproduction notice"* (PSS Tom 1: «Перепечатка разрешается безвозмездно»).

Johan: *"I'd might like to use this for the SDG dedication. Is there a verified translation by Chertkov? Also the facsimile for this is interesting as well as a photo."*

Follow-ups:
- **Verified Chertkov translation?** The printed edition already prints a French rendering directly beneath the Russian — «Reproduction libre pour tous les pays.» (free for all countries). Open question: is there a *published English* equivalent attributable to Chertkov (who ran the Free Age Press English-language editions of Tolstoy)? Worth a targeted check before quoting an English line as "Chertkov's".
- **Facsimile** is ready and PD: `extracts/pss-vol62-pages/page-004.png` (committed).
- **Photo** wanted to accompany the dedication — source/select one (Chertkov portrait by Repin is already cached: `visuals/commons-chertkov-portrait-repin.jpg`, PD; or a photo of the printed page).
- Ties to the existing [copyright-renunciation dive](../copyright-renunciation/) (the SDG dedication's primary-source grounding).

### B2. Are the genres notes / krug_chtenija / azbuka / comments in the schema?

Against the genre breakdown (notes 100 · krug_chtenija 444 · azbuka 784 · comments 807).

Follow-up: check whether `website/src/works/` and the works content model accommodate these. Note distinctions: *Круг чтения* and *Азбука* are anthology/primer **works**; *notes* are notebooks; **comments are the PSS editorial apparatus, not Tolstoy works** — likely should NOT be modelled as works. The TEI taxonomy types all four (`#notes`, `#krug_chtenija`, `#azbuka`/`#included`, `#comments`).

### B3. The 100-volume academic PSS (IMLI, 2000– ) — need more info

Against: *"the 100-volume academic PSS begun in 2000 at the Gorky Institute (IMLI) — its scholarly successor, still in progress."*

Follow-up: research the in-progress IMLI edition — scope, volumes published to date, editorial principles (de-Sovietised text + commentary), how it relates to / supersedes the Jubilee Edition, and availability (digital?). Currently sits in the dive's `notCovered`. Could become a short reference note or a `notCovered` → resolved item.
