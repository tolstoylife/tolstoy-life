# Verifier report — The Power of Darkness (Власть тьмы, 1886) novel-dive

**Role:** independent adversarial verifier (did not author the dive).
**Date:** 2026-06-10.
**Verdict:** CLEAN-WITH-MINORS — 0 BLOCKING, 6 MINOR.

Files reviewed: `index.md`, `dossier.yaml`, `extracts/*.txt`, the works/wiki schemas, and the
existing record `website/src/works/plays/drama/the-power-of-darkness/The Power of Darkness.md`.
`git` was not run (per instructions); the visuals-cache ignore status was confirmed from
`docs/.gitignore` directly, not via git.

---

## Check 1 — Byte-fidelity spot-check — PASS

Re-ran `verify_quotes.py docs/research/1886-the-power-of-darkness/dossier.yaml` independently:
**34/34 quotes verbatim, 0 facsimile missing, 0 label warnings — PASS.**

Three quotes independently re-derived by grepping the *named* extract file (not relying on the checker):

1. **`vt-kogotok`** (Act-5 proverb) → `extracts/v26_123_243_Vlast_tmy.txt`. Full `quoteRu`
   («…говорил ты мне: «коготок увяз и всей птичке пропасть», не послушал я, пес, твоего слова,
   и вышло по-твоему.») present verbatim as a single continuous string. Note: the prose *gloss*
   elsewhere renders the proverb with a comma (коготок увяз, всей птичке пропасть) but the
   load-bearing verbatim `quoteRu` uses «и», which is exactly what the extract contains. Genuine, not a fragment.
2. **`vt-ne-chelovek`** (variant Act 4, bone-crunch) → same extract. The bracketed elision
   `[…]` correctly elides the intervening «— кр... кр...,»; both fragments present, in order.
   Legitimate author-elision, not a checker-gaming truncation.
3. **`com-pobedonostsev-zola`** (18 Feb 1887 letter) → `extracts/v26_705_736_commentary.txt`.
   «Едва ли сам Золя дошел до такой степени грубого реализма, на какую здесь становится Толстой.»
   present verbatim.

Additional spot-checks also present: `vt-anisya-smother`, `plan-kogotok-seed` (Vlas/коленах),
`let-great-world` (the «большого света» fragment with its real elision).

---

## Check 2 — Claim-anchoring — PASS (with two MINOR prose wrinkles, see below)

Dates spot-verified against the commentary extract:
- **26 Oct 1886 OS** (Act 1, S. A. diary) — anchored (`com-sa-diary-act1`). ✓
- **Print permission 13 Jan 1887** — anchored: «13 января драма была разрешена к печати без
  всяких цензурных изъятий, за исключением…» in commentary. ✓
- **Paris 10 Feb 1888** — anchored (`com-theatre-libre`, verbatim). ✓
- **Stage ban lifted 15 Sep 1895** — anchored (`com-nicholas2-lifts`, verbatim). ✓
- **Epigraph restored 1913 Biryukov edition** — anchored («1913, впервые введен эпиграф из
  «Евангелия» от Матфея, исключенн[ый]…»). ✓
- **Maly 29 Nov 1895** — anchored («29 ноября — в московском Малом театре»). ✓

**100,000+ vs 250,000 discrepancy** — handled correctly. Flagged, not merged: index line 190
parenthetically records S. A. Tolstaya's 250,000-in-three-days figure as the larger one and says
"the two figures are recorded, not merged"; dossier `contradictions[]` names the apparatus
figure (100,000+) as the baseline and the 250,000 as S. A.'s reminiscence. Exemplary.

**Stanislavski-vs-Dec-1886 variant-Act-4 correction** — handled correctly. Index line 126 and
`com-variant-act4` + `needsReview` all date the variant to Dec 1886 and explicitly flag the
circulating secondary claim that credits Stanislavski (1902) with prompting it. Correctly anchored
to A. K. Chertkova's memoir.

Items not in the PSS commentary but legitimately anchored elsewhere (not unanchored):
- the **1909 (lost) film** → `_visuals.md` VIS-05 (still reproduced in Khanzhonkov's memoirs);
- the **Moscow-students gratitude episode** → `_scholarship.md` (Biryukov III.6/III.19, per Sergeenko);
- **Stanislavski 1902 MAT** → standard attributed fact, listed in `references.background`.

---

## Check 3 — Attribution discipline — PASS

Strong. The "Scholarly context" section (index line 274) is a model of the "ground in primary
before mainstream" rule:
- "naturalism" is reported as **a reading** ("Mainstream reference works file the play flatly as
  'naturalistic drama'… But the equation is less settled… The dive follows this: it reports
  'naturalism' as a reading").
- The Zola/Ibsen grouping is attributed to "mainstream reference works" + "German criticism of
  the 1880s–90s" (grounded in `_scholarship.md`, a naturalism-survey source), never asserted.
- **Gatrall (2008), Sizova (2023), Simmons, Stanislavski** are all named and their positions
  attributed. The marquee `extends` synthesis is explicitly labelled "the dive's synthesis,
  attributed as such" (line 61) and "a synthesis the corpus supports and the literature does not
  draw sharply" (line 276).
- Pobedonostsev's "Zola" charge is correctly placed in *his* mouth, not the dive's.
- The temperance reading is reported as "real but secondary," attributed to the in-circle sources.

No scholarly claim is laundered into the dive's own voice.

---

## Check 4 — Entity routing — PASS (1 MINOR)

`wikiType` values all valid per wiki-schema v1.4: 7× `character`, 13× `person`, 2× `concept`,
2× `institution`. Fictional figures → `character` with structured `prototypes[]`; real genesis/
censorship figures → `person`. Correct split.

**`prototypes[].certainty` — not over-claimed, matches the prompt's expected calibration:**
- Nikita→Koloskov, Anisya→Marfa, Akulina→Elena, Anyutka→Efimya: `author-stated`+`documented` ✓
  (schema: an author-stated attribution is `documented`).
- Akim→unnamed otkhodnik: `editorial`+`probable` ✓ (correctly NOT documented).
- Matryona: `editorial`+`conjectured`, note "No documented life-prototype" ✓ (matches the prompt's
  "Matryona has no documented prototype").

**MINOR (M1):** Mitrich→"a remembered retired-soldier type" is `basis: author-stated` +
`certainty: probable`. The schema states "an `author-stated` one is `documented`" (the basis/
certainty pairing rule). A "type" recalled in A. K. Chertkova's memoir is arguably `contemporary`
basis (a family member's recollection) rather than author-stated, which would make `probable`
consistent. The certainty is appropriately cautious; the *basis* label is the soft mismatch.
Recommend `basis: contemporary` (or `editorial`) to keep the pairing rule clean. Not blocking.

**`vaultStatus` — accurate.** Confirmed against the 14 live vault pages. Only `Vladimir Chertkov`,
`Sophia Tolstaya`, `Leo Tolstoy` exist and are the only three marked `exists`; all others `missing`.
Loose-matched every "missing" person (Pobedonostsev, Davydov, Stanislavski, Feoktistov, Lentovsky,
Savina, Antoine, Koloskov, Stakhovich, Alexander III) against the vault for the transliteration
gotcha — no false-negative `missing`. The empty-name Matryona prototype entry (`name: ''`) is
harmless but slightly untidy (could carry `note` only); not flagged as an error.

---

## Check 5 — workRecord — PASS (3 MINOR)

Field names mostly match `tolstoy-works-schema.md` v8. Both CORRECTIONS are present and
evidence-anchored:
- `publishedDuringLifetime → true` (refs `com-publication`, `com-100000`; note flags "record
  currently false"). ✓
- `publishedInRussiaDuringLifetime → true` (ref `com-publication`). ✓ Both correct against the
  record stub, which has both `false`.

Date fields use NS in the main field + OS in `oldStyle` (e.g. `dateWritingStarted: 1886-11-07`/
`oldStyle: 1886-10-26`). `titleAlternatives[]` uses the schema's `{title,type,language}` object
shape with valid `type` values (`subtitle`, `translation`). `epigraph`/`epigraphSource`/
`epigraphLanguage` valid. No invented field names; no fabricated dates/venues detected (Posrednik/
Sytin venue and Feb-1887 dates all anchored).

**MINOR (M2): `bans[].scope` violates the controlled enum.** Schema enum is
`complete-ban · passages-cut · serialization-refused · confiscation · pre-publication-rejected`.
The dossier uses free-text scopes: `'stage performance (public and imperial theatres)'` and
`'street/peddler retail sale of the brochure'`. This is a genuinely awkward fit (a stage-only ban
with the print permitted is not cleanly any enum value), but as written it is off-vocabulary.
Recommend mapping to `complete-ban` with the stage-vs-print nuance in `notes`, or proposing a
schema vocab addition. Since the workRecord is a *proposal* (not yet written into the record),
this is a pre-ingestion fix, hence MINOR.

**MINOR (M3): `bans[]` omits the lift date as a structured field.** The schema provides
`banLiftedDate`/`banLiftedDateOldStyle`; the central narrative fact (Nicholas II, 15 Sep 1895 OS /
27 Sep NS) is captured only in the `note` and `censorshipNotes`, not in the structured
`banLiftedDate` on the stage-ban object. Recommend adding it before ingestion.

**MINOR (M4): the second ban (MIIA street-retail) `authorityType: imperial-state`** is fine, but
its `scope` is likewise off-enum (same as M2).

These three are all confined to the `bans[]` block and do not touch the two headline corrections.

---

## Check 6 — coverage honesty — PASS

No surface is over-marked. "Visual & manuscript record" is `partial` (note: staging photos and
manuscripts largely rights-reserved/Russian-museum). "European stage career beyond Paris" is
`not-covered` (principle documented, per-city dates not confirmed). The full-23-redaction collation
and Soviet/world stage history are listed under `notCovered`. The five `covered` surfaces are
genuinely heavily evidenced. Honest.

---

## Check 7 — Voice & rights — PASS

- **Voice:** the dive's own voice is factual/bare; editorialising is confined to attributed
  scholarly positions and Tolstoy's own recorded ambivalence ("The author's later verdict" quotes
  him directly). No purple prose in the dive's voice.
- **Rights / images:** the five `<img>` embeds in `index.md` are all PD `usable:true` visuals
  (Repin VIS-03, Davydov VIS-10, Pobedonostsev VIS-09, French titlepage VIS-17, Brentano-1922
  VIS-04). The **CC-BY Maly (VIS-13)** is `usable:true` but `localPath: ''` (not downloaded) and is
  NOT embedded — correctly not treated as PD. The **rights-reserved ГМТ (VIS-14)** and **not-found
  Russian-first-ed (VIS-20)** are `usable:false`, `localPath: ''`, not embedded. The **wrong-
  Stakhovich Serov portrait (VIS-08)** is correctly `usable:false` with an IDENTITY-CAUTION note.
- **No rights-reserved/unknown image committed to `extracts/`** — `extracts/` holds only
  `.txt`/`.md`/`.html` (zero image files). No dive image lives under `website/src/`.
- The `visuals/` cache is git-ignored via the `research/*/visuals/` rule in `docs/.gitignore`
  (confirmed by reading the ignore file; git not run per instruction).

---

## Check 8 — Marquee integrity — PASS (1 MINOR)

The `confirms`+`extends`+`complicates` outcome is supported and carried in the prose:
- **`confirms`** (doctrine + locus of redemption): grounded in `vt-kogotok` (subtitle bookended),
  `plan-kogotok-seed` (doctrine in the night-written plan), `vt-akim-transfig`, and the Svobodin
  staging note (`let-svobodin-akim`). Strong.
- **`extends`** (practice-before-theory → What Is Art?): explicitly labelled a dive synthesis,
  attached to its complication, lightly buttressed by Sizova (2023). Honestly hedged.
- **`complicates`** ("art for the people" failed with its first peasant audience): **carried in
  the prose**, not buried. Appears in Key findings (line 23), the marquee section (lines 63–69,
  with `com-peasants-not-understood` quoted verbatim and the bitter Chertkov/Stakhovich
  "above the masses" irony), the Reception section (line 259), and "The author's later verdict."
  The `let-great-world` letter is the decisive primary anchor. Well integrated.

**MINOR (M5/M6 — two small prose wrinkles, both anchored, neither a fabrication):**
- **M5:** Index line 259 reads "When the play was finally staged in **1896** at the Maly…" — this
  blurs the Maly *première* (29 Nov 1895 OS, per the commentary and stated correctly at index line
  213) with the *students-gratitude episode* (Biryukov dates "the winter of 1896"). Both component
  facts are anchored, but the sentence as written produces an internal date inconsistency with
  line 213. Recommend "staged at the Maly (winter 1895–96)" or splitting the two events.
- **M6:** Index figcaption line 93 and the "people around the work" paragraph (line 116) call
  Davydov "the prototype of Akim" / "the meek old highway peasant who became Akim" more flatly than
  the dossier's own `editorial`+`probable` certainty (correctly stated at index line 235). The
  Davydov-supplied-peasant→Akim link is editorial conjecture, not documented; the prose should
  hedge it ("said to be the model for Akim") to match the dossier. Soft over-claim in prose voice,
  not in the structured data.

---

## Issue summary

**BLOCKING:** none.

**MINOR:**
- M1 — Mitrich prototype `basis: author-stated` mismatches the schema's basis/certainty pairing
  rule for a memoir-recalled "type"; prefer `contemporary`/`editorial`. (dossier `entities`)
- M2 — `bans[].scope` off the controlled enum (free-text "stage performance…"). (dossier `workRecord`)
- M3 — `bans[]` stage-ban object omits the structured `banLiftedDate` (1895). (dossier `workRecord`)
- M4 — second `bans[]` object scope likewise off-enum. (dossier `workRecord`)
- M5 — index line 259 "finally staged in 1896 at the Maly" contradicts line 213's 29 Nov 1895
  (1895 première vs 1896 students episode conflated). (index prose)
- M6 — Davydov-as-Akim-prototype stated more flatly in prose (lines 93, 116) than its
  `editorial`/`probable` certainty warrants. (index prose)

All six are pre-ingestion polish; none undermines the dive's evidence, attribution, byte-fidelity,
rights handling, or marquee. The two headline workRecord corrections are sound and anchored.

---

**VERDICT: CLEAN-WITH-MINORS — 0 BLOCKING, 6 MINOR.**
