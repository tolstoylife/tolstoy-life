# Verifier report — Art & aesthetics satellites

**Verifier pass (separate lane).** Adversarial verification of the completed "Art & aesthetics
satellites" multi-work theme dive. The verifier did not author any artefact.

**Date:** 2026-06-21
**Artefacts:** `index.md`, `dossier.yaml`, `extracts/*.txt`, `extracts/_piece_*.md`, `extracts/_scholarship.md`
**Ground-truth schemas:** `website/schema/tolstoy-works-schema.md` (v9), `website/schema/wiki-schema.md` (v1.4)

---

## Overall verdict: CLEAN-WITH-MINORS

All ten checks PASS. Two CONCERN-level prose-clarity flags surfaced (one index.md
compression, one cosmetic), neither a fabrication, neither blocking. **Must-fix items: 0.**
The dive is evidence-anchored, schema-valid, correctly attributed, rights-clean, and honest
about its gaps. Recommendation: **APPROVE** (the two minors are optional polish, safe to carry
into ingestion as-is or fix in a one-line pass).

---

## Check-by-check

### 1. Byte-fidelity (belt-and-braces) — PASS
- Re-ran `python3 docs/research/lib/verify_quotes.py dossier.yaml` → **26/26 quotes verbatim,
  0 missing, 0 skipped, PASS, exit 0.** Confirmed independently (not trusted from the brief).
- Independently re-derived 5 `evidence[].quoteRu` strings by direct `grep` against the named
  extract files — each returned exactly **1** match (no paraphrase, no drift):
  - `engwia-wholeness` → `v30_204_206…txt` ✓
  - `maup-three-conditions` (the triad tail) → `v30_003_024…txt` ✓
  - `gogol-talent-heart` («ужасная, отвратительная чепуха») → `v38_050_053_O_Gogole.txt` ✓
  - `carp-how-to-live` («самой наукой наук») → `v31_087_095…txt` ✓
  - `engwia-christ-censored` («за род человеческий») → `v30_204_206…txt` ✓
- Inline RU snippets embedded in index.md prose (not in the blockquotes) also trace to extracts:
  «под спудом», «учение Христа», «рождение к истинной жизни», «как должны жить люди» all found
  in `v26_648_651_O_Gogole.txt` / `v31_087_095…txt`; «прекрасной» (Carpenter "splendid") is in
  the Tom-31 commentary extract `_comm_v31_282_284…txt`. No free-floating Cyrillic.

### 2. Every primary claim in index.md is source-anchored — PASS
- All 4 marquee blockquotes carry a TEI/Tom page ref **and** an evidence id in backticks
  (`maup-three-conditions`, `engwia-wholeness`, `gogol-talent-heart`, `carp-how-to-live`).
- Inline secondary quotes in the "four pieces" section all carry an evidence id
  (`gogol-public-comic`, `gogol-canon-inversion`, `gogol-belinsky`, `carp-upper-classes`,
  `carp-counterfeit`, `carp-remedy`, `engwia-christ-censored`, `engwia-not-mine`, etc.).
- Genesis facts (Maupassant signed «2 апреля 1894. Воронеж»; Posse's 4 March 1909 request;
  Carpenter read Oct 1896, preface Oct 1897–Feb 1898; English preface signed «17 марта» 1898)
  all trace to the commentary close-reads (`_comm_v30…`, `_comm_v38_498…`, `_piece_*.md`).
- **CONCERN (minor, non-blocking):** index.md line 63 reads "commissioned by V. A. Posse and
  published in *Русское слово*." The commentary (`_comm_v38_498_498_O_Gogole.txt`) shows two
  distinct channels: Posse commissioned the piece for **his own** journal «Жизнь для всех»;
  the *Русское слово* No. 68 publication came via the correspondent **S. P. Spiro**. The dossier
  keeps these correctly separated (Posse = entity role "commissioned…for «Жизнь для всех»";
  `firstPublishedVenue` = "Русское слово, No. 68"). Only the index.md prose compresses them so a
  reader could infer Posse published in Русское слово. Both facts are individually sourced and
  correct — this is a one-clause clarity fix, not an error.

### 3. Scholarly / secondary claims are ATTRIBUTED — PASS
- "Scholarly context" names every source in-line: Maude (*Tolstoy on Art*, 1924); Wikipedia
  (*What Is Art?*, *Aylmer and Louise Maude*); Raptis/Biblio rare-book records; *Visions for
  Sustainability*; MIT *redingtn* pages; Belinsky (1847 letter); Bayley; Jahn.
- The contested "over-reaching / over-application" frame is explicitly assigned to
  "critics (John Bayley; Gary Jahn)" (index.md line 108), never stated in the dive's voice.
- The dive's own counter-reading ("more discriminating than the caricature predicts") is
  flagged as "the dive's own primary-grounded contribution, not a received consensus." Correct
  separation of received view vs dive contribution.
- The thin-Gogol honesty is stated ("the dive's reading runs ahead of the secondary literature
  there"), matching the `gogol-rebirth`/`gogol-threefold` triangulation `source` notes.

### 4. scholarship.triangulation integrity — PASS
- Programmatic check: **12 `evidenceRef`s, all resolve** to real `evidence[].id` values.
- **12 `relation`s, all valid** (∈ confirms|complicates|contradicts|extends): 5 confirms,
  4 extends, 1 contradicts (`engwia-true-form` → Grant Richards correction), 1 complicates
  (`carp-upper-classes` → the over-reach frame). 0 broken, 0 invalid.
- Cross-checked every other `evidenceRefs`/`relatedEvidence` array in the file (entities,
  workRecords, visuals): **0 broken references** anywhere.

### 5. Entities resolve — PASS
- All `wikiType` values are valid wiki-schema v1.4 types or the allowed `work` routing label:
  `work` (routing label — allowed per convention), `person`, `concept`. No invalid type.
- All `vaultStatus` ∈ {exists, stub, missing}. Only two `exists`: What Is Art? and Sergei Tolstoy.
- **'exists' spot-checks (all confirmed in the `website/` submodule index — the parent repo's
  `git ls-files` does NOT see submodule content, so the first-pass "none" was a false alarm;
  re-checked inside the submodule):**
  - `What Is Art?` → `src/works/non-fiction/essays-and-criticism/what-is-art/What Is Art?.md`,
    `id: what-is-art` ✓ (the dossier's `relatedWorks.id: what-is-art` is correct)
  - `Sergei Tolstoy` → `src/wiki/Sergei Tolstoy.md`, `id: sergei-tolstoy`, "Eldest son …
    (1863–1947)" ✓ — correctly the SON, matching the dossier disambiguation note
  - `Vladimir Chertkov` → `src/wiki/Vladimir Chertkov.md` ✓ (referenced in censorshipNotes)
  - `Pavel Birukoff` → `src/wiki/Pavel Birukoff.md` ✓
- **'missing' spot-checks (loose-matched transliterations before trusting):** Maupassant/Mopassan,
  Gogol, Carpenter/Karpenter, Maude, Belinsky, Turgenev, Nikiforov, Posse, Kenworthy, Gurevich,
  Volynsky — **all 0 hits in `src/wiki/`.** The `missing` labels are accurate.

### 6. workRecords are evidence-anchored and schema-valid — PASS
- All field names are real works-schema v9 fields (titleEn/Ru, titleAlternatives, mainCategory,
  subcategory, genre, language, completionStatus, publishedDuringLifetime,
  publishedInRussiaDuringLifetime, the date* family, firstPublished*Venue*, authoringLocations,
  relatedWorks, censorshipNotes, themes, epigraph/epigraphLanguage, identifiers.jubileeEdition.volumes,
  wordCount/wordCountEdition, notes). No invented field.
- **Shelving is correct and, crucially, matches the live treatise.** All four records shelve under
  `Non-Fiction / Essays and Criticism / genre: essay`. Independently confirmed that the already-live
  **What Is Art?** record itself sits at `non-fiction/essays-and-criticism/what-is-art/` with
  `mainCategory: Non-Fiction`, `subcategory: Essays and Criticism`, `genre: essay` — so the four
  prefaces mirror exactly where their governing treatise already lives. The dive did **not** invent a
  "Prefaces" subcategory or a `preface` genre; it shelves under the valid vocab and records the gap in
  `needsReview` (item 1, phase 0) for a Johan-approved decision. Exactly as instructed.
- `mainCategory` value "Non-Fiction" ✓; `subcategory` "Essays and Criticism" ✓; `genre` essay ✓ —
  all in the schema's controlled vocab (works-schema §2 table).
- `relatedWorks[].relationshipType` values used: `prequel` (Maupassant → what-is-art) and
  `companion` (English preface, Carpenter → what-is-art) — both in the controlled set
  (`cycle·sequel·prequel·revision·source·companion·adaptation`). The Maupassant record self-notes
  ingestion may prefer `source`; defensible.
- `publishedDuringLifetime`/`InRussia` values are defensible and sourced:
  - Maupassant: both true (Posrednik, Moscow, 1894) ✓
  - English preface: lifetime true (Свободное слово, Purleigh 1898); InRussia **false** with a
    `needsReview` flag to confirm — conservative and honest (the preface attacks Russian censorship).
  - On Gogol: both true (Русское слово, 24 Mar 1909 OS) ✓
  - Carpenter: both true (Северный вестник №3, 1898) ✓
- No fabricated dates/venues: OS→NS conversions are derived (+12d 1880s–90s, +13d 1909) and the
  derivation is itself flagged in `needsReview` (item 7). The Spiro/Posse channel distinction is
  preserved in the structured fields (see Check 2). Maupassant signing date, Posse request date,
  Русское слово No. 68 / 24 March — all corroborated against the commentary extracts.

### 7. Translations labelled — PASS
- All 4 index.md blockquote renderings carry **"*(working English)*"**.
- All **26** dossier `quoteEn` strings begin "(working English)" (programmatic count: 0 missing).
- Published-translation deferrals are correctly exempt and labelled as published: Maude (Maupassant),
  Dole 1899 (Carpenter — "it IS translated", sourced to Wikisource/Crowell vol. 11 in
  `_scholarship.md`), and the Gogol articles routed to the translation-gaps ledger as likely gaps
  ("do not assert translated", needsReview item 6).

### 8. No editorializing voice — PASS
- Contested labels are attributed outward: "over-reaching"/"over-application" → Bayley & Jahn;
  "he condemned Beethoven and Shakespeare" is quoted as a **caricature** the dive pushes back on.
- No "heretic" framing asserted. Triangulation verdicts are presented "as hypotheses, not asserted"
  (index.md line 33), and each piece's verdict line is hedged with its documented strain
  ("the join shows", "strain on 'vindicates'"). Voice stays bare/factual.

### 9. Rights hygiene — PASS
- `git check-ignore` confirms the **entire `visuals/` dir is ignored** (dir-level) and every file
  inside is individually ignored (the 4 jpgs + `_visuals-sweep.{md,html}`). `git ls-files` for the
  dir is empty — **no image is tracked.**
- Only **4** images on disk (Maupassant/Nadar, Gogol/Möller, Carpenter/Hollyer, Tolstoy 1897), all
  `licence: PD`, all `usable: true`.
- The **Aylmer Maude** portrait is correctly `licence: CC-BY-SA`, `usable: false`, `localPath: ""`,
  and was **not downloaded** (no maude/aylmer file on disk). A work-order note routes it to NPG/Bodleian
  for a PD alternative. No rights-reserved/unknown image committed.
- All 5 visuals blocks carry a `licence` field (4× PD, 1× CC-BY-SA).

### 10. Coverage honesty — PASS
- `coverage` ledger marks **Reception & afterlife = partial** with an accurate note ("only the
  Maupassant and English-edition prefaces have a settled received literature … the Gogol articles
  have essentially no dedicated English scholarship"). Not over-claimed.
- The other surfaces marked `covered` are genuinely covered (24 keystones, all four genesis windows
  pinned OS+NS, redactions characterised, censorship/translation status resolved per piece, 12
  triangulation entries). The `notCovered` list is candid (earlier Maupassant diaries not swept;
  Carpenter's own English article out of scope; Gogol's *Selected Passages* out of corpus;
  manuscript collation not done; the 1909 grading marks noted but not transcribed). Honest.

---

## Minor flags (optional polish — not must-fix)

1. **index.md line 63 — Posse/Русское слово compression (CONCERN, Check 2).** Suggest:
   "commissioned by V. A. Posse for his journal «Жизнь для всех», and first published (via the
   *Русское слово* correspondent S. P. Spiro) in *Русское слово* No. 68 on 24 March 1909 (OS)."
   The dossier already encodes this correctly; only the narrative compresses it.

2. **Cosmetic — keystone count.** index.md "Method" and `coverage` say "26 verbatim keystones"/
   "24 verbatim keystones" in different places (the evidence ledger has 26 rows incl. 2 variants;
   the "four pieces" body marquees are fewer). Not an error — just reconcile the headline number if
   tidying. No evidence claim is affected.

---

## Evidence summary

| Check | Result | Method |
|---|---|---|
| 1 Byte-fidelity | PASS | verify_quotes 26/26 exit 0 (re-run) + 5 independent greps (1 match each) + inline-snippet trace |
| 2 Primary claims anchored | PASS (1 minor) | every quote carries Tom ref + evidence id; genesis facts trace to commentary; Posse compression flagged |
| 3 Secondary attributed | PASS | Maude/Wikipedia/Raptis/Bayley/Jahn named in-line; dive contribution labelled |
| 4 Triangulation integrity | PASS | 12 refs all real, 12 relations all valid; 0 broken anywhere |
| 5 Entities resolve | PASS | types valid; 2 'exists' confirmed in submodule (what-is-art, sergei-tolstoy + Chertkov/Birukoff); 13 'missing' loose-matched to 0 hits |
| 6 workRecords schema-valid | PASS | all fields real; shelving mirrors live What Is Art? record; gap flagged not invented; publish flags defensible |
| 7 Translations labelled | PASS | 4/4 index + 26/26 dossier carry "(working English)"; published deferrals exempt |
| 8 No editorializing | PASS | contested labels attributed outward; verdicts hedged as hypotheses |
| 9 Rights hygiene | PASS | visuals/ git-ignored; 4 PD on disk; Maude usable:false, not downloaded; all licensed |
| 10 Coverage honesty | PASS | Reception correctly 'partial'; notCovered candid |

**Recommendation: APPROVE.** 0 must-fix. 2 optional minors. The dive is ingestion-ready; the
Posse/Русское слово clause is the only thing worth a one-line touch-up, and it is already correct in
the machine-readable dossier.
