# Verifier report — On Shakespeare and the Drama (work-dive)

**Verdict: CLEAN-WITH-MINORS** — 0 blockers, 0 major, 4 minor.

Independent Phase-5 adversarial verification by a reader who wrote none of the dive.
Mechanical gate already passed (`verify_quotes.py` → 28/28 verbatim, exit 0); this report
re-checks the judgement-level things the script cannot. All ten requested checks were run.
The dive is sound, well-anchored, and honestly scoped — the four minor items below are
polish/consistency, none gate the commit.

---

## What passed (evidence)

**1. Byte-fidelity spot-check (belt-and-braces) — PASS.** Six evidence rows across four
extract files re-checked with fixed-string `rg -F`; all six appear verbatim:
- `diary-22sep-preface` → `_diaries_1903-1904.txt` ✓
- `letter-stasov-9oct` → `_letters_window.txt` ✓
- `essay-epidemic-suggestion` → `v35_216_272_O_Shekspire_i_o_drame.txt` ✓
- `var-infection-cut` → `v35_557_577_Varianty.txt` ✓
- `comm-start-13sep` → `_commentary_istoriya-pisaniya.txt` ✓
- `var-preface-original` → `v35_557_577_Varianty.txt` ✓
Evidence block = exactly 28 rows, each with one `quoteRu` → matches 28/28.

**2. Primary claims anchored — PASS.** Sampled ~10 corpus claims; every one traces to an
extract:
- Start ~13 Sept 1903 (OS) → Grossman verbatim ("она была начата 13 сентября"). ✓
- "Finished" 19 Dec 1903 + last add 18 Jan / last MS 19 Jan 1904 → both diary quotes present;
  "48 dated covers… 13 сентября 1903 г. по 19 января 1904 г." verbatim in `_commentary_opisanie-rukopisej.txt`. ✓
- "Outgrew Crosby" genesis → letter "которое переросло статью Crosby" verbatim. ✓
- 8-chapter structure / King Leir "better than Shakespeare's reworking" → essay text verbatim. ✓
- Epidemic-suggestion thesis (Crusades / witches / torture / tulip mania / press "like a snowball")
  → essay verbatim, full surrounding paragraph confirmed. ✓
- Goethe genealogy ("Слава эта началась в Германии", Goethe "диктатором… в вопросах эстетических",
  "как вороны на падаль", objective-art) → essay verbatim, Ch VIII. ✓
- 1,151 manuscript-unit fond → "1151 рукописных единиц" verbatim in Grossman. ✓
- The cut moves (Shakespeare-the-man portrait, infection/union mechanism, Koran/Krymsky analogy,
  Turgenev anecdote that "slips and writes Duncan") → all present verbatim in the variants extract,
  including the draft's actual "Дункан". ✓
- Later verdict, 30 Sept 1906 diary (Goethe/Turgenev/Faust) → verbatim in Grossman commentary. ✓

**3. Secondary claims attributed, not asserted — PASS.** Every reception/scholarship claim
carries a named source in the dive's voice (Orwell, Knight, Shaw, Bloom, Gibian, Wilson, Brown;
the 1906–07 publication facts to Grossman/PSS editor). The quoted English phrases — Orwell's
"do dirt on" / "kill his enjoyment", Wilson's "fifteen thousand words of nonsense", Bloom's
"could not handle the influence", Shaw's "bardolatry" — all trace to the dive's own
`extracts/_scholarship.md` working notes (good provenance; not invented). The Fortnightly Review
Dec 1906 claim is hedged ("is recorded for") and routed to `needsReview`, not asserted.

**4. Scholarship triangulation valid — PASS.** All 7 `triangulation[].evidenceRef` resolve to
real `evidence[].id`; all 7 `relation` values are in {confirms, complicates, contradicts, extends}.

**5. Marquee discipline — PASS.** The marquee section opens "Set up as a hypothesis to test
against the text, not a verdict to assert," tests confirms/extends, and adds a self-critical third
edge (the unfalsifiable sincerity verdict). Every claim ties to evidence (three-criteria row,
epidemic-suggestion row, cut draft № 24). Index and dossier agree on the answer ("confirms + extends").

**6. Entities & workRecord — PASS (with minor #1 below).**
- `vaultStatus` claims verified by directory listing: only `Vladimir Chertkov.md` exists in
  `website/src/wiki/`; "What Is Art?" `exists` is accurate (it is a *works* record,
  `website/src/works/non-fiction/essays-and-criticism/what-is-art/What Is Art?.md`); all other
  entities correctly `missing`. `website/src/works/non-fiction/essays-and-criticism/` holds exactly
  `bethink-yourselves` + `what-is-art`, NO `on-shakespeare-and-the-drama`. ✓
- All 26 workRecord field names cross-checked against `website/schema/tolstoy-works-schema.md` —
  every one is a real key. Object-array shapes correct: `titleAlternatives[]` uses {title,type,language}
  with valid `type` values (subtitle/translation/working); `relatedWorks[].relationshipType: sequel`
  is in the enum; `bans: []` legal. Enums valid: `genre: essay`, `completionStatus: complete`,
  `firstPublishedVenueType: newspaper`. ✓
- OS→NS arithmetic re-computed (+13 days, 20th c.): 1903-09-13→1903-09-26 ✓, 1904-01-19→1904-02-01 ✓,
  1906-11-12→1906-11-25 ✓. All three correct. ✓

**7. Coverage honesty — PASS.** Reception is marked `partial` and the note is honest: contemporary
1906–07 press is thin, the 1907 "Press against Shakespeare" section not recovered, both flagged to
`needsReview`. No surface is over-claimed as `covered`.

**8. Voice — PASS.** No editorialising in the dive's own voice; translations consistently labelled
"(working English)" (10×). The contested label "Tolstoyan" is cross-linked to the dedicated
`../tolstoyanism/` dive with an explicit "contested label" gloss (see minor #4).

**9. Boundaries — PASS.** `extracts/` holds only PD primary text (essay, variants, both Grossman
commentary files, diaries, letters, the Tom 40 Crosby memoir) + the dive's own generated working
notes (`_scholarship.md`, `_deepread.md`, marked "layer: secondary | generated"). No rights-reserved
third-party text. `visuals/` is git-ignored — `git check-ignore` returns exit 0 for the cached
images (rule `research/*/visuals/` in `docs/.gitignore`); no image is committed or placed under
`website/src/`. All 5 visuals carry a PD licence in the dossier (4 downloaded, 1 — the Funk & Wagnalls
title page — PD-but-not-downloaded with a fetch recipe). ✓

**10. Internal consistency — PASS (with minor #2 below).** Index ↔ dossier agree on the key dates,
the publication story (Russkoe Slovo first → Sytin 1907 → English editions bound with Crosby), and
the marquee answer.

---

## Issues

### MINOR

**Minor 1 — `wikiType: work` is not in the live wiki schema.**
`dossier.yaml:294` and `:374` route two entities ("On Shakespeare and the Drama", "What Is Art?")
as `wikiType: work`. The live `website/schema/wiki-schema.md` type table and the validator's
`WIKI_TYPES` (`website/.github/scripts/validate-frontmatter.mjs:34-37`) list 12 types and do **not**
include `work`. This is the dive's internal routing label (works go to `works/` records, not `wiki/`
pages — and indeed this entity's real home is the `workRecord` block, which is correct), and the
verifier brief + project memory both note `work` as an accepted dive convention ("Lab-only 13th wiki
type"). So this is not a fabrication and the routing is right — but a reader cross-checking against
the wiki schema will trip on it.
*Fix:* add a one-clause note on the two `work` entities, e.g.
`# routing label only — 'work' is not a wiki/ type; real home is the workRecord block`, or set
`vaultStatus`/a comment making explicit these route to `works/`, not `wiki/`.

**Minor 2 — index ↔ dossier disagree on which drafts are characterised.**
`index.md:217` (and `:139`) say key drafts "№ 1, 6, 8, 11, 12" are characterised; `dossier.yaml:712`
(`notCovered`) says "№ 1, 6, 8". The index figure is the correct/fuller one — manuscript units
рук. № 11 and № 12 are genuinely used in evidence rows (`var-awl-objectivity` = рук. № 11,
`var-infection-cut`/`var-hamlet-nochar` reference рук. № 11/12). The dossier line is stale.
*Fix:* update `dossier.yaml:712` to "№ 1, 6, 8, 11, 12" to match the index.

**Minor 3 — the "25 September (a date on draft № 6)" date is not anchored in the committed extracts.**
`index.md:149` states: "By **25 September** (a date on draft № 6) the argument's spine was already a
numbered list of eleven 'defects'…". The numbered defect list itself IS in the variants extract
(verified: "2) Запутанность завязки", "6) …напыщенным… языком", anachronism/indecency/immorality all
present), so the *substance* is sound. But the specific date assignment "25 September → draft № 6" does
not appear in any extract file (`rg "25 сент"` and `rg "№ 6"` across `extracts/` return nothing). It
likely comes from Grossman's manuscript-by-manuscript listing that wasn't fully pulled into the
committed extracts.
*Fix:* either add the supporting line to a commentary extract, soften to "an early draft" /
"a late-September draft", or tag the precise date `needsReview`.

**Minor 4 — "American Tolstoyan" used unqualified before the contestation is flagged.**
`index.md:24`, `:72`, `:110` call Crosby "American Tolstoyan" plainly; the "contested label" gloss
and cross-link to `../tolstoyanism/` only arrives at `:203`. The label is ultimately handled correctly
(attributed + cross-linked once), so this is the lightest of touches.
*Fix (optional):* on first use (`:24` or `:72`) link or qualify "[Tolstoyan](../tolstoyanism/index.html)"
so the contestation travels with the first occurrence.

---

## Bottom line
No blocker, no major. Byte-fidelity holds beyond the 28/28 gate; every sampled primary claim is
anchored; secondary claims are attributed with real (not fabricated) quotes; schema fields, enums,
object shapes and OS/NS arithmetic are all correct; vault/works directory claims are accurate;
boundaries and git-ignore are clean; the marquee is a genuine tested hypothesis. The four minor items
are consistency/polish and safe to fix at ingestion or in a quick pass. **CLEAN-WITH-MINORS.**
