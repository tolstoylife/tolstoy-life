---
title: "Verifier report — After the Ball (После бала) 1903 corpus dive"
layer: reference
date: 2026-06-12
role: independent verifier (adversarial, evidence-based)
verdict: CLEAN-WITH-MINORS
---

# Verifier report — «После бала» (After the Ball) 1903 dive

Independent adversarial check of a completed novel-mode corpus dive. I did not write it.
Method: re-ran the mechanical gate, then performed the judgement-level checks the script
cannot. Findings are located (file + line/section) and severity-rated.

## Summary verdict

**CLEAN-WITH-MINORS** — 0 blockers, 0 should-fix, 3 minor, 4 nit.

The dive is sound. Byte-fidelity passes (21/21). Every primary claim in `index.md` ties
to an evidence row or is attributed. Secondary scholarship is attributed, not asserted.
The marquee (`complicates` + `extends`) is genuinely tested and the high-value `extends`
claim is real — the variants do show the narrator entering military service, which the
published version reverses. Dossier structure, entity routing, prototype certainty,
workRecord schema validity, NS dates, coverage honesty, voice, and rights all check out.
The minors are small wording/consistency items, none load-bearing.

---

## 1. Byte-fidelity (mechanical gate + spot-check)

- `verify_quotes.py` re-run: **21/21 verbatim, 1 facsimile ok, 0 missing — PASS (exit 0).**
- Independent spot-check across five different extract files (story / variants / commentary /
  diary / letter) — each `quoteRu` found exactly once in its named extract:
  - E07 published ending — `extracts/v34_116_125_Posle_bala.txt` ✓
  - E10 variant (narrator serves) — `extracts/v34_484_490_Posle_bala_Varianty.txt` ✓
  - E11 variant (becomes the colonel) — same file ✓
  - E12 letter «легальном издании» — `extracts/v74_144_...6may.txt` ✓
  - E13 diary «Рассказ о бале и сквозь строй» — `extracts/v54_177_178_1903_06_09.txt` ✓
  - E15 «Николай Палкин» recollection — `extracts/v34_550_551_Istorija.txt` ✓
  - E21 first-print 1911 — same file ✓
- Translation faithfulness: working-English renderings checked against the Russian in
  context (E08 «пошла на убыль» = "began to fade"; E18 read in its full diary line
  «Недоволен. За то „А вы говорите" недурно»). No overstatement or editorialising in the
  translations. All carry "(working English)". **No distortions found.**

## 2. Every primary claim in index.md is source-anchored

Walked every factual assertion about text / genesis / prototype / variants / dates /
publication. Each ties to an evidence row (E01–E21) or is explicitly attributed:
- Kishinev-commission genesis → E12, E13; conception 9 June beside Hadji Murat → E13
  (verbatim «подвигаюсь в Николае Павловиче» confirmed in the 9 June extract).
- 1886 «Николай Палкин» as the seventeen-year-old memory → E15.
- Prototype (brother Sergei / Koreysh) → E14 (author-stated sujet) + attribution.
- Ending moved complicity → refusal → E09 / E10 / E11 / E07.
- Two-day draft, title walk, 1911 first print → E17, E19, E20, E21.

**No unanchored factual assertion stated in the dive's own voice was found.** (Minor M1
below on one slightly loose gloss — a faithfulness nuance, not an unanchored claim.)

## 3. Secondary / scholarly claims are attributed, not asserted

§Reception and §Scholarly-context consistently attribute: "Trostnikov 1965, Zhdanov 1971,
via Zholkovsky", "Shklovsky … via Russian pedagogy", "per the Tolstoy State Museum",
"Zholkovsky reads Ivan's withdrawal as…". The thin-evidence Eikhenbaum point is openly
hedged ("No stand-alone Eikhenbaum essay … was located", and flagged in `needsReview`).
The contested label **«Tolstoyan» is handled as the mainstream's word** and linked out to
the project's tolstoyanism dive (index.md lines 196, 213, 263) — not adopted in the dive's
own voice. **Clean.**

## 4. The marquee is tested, not foregone

The hypothesis "the story is really about «случай» (chance)" is framed as
"**Hypothesis (to test, not assert)**" (index.md line 30) and worked through three
independent pushes (genesis, text, redaction history) before the `complicates` + `extends`
outcome. This reads as a tested triangulation, not a pre-baked conclusion.

**The `extends` claim — the dive's highest-value contribution — is real and verified.**
The variant extract (`v34_484_490_Posle_bala_Varianty.txt`, line 75) reads, in the
narrator's own first person: «…после университета **поступил в военную службу** … все-таки
считал, что **военная служба хорошее дело**» (E10), and a second variant has him become
like the colonel and repent only in old age (E11). The published ending (E07) reverses
this to «нигде не служил … не годился». So the variants genuinely show the narrator
entering service, which the published version negates — the dive's claim that Tolstoy
*built* the non-participation reading by hand is primary-sourced, not asserted. **Holds.**

## 5. Dossier structural integrity

- **triangulation** — all 5 entries reference real evidence IDs (E07×2, E10, E04, E15) and
  use valid relations (complicates / confirms / extends — all in the
  confirms/complicates/contradicts/extends enum). ✓
- **entities** — all 15 route to valid wiki types per `wiki-schema.md` v1.4
  (character ×3, person ×10, concept ×1, event ×1). vaultStatus accurate:
  - "Sergei Tolstoy.md" in the vault is confirmed the **SON** (Sergei Lvovich, 1863–1947,
    composer/musicologist) — `website/src/wiki/Sergei Tolstoy.md` lines 5–22. The dive's
    "Sergei Nikolaevich Tolstoy" (the **brother**, 1826–1904) is correctly `vaultStatus:
    missing` with an explicit CAUTION not to conflate (dossier lines 440–451). **No
    conflation.** ✓
  - "Leo Tolstoy" and "Vladimir Chertkov" correctly `exists` — both files present in
    `website/src/wiki/`. ✓
- **prototypes[]** — all three certainties are `probable` (lines 371, 394, 418). The
  colonel↔Koreysh dancing/flogging fusion is `probable`, with an inline note that it "rests
  on one museum source — hence «probable», not «documented»" and a matching `needsReview`
  entry. The two "documented" strings elsewhere are (a) the `person` role description for
  Koreysh as the documented love-plot father — legitimate, and (b) prose explaining why the
  fusion is *not* documented. **Not over-claimed.** ✓

## 6. workRecord proposals — evidence-anchored and schema-valid

Checked every `workRecord.fields[]` name against `tolstoy-works-schema.md` (v9). All are
real schema keys. Enums valid:
- `genre: short_story` ✓, `mainCategory: Fiction` ✓, `subcategory: Short Stories` ✓
  (Short Stories is a valid subcategory under Fiction, schema line 73).
- `firstPublishedVenueType: book` ✓ (enum: journal/newspaper/book/samizdat).
- `relatedWorks[].relationshipType: source` ✓; `completionStatus: complete` ✓ (with an
  honest caveat re «окончательной отделки не получил», also in needsReview).
- `titleAlternatives[].type: working`, `.language: ru` ✓.
- `bans: []` is **defensible** — there was no banning authority; the story was self-withheld
  under anticipated censorship and published freely posthumously. The dossier documents this
  in `censorshipNotes` and an inline note, exactly as the schema intends. ✓
- **NS dates verified**: OS 1903-08-06 → NS **1903-08-19** ✓ and OS 1903-08-20 → NS
  **1903-09-02** ✓ (independently computed, +13 for 1903). `oldStyle` companions present on
  the dated fields and inside `authoringLocations`. **No fabricated date or venue; no
  invalid field name.** Page ranges are correctly distinguished — 116–125 (PSS т.34 modern
  text) vs 117–128 (the 1911 «Посмертные» first edition); no conflation.

## 7. coverage honesty

- The full-text close-read is plausible (a ~10-page story; the marquee, the suede-glove
  motif, the ending, and all six variants are all worked from the text). `covered` is honest.
- "Publication, censorship & translation" = `partial` is **honest**: the translation lineage
  is genuinely uncollated — only a passing mention of Maude survives in the `_scholarship`
  sidecar, no collation. The `notCovered` block and "Material not covered" section both name
  it. No `covered` surface is really `partial`. ✓

## 8. Voice & rights

- Voice is bare and factual; no editorialising in the dive's own voice beyond attributed
  readings.
- All translations carry "(working English)". ✓
- `visuals/` is git-ignored (confirmed: `git check-ignore` returns the path from both repo
  root and `docs/`; **0 files tracked under visuals/**). The PD facsimile .png lives in
  `extracts/` and is **not** git-ignored (eligible to commit — correct, it is PD Tolstoy
  text). The whole dive dir is currently untracked (`??`) — the expected pre-commit state.
  When committed, the PD facsimile goes in and the rights-various Commons images stay out.
  **No rights-reserved image will be committed.** ✓

---

## Findings (severity-rated)

**M1 (minor) — index.md line 96–98, E18 gloss is looser than the dossier's.**
The dossier E18 `quoteEn` correctly renders «За то „А вы говорите" недурно» as "On the other
hand, 'But You Say' is not bad." In index.md the same quote is introduced as Tolstoy "gave
his own modest verdict, naming the story by its then-title «А вы говорите»" and the block
quote is left without the "On the other hand…" framing visible in the prose. Faithful, but
the prose slightly under-translates the contrastive «За то» (he is contrasting it favourably
against the tales he was «недоволен» with). Cosmetic; the byte-true quote and the dossier
gloss are both correct.

**M2 (minor) — index.md line 248 / notCovered, the «Николай Палкин»↔Koreysh "same man"
question.** The dive is careful to keep this `probable`, but the §Characters prose (line 186)
states "the «Николай Палкин» colonel is the same recollection" with more confidence than the
commentary's own "relates *apparently* to the Kazan period." The hedge exists elsewhere, so
this is a tone wobble, not an over-claim — worth softening "is the same recollection" to
"apparently the same recollection" at ingestion.

**M3 (minor) — references cite letter №222 (25 Aug 1903) but it is not used as evidence.**
Both index.md line 267 and dossier line 994 list т.74 letter №222 in the primary references,
yet no evidence row draws on it (only №144 is cited, as E12). Harmless, but a reader chasing
the reference will find it unused. Either cite it or drop it from the primary list.

**N1 (nit)** — index.md line 22 uses ``complicates`d`` and ``extends`ed`` (backtick-verb +
suffix). Reads awkwardly; cosmetic.

**N2 (nit)** — the `contradictions` block (dossier 957–960) is a genuinely useful catch (the
commentary's «т. 73» / «печатном» vs the letter's т.74 / «легальном»). Independently
confirmed the letter file contains «легальном». No action; noting it as a positive.

**N3 (nit)** — `coverage` lists "Manuscript repository / scans" as `not-covered` while the
prose says 12 MSS / 104 leaves are summarised; the distinction (commentary summary vs actual
scans) is correct but a reader may read the two as contradictory. Wording only.

**N4 (nit)** — Ivan Zakharyin-Yakunin and Nikolai Obolensky flagged as borderline mints in
`needsReview` — correctly deferred to the ingestion phase; no verifier action.

---

## Overall verdict

**CLEAN-WITH-MINORS** — 0 blockers, 0 should-fix, 3 minor (M1–M3), 4 nit (N1–N4).
The dive is accurate, well-anchored, honestly attributed, schema-valid, and rights-clean.
The marquee `extends` claim — the variants showing the narrator once served — is the
dive's highest-value finding and it is fully borne out by the primary text. Nothing blocks
ingestion; the minors are wording/consistency polish for the ingestion pass.
