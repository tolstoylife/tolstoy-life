# Phase-5 Verifier Report — *What Is Art?* (Что такое искусство?) corpus work-dive

**Date:** 2026-06-07
**Verifier:** Phase-5 judgement-level review (skeptical, fresh pass)
**Scope:** `index.md`, `dossier.yaml`, `extracts/` deliverables, against the read-only source corpus.
**Mechanical gate already passed:** `verify_quotes.py` 23/23 (not re-run; this pass does what a script cannot).

**Verdict: CLEAN-WITH-NOTES.** No must-fix items. Two should-fix items (one unanchored anecdote, one quoted-Russian term that is not verbatim-sourced) and a handful of nits. The dive is byte-faithful where it claims to be, attribution discipline is exemplary, the concept map is rigorously labelled, and the schema/entity/triangulation layers are sound apart from one controlled-vocabulary value.

---

## Check-by-check

### 1. Byte-fidelity spot-check — PASS
Five `evidence[].quoteRu` confirmed verbatim in their named extract files (beyond the 23/23 mechanical gate):
- `wia-selfcondemn-xvi` → `extracts/v30_027_203_notes.txt` — **verbatim, present** (the recovered self-condemnation footnote; sits inside the larger recovered note bracket, intact).
- `wia-pref-grot` (preface, Grot's softening list) → `v30_204_206_…txt` — verbatim.
- `wia-pref-censor-redemption` (preface) — verified verbatim elsewhere in the same file.
- `wia-genesis-prostitution` (diary 19 Feb 1898) → `v53_182_184_1898_02_19.txt` — verbatim.
- `wia-stasov-books` (letter 3 Sep 1897) → `v70_157_V_V_Stasovu.txt` — verbatim.
- `wia-genesis-jan1897` head + ellipted tail → `v88_431_yanvarya12.txt` — both halves verbatim around the elided `[…]`.
- Spot bonus: `wia-kant-iii` and `wia-guyau-iii` both verbatim in the treatise extract.

### 2. Primary claims anchored — MOSTLY PASS, one gap (should-fix)
Dates, chapter numbers, the publication sequence, the people, the textual history all trace to an extract or to the attributed Gudzy commentary. Verified live:
- "first five chapters … No. 5 (Nov–Dec 1897)… released 17 March 1898" — supported by the Gudzy history (`v30_509_555`); the 17 March date is corroborated by Tolstoy's 17 March letter to Chertkov cited there.
- "S. A. Tolstaya's Collected Works (Kushnerev, early April 1898)" and "Posrednik … closest to her text" — both in `v30_509_555` (Кушнерев ×3, Посредник ×3).
- "~seventy works on aesthetics" — anchored: Lazursky's diary in the commentary records Tolstoy's "около семидесяти выписок."
- **Lazursky's role** ("checked Tolstoy's summaries of the aestheticians … against their source texts") — strongly anchored: the commentary quotes Lazursky's diary, Tolstoy asking him to "проверить его изложение взглядов разных эстетиков и писателей с цитатами … нет ли где неточности; выставить страницы цитат." Excellent grounding.
- **Wagner "attended one act in Moscow"** (concept-map row) — anchored to the treatise's own Ch XIII first-person performance account ("Когда я пришел, огромный театр уже был полон…", "как я был раз на репетиции…"). Not a fabricated biographical assertion.

**GAP (should-fix #1):** `index.md` line 45 — "*(Chekhov, visiting him in March, reported that Tolstoy had "read sixty books on art")*." This anecdote is **not anchored** to any extract or to the attributed commentary. The only Chekhov reference in the Gudzy history (`v30_509_555`) is an unrelated anecdote (Chekhov telling Tolstoy about Nosilov's story "Театр у вогулов"). The "sixty books on art" figure is a secondary biographical anecdote presented in the dive's own voice with no citation. Either source it, attribute it ("by a widely-repeated anecdote…"), or drop it — the adjacent "seventy works" figure is already properly anchored and carries the point.

### 3. Attribution discipline — PASS (exemplary)
- Reception section explicitly frames reviews "as attributed opinion, not verdict"; every verdict is named + quoted (Faguet, Rilke, Shaw, Walkley). No contested label asserted in the dive's voice.
- "moralist"/"narrow-minded" appear only inside Faguet's quoted words; "moralistic excess"/"arbitrary" appear only as the attributed mainstream foil (Bayley; Simmons) and are then explicitly rebutted per the project voice-rule.
- No "philistine" anywhere; no contested label sticks in the dive's own voice.
- Scholarly-context attributes every claim by name+year (Jahn 1975, Bayley 1986, Mounce 2001, Šilbajoris 1991, Maude).

### 4. Concept/philosopher map integrity — PASS
- `extracts/_concept_map.md` reading-conventions block states the "received reading" column is "the scholarly-consensus *foil* … not a truth Tolstoy 'got wrong,'" and that all "faithful or flattened?" judgements are "the dive author's own analytical reading, not settled fact." The `index.md` table header carries the same framing. Matches the `needsReview` admission that no monograph argues the flattening at length — the dive does not pretend a scholarly backer exists.
- Spot-checked two philosopher rows against the treatise text:
  - **Kant** — the disinterested-pleasure rendering ("Urtheil ohne Begriff und Vergnügen ohne Begehren") is verbatim in the treatise; the "flattened into hedonism" judgement is borne out by Tolstoy's own Ch VI "красота есть … то, что нам нравится." Fair.
  - **Guyau** — the admired passage ("Искусство … поднимает человека из личной жизни в жизнь всеобщую") and the "cookery/perfume/touch" objection ("искусством признается искусство костюмерное, вкусовое и осязательное") are both verbatim. The "partly flattened, partly the unacknowledged source" reading is fair and textually grounded.
- Byte-fidelity notes in the map are scrupulous (OCR-artifact elisions at Schopenhauer/Schelling flagged rather than silently corrected; footnote superscripts omitted by stated policy).

### 5. Triangulation validity — PASS
- 5 `scholarship.triangulation[]` entries; all 5 `evidenceRef` values resolve to real `evidence[].id` (`wia-def-v`, `wia-religious-criterion-xvi`, `wia-selfcondemn-xvi`, `wia-stasov-books`, `wia-pref-censor-redemption`).
- All 5 `relation` values are in the allowed set (confirms ×2, complicates ×2, extends ×1).
- (`wia-maupassant-3conditions` is referenced under `contradictions[]`, also a valid id — not a triangulation row.)

### 6. Entities — PASS
- All `wikiType` values valid (person ×11, concept ×4, institution ×2, work ×1).
- `vaultStatus`: 3 `exists`, 14 `missing`, 1 `stub`. Verified against `website/src/wiki/` and `website/src/works/`:
  - `exists`: Leo Tolstoy (`Leo Tolstoy.md` present), Vladimir Chertkov (`Vladimir Chertkov.md` present), Pavel Birukoff (`Pavel Birukoff.md` present). **All correct.** Note: the brief anticipated only Birukoff + Chertkov, but `Leo Tolstoy.md` does exist in the vault, so `exists` for Tolstoy is accurate, not an over-claim.
  - `stub`: What Is Art? (work) — `What Is Art?.md` exists with `recordStatus: draft` and empty/false fields. Calling it a `stub` is accurate.
  - `missing`: Maude, Grot, Stasov, Lazursky, Strakhov, Taneyev, Kant, Wagner, and the concept/institution entities — none have wiki pages (the wiki dir holds only Tolstoy-family + Birukoff + Chertkov + Tolstoyanism pages). All correct.

### 7. workRecord — MOSTLY PASS, one controlled-value error (should-fix)
- All proposed `field` names are real schema keys (`tolstoy-works-schema.md`): the chronology fields, `firstPublished*`/`firstPublishedInRussia*`, `publishedDuringLifetime`, `publishedInRussiaDuringLifetime`, `censoredVersionExists`, `censoredVersionNotes`, `titleAlternatives`, `bans`, `authoringLocations`, `identifiers.jubileeEdition.volumes`, `themes` — all present in the schema (the array fields appear as `bans[]` / `authoringLocations[]`).
- `titleAlternatives` uses the correct object shape (`title`/`type`/`language`); `type: working` and `language: ru` are valid enum/code values. **Correct.**
- **`publishedInRussiaDuringLifetime: true` correction — justified.** Schema defines it as `true` if legally published in Russia before Nov 1910, `false` if banned or only abroad. The censored serial (1897–98) and Tolstaya's Collected Works (1898) were legally published in Russia in censored form; censored ≠ banned. The dive flags the censorship via `censoredVersionExists: true` + notes. Defensible and well-documented.
- **SHOULD-FIX #2: `bans[].scope` uses a free-text value, not a controlled-vocabulary value.** Dossier line ~675: `scope: "the complete / uncensored text (only a censored version could appear in Russia in Tolstoy's lifetime)"`. The schema enumerates `bans[].scope` as `complete-ban · passages-cut · serialization-refused · confiscation · pre-publication-rejected`. The episode described (whole passages cut from the journal book by the spiritual censor) maps to **`passages-cut`**; the free-text string belongs in `bans[].notes`. The dossier's own `note` already concedes "Not a clean outright ban" and suggests ingestion may prefer to record this only via `censoredVersionExists` — so this is a flagged soft spot, but the literal `scope` value as written is not schema-valid and would fail a strict validator. (`authorityType: holy-synod` is valid; `banningAuthority: "Spiritual Censorship (Russian Orthodox)"` is free-text and fine, with the dossier's own "verify the authority's exact name" caveat.)

### 8. Coverage honesty — PASS
7 `covered`, 4 `partial`. The `partial` flags are honest and match the dive: "Redactions & textual history" (variants not deep-collated), "Reception — Russian society & church" (Stasov's published reaction not recovered), "Visual & manuscript record" (gaps listed), "The author's later verdict" (post-1898 not swept). No `covered` surface is over-claimed — each `covered` entry corresponds to substantive material actually present.

### 9. Translations labelled — PASS
17/17 blockquotes in `index.md` carry "(working English)"; 23/23 `quoteEn` in `dossier.yaml` carry "(working English)". Complete.

### 10. Rights / hygiene — PASS
- `extracts/` holds only `.txt` (PD Tolstoy text), `.md`/`.html` (analysis deliverables), and `_recover_notes.py`. No images.
- `visuals/` holds 5 cached `.jpg`s and is confirmed git-ignored (`git check-ignore` returns the path).
- No image files tracked anywhere in the dive directory (`git ls-files` clean of image extensions). No image committed into `website/src/`.
- The one rights-reserved item (Maude CC-BY-SA portrait) is correctly recorded with `localPath: ""` (not downloaded) and `licence: CC-BY-SA`.

### 11. nl2br rendering — PASS
All 17 `index.md` blockquote lines start with `> ` and are each a single source line (no wrapped continuation lines). Paragraphs are single-line (longest lines are intact paragraphs, not ragged wraps). No `<br>`-ragging risk.

---

## Findings, severity-ranked

### Must-fix
*(none)*

### Should-fix
1. **Unanchored Chekhov anecdote** — `index.md` line 45: "Chekhov … reported that Tolstoy had 'read sixty books on art'." Not in any extract or in the attributed commentary (the commentary's only Chekhov anecdote is unrelated — the Nosilov story). Source it, attribute it as a received anecdote, or drop it; the properly-anchored "seventy works" figure beside it already carries the point.
2. **`bans[].scope` is not a schema controlled value** — `dossier.yaml` `workRecord → bans[].scope` is a free-text sentence; the schema enum requires one of `complete-ban / passages-cut / serialization-refused / confiscation / pre-publication-rejected`. Use `passages-cut` and move the explanatory sentence to `bans[].notes`. (The dossier already flags this area as soft.)

### Nits
3. **ё/е mismatch in an inline-prose quotation** — `index.md` line 45 renders the cited phrase as "учёная и не захватывающая" (with **ё**), but the source (and the line-49 evidence blockquote) read "ученая" (with **е**). The blockquote/evidence is correct; only the inline prose paraphrase introduced the ё. Inexact rendering of a cited Russian phrase; outside the byte-fidelity gate but worth normalising to the source spelling.
4. **Quoted Russian term not verbatim-sourced** — `index.md` line 196 presents «вступительная часть» in quotation marks as if a verbatim term for the Maupassant preface, but that exact phrase appears in none of the five candidate extracts (Gudzy history, MS description, textological commentary, or the Maupassant preface). The commentary instead says the preface "близко соприкасалась с вопросами искусства" and that Tolstoy "не полностью высказал свой взгляд." The English gloss ("the treatise's true introductory part") is fine as characterization; recommend either dropping the Cyrillic quotation marks or replacing with a phrase that is actually in the source, so a quoted term is genuinely a quotation.
5. **"forty chapters to twenty"** is a reasonable synthesis of Gudzy's commentary (pagination "1—40"; "более чем на двадцать глав"), not a single verbatim statement — acceptable because it is attributed to the commentary, noted here only for transparency.

---

## Bottom line
The dive is faithful, well-attributed, and schema-aware. The two should-fix items are small and localised (one sentence to source/attribute; one enum value to correct), and neither touches the byte-faithful evidence layer or the dive's argument. No blocking issues.
