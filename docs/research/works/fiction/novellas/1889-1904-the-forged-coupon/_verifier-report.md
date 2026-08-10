# Verifier report — The Forged Coupon (Фальшивый купон) dive

**Verdict: CLEAN-WITH-MINORS** (separate-pass, adversarial; verifier did not author the dive)
**Date:** 2026-06-12
**Mechanical gate:** `verify_quotes.py` already PASSES (25/25 verbatim, exit 0). This pass covers the judgement-level checks the script cannot make.

**Counts:** 12 checks — 11 PASS, 1 PASS-WITH-MINORS (workRecord field-name mismatches). 0 fidelity failures, 0 attribution failures. 4 minor items for the human ingestion step (all already self-flagged by the dive, except the specific field-name corrections, which are named below).

---

## Check-by-check

### 1. Byte-fidelity sample — PASS
Re-derived far more than the requested 4–5 quotes. **17 distinct `quoteRu` strings** confirmed verbatim against their named extract files via exact-string match:
- Centrepiece ch XXIII (`v36_005_053_main.txt`): the full hinge block re-derived line-by-line — `За перегородкой лежала в постели…`, all six dialogue lines, `но она не подняла рук, не противилась…`, `Пожалей себя. Чужие души, а пуще свою губишь`, the kill line — every line present and exact. (The only multi-line whole-block match that returned "false" was a presentation artefact: the raw extract separates dialogue paragraphs with blank lines `\n\n`, which the index.md blockquote collapses to `\n`. The *text* is byte-identical; no content drift.)
- Origin (`мошенник`), conversion (`Степан стал другим человеком`), executioner (`плети — так плети, а убивать закона нет`), brothers (`все люди братья`) — all exact.
- Genesis diaries (`_diaries-genesis.txt`): 1889-05-29 germ, 1898-06-12 elastic-balls, 1903-12-25 «очень sobre», 1904-01-22 devils-waver, 1902-10-06 — all exact.
- Commentary excerpts (`v36_commentary-excerpts.txt`): devils redaction, Stanislavsky attribution, `однако с цензурными урезками` — all exact.
- Genesis-from-commentary (`v36_genesis-records-from-commentary.txt`): 1886 programme dream-vision, Larivon `Повели Ларивона в острог` — all exact.
- Letter (`v75_013…`): `если помнишь, я давно начал, и дополнение о религии` — exact.
- **Cross-checked against the live TEI** (`v36_005_053_Falshivyj_kupon.xml`): the centrepiece (`не подняла рук, не противилась`; `Пожалей себя…`), origin (`ты будешь мошенник`), brothers (`все люди братья`), conversion (`Степан стал другим человеком`) all present in source. No transcription drift between TEI → extract → dive.

### 2. Every primary claim source-anchored — PASS
Walked Key findings, the marquee, and Genesis. Each factual primary assertion ties to an evidence row / extract: the doubled-chain diagram → `ev-program-1886`; the elastic-balls mechanism → `ev-diary-1898-06-12`; the «sobre» de-allegorisation → `ev-diary-1903-12-25` + `ev-diary-1904-01-22` + `ev-devils-redaction`; the two prototypes → `ev-prototype-larivon` / `ev-prototype-stanislavsky`; the 1911 censorship → `ev-pub-censorship`. The composition-network names (Gorky/Pyatnitsky, the daughter-copyists, the L. L. letter) trace to the dated diary/letter evidence rows. No unanchored primary assertion found.

### 3. Secondary claims attributed, not asserted — PASS
Scholarly context + Reception attribute throughout: Kliger/Zakariya, Simmons, Wilson, Troyat, the 1912 Bernstein intro, the Bryn Mawr exhibit, Pipolo/Schrader on Bresson, the translator lineage. Every secondary name in index.md is backed in `_scholarship-sweep.md` (Kliger ×12, Zakariya ×13, Bresson ×20+, Bryn Mawr ×4, Cannes ×3, Simmons ×7, the translators present). No secondary claim stated as the dive's own fact.

### 4. scholarship.triangulation — PASS
All 7 `evidenceRef`s resolve to real evidence ids. All 6 `relation` values are valid (`extends` ×3, `confirms`, `complicates`, `contradicts`). The marquee's `confirms`+`extends` outcome is mirrored in the triangulation block.

### 5. Entities / novel routing — PASS
- Fictional figures → `character` (8): Stepan, Maria Semyonovna, Prokofy, Fyodor Smokovnikov, Mitya Smokovnikov, Mahin, Misail, Sventitsky. Correct.
- The sect → `group` (1). Correct (members + geography + founding test in wiki-schema §group).
- Real people → `person` (7): Tolstoy, Chertkov, M. L. Obolenskaya, Alexandra Tolstaya, L. L. Tolstoy, Gorky, Bresson. Correct.
- `prototypes[]` certainty **not over-claimed**: Larivon = `author-stated`/`documented` (Tolstoy named him in *Notes of a Christian*, quoted in the commentary) — defensible; Stanislavsky = `editorial`/`documented` (commentary "almost exactly reproduces") — defensible. Neither is `definitive`, correctly.
- `vaultStatus` calls reasonable; M. L. Obolenskaya carries its own transliteration-gotcha note (`Maria Tolstaya` may collide) and is self-flagged in needsReview.
- INFORMATIONAL (not a defect): the novella itself is routed `wikiType: work`, which is **not one of the 12 wiki-schema types**. This is the dive's deliberate routing marker to the separate `works/` schema (the entity's `role` says "record-creating workRecord" and a full `workRecord:` block exists). Self-consistent and matches the Tolstoy-Lab "Lab-only 13th type `work`" precedent. Not a mis-route.

### 6. Translations labelled "(working English)" — PASS
Every `quoteEn` in the dossier and every translated block in index.md carries the "(working English)" tag.

### 7. No editorializing voice; contested label attributed — PASS
The "Tolstoyan"/Christian-anarchist label is cross-linked to `../tolstoyanism/index.html` and explicitly marked "the contested label, interrogated there, not asserted here" (index.md L249) and "the label that the dive *confirms* but finds under-described" (L183). Not asserted in the dive's own voice. Project voice held — factual, bare.

### 8. Rights / PD hygiene — PASS
- `docs/.gitignore` L18 ignores `research/*/visuals/`; `git check-ignore` confirms `visuals/Tolstoy-Scherer-Nabholz-1902.jpg` is ignored.
- `git ls-files …/visuals/` returns empty — **no photo is tracked**. The 9 downloaded photos (all PD: 1902–1908 Tolstoy portraits) live only in the git-ignored cache.
- `extracts/` is NOT ignored (committable) and holds only `.txt` (Tolstoy's own PD words + short attributed commentary excerpts); no image files in `extracts/`.
- No `forged/coupon/kupon` image committed anywhere under `website/src/`. The rights-reserved film stills (Bresson, Louhimies) are metadata-only (`usable: false`).

### 9. workRecord — PASS-WITH-MINORS (the one substantive minor)
Record-creating proposal is evidence-anchored; no fabricated dates/venues (1911 Moscow censored + Berlin uncut, posthumous, 1889–1904 window all trace to evidence). Sound calls: `genre: novella` ✓, `mainCategory: Fiction` ✓, `subcategory: Novellas` ✓ (valid under Fiction), `publishedDuringLifetime: false` / `publishedInRussiaDuringLifetime: false` ✓, `bans[].scope: passages-cut` ✓ (valid enum, schema L332).
**MINOR — field-name mismatches vs the live works schema / live records** (the dive's needsReview already says "schema-exact field shapes must be checked"; the specific corrections for the ingestor):
- `dateWritingFinished` → live field is **`dateWritingCompleted`** (0 records use `dateWritingFinished`).
- `datePublished` → live field is **`dateFirstPublished`** (0 records use `datePublished`).
- `publishedPosthumously` → **no such field** in schema or on any of the 15 live records (derivable from `dateFirstPublished` 1911 vs death 1910; drop or treat as note).
- `setting` → **no such field** on any live record (no home in the works schema; keep as prose, not a frontmatter field).
- `titleAlternatives[].type: original` → schema enum is `working · translation · subtitle · variant`; **`original` is not valid** (use `variant` or carry the Russian title via the record's `titleRu`-equivalent). `type: translation` entries are fine.
- `relatedWorks[].relationshipType: thematic` → schema enum is `cycle · sequel · prequel · revision · source · companion · adaptation`; **`thematic` is not valid** (the dive self-flags this; closest valid value for the Power of Darkness / Resurrection links is likely `companion`). 
None of these are fabrications; all are proposal-stage shape mismatches the human ingestion step must reconcile, and the dossier explicitly defers field shapes to that step.

### 10. Coverage ledger honest — PASS
"The author's later verdict" correctly `partial` (Tolstoy left no settled judgment of the unfinished tale; the Dec 1904 subject-list note is the nearest — honest). "Reception & afterlife" `covered` is defensible: posthumous 1911 censorship + Bresson + Louhimies + scholarly reception, with the negative result (no Soviet/pre-1983 adaptation) logged. No `covered` that the evidence shows is really `partial`.

### 11. Bare-voice standing sections — PASS
Themes, Reception, Scholarly context all attribute-don't-assert; the dissenting "Part II is the proof" reading is explicitly the dive's primary-grounded position set against the Bresson tradition, not smuggled in as consensus.

### 12. Marquee integrity — PASS
The `confirms`+`extends` outcome is argued from three numbered evidence points (1886 diagram, 1898 mechanism, the deliberate de-allegorisation), each tied to an evidence row — not asserted. The 1886-programme provenance caveat (commentary-mediated, not in local TEI) is carried honestly and consistently in the marquee (L38), Genesis, Method (L247), the evidence-row significance, notCovered, and needsReview.

---

## Summary for the ingestor (open minors, all non-blocking)
1. **workRecord field names** — rename `dateWritingFinished`→`dateWritingCompleted`, `datePublished`→`dateFirstPublished`; drop `publishedPosthumously` and `setting` (no live field); fix `titleAlternatives[].type: original`→`variant`; resolve `relatedWorks[].relationshipType: thematic`→a valid enum (likely `companion`). (Dive self-flagged the need to check; specifics named here.)
2. `wikiType: work` on the novella is a routing marker to the works schema, not a wiki type — expected, but worth a one-line note at ingestion so it isn't read as a wiki page.
3. Berlin «Свободное слово» vs the 1912 Ladyschnikow set — confirm one-vs-two editions before writing the publication record (already in needsReview).
4. Cannes 1983 prize name — confirm before any page asserts it (already in needsReview).

No fidelity or attribution failures. The dive is ingestion-ready once the human step reconciles the workRecord field shapes.
