# tolstoydigital TEI Reference Data

Date: 2026-05-10
Context: Documentation of the tolstoydigital/TEI repository and its relationship to the 91st volume index of Tolstoy's Jubilee Edition. Covers what we have, what we don't, and how it relates to the tolstoy.life data pipeline.

---

## 1. The Jubilee Edition and the 91st volume

The Jubilee Edition (*Полное собрание сочинений*, 1928–1964) is the authoritative complete works of Leo Tolstoy, published in 90 volumes. A 91st volume was published in 1964 as a comprehensive index to the entire set. It contains:

- An alphabetic index of proper names (persons, places, organisations) — approximately 16,000 annotated entities
- An alphabetic index of Tolstoy's works as published in the edition
- An alphabetic index of correspondents
- A chronological index of works

The 91st volume is a navigation tool: it tells you that a given person or place appears on page X of volume Y of the print edition. It does not contain Tolstoy's texts themselves.

A PDF guide to the Jubilee Edition is held at `primary-sources/jubilee-edition/tolstoy-jubilee-edition-guide.pdf`.

The 91st volume index has also been digitised as a web application: [index.tolstoy.ru](http://index.tolstoy.ru/), with a project page at [tolstoy.ru/projects/91-index/](http://tolstoy.ru/projects/91-index/). The web app adds fuzzy search and network graph visualisation — co-occurrence of names on the same page becomes a graph edge, revealing Tolstoy's social network as documented in his own texts.

---

## 2. "All Tolstoy in One Click" — the digitisation project

The plain text corpus that underpins the tolstoydigital TEI repository was produced by a crowdsourcing project called *Весь Толстой в один клик* ("All Tolstoy in One Click"), completed in 2014.

**The problem:** The Jubilee Edition had only ever been printed in a run of 5,000 copies and never reprinted. By the early 2010s it was a bibliographic rarity, held mainly in private collections and specialist libraries.

**Initiated by** Fyokla Tolstaya — Leo Tolstoy's great-great-granddaughter and one of the key figures behind the broader tolstoydigital project — together with the Leo Tolstoy State Museum in Moscow.

**How it worked:** ABBYY ran their FineReader OCR software on scanned PDFs of all 90 volumes. The OCR output then needed human verification — not straightforward, since Tolstoy wrote in Russian (sometimes in pre-reform orthography), French, Greek, Latin, and other languages. Rather than hire professional correctors, the project crowdsourced the proofreading through a dedicated website ([readingtolstoy.ru](http://readingtolstoy.ru/)). Over 3,000 volunteers from 49 countries each received a licence for FineReader and a packet of 20 pages to verify.

**Result:** All 46,820 pages and 14.5 million words were proofread in 14 days — 8.5 volumes per day. The texts went live on [tolstoy.ru](https://tolstoy.ru) as 761 electronic book files, freely available in PDF, FB2, and EPUB formats.

**The chain to the TEI corpus:** Jubilee Edition (print, 1928–1964) → crowdsourced OCR and proofreading (2014) → plain text on tolstoy.ru → TEI/XML encoding by the tolstoydigital team → `texts/` and `texts_txt/` in the GitHub repository.

The `texts_txt/` folder in the tolstoydigital/TEI repo is essentially this digitised corpus in plain text form, making it the most directly usable asset for LightRAG ingestion.

*Further reading:* The project is documented in the Orekhov (2020) paper held at `primary-sources/jubilee-edition/91vol.pdf`, and in an [ABBYY blog post](https://www.abbyy.com/blog/tolstoy-digitized-for-future-generations/).

---

## 3. The tolstoydigital TEI repository

The repository [github.com/tolstoydigital/TEI](https://github.com/tolstoydigital/TEI) is the output of the *Слово Толстого* (Word of Tolstoy) project, a digital humanities initiative by HSE (Higher School of Economics, Moscow). It contains the full 90-volume Jubilee Edition encoded in TEI/XML, plus structured reference data.

### Repository structure

| Folder | Contents |
|---|---|
| `texts/` | TEI/XML encoded texts — the full 90 volumes |
| `texts_txt/` | Plain text versions of the same content |
| `texts_front/` | Front matter for the volumes |
| `headers/` | TEI headers |
| `reference/` | Structured reference data (see below) |
| `tolstoy-bio/` | Biographical text in TEI/XML |
| `tolstoy_bio_front/` | Front matter for the biography |
| `images/` | Images referenced in the texts |
| `audio/` | Audio recordings |
| `utils/` | Python utility scripts |

1,232 commits as of May 2026. Companion scripts at [github.com/Levabu/tolstoy_digital](https://github.com/Levabu/tolstoy_digital). Licence: CC BY-SA (declared in XML headers; no separate licence file in the repository root).

### What we currently hold

Only the `reference/` folder has been downloaded, stored at `primary-sources/tolstoydigital-TEI/reference/`. The full corpus of encoded texts (`texts/`, `texts_txt/`) has not been cloned.

---

## 4. The reference files

The nine XML files in `reference/` are structured entity data built to support the TEI encoding project. They are the machine-readable counterpart to the 91st volume index.

| File | Contents |
|---|---|
| `personList.xml` | 3,113 persons with structured attributes and IDs |
| `locationList.xml` | 770 locations |
| `bibllist_works.xml` | Catalogue of Tolstoy's works in the 90-volume edition |
| `bibllist_bio.xml` | Biographical bibliography |
| `sourceList.xml` | List of sources referenced in the edition |
| `taxonomy.xml` | Classification taxonomy for the encoded texts |
| `taxonomy_front.xml` | Taxonomy for front matter |
| `Dictionary.xml` | Terminology dictionary |
| `listMedia.xml` | Media asset list |

An additional file `All_tags_in_Tolstoy_letters_and_diaries.xlsx` documents all TEI tags used in the letters and diaries corpus.

### Relationship to the 91st volume

The 91st volume (1964) is the intellectual source: the tolstoydigital team used it as the foundation for their entity lists. The TEI reference files are not a direct digitisation of the print index — they are a richer, purpose-built dataset:

- Entities have unique XML IDs (usable as stable references)
- Structured attributes (dates, alternate names, roles, nationalities)
- Typed relationships between entities
- Direct linkage to the TEI-encoded texts rather than print page references
- Additional files (`Dictionary.xml`, `taxonomy.xml`) that go beyond the scope of the 91st volume entirely

The 91st volume answers "where in the 90 volumes is this person mentioned?" The TEI reference files answer "what is known about this person, and how are they connected to Tolstoy's texts and to each other?"

---

## 5. Relevance to tolstoy.life

### Current use

The reference files are the primary structured source for wiki entities. Person and location entries in `personList.xml` and `locationList.xml` directly inform wiki stubs in `website/src/wiki/`. The `bibllist_works.xml` catalogue underpins `website/src/works/`.

### Planned use — full corpus

The `texts_txt/` folder (plain text versions of all 90 volumes) is the most immediately valuable undownloaded asset. These are the source texts that would be ingested into LightRAG for knowledge graph construction — far richer than the current 29-document vault.

### Fork strategy

A fork of `tolstoydigital/TEI` to the `tolstoylife` GitHub organisation would serve two purposes: signal of intent (tolstoy.life is building on this data seriously), and a stable local reference point for the data the platform depends on. 13 forks already exist; the CC BY-SA licence explicitly permits this. Reaching out to the tolstoydigital team (Anastasia Bonch-Osmolovskaya, Fёkla Tolstaya, Boris Orekhov) to introduce the project is advisable before or alongside the fork.

---

## 6. Next steps

- [ ] Fork `tolstoydigital/TEI` to `tolstoylife` org
- [ ] Full `git clone` of the fork into `primary-sources/tolstoydigital-TEI/`
- [ ] Assess `texts_txt/` volume and structure for LightRAG ingestion planning
- [ ] Contact tolstoydigital team to introduce tolstoy.life
