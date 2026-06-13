# Verifier report — "The break with the Church — Tolstoy, the Holy Synod, and the 1901 excommunication"

**Role:** separate-pass, adversarial verifier (did not author the dive).
**Date:** 2026-06-13
**Mechanical gate:** verify_quotes.py 35/35 verbatim, exit 0 — already PASSED upstream; NOT re-run here.
**Scope:** the judgement-level checks the script cannot make.

---

## Check 1 — Spot-check byte-fidelity (belt-and-braces) — PASS

Picked five rows across all four genres and confirmed each `quoteRu` appears verbatim in its named extract `.txt` (grep, exact substring):

| Ref | Genre | Extract | quoteRu probe | Found |
|---|---|---|---|---|
| E01 | work (Reply / edict text) | v34_245_253_Otvet…pisma.txt | «явно перед всеми отрекся от вскормившей и воспитавшей его матери» | 1 ✓ |
| E10 | diary (19 Mar 1901) | diary_v54_090_093_1901_03_19.txt | «странное отлучение от церкви и вызванные им выражения сочувствия» | 1 ✓ |
| E17 | letter (Nicholas II) | letter_v73_204_NikolayuII.txt | «пишу Вам как бы с того света, находясь в ожидании близкой смерти» | 1 ✓ |
| E08 | apparatus/commentary | v34_575_577_Otvet…fev.txt | «составленное Победоносцевым» | 1 ✓ |
| E21 | apparatus/commentary | v39_225_228_Religija…pisani.txt | «Противоречия эмпирической нравственности» | 1 ✓ |
| E34 | work (children's gospel) | v37_097_147_Uchenie…detej.txt | «дух божий живет в каждом человеке» | 3 ✓ |

Every `quoteEn` in the dossier carries the `(working English)` label (confirmed across the E-series; the label is also carried through into index.md's block quotes). PASS.

## Check 2 — Claim anchoring — PASS

Every primary factual claim in the dive's own voice traces to an E-ref or the apparatus. Spot audit of the load-bearing claims:
- "diary records the excommunication only on 19 March 1901" → E10.
- "the church is a worldly institution … set down in 1893" → E19, E25.
- the double-programme year-end line → E16.
- the credo / bird-eggshell / renunciation-inverted hinges → E04, E06, E03.
- the death-threat edge → E05.
- foreign-first / Russian-cut publication pattern → E09, E21.
- workRecord dates → all carry OldStyle companions (11/11; correct +12 for 1893/1896, +13 for 1900+) and a `source` field (PSS page or diary). No fabricated bare dates.

Reception claims that are not corpus-anchored are attributed to a named secondary source (see Check 3/8), not floated as the dive's own primary findings. No unanchored primary claim found. PASS.

## Check 3 — Attribution of secondary/scholarly claims — PASS

Scholarship is attributed, not asserted in the dive's voice. The contested Pobedonostsev-authorship point is handled correctly and presented BOTH ways, attributed, asserting neither:
- Key-findings bullet (l.20): "The PSS apparatus (Soviet, 1952) credits Pobedonostsev with drafting it (E08); … Kolstø's *Heretical Orthodoxy* (2022) reverses this from the archives … The dive presents both, attributed."
- Scholarly-context para (l.149): explicitly frames it as "contradicts, and the contradiction is internal to the sources … The dive carries both and asserts neither … the question of who drafted the 1901 text is open between the apparatus and the archive."
- Other scholarship is named: "Medzhibovskaya (2008) reads…", "Maude (1910, ch. 16) and Bartlett (2010) supply the reception narrative…", "Kolstø (2022) calls the document…".

No byte-fidelity demanded on secondaries; each secondary claim has a named source. PASS.

## Check 4 — Loaded labels — PASS

- "heretic": 3 occurrences, all attributed/distanced — "popular memory of 1901 is of a heretic cast out" (framing it as the popular misreading the dive then corrects), John of Kronstadt "denounced Tolstoy as a heretic", and l.151 "the press of 1901 called … Tolstoy a heretic; both labels belong to the Synod and the newspapers, not to this dive's voice."
- "Tolstoyan"/«толстовство»: l.151, explicitly assigned to the press and noted as disowned by Tolstoy in 1897.
- "apostate": not used.
- "anathema"/«анафема»: used only to draw the отлучение-vs-anathema distinction, never adopted as a description of the act. The distinction is made up front (l.13: «отлучение» = separation, not the liturgical «анафема»; "excommunication" retained with that qualification) and reinforced at l.137 ("it was not a formal anathema") and l.149.

The отлучение-vs-anathema distinction is made clearly and repeatedly. PASS.

## Check 5 — Scholarship triangulation — PASS

Six triangulation entries; every `evidenceRef` (E03, E02, E08, E04, E25, E05) is a valid E-series id; every `relation` is in the enum (extends ×3, complicates ×1, contradicts ×2). Honesty of assignment:
- E08 → contradicts: genuine — Kolstø reverses the PSS apparatus on authorship. Correct.
- E04 → contradicts: genuine — Tolstoy affirms faith against the "God-denying" framing. Correct.
- E02 → complicates: correct — anathema framing complicated, not flatly contradicted (it WAS an exclusion, just not an anathema).
- E03, E25 → extends: genuine — the corpus dates/clusters what biographies state thematically; not mere "confirms."
- E05 → extends: defensible. The pastoral-measure framing vs the documented backfire could arguably be "complicates," but "extends" is honest (it adds the backfire/incitement dimension rather than negating the Church's stated intent). Not a mislabel.

No "extends"/"contradicts" found that is really a "confirms." PASS.

## Check 6 — Entities — PASS

14 entities. All `wikiType` values valid against wiki-schema (12 types): person ×11, institution ×2, event ×1. No invalid type.

vaultStatus vs the supplied ground truth (only Chertkov, Sophia, Birukoff exist among people; all others missing): the two `exists` entries are exactly **Vladimir Chertkov** and **Sophia Tolstaya**. Birukoff is not a cast member of this dive (he appears only in the textual-history note about the 1898/1893 dating error, not as an entity), so "3 exist" ground truth correctly resolves to the 2 present. Every other person/institution/event is `missing` — matching ground truth (Pobedonostsev, Antony Vadkovsky, Maude, Nicholas II, Nikolai Mikhailovich, Stakhovich, Gizycki, John of Kronstadt, Verigin, the Synod, «Свободное слово»). No `stub` misapplied; no vaultStatus disagrees. PASS.

## Check 7 — WorkRecords — PASS

(a) **Field names:** all are real works-schema keys — titleEn/Ru, titleAlternatives, mainCategory, subcategory, genre, language, completionStatus, the date/venue fields, firstPublishedVenueType, publishedDuringLifetime, publishedInRussiaDuringLifetime, excommunicationRelated, censoredVersionExists, bans, authoringLocations, relatedWorks, identifiers.jubileeEdition.volumes. No invented field. (The only non-key is `NOTE` — see (e).)

(b) **Controlled vocab:** genre = essay ×5, religious ×1 (both in enum); mainCategory = Non-Fiction (valid); subcategory = "Essays and Criticism" / "Educational" (both valid under Non-Fiction); bans[].scope = complete-ban, confiscation (both valid); bans[].authorityType = holy-synod, imperial-state (both valid); titleAlternatives.type = translation, variant (both valid); relatedWorks.relationshipType = companion (valid).

(c) **Dates/venues/bans anchored:** all 11 dateWriting* values carry OldStyle companions with correct offsets; every field carries a `source` (PSS page / diary) or evidenceRef. Bans cite PSS pages and E09/E21. No fabricated date/venue.

(d) **Restoration of Hell = RECONCILE:** `create: false`, workId `destruction-of-hell-and-its-restoration`, recordPath identical to the 1903-folk-tales dive's record (which owns it at `create: true`). Confirmed not a duplicate creation; this dive folds in only excommunicationRelated, the To-the-Clergy companion tie, and the Tchertkoff English-title alt.

(e) **The "NOTE" pseudo-field:** reads unambiguously as a deliberate annotation — its value opens "RECONCILE — NOT a new proposal…" and instructs the ingestor not to create a second record. Clearly not presented as a schema field.

Genre/subcategory uncertainties are NOT asserted high-confidence: the children's-gospel subcategory is `confidence: low` + needsReview; the five articles' genre is `confidence: medium` with `alt:` notes + needsReview; Religion and Morality subcategory `confidence: low`. Correctly hedged. PASS.

## Check 8 — Coverage honesty — PASS

- Reception marked "covered" but the Sofia/Antony exchange is honestly flagged "secondary only" in the coverage note AND inline in index.md (l.141, "the substance here is secondary") AND in needsReview/notCovered (Sofia's letter text paywalled/not digitised).
- The edict-authorship contradiction IS surfaced: in the Scholarly-context coverage note ("the Pobedonostsev-attribution reversal (contradicts the PSS apparatus)"), in the contradictions block, and in needsReview.
- Two surfaces honestly downgraded to `partial`: "Redactions & textual history" (variants not collated) and "The author's later verdict" (no separate late re-assessment). The student-march venue ambiguity (St Petersburg vs Moscow) is flagged inline and in needsReview.

No surface marked "covered" that the evidence shows is really partial. PASS.

## Check 9 — Voice — PASS (with one minor)

Register is plain and factual; no hagiographic editorializing. The "soft Tolstoy" trap is actively avoided — the calm late register (E10 «странное», E15 flour-with-lime) is read as worked-out detachment and a sharpened diagnosis, NOT as retreat or mellowing; "Why this matters" frames the constructive core without softening the anticlerical edge (church as «прививка ложного христианства» / «мирское учреждение … враждебное» carried at full strength). Working-English translations consistently labelled.

MINOR (voice/precision): l.26 and elsewhere use "the man the Synod declared God-denying" — fine as attributed framing, but the phrase "recovers a constructive core" (l.26) leans mildly interpretive/advocative. It is anchored (E16, E34, E35) and stays on the right side of the voice rule, but it is the one sentence closest to the line. Not a failure.

## Check 10 — Boundaries — PASS

- `extracts/` holds only `.txt` (111 primary extracts) + the working `_*.md` sweeps (5) + their rendered `_*.html` (5). No binary/image file staged under `extracts/` (find returned nothing; extension census = {.txt, .md, .html} only).
- `visuals/` holds 13 cached PD `.jpg` files and is git-ignored via `docs/.gitignore:18` (`research/*/visuals/`), confirmed by `git check-ignore -v`.
- No image committed under `website/` for this dive (git status shows only the normal `? website` submodule pointer).
- index.md `<img>` tags point at `visuals/…` (the git-ignored cache), consistent with the documented repopulate-on-clone model.

PASS.

---

## Minor concerns (non-blocking)

1. **«Свободное слово» entity naming (entities block).** `name: "«Свободное слово» (Free Word / Free Age Press)"` with `wikilinkTarget: "Svobodnoe Slovo"`; the `role` note conflates then disambiguates ("Distinct from the English-language Free Age Press partner"). The parenthetical "Free Age Press" in the display name risks the very conflation the note warns against — at ingestion, prefer the bare «Свободное слово» / Svobodnoe Slovo and keep Free Age Press out of the title. Cosmetic; flagged for the ingestion step, already half-caught by the role note.

2. **Voice — "recovers a constructive core" (l.26).** The one phrase closest to advocative register; anchored and acceptable, noted only for awareness.

3. **E05 → "extends" relation.** Defensible but the closest call in the triangulation; "complicates" would also be honest. Not a mislabel.

None of these affects byte-fidelity, anchoring, attribution, vocab validity, or the reconcile.

---

## Overall verdict

**CLEAN-WITH-MINORS** — 0 FAIL, 3 CONCERN (all cosmetic/ingestion-time, listed above). All ten judgement-level checks PASS. The contested Pobedonostsev-authorship point is correctly double-attributed and left open; loaded labels are all distanced to the Synod/press/scholarship; the отлучение-vs-anathema distinction is made; workRecord fields and controlled vocab are valid; the Restoration of Hell record is a correct reconcile, not a duplicate; and the boundaries hold (no media under extracts/, none under website/).
