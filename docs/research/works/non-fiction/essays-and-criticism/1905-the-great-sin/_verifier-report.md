# Verifier report — *The Great Sin* (Великий грех, 1905) corpus-dive

**Verdict: NEEDS-FIXES → RESOLVED 2026-06-21** (all three fixes applied: findings 1 & 2 — the genesis paragraph re-ordered so the 17 April letter follows 16 April, and the Key-findings "same day"→"day before (20 April)" peasant-reproach date; finding 3 — `firstPublishedVenueType` `magazine`→`journal`. Re-validated: YAML OK, verify_quotes 27/27 PASS, HTML rebuilt. Dive is now CLEAN.)

Original verdict: **NEEDS-FIXES** (two factual chronology errors in the narrative + one invalid schema enum value). Everything else is clean: byte-fidelity holds 27/27 plus a 6-quote cross-genre spot-check, the marquee claim is strongly grounded in the PSS commentary, secondary claims are attributed, entities/relations/triangulation are honest, and file hygiene is correct. The fixes are small and surgical; none touches the dive's argument or its evidence base.

Checked cold, separate pass. `verify_quotes.py` re-run: **27/27 verbatim, 0 label warnings, PASS**.

---

## Findings

### 1. [blocker] index.md:72 — "The next day, 17 April" is a chronology error (the letter predates the 21 April it follows)

`index.md` line 72 reads: *"The next day, **17 April**, Tolstoy confirmed the project to Chertkov…"* — but it sits immediately after the **21 April** paragraph (lines 68–70). 17 April is not "the next day" after 21 April; it is **four days before**. The letter (E24, dated `1905-04-17`) actually follows the **16 April** diary entry (E21) by one day. The dossier evidence dates are all correct — this is purely a narrative sequencing slip in the prose.

The whole genesis paragraph is mis-ordered: it runs 16 Apr (line 66) → 21 Apr (lines 68–70) → 17 Apr (line 72), so the 17 Apr letter is stranded out of sequence and mislabelled "the next day."

**Fix:** re-order so the 17 April letter follows the 16 April diary entry (its true place — "the next day" is then correct relative to 16 April), then move to 21 April for the composition-start + peasant reproach. Or, if the current paragraph order is kept for rhetorical reasons, change "The next day, 17 April" to something like "The day after the first diary note — **17 April** — Tolstoy confirmed the project to Chertkov" and place it before the 21 April material. Do not leave "the next day" attached to a date earlier than the paragraph it follows.

### 2. [blocker] index.md:22 vs index.md:70 — the peasant reproach is dated inconsistently ("same day" vs "the day before")

- Line 22 (Key findings): *"**The same day** he began the essay, a peasant reproached him…"*
- Line 70 (Genesis): *"…had reproached Tolstoy **the day before**…"* (i.e. 20 April, the essay begun 21 April).

These contradict each other. The dossier settles it: E23's significance and the Buturlin entity (dossier line 325) both place the reproach on **20 April 1905 — the day before** composition began (the 21 April diary entry *records* the previous day's encounter). Line 70 is right; line 22 is wrong.

**Fix:** change line 22 to "The day before he began the essay, a peasant reproached him…" (or "On the eve of beginning the essay…"). This also keeps it consistent with the dossier and the diary's own retrospective phrasing.

### 3. [minor] dossier.yaml:580–582 — `firstPublishedVenueType: "magazine"` is not a valid enum value (will fail the validator)

The proposed `workRecord` field `firstPublishedVenueType` is set to `magazine` (dossier line 581). The live works schema (`website/schema/tolstoy-works-schema.md` line 103) and the validator (`website/.github/scripts/validate-frontmatter.mjs`, `VENUE_TYPES = ["journal", "newspaper", "book", "samizdat"]`) **do not include "magazine."** Applied as-is this would fail `validate-frontmatter.mjs`.

The dossier note already hedges ("Use the enum's nearest value — magazine or journal; verify against the live venueType enum") and `confidence: medium`, so this was flagged — but the headline `value:` proposes the wrong token. Русская мысль was a "thick journal" (literary-political monthly), so the correct value is **`journal`**.

**Fix:** change the proposed `value` to `journal`. (The needsReview item at dossier:664 can then be marked resolved.) Same applies if a `firstPublishedInRussiaVenueType` is added on application — use `journal`.

### 4. [nit] index.md:163 — "«Свободное слово» (No. 98)" is correct; flagging only to confirm it was checked

The commentary (commentary extract line 109) confirms **No. 98** for the main essay («Великий грех», subtitle «О земельной собственности»), and No. **17–18** for the *separate* withdrawn-introduction printing («Необходимый переворот», commentary line 117). index.md cites No. 98 for the essay (line 163) and does not misattach 17–18. No error — recorded so the next reader doesn't re-flag the two numbers as a conflict. No fix needed.

### 5. [nit] dossier.yaml:606–608 — transcriber list is grounded, but Igumnova's patronymic varies in the source

The `transcriptions[]` proposal lists Igumnova, Schmidt, A. L. Tolstaya, Makovitsky, M. L. Obolenskaya — all confirmed as copyists in the commentary (mss. №3/4/5; Obolenskaya copied the sent text, commentary lines 7/19/37/79). Grounded. One detail: the commentary spells Igumnova's initials inconsistently — **«Ю. И. Игумнова»** (line 19/79) and **«Ю. К. Игумновой»** (line 37). The dossier uses "Yulia Ivanovna" (Ю. И.). That is the more frequent form in the apparatus and is almost certainly correct (Yulia Ivanovna Igumnova is the known secretary); the «Ю. К.» is likely an OCR/source typo. No fix required, but worth a one-line note if the record is applied, so an editor doesn't "correct" it the wrong way.

---

## Checks that passed (evidence)

| Check | Result | Evidence |
|---|---|---|
| Mechanical quote gate | PASS | `verify_quotes.py` → 27/27 verbatim, 0 label warnings |
| Byte-fidelity spot-check (6 quotes, all genres) | PASS | E12 (work), E15 (variant), E18+E19 (commentary), E23 (diary), E24 (letter) — each `grep`-confirmed verbatim in its named extract |
| `(working English)` labelling | PASS | every `quoteEn` in the ledger carries "(working English)"; index.md stages and inline glosses all carry "— working English" |
| **Marquee claim grounded** | PASS | The "Chertkov cut the anarchist sentence *because it contradicted* the reform argument" claim is directly supported: commentary line 119 states Chertkov motivated the excision because the paragraph «стоит в противоречии со всем предыдущим, где утверждается необходимость внешнего изменения форм пользования землей.» The separate printing as «Необходимый переворот» is confirmed at commentary line 117. Not overstated. |
| Marquee relation honest | PASS | triangulation E12 = `complicates`, E15 = `extends` (not `confirms`); only E3 (lifelong Georgism) = `confirms`, correctly |
| "Published legally in Russia in lifetime" | PASS | commentary line 109: appeared in the July 1905 Русская мысль + Posrednik brochure, in lifetime; `publishedInRussiaDuringLifetime: true` is defensible. The 1911 collected-edition confiscation is correctly kept separate (censorshipNotes). |
| Secondary claims attributed | PASS | Wenzer 1997, Lebrun 1956, the "A Great Iniquity" translator's footnote, the Русская мысль disclaimer, Henry George biographical facts (Britannica + Wikipedia), Bartlett/Wilson/Maude — all attributed inline AND in References; none asserted in the dive's own voice |
| triangulation evidenceRefs valid | PASS | E12, E15, E20, E3, E13 all exist in the ledger; all `relation` values are in the legal enum |
| Entities → valid wiki types | PASS | person / concept / work only used; all in the v1.4 `WIKI_TYPES` enum |
| vaultStatus accuracy | PASS | Chertkov `exists` (`website/src/wiki/Vladimir Chertkov.md` present); Maria Tolstaya `exists` (page present, and it genuinely carries the daughter-vs-sister concern the dossier flags — the page is "Maria Lvovna … Obolenskaya," matching the copyist, so the disambiguation caveat is honest and correctly routed to needsReview); George/Nikolaev/Mazzini/Makovitsky/Buturlin correctly `missing` (no vault pages on loose match) |
| workRecord field names match live schema | PASS (one exception, finding 3) | genre `essay`, subcategory `Essays and Criticism`, mainCategory `Non-Fiction`, the `...OldStyle`/`...Approximate` companions, manuscripts/transcriptions/authoringLocations shapes all match `tolstoy-works-schema.md` v9 and the Bethink Yourselves reference record — except `firstPublishedVenueType: magazine` (finding 3) |
| Old-Style date handling | PASS | dates carry `oldStyle` + `approximate`; `dateWritingStarted 1905-04-21` flagged Old Style (Russia on Julian); the dossier does not silently convert to NS, consistent with the diary source |
| coverage honesty | PASS | Reception & afterlife = `partial` (named Russian critical replies not found — honest, corroborated by the commentary carrying only the editors' disclaimer); author's-later-verdict = `partial`; characters & prototypes = `not-covered` (non-fiction). No surface over-claimed as `covered`. |
| Bare voice / no editorializing | PASS | no contested labels ("Tolstoyan"/"heretic") asserted in the dive's own voice; the Georgist-movement reading is explicitly tagged "movement-aligned reading by interested parties" (index.md:119) and read critically per dive method; the verdict is "complicates, not contradicts," which the evidence supports |
| File hygiene — extracts | PASS | `extracts/` holds only `.txt` verbatim + the `_scholarship` notes; no images/binaries |
| File hygiene — visuals git-ignored | PASS | `docs/.gitignore` line 22 `research/*/visuals/`; `git check-ignore` confirms the cache is ignored; `git ls-files` on the visuals dir returns empty (nothing committed) |
| No rights-reserved image in website/src | PASS | `git ls-files website/src/` has no Great-Sin/Henry-George images; all 8 visuals are PD and live only in the ignored cache |
| Draft note | PASS | `website/src/posts/notes/2026-06-21-the-great-sin.md` exists with `draft: true` (line 6); content is accurate and plain-voiced |

---

## Summary

The dive is evidentially solid and the marquee — the hardest claim to make responsibly — is the *best-supported* part of it: the PSS commentary states in Chertkov's own motivation that the anarchist paragraph "stands in contradiction" with the rest, exactly as the dive says, so "managed by scissors, not resolved by argument" is earned, not rhetorical. The three things to fix before this is clean are mundane: two date-sequencing slips in the prose (findings 1 and 2) and one wrong enum token in the proposed record (finding 3). Findings 4 and 5 are recorded for the next reader and need no action.

Recommendation: **REQUEST_CHANGES** — fix findings 1–3 (all small), then the dive is CLEAN.
