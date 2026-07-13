---
layer: reference
lastUpdated: 2026-05-30
tags: [research]
---

# tolstoydigital TEI Reference Data

> **Superseded.** This note has been folded into — and substantially extended by — the consolidated reference dive **[The Jubilee Edition and the tolstoydigital TEI/XML corpus](jubilee-edition-tei-corpus/)** (2026-05-30), which now tells the full history (the printed edition, its makers and Soviet-era constraints, and the digitisation chain) and documents the structure of the collections (TEI document anatomy, the nine reference files, the witness corpora) with a byte-faithful evidence ledger. Start there.

For the Tom-number ↔ local-PDF resolver, see [pss-volume-mapping.md](pss-volume-mapping.md) (still canonical).

---

## Quick reference (retained)

- **Corpus repo:** [github.com/tolstoydigital/TEI](https://github.com/tolstoydigital/TEI) — "All of Tolstoy in TEI/XML"; CC BY-SA (declared in the XML headers' `<availability>`, not a repo LICENSE file). The build-scripts repo the README points to, `Levabu/tolstoy_digital`, is now a dead link (404).
- **Local clone:** `primary-sources/tolstoydigital-TEI/` — see the dive's §5 for the full structural inventory.
- **The 91st-volume index web app:** [index.tolstoy.ru](http://index.tolstoy.ru/) (project page [tolstoy.ru/projects/91-index](http://tolstoy.ru/projects/91-index/)).

## Open actions (carried forward)

- [ ] Fork `tolstoydigital/TEI` to the `tolstoylife` org (provenance + stable upstream).
- [ ] Contact the Tolstoy Digital team (Bonch-Osmolovskaya, Fyokla Tolstaya, Orekhov) to introduce tolstoy.life.
- [ ] Add a `tolstoydigital-tei` source id to `website/schema/sources.yaml` (the corpus underpins the vault but isn't a registered source).
- [ ] Assess `texts_txt/` for LightRAG ingestion planning.
