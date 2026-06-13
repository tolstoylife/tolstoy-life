# Verifier report — The Christian Teaching (Христианское учение, 1894–96)

Independent judgement-level verification (the author of this report did NOT write the dive).
Mechanical byte-gate `verify_quotes.py` already PASSED 35/35; this report covers the
checks that gate cannot make. Date: 2026-06-13.

**Overall verdict: CLEAN-WITH-MINORS** — 0 FAIL, 2 MINOR.

---

## 1. Belt-and-braces byte-fidelity — PASS
Five+ quotes grepped across the three genres; each `quoteRu` appears verbatim
(exactly once) in its named extract:
- E3 work-text ch.4 «Человек хочет быть зверем или ангелом…» → in `v39_117_191…txt`, sits under `[head] 4`. ✓
- E13 work-text ch.38 «Истина не может войти в человека помимо разума» → under `[head] 38`. ✓
- E22 commentary «Статья разбита Чертковым на восемь частей» → in `v39_242_247_commentary.txt`. ✓
- E23 commentary «2154 лл.» → in commentary. ✓
- E28 letter «опасность отвлеченного умствования» → in `L1894_10_22_Popov_a.txt`. ✓
- (also confirmed) E24 diary, E33 diary, E30 letter — each verbatim, count 1.
Chapter placement spot-checked for every main-text quote (E3→4, E5→7, E7→13, E8→15,
E9→24, E10→31, E11→35, E13→38, E14/E15→60, E16/E17→64). All match the cited chapter.

## 2. Primary claims are source-anchored — PASS
- "64 chapters": `grep -c "^\[head\]"` = 66 = title head + Preface head + chapters numbered 1–64
  (first numbered head = "1 ДРЕВНИЕ ВЕРОУЧЕНИЯ", last = "64 ЧЕГО ЧЕЛОВЕК МОЖЕТ ОЖИДАТЬ В БУДУЩЕМ?").
  66 − 2 = 64. Correct.
- Composition start (23 Mar – 21 Apr 1894): commentary l.5, verbatim. ✓
- 2154 leaves / 115 manuscripts (рук. №№ 1–115): commentary l.53, verbatim. ✓
- Rough completion 5 Oct 1896 on рук. №113 (M. L. Tolstaya's date): commentary ll.37, 93. ✓
- Publisher facts (Brotherhood Publishing Co., London 1898, reprinted NY; Purleigh Russian ed.;
  Chertkov's 8 parts + §§1–404 "для удобства читателя"; posthumous Russian 1911 + Birukov 1913):
  commentary l.51, verbatim. ✓
No floating primary claims found.

## 3. Secondary claims are ATTRIBUTED, not asserted — PASS (with 1 MINOR)
- Scholarly context attributes Stepanova (2020), Maude (1910, quoted + dated),
  Medzhibovskaya, Gustafson. Maude's "minor/abstract/unfinished" framing is explicitly
  flagged "attributed, not adopted." Reception section qualifies "thin" with an
  open-archive caveat. No mainstream view stated as fact.
- MINOR: **Gustafson** is named as a counter-authority in Scholarly context but is the one
  named scholar absent from the **References** list (Maude, Stepanova, Medzhibovskaya, Bartlett
  are all present). Add a Gustafson entry to References, or drop the name.

## 4. Triangulation integrity — PASS
All six `triangulation[].evidenceRef` (E8, E10, E28, E31, E21, E22) resolve to real
ledger ids. All `relation` values valid: extends ×3, complicates ×1, confirms ×1,
contradicts ×1 — every one ∈ {confirms, complicates, contradicts, extends}.

## 5. Entities & vaultStatus — PASS
`wikiType` values used: person ×9, concept ×2, work ×1 — all valid (work = the Lab/works-record
entity, not a wiki page; flagged as such in `role`). vaultStatus spot-checks vs `rg --files website/src/wiki/`:
- Vladimir Chertkov → `Vladimir Chertkov.md` exists. claimed exists ✓
- Pavel Biryukov → `Pavel Birukoff.md` exists (loose translit). claimed exists ✓
- Evgeny Popov → no file. claimed missing ✓
- Tatyana / Sophia / Alexandra / Maria Tolstaya → all exist. claimed exists/stub ✓
- Ivan Tolstoy (Vanichka) → no file. claimed missing ✓
Maria/Alexandra disambiguation correctly deferred to needsReview (not asserted).

## 6. workRecord soundness — PASS
- `action: create`, `recordExists: false`; on-disk dir
  `website/src/works/non-fiction/treatises/the-christian-teaching/` confirmed ABSENT. ✓
- `titleAlternatives[].type`: 5×working + 1×translation — all ∈ {working, translation, subtitle, variant}. ✓
- `completionStatus: incomplete` ∈ {complete, incomplete, fragmentary}; judgment call documented in needsReview. ✓
- `relatedWorks[].relationshipType`: companion ×2 ∈ enum. ✓
- `firstPublishedVenueType: book` ∈ {journal, newspaper, book, samizdat}. ✓
- `bans` omitted (no documented ban). ✓
- Free Age Press correction PRESENT (key findings + publication section + needsReview):
  "1898 imprint is Brotherhood Publishing Co.; FAP founded 1900." No fabricated dates/venues. ✓
- German title `Das christliche Glaubensbekenntnis` flagged low-confidence placeholder. ✓

## 7. Translations labelled — PASS
index.md: 23 Cyrillic blockquote glosses, 23 "(working English)" markers — every gloss tagged.
dossier: all 35 `quoteEn` carry "(working English)". Inline parenthetical paraphrases attached
to the Russian (dive convention) are not blockquoted translations — acceptable.

## 8. Bare voice — PASS
Marquee stated as a tested claim ("it systematises and calms the doctrine; it does not soften it",
relation language confirms/complicates/extends/contradicts), not asserted. No contested mainstream
label ("Tolstoyan", "moralistic dogmatist") adopted in the dive's own voice — the sole "Tolstoyan"
hit is the venue name "Tolstoyans" in References; "two Tolstoys" appears only inside an attributed
description of the scholarly reflex. No hagiography.

## 9. Rights hygiene — PASS
- `extracts/` holds only PD text extracts — no image files (jpg/png/gif/pdf/webp). ✓
- No image files tracked under the dive dir or under `website/src/` for this dive. ✓
- `visuals/` is git-ignored (confirmed via `git check-ignore`). ✓
- Every visual (V01, V02, V04, V06, V09, V10) carries a `licence`: 5×PD + 1×unknown (V10 manuscript). ✓
- Only V01/V04/V06 (all PD) embedded in index.md; the `unknown`-licence V10 is NOT embedded. ✓

## 10. nl2br prose — PASS
Paragraphs/blockquotes are single source lines (longest prose lines 845–1171 chars);
no hard-wrapping that nl2br would turn into spurious breaks.

---

### Minor items (non-blocking)
1. Gustafson named in Scholarly context but missing from the References list (item 3).
2. Narrative nuance (not an error): index.md line 147 glosses молитва временная / ежечасная,
   whose own chapter heads are 61/62, while the two prayer quotes (E14/E15) correctly sit in
   ch.60 «О МОЛИТВЕ» (which introduces prayer). Cited "ch.60" is accurate; consider a half-line
   noting chs 61–62 elaborate each prayer, for reader precision. Optional.

### Overall verdict
**CLEAN-WITH-MINORS** — 0 FAIL, 2 MINOR. The dive is byte-faithful, source-anchored,
correctly attributed, schema-sound, rights-clean, and bare in voice. Safe to ship; the two
minor items are cosmetic.
