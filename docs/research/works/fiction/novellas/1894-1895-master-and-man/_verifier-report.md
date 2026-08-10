# Verifier report — Master and Man (Хозяин и работник) novella-dive

**Role:** independent adversarial verifier (fresh context). Did not produce the dive.
**Date:** 2026-06-10
**Mechanical gate:** verify_quotes.py 24/24 PASS (not re-run, per instructions). This report covers the judgement-level checks the script cannot make.

---

## 1. Byte-fidelity spot-check (belt-and-braces) — PASS

Five quotes pulled from index.md across all four genres, each confirmed verbatim in the named extract:

| # | Quote (head) | Genre | Extract | Result |
|---|---|---|---|---|
| 1 | «ему кажется, что он — Никита, а Никита — он, и что жизнь его не в нем самом, а в Никите» | work text (ch. IX) | v29_003_046_main-text.txt | verbatim ✓ |
| 2 | «покрывая его не только своей шубой, но и всем своим теплым, разгоряченным телом» | work text (ch. IX) | v29_003_046_main-text.txt | verbatim ✓ |
| 3 | «он Никита, а Никита — он … Жив Никита, значит я жив» (вариант № 33, рук. 11) | variant/proof | v29_295_324_variants.txt | verbatim ✓ |
| 4 | «Нет характера ни того, ни другого. Теперь знаю, что сделать» | diary 6 Jan 1895 | _diaries_composition.txt | verbatim ✓ |
| 5 | «почти безумный припадок … Она была близка к самоубийству» | letter to Strakhov 14 Feb 1895 | _letters_composition.txt | verbatim ✓ |

Additionally cross-checked the coda quote «как желал, под святыми и с зажженной восковой свечкой в руках»: index.md uses the diminutive «свечкой», and the **final text** (v29_003_046, ch. X) also reads «свечкой» — the «свечой» form appears only in the earlier variant № 17. So the index correctly tracks the final text. No discrepancy. All other index/dossier prose quotes spot-checked (benefactor line, 40-roubles ledger, «двух смертей не бывать», «Известно, грехи», «Довольно ничтожно», Strakhov veto) also matched.

## 2. Keystone claim — substitutionary death was a LATE proof-stage addition — PASS (HOLDS)

This is the dive's central finding and it holds completely against the primary record.

- **First rough redaction (Первая черновая редакция, рук. 2):** Brekhunov's awakening is solitary and self-regarding — «И вдруг ему стало светло, радостно. Он поднялся над всем миром… Он узнал себя, узнал в себе что-то такое высокое, чего он в 40 лет ни разу не чувствовал в себе» (extract line 281). It is NOT tied to saving Nikita. The draft then ends on the workman alone: Nikita wakes, recognises the «холодное дерево» as the dead master, «Андреич как чурбан отвалился на снег», and «огляделся и в 100 саженях увидал, что чернеется, и пошел туда. Это была деревня» (line 285). No deliberate warming, no merging of selves, no «Жив Никита, значит жив и я». Confirmed verbatim.
- **Variant № 33 (рук. № 11):** the «Описание»/«Варианты» extract explicitly heads this block «№ 33 (рук. № 11)» (line 545) and carries the self-dissolution in final form: «ему кажется, что он Никита, а Никита — он, и что жизнь его не в нем самом, а в Никите… — Жив Никита, значит я жив» (line 547). The dive's identification of рук. 11 as the *Severny Vestnik* galley-proof stage is consistent with the manuscript description and the letters (proofs ran Jan–Feb 1895; final corrected proofs sent to the editorial office mid/late Feb per letters v68_030/v68_031).
- **The intermediate build** is also evidenced: var № 18 / рук. 4 «А на что ему жить? Какая его жизнь» (line 411) and var № 26 / рук. 5 «Тот ужас смерти, который он испытывал сейчас, он перенес на Никиту» (line 497) — both verbatim.
- **The diary agrees to the day:** 6 Jan 1895 «Нет характера ни того, ни другого. Теперь знаю, что сделать» (v53_003_004). The 3 Jan entry «Стало порядочно по художественности, но по содержанию еще слабо» frames it exactly as the dive narrates.

The keystone is a documented compositional fact, not merely an interpretation. No issue.

## 3. Secondary/scholarly claims attributed, not asserted — PASS-WITH-NOTES

Every *specific* scholarly claim in the dive is attributed: Gustafson (emblematic/theological realism; does not trace to On Life), Deresiewicz (renunciation-to-death; "biblical simplicity"; Nikita "holds his life cheap"), Saunders (redirection of "same old energy"), Austin (church-reader on parallel salvation). All four are quoted/named at point of use AND carry a References entry. The dossier `scholarship.source` fields name sources per triangulation row. No scholarly proposition is smuggled in as the dive's own factual voice.

**MINOR:** Simmons and Wilson are named once (index.md l.187) as part of "the biographical and critical mainstream (Troyat, Bartlett, Simmons, Wilson)" but have **no References entry**. They are invoked as a named camp generality, not as the source of any specific quoted claim (each specific claim in that paragraph routes to Gustafson/Deresiewicz/Saunders, who are referenced), and both are real, standard Tolstoy biographers, so nothing is fabricated. Adding two References lines (Ernest J. Simmons; A. N. Wilson) would close the loop. Polish, not a must-fix.

## 4. scholarship.triangulation — PASS-WITH-NOTES

All four rows reference valid evidenceRefs (E1, E3, E12, E2) and use valid relations (extends, complicates, extends, extends). Marquee outcomes match the prose:
- On Life (E1) → `extends` ✓ (index l.41)
- exploiter (E3) → dossier `complicates`; index narrates "`complicates` → `extends`" ✓ (index l.55) — defensible arc: the received view *complicates* the simple reading, the dive then *extends* past it. The single-enum dossier field correctly stores the received-view relation (`complicates`).
- What Is Art (E2) → `extends` ✓ (index l.57)

**MINOR labelling wrinkle:** the top-line "Marquee verdict: `confirms` + `extends`" (index l.21) introduces "`confirms`," but none of the three individual hypothesis outcomes is labelled `confirms` (they are extends / complicates→extends / extends). "Confirms" here evidently denotes the broadly-agreed base ("the death dramatizes On Life — broadly agreed") with the dive's own contribution being `extends`. Reasonable, but the bare-`confirms` token is not anchored to a triangulation row. Cosmetic.

## 5. Entities — PASS

- **Brekhunov & Nikita** routed as `character`, vaultStatus `missing` — confirmed: no `Vasily Brekhunov.md` / `Nikita*.md` (and no loose-match brekhunov/brexunov/nikita) in website/src/wiki. ✓
- **prototypes[]** NOT over-claimed: both carry `basis: editorial`, `certainty: conjectured`, `person: ""`, with notes explicitly stating "no single documented prototype" and "Do not assert a specific model." Correctly conservative — Brekhunov's name is treated as an authorial characterising name (брехать), Nikita as a Yasnaya-Polyana type. ✓
- **vaultStatus `exists`** (5): Sophia Tolstaya, Vladimir Chertkov, Pavel Birukoff, Tatyana Tolstaya, Maria Tolstaya — all five files present (transliteration cases handled: Sofia→"Sophia Tolstaya.md", Biryukov→"Pavel Birukoff.md"). ✓
- **vaultStatus `missing`** (Strakhov, Gurevich, Volynsky, Meyendorf, Olsufyeva, Orlov, Vanechka/Ivan Lvovich): all genuinely absent, including under loose transliteration matches (strakhov/gurevich/volynsk/flekser/meyendorf/majndorf/olsufy/orlov) — no transliteration-gotcha false-missing. ✓

## 6. workRecord — PASS

- All proposed field names exist in website/schema/tolstoy-works-schema.md (publishedDuringLifetime, publishedInRussiaDuringLifetime, dateWritingStarted, dateWritingCompleted, dateFirstPublished, firstPublishedVenue, firstPublishedVenueType, dateFirstPublishedInRussia, firstPublishedInRussiaVenue, authoringLocations, relatedWorks, relationshipType). ✓
- **OS→NS arithmetic (+12 days, 19th c.) all correct:** 1894-09-06 → 1894-09-18; 1895-01-14 → 1895-01-26; 1895-03-05 → 1895-03-17. Verified by computation. ✓
- **Two CORRECTIONS valid:** live record currently has `publishedDuringLifetime: false` and `publishedInRussiaDuringLifetime: false`; both → `true` is correct. The novella WAS published March 1895 (15 years before Tolstoy's death), in Russia, legally (censor's permission 17 Feb 1895), uncensored. ✓
- No fabricated dates/venues: Severny Vestnik no. 3 (March 1895), pp. 137–175, plus simultaneous Posrednik + SAT vol. 14, all consistent with «История писания». The dossier appropriately flags the `oldStyle`/`approximate` inline keys as "shape to the schema" (the schema uses sibling `*OldStyle`/`*Approximate` fields) — a mapping note for the ingestion step, correctly left to a human. ✓

## 7. Coverage ledger honesty — PASS

Reception marked `partial` is honest: the gap (specific 1895 Symbolist/Severny-Vestnik-circle reviews not retrieved) is named in the note, in `notCovered`, in `needsReview` (Leskov), and in the index's "Material not covered." Nothing is marked `covered` that the evidence shows is partial. The Leskov non-claim is handled with admirable restraint (died 5 Mar 1895 = day of release, so no public reaction could exist — correctly NOT asserted). `Source-research sub-layer` correctly marked `not-covered` / not-applicable (invented work, no «Список источников»).

## 8. Bare voice / attribute-don't-assert — PASS

Genesis, Reception, and Scholarly-context keep the project's factual register. Contested framings are attributed, not adopted: the conversion-parable and Ivan-Ilyich-diptych readings are explicitly flagged as "positions to attribute, not baselines to confirm" (index l.12); the popular-biography over-emphasis on the domestic drama is named as *their* framing (Bartlett; Meek), not endorsed. Tolstoy's own dislike of the story is carried "as his own verdict, attributed — not as the dive's evaluation." No editorial labels stick in the dive's own voice.

## 9. Rights — PASS

- visuals/ IS git-ignored (`git check-ignore visuals` → match). ✓
- No image files (.jpg/.png/etc.) committed anywhere under the dive (`git ls-files`). ✓
- The Posrednik dealer scan (russia-posrednik-1895-first-edition) is catalogued-only: `access: restricted`, `rights: rights-reserved`, `licence: rights-reserved`, `usable: false`, `localPath: ""`, note "NOT downloaded." Correct — no rights violation. ✓

## 10. Translations labelled — PASS

All 13 working-English renderings in index.md carry the "(working English)" tag. The dossier quoteEn fields likewise prefix "(working English)". ✓

---

## Summary

| Check | Verdict |
|---|---|
| 1 Byte-fidelity spot-check | PASS |
| 2 Keystone (late proof-stage substitution) | PASS — holds |
| 3 Scholarly attribution | PASS-WITH-NOTES (Simmons/Wilson lack References entries) |
| 4 Triangulation | PASS-WITH-NOTES (bare-`confirms` token unanchored) |
| 5 Entities / vaultStatus / prototypes | PASS |
| 6 workRecord (dates, corrections, fields) | PASS |
| 7 Coverage honesty | PASS |
| 8 Bare voice | PASS |
| 9 Rights | PASS |
| 10 Translations labelled | PASS |

**MUST-FIX:** none.

**MINOR (polish, optional):**
1. Add References entries for Simmons (Ernest J. Simmons, *Leo Tolstoy*) and Wilson (A. N. Wilson, *Tolstoy*), or drop the two inline names — currently named as "mainstream" without a References line.
2. The top-line marquee token "`confirms` + `extends`" introduces a `confirms` that none of the three per-hypothesis outcomes carries; consider rewording to make clear `confirms` = the broadly-agreed base and `extends` = the dive's contribution (the prose already says this; only the compressed token is loose).

The keystone redaction claim — the dive's central finding — is fully verified against «Варианты» / «Описание рукописей» and corroborated to the day by the diary. All factual anchors, dates, corrections, vaultStatus values, and rights handling check out.

## VERDICT: PASS-WITH-NOTES (0 must-fix, 2 minor)
