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

**Resolved 2026-05-31:** added an `edition` wiki type (10th) to `wiki-schema.md` v1.3. Fields: `editionType` (`complete-collected`/`academic-critical`/`popular`/`selected-works`/`translation-series`/`other`), `format` (`print`/`digital`/`both`), `editorInChief`, `publisher`/`publisherCity`, `publicationStartDate`/`EndDate` (+OldStyle/Approximate), `volumes`, `basedOn`, and `sourceId` (the bridge to `sources.yaml`). Also reconciled the validator's `WIKI_TYPES`, which had silently drifted to only the original 4 (missing the 5 types added in v1.1) — now the full 10. **Routing:** the Jubilee Edition → `edition`; Tolstoy Digital stays `institution` (the DH *project*, not the edition). The verified `dossier.yaml` routing snapshot is left as-is; future ingestion should use `wikiType: edition` for the Jubilee Edition row.

### A2. Is `sources.yaml` updated, or is that for the ingestion phase? (Johan's question)

**Status:** NOT updated. The corpus-dive skill's write boundaries exclude `website/schema/sources.yaml` (it writes only to `docs/research/**` and `website/src/posts/notes/`), so the dive did **not** add a source id. Adding a `tolstoydigital-tei` source id is therefore an **ingestion-phase decision**, not something the dive did. `sources.yaml` already holds the related ids `jubilee-edition`, `tolstoy-museum-moscow`, `rgb-tolstoy-fond`, `yasnaya-polyana-archive`, `wikidata`. Suggested new entry: `id: tolstoydigital-tei`, type `database`/`primary`, CC BY-SA (header-scoped).

**Resolved 2026-05-31:** added `id: tolstoydigital-tei` to `sources.yaml` — type `database` (chosen over `primary` to match the existing pattern of `wikidata` / `internet-archive`), CC BY-SA noted as header-scoped, local clone path recorded. Entity rows that previously cited `sources: []` (Tolstoy Digital, and the four DH leads) can now cite `tolstoydigital-tei`.

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

**Researched 2026-05-31:** No English translation of the PSS notice «Перепечатка разрешается безвозмездно» is attributable to Chertkov — the 1928/1935 edition printed only the Russian + the French «Reproduction libre pour tous les pays». The authentic English equivalent in Chertkov's *own* publishing is the **Free Age Press** (the press he founded and funded, 1900, Christchurch/Maldon, England; managed by Arthur C. Fifield): its Tolstoy editions bore the title-page mark **«No Rights Reserved»**, with the prospectus line *"As it is Tolstoy's desire that his books shall not be copyrighted, our editions will, whenever possible, be free to the world."* Confirmed on scans of *The Slavery of Our Times* (1900, tr. Aylmer Maude) and *Letters to Friends on the Personal Christian Life*; Tolstoy blessed the policy in his letter to the Free Age Press, 24 Dec 1900 ("…absolutely free to all who may wish to make use of it").

- **For the SDG dedication:** «No Rights Reserved» (Free Age Press, 1900) is the citable English line — attributed to the FAP, **not** presented as a translation of the PSS notice. It is the genuine English-language root of the same renunciation principle, ~28 years before the Soviet edition.
- **Photo:** the most apt visual is a Free Age Press title page bearing «No Rights Reserved» (PD, pre-1923; downloadable from archive.org, e.g. `slaveryourtimes00tolsiala`). The cached Repin portrait of Chertkov works as the "who".
- ⚠ **Verify** the exact prospectus wording against a clean scan before quoting it verbatim on the site (sources so far are OCR). Sources: archive.org (`slaveryourtimes00tolsiala`, `pamphletstransl00tolsgoog`), marxists.org *Letters to Friends*, Wikisource *Letter to the Free Age Press*.

### B2. Are the genres notes / krug_chtenija / azbuka / comments in the schema?

Against the genre breakdown (notes 100 · krug_chtenija 444 · azbuka 784 · comments 807).

Follow-up: check whether `website/src/works/` and the works content model accommodate these. Note distinctions: *Круг чтения* and *Азбука* are anthology/primer **works**; *notes* are notebooks; **comments are the PSS editorial apparatus, not Tolstoy works** — likely should NOT be modelled as works. The TEI taxonomy types all four (`#notes`, `#krug_chtenija`, `#azbuka`/`#included`, `#comments`).

**Resolved 2026-05-31:** checked. *Азбука* already exists as a work (`src/works/fiction/childrens-literature/ABC Book.md`) but was shoe-horned into `genre: fragment` — no native primer value existed. *Круг чтения* is not yet a work. The works `genre` controlled list (`tolstoy-works-schema.md` v7 + the validator enum) gained `primer` (Азбука, Новая азбука) and `anthology` (Круг чтения, Путь жизни, На каждый день). *comments* confirmed **not** works (editorial apparatus) — not modelled. *notes* (notebooks) left unmodelled for now: closest existing genre is `diary`; no `notebook` value added pending a concrete need. **Open follow-up:** migrating the existing `ABC Book.md` from `genre: fragment` → `primer` is a vault-content edit (a "generated" work file; needs the read-discuss-write protocol) and was *not* done here.

### B3. The 100-volume academic PSS (IMLI, 2000– ) — need more info

Against: *"the 100-volume academic PSS begun in 2000 at the Gorky Institute (IMLI) — its scholarly successor, still in progress."*

Follow-up: research the in-progress IMLI edition — scope, volumes published to date, editorial principles (de-Sovietised text + commentary), how it relates to / supersedes the Jubilee Edition, and availability (digital?). Currently sits in the dive's `notCovered`. Could become a short reference note or a `notCovered` → resolved item.

**Researched 2026-05-31:** The academic *Полное собрание сочинений Л. Н. Толстого в 100 томах* — prepared by the Tolstoy group at **IMLI RAN** (A. M. Gorky Institute of World Literature), publisher **«Наука»**, Moscow; begun **2000** (Vol. 1 = 1850–1856).
- **Structure** — by *series*, not one running sequence: «Художественные произведения» (Literary Works, ≈18 vols); «Редакции и варианты художественных произведений» (Editions & Variants, ≈17 vols, dual-numbered, e.g. Том 4 (21)); plus planned Письма (Letters), Дневники и записные книжки (Diaries & Notebooks), and journalistic / religious-philosophical series — ≈100 vols in all.
- **Published to date** — in progress and slow: Vol. 1 (2000); the Literary-Works series through Том 9 (unfinished works 1863–1884, 2014) and Том 11 (*Anna Karenina*); Editions & Variants vols 1, 4 (=21), 8. Roughly a dozen-plus of 100 across series. *Exact current count not authoritatively pinned* — secondary sources give 7 / 8 / "≈10 by 2013" / Vol. 11; check the IMLI or «Наука» catalogue (or RGB) for a definitive figure.
- **Principles / de-Sovietisation** — texts re-verified against autographs, authorized copies, and first editions; previously unpublished fragments restored; dedicated Editions-&-Variants and unfinished-works series (the "creative laboratory"); fuller modern commentary, free of the Jubilee Edition's Soviet-era framing and its reserved "right of omission".
- **Relation to the Jubilee Edition** — the scholarly successor; supersedes its textual choices, but the 90-vol edition remains the only *complete* edition and the citation standard until the 100-vol finishes (decades off at current pace).
- **Digital availability** — mostly print; imwerden.de hosts Vol. 1 (2000) as PDF; no comprehensive free digital corpus (the platform's local corpus remains the 90-vol Jubilee). Resolves the first `notCovered` item. Sources: imli.ru, old.imli.ru/tolstoy/Ptushkina.php, labirint (Vol. 11), Cambridge *Tolstoy in Context* ch. 34, Russia Beyond.
