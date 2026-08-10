# Verifier report — The Slavery of Our Times (Рабство нашего времени) work-dive

**Verdict: CLEAN-WITH-MINOR-CONCERNS**
**Date:** 2026-06-07 · independent opus verifier pass (adversarial; verifier did not author the dive)
**Mechanical gate:** `verify_quotes.py` PASS (35/35 byte-faithful, 0 label warnings) — re-confirmed by spot-check, not re-run in full.

**Tally:** 1 CONCERN (item 5 — invalid wikiType `organization`), 0 FAIL. One sub-minor note on a stray pre-reform token in non-cited extract text (item 1). Everything else PASS.

---

## 1. Byte-fidelity spot-check + orthography — PASS (with one sub-minor note)

Seven `quoteRu` drawn at random confirmed verbatim (literal `grep`, count=1 each) in their **named** extract files:

| id | extract | result |
|---|---|---|
| W8 (Marx expropriation) | `v34_144_199_…txt` | ✓ |
| W12 («Одно средство порабощения…») | `v34_144_199_…txt` | ✓ |
| D2 (chain-of-slavery diary) | `v54_010_015_1900_03_13.txt` | ✓ |
| V1 (Никита! / Ageev) | `v90_169_173_…Varianty.txt` | ✓ |
| L1 (Chertkov genesis 36-hours) | `v88_581_…txt` | ✓ |
| W13 (Henry George) | `v34_144_199_…txt` | ✓ |
| V2 (Marx-in-German 2nd quote) | `v34_491_502_…Varianty.txt` | ✓ |

**Orthography:** a scan of all 14 `.txt` extracts for pre-reform letters (ѣ і ѳ ѵ) returns **0** in every file — `extract_tei.py --choice=reg` resolved the pre-1918 orthography as required. Headers/`# bibl` lines are modern orthography.

**Sub-minor note (not a fidelity failure):** one word-final `ъ` survives corpus-wide — `…Кончил все письма и дневникъ?.` (`v54_024_025_1900_05_02.txt`, line 27). The trailing `?` marks it as an uncertain-reading TEI editorial artifact, not resolved by `--choice=reg`. It is **not inside any cited `quoteRu`** (confirmed: 0 hits for `дневникъ` in `dossier.yaml`) and does not touch the genesis evidence (D3 quotes only «Все время был занят двумя статьями. И хочется думать, что кончил.», which is verbatim-clean). No action required for this dive; the extract is faithful to its TEI source. Worth noting only as a known `--choice=reg` edge case (uncertain-reading tokens).

## 2. Primary claims source-anchored — PASS

Every load-bearing factual claim in `index.md` traces to an evidence row, the editorial-history extract (`v34_563_567_history.txt`), or the PSS apparatus. The specifically-named claims all check out:

- **36-hour / Moscow–Kazan goods station genesis** → L1 (letter, verbatim) + `v34_563_567_history.txt` (visit dated 26 Dec, work begun 27 Dec). Confirmed in history extract: «Толстой ездил на товарную станцию Казанской ж. д. 26 декабря… 27 декабря… приступил к работе…».
- **"13 March 1900 diary states the thesis"** → D2, verbatim in `v54_010_015_1900_03_13.txt`.
- **Three causes (landlessness, taxes, manufactured needs)** → W13/W14 (ch. IX), anchored.
- **Marx-against-Marxism** → W8 (the one kept *Capital* quote, ch. XXIV) + V2 (cut German 2nd quote); both verbatim. The "read *Capital* / annotated YP copy" claim is attributed to Breitburg 1935 via the PSS apparatus (not asserted bare).
- **Title evolution** (Самый дешевый товар → Денежное рабство → Насилие и рабство → Новое рабство → Рабство нашего времени) → anchored to the history apparatus and D4 (records «Новое рабство»); рук. №43 cited for the final title.
- **Publication/ban sequence** (Free Word 1900; *Severny Kurier* blocked 13 Apr 1900; 1911 confiscation 19 Apr 1911; full Russian 1917) → PSS history; consistent between `index.md`, the `workRecord` fields, and `censorshipNotes`.

No primary claim found floating without an anchor.

## 3. Scholarship attributed, not asserted — PASS

The "Scholarly context" section and `scholarship` block attribute every secondary claim to a named source — Maude (1900/1902), Simmons (1946), Bartlett (2010), Wilson (1988), Wenzer (1997), Breitburg (1935), Christoyannopoulos (2012). The two key ones:

- **Henry George "trough" (Wenzer 1997)** — attributed in body («Kenneth Wenzer… documents that…») and in `scholarship.triangulation` (`evidenceRef: W13`, `source: Wenzer…`). The dive correctly separates Wenzer's *fact of rejection* from the dive's own *internal textual reason* (obligatory rent = legal compulsion, ch. XI).
- **Marx marginalia (Breitburg 1935)** — attributed both in body and triangulation (`evidenceRef: W8`), flagged "cited in the PSS apparatus… not independently web-verifiable."

Uncertainty acknowledged: Christoyannopoulos subsection marked "[subsection content unverified]" / "UNVERIFIED at subsection level"; Volkov 2021 "abstract only (paywalled)"; Bartlett/Wilson "not page-checked." Contested labels ("utopian," "a crank," "impractical") are explicitly presented as "the outside's words… the mainstream's words about Tolstoy's economic thought in general, never asserted" (index.md "Labels to attribute, not assert"; scholarship.summary). PASS.

## 4. scholarship.triangulation integrity — PASS

All six `evidenceRef` values (D2, W13, W17, W8, W1, L1) resolve to real `evidence` ids. All `relation` values are within the enum: `extends` ×3, `confirms` ×2, `complicates` ×1. The George entry is `complicates` (correct — it complicates the "Tolstoy the Georgist" picture). The Marx entry (W8) is `extends` and the laws→violence→government chain (W17) is `confirms` — both sensible.

## 5. Entities + vaultStatus — CONCERN

**Invalid wikiType found.** `wiki-schema.md` v1.3 defines **ten** types (person, place, event, concept, translator, institution, adaptation, criticalWork, archivalFond, edition) and the validator `WIKI_TYPES` matches that list. The entity **"Free Word Press (Svobodnoe Slovo)" uses `wikiType: organization`** (`dossier.yaml` line ~586), which is **not in the vocabulary**. The correct type is **`institution`** (the schema lists "Publishers, archives, organisations" under `institution`, with `institutionType: publisher`). This is the exact failure the prompt flagged as an example. All other wikiTypes are valid: person ×13, concept ×1, work ×1. → **Fix: change `organization` → `institution` before ingestion.**

**vaultStatus spot-check — PASS.** Listing `website/src/wiki/`:
- Marked `exists` and present: **Leo Tolstoy**, **Vladimir Chertkov**, **Maria Tolstaya** ✓ (`Leo Tolstoy.md`, `Vladimir Chertkov.md`, `Maria Tolstaya.md`).
- Marked `missing` and confirmed absent (loose-matched, transliteration gotcha respected): **Aylmer Maude**, **Henry George**, **Karl Marx**, **Robert Owen**, **John Ruskin** — none present. Also absent and correctly `missing`: Ageev, La Boétie (`boeti`/`boetie`), Schmitt, Clarke, Baryatinsky, Svobodnoe Slovo. No false `missing`.

(Note: `wikiType: work` for the work itself is internally consistent with the dossier's own convention — the work is routed to a `workRecord`/`works/` record, not a `src/wiki/` page, so it does not need to be one of the 10 wiki article types; flagged only for awareness, not a defect.)

## 6. workRecord integrity — PASS

All proposed `field` names are real schema keys and all appear in the sibling `Bethink Yourselves!.md` record: titleEn/titleRu/titleAlternatives, mainCategory, subcategory, genre, language, completionStatus, publishedDuringLifetime, publishedInRussiaDuringLifetime, the date quartet, firstPublishedVenue(+Type), dateFirstPublishedInRussia(+Venue), authoringLocations, samizdatCirculation, censoredVersionExists, censorshipNotes, bans, excommunicationRelated, relatedWorks, themes, epigraph, identifiers.jubileeEdition. No invented field name.

- **Date sub-flags correct:** `dateWritingStarted` carries `oldStyle: "1899-12-27"` (the 27 Dec OS sketch) with NS `1900-01-08`, `approximate: false`; `dateWritingCompleted` NS `1900-08-12` / OS `1900-07-30`, `approximate: true` (tail correctly flagged fuzzy — afterword/epigraphs Aug, ch. XIV corrections Sept). `dateFirstPublished: "1900"` and `dateFirstPublishedInRussia: "1917"` both `approximate: true`. OS+12 (1899) and OS+13 (1900) conversions are arithmetically correct per the post-1 Mar 1900 rule.
- **No fabricated date/venue:** Free Word / Berlin 1901 (Caspari, Steinitz) / Maude Free Age Press / *Severny Kurier* / 1911 confiscation (19 Apr 1911) / 1917 (Edinenie, Posrednik) all trace to the PSS history. The one dated `bans[]` entry (Moscow Court of Justice, 1911-04-19, `confidence: medium`) is honestly flagged as the single dated authority-action in the corpus.
- **`excommunicationRelated: false` justified:** the 1901 Synod decree cited *Resurrection* and doctrinal grounds, not this economic treatise. Consistent across `workRecord`, `index.md` ("The Church and the 1901 excommunication"), and `scholarship.triangulation[L1]`. The dive is careful **not** to present the excommunication as targeting this work. Correct.

## 7. Coverage honesty — PASS

The `coverage` ledger is honest. Two surfaces are marked `partial` and both genuinely are:
- **Reception & afterlife = partial** — matches `index.md`'s own caveat that "the contemporary critical reception is thin… no systematic study of its Western newspaper reception in 1900–01 was recovered." Honest.
- **The author's later verdict = partial** — matches the `index.md` admission that "A dedicated sweep of the post-1900 diaries for an explicit later verdict… was not made and is flagged in `needsReview`." Honest.
- **Visual & manuscript record = partial** — matches the Commons-only sweep + missing first-edition title pages. Honest.

Nothing marked `covered` that is really partial. `needsReview` (5 items) and `notCovered` (5 items) are consistent with the `index.md` "Material not covered" section.

## 8. Translations labelled — PASS

All **35/35** `quoteEn` entries in `dossier.yaml` carry the `(working English)` label (grep: 0 unlabelled). In `index.md`, every block-quote translation is prefixed `(working English)`, and `titleAlternatives`/prose marks the singular *The Slavery of Our Time* as a "variant title." PASS.

## 9. Voice — PASS

The dive reports Tolstoy's argument and attributes scholarship without endorsing or refuting him. The framing verbs are descriptive ("The argument is structural," "He quotes," "The remedy is individual non-participation," "the work builds this into a chain"). Where the dive could most easily slip — the "Why this matters" and "Scholarly context" sections — it stays on the report side: it calls the work "the hinge between Tolstoy's religious anarchism and his economics" (a structural/historical claim, defensible from the corpus), and it consistently quarantines evaluative labels as the mainstream's ("filed, with a shrug, under Christian anarchism"; "the outside's words"). No sentence reads as the dive taking sides for or against Tolstoy's thesis. PASS.

## 10. Rights hygiene — PASS

- **`extracts/` is text-only:** 14 `.txt` source extracts plus 4 generated `_scholarship`/`_visuals` `.md`/`.html` working files. No images.
- **No rights-reserved image committed:** `git status --porcelain` shows the dive dir as a single untracked `?? docs/research/1900-the-slavery-of-our-times/`; `git ls-files` for the dir returns **nothing** (nothing tracked yet). `visuals/` is git-ignored via `docs/.gitignore:18` (`research/*/visuals/`) — confirmed by `git check-ignore -v` resolving `visuals/commons-henry-george.jpg` to that rule. The 6 cached `.jpg`s (incl. the CC-BY-SA Maude portrait) will not be committed. `extracts/*.txt` are confirmed **not** ignored (correctly tracked-eligible, PD source text).
- **CC-BY-SA images flagged for the gate, not asserted publishable:** the Maude portrait (`licence: CC-BY-SA`, `note: "publication needs the Lafayette/V&A credit"`) and the La Boétie/Montaigne engraving (`licence: CC-BY-SA`, `usable: unknown`, "not downloaded… needs crediting at publication") are recorded with attribution requirements and routed to `needsReview`/publication gate. `index.md` "Visual & manuscript record" repeats this. Correct.

---

## Required fix before ingestion (1)

1. **`dossier.yaml`** — the "Free Word Press (Svobodnoe Slovo)" entity has `wikiType: organization`, which is not one of the 10 valid wiki types. Change to **`institution`** (with `institutionType: publisher` to be set on the eventual wiki page). This is the only blocking schema error.

## Optional / awareness (1)

2. The stray pre-reform `дневникъ?` token in `v54_024_025_1900_05_02.txt` (line 27) is an uncertain-reading TEI artifact outside all cited quotes. No action needed for this dive; noted as a `--choice=reg` edge case for uncertain-reading tokens.

**Bottom line:** the dive is byte-faithful (35/35, re-spot-checked), correctly orthography-normalised, scholarship-attributed, voice-clean, rights-clean, and its workRecord/coverage/translation discipline is sound. One genuine schema defect (`organization` → `institution`) keeps it from fully CLEAN.
