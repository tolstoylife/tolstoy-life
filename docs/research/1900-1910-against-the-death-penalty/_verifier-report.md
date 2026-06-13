# Verifier report — "Against the death penalty" (1900–1910) corpus theme-dive

**Verifier:** independent adversarial pass (did not write the dive)
**Date:** 2026-06-13
**Scope:** judgement-level checks beyond the mechanical byte-fidelity gate (verify_quotes.py already PASSES 30/30, 1 facsimile OK).
**Verdict:** CLEAN-WITH-MINORS — 0 blockers, 1 should-fix, 3 nits.

---

## Blockers

None.

---

## Should-fix

1. **Stolypin-article date slip in the Key findings (index.md line 21).** The first
   "named provocations" bullet places A. A. Stolypin's *Novoe Vremya* article "**in 1909**":
   > "…and, in 1909, an article in *Novoe Vremya* by A. A. Stolypin — brother of the
   > Prime Minister — that defended the gallows with the Gospel."

   The article was published **18 December 1908**; Tolstoy's reply («Смертная казнь и
   христианство») was January 1909. The dive's own body text has it right (line 109:
   "an article in *Novoe Vremya* (18 Dec 1908)"), and the dossier carries **18 Dec 1908**
   consistently in five places (lines 297, 605, 845, 1024, and the triangulation at 845).
   So the index summary contradicts the dive's own dossier and body. It is a prominent,
   factually-wrong date in a key-findings bullet. Fix: change "in 1909" to "in late 1908"
   (or "in December 1908"), or reword to "an 18 Dec 1908 article … which Tolstoy answered
   in 1909." Low effort, high visibility.

---

## Nits

1. **"examining magistrate" abbreviation drift (cosmetic).** The 1907 framing quote's
   working English in index.md (line 93) renders the magistrate as "**an** examining
   magistrate," while the dossier quoteEn (id `nikogo-felten-framing`, line 224) and the
   Russian both specify "a **St Petersburg** examining magistrate" («Петербургским
   судебным следователем»). Both are byte-faithful to the *Russian* (the Russian is
   verbatim in the extract — confirmed); only the English gloss is shortened in the index.
   Not a fidelity issue; harmonise if convenient.

2. **"death penalty was a newcomer to Russian law" stated in the dive's own voice
   (index.md line 18), but adequately hedged.** The Key findings bullet asserts the
   legal-history substance ("Empress Elizabeth's de-facto moratorium (from 1744) was real
   and, by one account, unique in Europe; the ordinary 19th-century criminal code carried
   no death penalty for common crimes") before the Scholarly-context section attributes it
   (Marasinova 2018; TASS; Wikipedia, line 201). The bullet does include the
   "by one account" qualifier and the body flags that Tolstoy "overstates the case for the
   military and political-crime provisions," so this is within tolerance — but a reader of
   the Key findings alone meets the historical claim before its attribution. Optional:
   add a four-word "(scholarship confirms the substance)" cross-pointer in the bullet, as
   the dive in fact does at line 18 ("Scholarship confirms the substance"). On re-read this
   is already present — recording as a non-issue / monitor-only.

3. **`firstPublishedVenueType: samizdat` for the three Свободное слово works** is a
   known enum gap (the schema offers only journal/newspaper/book/samizdat, no "émigré
   press"). This is *correctly* surfaced in `needsReview` (dossier line 1083) and the
   workRecord `source`/`confidence: low` notes, so it is honestly flagged, not hidden.
   No action needed beyond the existing flag; recorded here for completeness.

---

## Checks performed and passed

**1 — Byte-fidelity spot-check (belt-and-braces).** Re-verified 10 quoteRu rows across
all six works + the diaries against their named extracts with literal `grep -F`
(no normalisation): `neubij-hypocrisy` (v34_200_205), `tsarju-death-penalty-unrussian`
(v34_239_244), `sredstvo-all-rests-on-killing` (v34_254_269),
`nikogo-execute-me` (v37_039_054), `smertkazn-shame` + `smertkazn-stn-blasphemy` +
`smertkazn-cannot-be-silent` (v38_039_048), `tridnja-chain-to-gallows` (v38_019_022),
`gen-neubij-dispatch` (v54_032_033), `gen-smertkazn-provoke` (v57_013_014). **All 10
verbatim.** Both committed facsimiles exist (`v34_200_Ne_ubij_opening_facsimile.png`
220 KB, `v38_039_Smertnaja_kazn_opening_facsimile.png` 282 KB).

**2 — Claim anchoring.** Primary factual claims trace to evidence rows / extracts / PSS
commentary. Dates, venues, the Gorlovka numbers (131/92/32/24/8, attributed to
Wikipedia RU + Sergeenko PSS т.38), the Kropotkin execution tally (attributed), and the
death-penalty-history claim (attributed Marasinova/TASS/Wikipedia) are all sourced. The
single-source reception detail (the 1 Jan 1909 «Даровать жизнь» imperial resolution) is
explicitly flagged as resting on the PSS commentary alone in both the index ("Material
not covered") and `needsReview`.

**3 — Attribution of scholarship.** The "Scholarly context" section attributes every
secondary claim (Bartlett 2010; Maude 1911; Marasinova 2018; Kropotkin 1909; Find a
Grave; Wikipedia titles) with explicit *(Attributed: …)* tags. Mainstream framing is
positioned as contrast-to-read-critically, not baseline. No secondary claim asserted as
bare fact.

**4 — Translations.** All 10 Russian blockquotes carry a working-English label. (My first
grep undercounted 9/10; the missing one is line 113, labelled
`*(working English, quoting Stolypin)*` — a *more precise* variant, correctly flagging it
as Tolstoy quoting Stolypin. Not a finding.)

**5 — Dossier structure.** `scholarship.triangulation` — all 11 `evidenceRef` ids resolve
to defined evidence rows; all `relation` values valid (confirms ×2, complicates ×2,
extends ×7; no contradicts, which is fine). `entities` — all `wikiType` values valid per
wiki-schema v1.4 (concept ×2, edition, event, institution, person ×9). vaultStatus
spot-checked: **Vladimir Chertkov** `exists` ✓ (`Vladimir Chertkov.md`), **Pavel Birukov**
`exists` ✓ (vault file is `Pavel Birukoff.md` — the transliteration is correctly noted in
the entity role). All entities marked `missing` (Umberto, Nicholas II, A. A. Stolypin,
Felten, Gusev, Boulanger, Ladyzhnikov, Free Age Press, Obnovlenie, the Gorlovka event,
the two concepts) genuinely absent from the 14-file vault on loose match.

**6 — WorkRecords (the six proposals).** All six carry `create: true`. Field names match
the works-schema v9. List-typed fields are object arrays: `titleAlternatives`
(types working ×11 / subtitle ×3 — both valid), `bans` (scope: confiscation ×3 /
passages-cut ×1 — both valid v9 enum values; authorityType: imperial-state ×4 — valid),
`relatedWorks` (relationshipType: companion ×7 / sequel ×2 — both valid). genre `essay`
×6 valid. firstPublishedVenueType journal/newspaper/samizdat — all in-enum (samizdat is
the flagged émigré-press compromise). No fabricated dates/venues found; OS↔NS conversions
flagged as partly-approximate in needsReview. The Three-Days shelving (Non-Fiction vs
Fiction/Sketches) and genre ("essay" for очерки) ambiguities are honestly surfaced in
needsReview.

**7 — Coverage honesty.** Ledger is honest. One surface is `partial` (Reception &
afterlife — correctly, since lifetime reception *was* the censorship and discrete critical
reception is thin). The rest marked `covered` are genuinely covered (all eight extracts
read in full; six genesis diary rows; full field sets on six workRecords). No `covered`
masking a `partial`.

**8 — Voice.** Plain and factual. No advocacy adjectives (scanned for
brilliant/powerful/moving/courageous/heroic/profound/etc. — zero hits), no "Tolstoy was
right" value judgments. Contested labels (Tolstoyan, Christian anarchism) explicitly
attributed to the mainstream and pointed-at, not adopted (disclaimer at line 197 + the
"Place in the cluster" note at line 226).

**9 — Boundaries.** `git check-ignore` confirms `visuals/*` (commons-umberto-i-1904.png),
`index.html`, and the extract `.html` files are all git-ignored. The dive dir is currently
**entirely untracked** (`?? docs/research/1900-1910-against-the-death-penalty/`) — nothing
committed yet — so no rights-reserved image is staged; when added, the .gitignore rules
will keep only PD material (Tolstoy text extracts, the two PD facsimiles, the .md/.yaml,
and the research-note .md files) in the tree. The four Commons images (all PD per the
dossier `licence: PD`) sit only in the ignored `visuals/`. Boundary conditions met.

**10 — Internal consistency.** «Не убий никого» is dated **1907** consistently throughout
index.md (never 1908); the contradiction note (dossier line 1069) correctly identifies the
PSS т.37 commentary typo «продолжалась до 5 августа 1908 г.» (verified verbatim in
`v37_414_416_..._Istorija.txt` line 7) against the work-text dateline «5 августа 1907 г.»
(verified in `v37_039_054...txt` line 155) — the 1907 correction is sound. The "execute me
too" 1907-before-1908 claim is internally consistent (key findings, threads,
place-in-cluster). The A. A. Stolypin = PM's-brother claim appears 3× in index, all
consistent and attributed. **The one inconsistency found is the should-fix above:** the
Stolypin-article date in the Key findings (line 21, "in 1909") contradicts the dossier and
body (18 Dec 1908).

---

## Overall verdict

This is a sound, well-anchored multi-work theme-dive. Byte-fidelity holds on a 10-row
re-spot-check across all six works and the genesis diaries; both PD facsimiles are present;
the six record-creating workRecords are schema-conformant (v9 field names, object-array
list fields, valid bans/authorityType/relationshipType/genre/venueType enums, `create:
true` throughout) with their genuine edge cases (samizdat venue-type, Three-Days shelving,
OS↔NS approximations, the single-source imperial-resolution date) honestly surfaced in
`needsReview` rather than buried. Scholarship is attributed, not asserted; the voice is
plain and the contested labels are pointed-at, not adopted; the coverage ledger is honest;
and the git boundaries (visuals/ and .html ignored, only PD material trackable) are
correctly configured. The contradiction note's "1907-not-1908" correction is verified
against both the commentary typo and the work-text dateline. The single substantive defect
is one prominent dating slip — the Stolypin article placed "in 1909" in the Key findings
where the dive's own dossier and body correctly read 18 December 1908. That is a should-fix,
not a blocker. Everything else is cosmetic. **CLEAN-WITH-MINORS.**
