# Verifier report — Hadji Murat (Хаджи-Мурат) novel-dive

**Verifier:** independent (did not author the dive).
**Date:** 2026-06-09.
**Inputs checked:** `index.md`, `dossier.yaml`, `extracts/*.txt` + `_*.md` briefs, `visuals/`, against `wiki-schema.md` v1.4, `tolstoy-works-schema.md` v7, and the live `Master and Man.md` record.

**Verdict: CLEAN — 0 blocking issues, 5 minor issues.**

---

## Check 1 — Byte-fidelity (belt-and-braces on verify_quotes) — PASS

- Re-ran `python3 docs/research/lib/verify_quotes.py docs/research/1896-1904-hadji-murat/dossier.yaml`. Output: **`SUMMARY: 34/34 quotes verbatim, 0 facsimile missing, 0 skipped, 0 label warning(s) — PASS`**, exit code **0**. Matches the dive's stated 34/34.
- Manual independent `grep -F` re-check of 4 rows across genres (whitespace-normalized substring):
  - **works** — `hm-death-thistle-simile` («со всего роста, как подкошенный репей, упал на лицо и уже не двигался.») — verbatim in `extracts/v35_005_118_Hadzhi_Murat.txt`. ✓
  - **diary** — `d-eagerness-and-shame` («писал Хаджи Мурата, то с охотой, то с неохотой и стыдом.») — verbatim in `extracts/diary-v54_134_135_1902_08_05.txt`. ✓
  - **letter** — `l-korganov-credo-1902` («когда я пишу историческое, я люблю быть до малейших подробностей верным действительности.») — verbatim in `extracts/v73_423_Korganov.txt`. ✓
  - **commentary** — `c-belgard-verdict` («император Николай I подвергается недопустимым, крайне грубым и оскорбительным для его памяти нападкам») — verbatim in `extracts/v35_629_631_Istorija_pechatanija.txt`. ✓
- No discrepancies. All four are exact substrings of their named extract files.

## Check 2 — Every primary claim in index.md is source-anchored — PASS

Traced the load-bearing primary claims to evidence rows / extracts:
- **82-item source list** — `extracts/v35_631_633_Spisok_istochnikov.txt` is numbered through item **82** (last entry "82. Янжул…"); the editors' figure is confirmed. ✓
- **2166 manuscript sheets** — verbatim in `v35_648_666_Opisanie_rukopisej.txt` («общее их количество составляет 2166 листов»). ✓ (`c-2166-sheets`)
- **Ten redactions / «редакция десятая»** — verbatim in `v35_583_629_Istorija_pisanija.txt`. ✓ (`c-tenth-redaction`)
- **Nicholas-I chapter cut to "four-and-a-half pages"** — `v35_629_631_Istorija_pechatanija.txt` contains "4 1/2 страниц". ✓
- **151 documents hand-copied by Esadze** — verbatim in `v35_583_629` («Эсадзе собрал и собственноручно переписал 151 документ»). ✓
- **Loris-Melikov record / «Русская старина» 1881, no. 3** — confirmed in `v35_634_643_Primechanija.txt` (multiple citations "«Русская старина», 1881, 3"). ✓
- **Biryukov "schoolboy / ate a pastry / in a whisper" anecdote** — verbatim in `v35_583_629` line ~769 («каким школьник рассказывает своему товарищу, что он съел пирожное… стыдится признаться»); the PSS dates it to Biryukov's 1905–06 biographical gathering. ✓
- **Censorship is posthumous; Belgard / Main Directorate for Press Affairs; Chertkov's Berlin edition restored the cuts** — `c-belgard-verdict` + `c-berlin-uncensored`, both verbatim. ✓
- Diary/letter dates, addressees, and the not-publish-in-lifetime decision (`c-not-publish-lifetime`) all trace to evidence rows.

No primary claim was found asserted without support.

## Check 3 — Scholarly/secondary claims attributed, not asserted — PASS

- Every scholarly claim in "Scholarly context" and the dossier `scholarship` block is attributed to a named source (Bloom 1994, Bartlett 2010, Wilson, Simmons 1968, Herman 2005, Shklovsky 1981, Bojanowska 2022, Gould 2013, Kokobobo 2017, Grasso 2023) and appears in `references.background` and/or the 25-source list in `extracts/_scholarship.md`. ✓
- The three mainstream framings the check names are each quoted-and-attributed, never asserted in the dive's own voice as fact:
  - "anti-imperialist masterpiece" — line 12 ("positions to attribute"), line 20 ("the 'anti-imperialist' label, however, is the mainstream's"), line 202 ("stays the mainstream's").
  - "his farewell to art" — line 12 (quoted as a "mainstream framing… to attribute").
  - "fulfils What Is Art?" — lines 19, 200 (attributed to Simmons; "the 'fulfilment' reading is the scholar's reconstruction, not his").
- The dive's own analytic synthesis ("the un-moralized close is the closest the work comes to obeying the treatise") is hedged ("arguably") and tied to Herman's "silence" reading, not stated as fact. ✓

## Check 4 — scholarship.triangulation + entities.evidenceRefs integrity — PASS

Programmatic check (parsed YAML):
- All **5** `triangulation[].evidenceRef` resolve to real `evidence[].id` (`d-eagerness-and-shame`, `hm-death-nightingales`, `hm-nicholas-selfdeception`, `hm-aul-beyond-hatred`, `c-tenth-redaction`). No dangling refs. ✓
- All **5** `relation` values are in {confirms, complicates, contradicts, extends} (extends ×1, confirms ×3, complicates ×1). ✓
- All `entities[].evidenceRefs` resolve to real evidence ids. No dangling refs. ✓
- (Bonus) all `visuals[].relatedEvidence` resolve to real evidence ids. ✓

## Check 5 — Entity routing (wiki-schema v1.4) — PASS

- All 18 `entities[].wikiType` values are valid v1.4 types (person ×12, character ×3, group ×1, event ×1, concept ×1). ✓
- `vaultStatus` accuracy verified against `website/src/wiki/` (14 pages total): the four flagged `exists` (Leo Tolstoy, Vladimir Chertkov, Pavel Birukoff, Sophia Tolstaya) all exist as files; every entity flagged `missing` has **no** vault page, confirmed by loose transliteration matching (per the transliteration-gotcha caution) over both filenames and content — no false `missing`. ✓
- Character/prototype routing is coherent and matches the brief: Hadji Murat = `character` (titular) + prototype edge to the historical figure; Nicholas I / Shamil / Vorontsov / Loris-Melikov = `person`; Butler (prototype F. F. Kutler) + Marya Dmitrievna = `character`; Caucasus highlanders = `group` (groupType ethnic-group). The genuine routing judgment calls (historical-Hadji-Murat-also-a-person; satirical-Nicholas-as-character; Marya Dmitrievna tiering) are openly logged in `needsReview`, per `feedback_explain_schema_before_edit`. ✓

## Check 6 — Translations labelled — PASS (with minor note, see Issue 2)

- All **13** staged/blockquote English renderings carry `*(working English)*`; every `quoteEn` in the dossier begins "(working English)". ✓
- Inline parenthetical glosses of short Russian phrases (e.g. lines 16, 18, 47, 73, 85, 107, 121) use bare `("…")` without the label. This **matches the established dive convention** — the *Resurrection* and *Kreutzer Sonata* dives do exactly the same (reserve `(working English)` for blockquote renderings, gloss inline phrases unlabelled). Not a regression; logged as minor for consistency only (Issue 2).

## Check 7 — No editorializing voice — PASS

- Read the interpretive passages (Key findings, "The reading," Why this matters, Themes). Tolstoy's shame is rendered as ascetic guilt over whether a renunciant should make art at all — **not** recast as hypocrisy, and **not** softened. No anachronistic hardening (no "anti-war tract," no modern political label) stated as fact. The contested labels are consistently attributed. The marquee conclusion ("the contradiction was lived, not reconciled") is grounded in the diary record. ✓

## Check 8 — workRecord integrity — PASS

- **Record-CREATING confirmed:** no `website/src/works/.../hadji-murat/` record exists (directory absent; `git ls-files` over the works tree returns nothing for "hadji"). ✓
- **Field names** all match real keys in the works schema or the live Master and Man record: `title` / `mainCategory` / `subcategory` are not in the schema *document* but **are present in the live Master and Man frontmatter** (Eleventy-layer convention), so they are correct against the stated reference record. All other fields (`titleRu/En`, `titleAlternatives`, `genre`, `completionStatus`, the `published…` booleans, the date fields, `firstPublishedVenue`, `dateFirstPublishedInRussia`, `firstPublishedInRussiaVenue`, `bans`, `censoredVersionExists`, `censoredVersionNotes`, `excommunicationRelated`, `relatedWorks`, `authoringLocations`, `themes`, `epigraph`) are real schema keys. ✓
- **Controlled vocab** all valid: genre `novella`; completionStatus `incomplete`; titleAlternatives.type `working`; bans.scope `passages-cut`; bans.authorityType `imperial-state`; relatedWorks.relationshipType `companion` (×2). ✓
- **Evidence-anchored values:** posthumous publication (publishedDuringLifetime=false ← `c-not-publish-lifetime`); `bans` passages-cut + `censoredVersionNotes` (Nicholas-I chapter >10pp→4½pp, ch. XVII excised, Berlin restored, 1917 first uncensored Russian) accurate to `c-belgard-verdict` / `c-berlin-uncensored` and the commentary. No fabricated dates/venues. ✓
- Date fields carry `oldStyle` + `approximate` sub-flags as required. ✓
- See Issue 3 (the `jubileeEdition.volumes` field-name is partially-qualified) — minor, self-flagged in the field note.

## Check 9 — coverage honesty — PASS

- "Reception & afterlife" is honestly marked **partial** — the note correctly explains the work appeared after Tolstoy's death so early Russian critical reception is thin in the corpus; the posthumous censorship is the primary reception captured. ✓
- All surfaces marked `covered` are backed by the evidence/extracts examined; none over-claims. The textual surface honestly states "light layer by design / scene-led close-read, not every chapter"; redactions honestly state "sampled, not collated." The `notCovered` ledger and `needsReview` are candid. ✓

## Check 10 — File hygiene — PASS

- `extracts/` holds only verbatim TEI extracts (`*.txt`) + PD provenance briefs (`_deepread`, `_diaries`, `_genesis_commentary`, `_letters`, `_scholarship`). No rights-reserved content. ✓
- `visuals/` is git-ignored (`docs/.gitignore:18: research/*/visuals/`); `git check-ignore` confirms; **no** `.jpg`/`.png` is tracked. The dossier records a per-image `licence` (PD for usable images; `unknown` + `usable:false` for the GMT-held daguerreotype). ✓
- All **4** index.md embedded `<figure>` images (`commons-lanceray-hadji-mural-1913.jpg`, `commons-portrait-shamil-levitsky-1861.jpg`, `commons-portrait-nicholas1-botman-1856.jpg`, `commons-caucasus-aivazovsky-gunib-1869.jpg`) exist in `visuals/`. ✓
- (Note: the entire dive directory is currently untracked (`?? docs/research/1896-1904-hadji-murat/`) — expected for an in-progress dive on a working branch; not a hygiene fault.)

---

## Minor issues (none blocking)

1. **`два полюса` quote provenance under-flagged (attribution precision).** index.md line 20/189 presents «два полюса властного абсолютизма — азиатского и европейского» as "He described the parallel as «…»" / "Tolstoy's stated design," and the dossier triangulation sources it to "(PSS 35 commentary)". The phrase is verbatim in `v35_583_629_Istorija_pisanija.txt` (line ~651) but its actual provenance is a statement Tolstoy made **to S. N. Shulgin, recorded in Shulgin's memoir** within the commentary — i.e. oral-via-memoir, not Tolstoy's own writing. The scholarship brief correctly says "in conversation"; index.md/dossier do not carry that one-remove flag. The claim is true and the dive rightly treats it as Tolstoy's design, but it is rendered in guillemets like a verified quote while sitting **outside** the 34-row byte-verified ledger. Consider a "(to Shulgin, recorded in the commentary)" qualifier at ingestion.

2. **Inline glosses unlabelled (consistency only).** Short inline Russian phrases are glossed `("…")` without `(working English)`. Matches *Resurrection* / *Kreutzer* convention, so not a regression; noted only because the dive's Method line says "Working-English translations are labelled" without the inline-vs-blockquote carve-out.

3. **`jubileeEdition.volumes` field-name partially qualified.** The workRecord field is named `jubileeEdition.volumes`; the schema path is `identifiers.jubileeEdition.volumes`. The field's own `note` flags the correct nesting, so ingestion has the guidance — cosmetic.

4. **5 Aug 1902 citation slightly redundant.** "PSS Tom 53–54 (Tom 54, pp. 134–135)" (index.md line 47) doubles the tom; the parenthetical pin is correct (matches extract `diary-v54_134_135`). Cosmetic.

5. **Censor first-name variance across files.** index.md/dossier give the censor as "A. V. Belgard"; the scholarship brief calls him "Alexey Belgard." The PSS extract uses initials "А. В. Бельгард" — index/dossier match the primary; the brief's first name is a secondary-source nicety. Harmless, noted for tidiness.

---

## Summary

The dive is byte-faithful (34/34 independently re-verified + 4 manual cross-genre spot-checks), structurally sound (all triangulation/entity/visual refs resolve, all enums valid), schema-correct (record-creating workRecord with real field names and valid controlled vocab), and disciplined in voice (mainstream labels attributed, no softening or anachronistic hardening, coverage honestly partial where thin). Entity routing applies wiki-schema v1.4 coherently and vaultStatus is accurate against the live vault. The five minor issues are attribution-precision and cosmetic; none rises to blocking.
