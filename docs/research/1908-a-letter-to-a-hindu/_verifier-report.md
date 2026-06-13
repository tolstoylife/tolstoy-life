# Phase-5 Verifier Report — "A Letter to a Hindu" (1908)

**Verdict:** CLEAN-WITH-MINORS
**Date:** 2026-06-13
**Reviewer:** fresh-context Phase-5 verifier (separate pass; did not author the dive)
**Mechanical gate:** `verify_quotes.py` reports 29/29 quoteRu verbatim, exit 0 (accepted, not re-run here).

This is a judgement-level review on top of the mechanical gate. One genuine inaccuracy was found (an entity `vaultStatus`), plus a handful of awareness notes. Nothing rises to a fidelity or attribution failure.

---

## Checklist (9 areas)

### 1. Byte-fidelity spot-check — PASS
Five `evidence[].quoteRu` values confirmed verbatim by my own reading of the named extract, independent of `verify_quotes.py`:

| evidence id | extract | result |
|---|---|---|
| `hindu-thirty-thousand` | `v37_245_272…txt` (l. 273) | verbatim ✓ |
| `hindu-drunkard` | `v37_245_272…txt` (l. 273) | verbatim ✓ |
| `hindu-marquee-lever` | `v37_245_272…txt` (l. 279) | verbatim ✓ |
| `hindu-diary-6dec` | `v56_162_163…txt` (l. 9) | verbatim ✓ |
| `gandhi-last-transvaal` | `v82_178…txt` (l. 17) | verbatim ✓ |

No divergences. Note (not a defect): the dossier comment correctly flags the source's own transcription artefacts ("очен" for "очень" in `gandhi-confirm`; the extract also carries "Jndian", "strugle", "wordly", "illooking", "drikn" in the 1909 English) — these are preserved as-is from the TEI, which is correct verbatim behaviour. The dive does not silently "correct" the source.

### 2. Claim-anchoring (primary) — PASS
Every primary-source claim in `index.md` traces to an evidence row / extract:
- The consent thesis, the "thirty thousand" arithmetic, the drunkard image, the withdrawal-lever, the science-ballast second front → `hindu-thesis-oppression`, `hindu-thirty-thousand`, `hindu-drunkard`, `hindu-marquee-lever`, `hindu-self-enslaved`, `hindu-science-ballast`.
- The Spencer frame → `hindu-spencer-frame` (letter) + `hindu-spencer-source` (commentary). The verbatim Spencer line is present in the extract at l. 109/265.
- The self-disparagement thread (June "stumbled", 28 Nov, 6 Dec, 14 Dec) → the five dated diary evidence rows; all four quoted verbatim fragments are present in their extracts.
- The 413-sheet / 29-redaction history → `hindu-mss-413`.
- The reversal ("very much approved") → `hindu-tolstoy-approved`.
- The Gandhi correspondence (authorship, reincarnation, Transvaal tie, Hind Swaraj, last letter, "most important… in the world") → `gandhi-*` rows.
- The Das rejection is correctly handled as **secondary/attributed**, not asserted as primary (see §3).
- The "executions that day / I Cannot Be Silent" detail is anchored in the 14 Dec diary extract ("вешанье, мучанье людей", confirmed at `v56_163` l. 7).

No primary claim is asserted in the dive's own voice without an anchor.

### 3. Attribution of secondary claims — PASS
Gandhi reception dates, Hazama, Mantena, Guha, Doke, the satyagraha divergence, and Das's rebuttal are all attributed in-voice ("Hazama (2023) shows…", "Mantena (2012) reads…", "Doke's 1909 …", "Das … published an 'Open Letter' …") and each is backed by a named References / `_scholarship.md` entry. The serialization dates (25 Dec 1909 / 1 Jan / 8 Jan 1910) are presented as the scholarship's resolution of the PSS's looser "January 1910", not as corpus fact. The Das rebuttal is explicitly flagged in `notCovered` / "Material not covered" as known from SAADA, not held in the corpus — the right move. No secondary claim is stated as bare fact.

### 4. Scholarship triangulation validity — PASS
All five `triangulation[].evidenceRef` values exist in `evidence[]`: `hindu-marquee-lever` (×2), `hindu-thirty-thousand`, `hindu-spencer-frame`, `gandhi-last-transvaal`. All five `relation` values are in the allowed set {confirms, complicates, contradicts, extends}. Relations are defensible:
- `confirms` (letter shaped Gandhi in SA) — well attested.
- `complicates` (≠ source of satyagraha) — supported by Hazama/Mantena.
- `contradicts` on the Das-rejection row — correct: the intended recipient publicly rejected the counsel; "contradicts" is the honest label (the conventionalView "Tolstoy's counsel was welcome to the movement" is genuinely negated).
- `extends` ×2 (Spencer frame undiscussed in scholarship; stronger "most important in the world" phrasing from the primary Russian) — both are corpus-supplied readings beyond the literature.

### 5. Entities — PASS-WITH-ONE-FIX
`wikiType` values used: `person` (8), `concept` (2), `work` (1). `person` and `concept` are valid. `vaultStatus` accuracy, verified against `website/src/wiki/` (16 files total):
- `Vladimir Chertkov` → `exists` — **correct** (`Vladimir Chertkov.md` present).
- Gandhi, Das, Bharati, Vivekananda, Makovitsky, Gusev, Škarvan → `missing` — **correct**; loose-matched each surname (incl. the transliteration gotcha) — none has a dedicated page.
- `Free Hindustan` → `missing` — **correct**.
- **`Non-resistance` → `stub` is INACCURATE.** There is no dedicated non-resistance wiki page; the term appears only *inside* `Christian Anarchism.md`, `Leo Tolstoy.md`, and `Tolstoyanism.md`. With no standalone page, the honest status is `missing` (or, if the intent was "covered within Christian Anarchism", say so explicitly). As written, an ingestor could read `stub` as "a thin page exists" and skip creating one. **Must-fix (small).**

`wikiType: work` (the subject letter, 1 row): `work` is **not** in the live validator's `WIKI_TYPES` (the 12 types are person/place/event/concept/translator/institution/adaptation/criticalWork/archivalFond/edition/character/group). This is the known Tolstoy-Lab "13th type" convention, and the letter is *also* correctly routed to a `workRecord` (the live model for a work). So this is not a vault-page defect — but `vaultStatus: missing` on a `work`-typed row is slightly misleading, since the work will live as a `works/` record, not a `wiki/` page. Awareness note, not a blocker (see optional nits).

### 6. Translations labelled — PASS
Every `quoteEn` is labelled. The authorized published text carries "(Tolstoy/Chertkov English, 1909)" or "(Tolstoy's own English, in the same letter)"; the dive's own glosses (commentary, diaries, the Das appeal, the last-letter passages) carry "(working English)". Spot-checked all 19 evidence rows with a `quoteEn` — no unlabelled `quoteEn` found. The labelling correctly distinguishes the authorized 1909 translation (which the TEI carries) from working glosses, including the subtle case that `gandhi-last-love` / `gandhi-last-transvaal` are "(working English)" because the last letter's published English differs from the corpus Russian — consistent with the dive's own marquee point.

### 7. workRecord schema match — PASS
All `workRecord.fields[].field` keys are real keys in `tolstoy-works-schema.md` (titleEn, titleRu, titleAlternatives, mainCategory, subcategory, genre, language, completionStatus, publishedDuringLifetime, publishedInRussiaDuringLifetime, dateWritingStarted, dateWritingCompleted, dateFirstPublished, firstPublishedVenue, firstPublishedVenueType, dateFirstPublishedInRussia, firstPublishedInRussiaVenue, firstPublishedInRussiaVenueType, epigraph, epigraphAuthor, themes, samizdatCirculation, bans, relatedWorks, identifiers.jubileeEdition.volumes). Values are evidence-anchored:
- `genre: essay`, `subcategory: "Essays and Criticism"`, `mainCategory: "Non-Fiction"` — valid enum values; `Essays and Criticism` is a real `Non-Fiction` subcategory; the open-letter→essay reasoning is sound and flagged `confidence: medium`.
- **OS→NS conversions all verified (+13 days, correct for 1908–1909):** dateWritingStarted 1908-06-07 OS → 1908-06-20 NS ✓; dateWritingCompleted 1908-12-14 OS → 1908-12-27 NS ✓; dateFirstPublished 1909-04-19 OS → 1909-05-02 NS ✓ (each recomputed independently). The OS values are carried in `oldStyle:` companions.
- `dateWritingStarted` value 1908-06-07 (OS) matches the commentary ("7 June 1908"); the dive prose's "7 June 1908 (OS)" is consistent. (Minor prose/field cosmetic: the index "Genesis" section also says "**7 June 1908**" but the marquee Key-findings bullet doesn't restate a date — no conflict.)
- List-typed fields are shaped as object arrays: `titleAlternatives` → `[{title,type,language}, …]`; `relatedWorks` → `[{id, relationshipType}, …]` with valid `relationshipType` enums (source, companion); `bans` → `[]` (empty, justified). All correct shapes.
- No fabricated venues/dates: «Киевские вести» no. 103 / «Русские ведомости» no. 89, 19 April 1909 (OS) trace to `hindu-pub-russian`; the 1911 full-text venue is named.

One honest edge correctly flagged in `needsReview`: `publishedInRussiaDuringLifetime: true` is technically right (1909 excerpts) but the full text is posthumous 1911 — the nuance is routed to `censorshipNotes` and `needsReview`, not buried.

### 8. Coverage honesty — PASS
`coverage[]` markings are honest. "Redactions & textual history" = `partial` (aggregate 413/29 captured, individual variants not collated) — accurate. "Reception — Russian society & church" = `partial` with an explicit note that no Synod/critic storm was found and it is "marked partial honestly, not padded" — this is correct and commendably self-aware; the dive does not inflate a thin surface to `covered`. The `covered` surfaces (genesis, what-the-work-says, the people, publication, the Gandhi story, the cluster, the author's verdict, visuals) each have substantive evidence behind them. No surface is over-claimed.

### 9. Rights / voice — PASS
- **Rights:** `visuals/` is confirmed git-ignored (`git check-ignore` positive) and `git ls-files` shows nothing tracked under it. The six cached images — including the only rights-encumbered one, the CC-BY-SA Linotype photo — are local-only, none committed. `extracts/` holds only text; no PD facsimile is committed (none was available; the dir-mislabel gotcha that blocked a PSS Tom 37 facsimile is documented). No rights-reserved image is in the repo.
- **Voice:** prose is bare/factual. Contested movement labels are attributed to the outside, not asserted — "[Tolstoyan]"/"tolstoyanism" are explicitly kept as "the mainstream's word, not its own" (Scholarly-context section), and the satyagraha-vs-non-resistance distinction is argued from sources rather than declared. The "Why this matters" section editorialises lightly ("the work's strangely low standing") but stays anchored to the documented diary record. Acceptable.

---

## Required fixes (must-fix)

1. **`entities[]` — "Non-resistance" `vaultStatus`.** Change `stub` → `missing` (no dedicated `wiki/` page exists; the term lives only inside Christian Anarchism / Leo Tolstoy / Tolstoyanism). As-is, `stub` risks telling the ingestor a thin page already exists, which would suppress page creation. If the intent was "subsumed under Christian Anarchism," state that in the entity `role`/note instead of using `stub`.

## Optional nits (non-blocking)

1. **`work`-typed entity vs live `WIKI_TYPES`.** The subject-letter entity uses `wikiType: work`, which the live validator does not accept (it's the Lab-only 13th type). The work is correctly carried as a `workRecord`, so this is harmless, but consider noting in the row that the live destination is a `works/` record, not a `wiki/` page — `vaultStatus: missing` reads as "needs a wiki page" otherwise. Consistent with prior shipped dives; flagging only for tidiness.
2. **`needsReview` already captures** the secondary-quote precision items (Gandhi preface phrasings, "most important in the world" vs "most weighty practical proof", the Spencer-frame English-edition absence) and the transliteration-at-ingestion check for the missing entities. These are correctly deferred, not asserted. No action needed; listed here only to confirm the verifier saw and agrees with the deferrals.
3. **Russian transcription artefacts** ("очен", "Jndian", "illooking", etc.) are faithfully preserved from the TEI. Correct, but worth a one-line note at ingestion so a future editor doesn't "fix" them into the wiki and break a future verbatim re-check.

---

## Summary
Fidelity is solid: 5/5 independent byte-checks verbatim on top of the 29/29 mechanical pass; every primary claim anchored; every secondary claim attributed and sourced; triangulation refs and relations valid and defensible; translations all labelled; workRecord keys real and OS→NS math correct; coverage honest; rights clean; voice bare and attributing contested labels outward. One small must-fix (the "Non-resistance" `vaultStatus: stub` → `missing`) and three optional tidiness nits.
