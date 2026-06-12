# Phase-5 verifier report — "The late voice: encryption & compression (1900–1910)"

**Verifier:** fresh-context adversarial pass (author did not self-approve).
**Date:** 2026-06-12.
**Overall verdict:** CLEAN-WITH-MINORS. 0 must-fix items; 3 minor items (all already partly captured in `needsReview` or harmless metadata polish).

---

## Mechanical gate (re-run)

`python3 docs/research/lib/verify_quotes.py docs/research/late-voice-encryption-compression/dossier.yaml`
→ **56/56 quotes verbatim, 0 facsimile missing, 1 skipped (`fuse-krug-censored-thoughts`, the deliberate no-quoteRu fusion row), 0 label warnings — PASS.** Re-confirmed independently.

---

## Check 1 — Byte-fidelity (belt-and-braces) · PASS

Opened the named extract for a sample of 8 rows spanning both threads and confirmed the `quoteRu` appears verbatim (whitespace-normalised; bracketed `[…]` are author elisions):

| Row | Extract | Type | Verbatim? |
|---|---|---|---|
| `key-sholom-aleichem` (keystone) | `extracts/v74_144_…` | fresh | YES |
| `chan-rule-only-through-you` (Chertkov) | `extracts/v88_607_…` | fresh | YES |
| `chan-all-or-nothing` (Chertkov) | `extracts/v89_757_…` | fresh | YES |
| `comp-krug-stated-aim` (anthology) | `extracts/v41_009_009_…` | fresh | YES |
| `enc-razrushenie-invented-church` | `../1903-folk-tales/extracts/v34_100_115_…` | REUSED `../` | YES |
| `enc-resurrection-survival-sentence` | `../1889-1899-resurrection/extracts/v32_003_445_…` | REUSED `../` | YES |
| `comp-eto-ty` | `../1903-folk-tales/extracts/v34_138_140_…` | REUSED `../` | YES |
| `enc-kreutzer-samizdat` | `../1887-1889-the-kreutzer-sonata/extracts/v27_563_624_…` | REUSED `../` | YES |

All 17 `../<slug>/extracts/…` reused paths resolve on disk (checked every reused row, not only the sampled four). No dangling sibling-extract pointer.

## Check 2 — Primary claims source-anchored · PASS

Read `index.md` end to end. Every primary (Tolstoy-sourced) factual claim traces to an evidence row / extract:

- The seven staged blockquotes in "The shape of the question" each carry a PSS Tom + extract-id citation on the following line (`v74_144`, `v77_218`, `v88_607`, `v34_100_115` reused, `v32_003_445` reused, `v34_138_140` reused, `v41_009_009`). All seven cited paths resolve on disk.
- "Key findings" bullets: the quantitative/primary claims are anchored — e.g. *Master and Man* "15,000 copies in four days" is carried verbatim from the sibling `1894-1895-master-and-man` dive (index L19, L157; dossier L319, L433); the channel-spectrum worked examples each point at a dive that exists on disk.
- The channel-spectrum table has exactly 8 tiers, matching the "eight-tier channel spectrum" / "tiers 4–8" prose.
- No primary claim in the dive's own voice was found that lacks an evidence anchor.

## Check 3 — Secondary claims attributed, not asserted · PASS

Every scholarly claim in "Scholarly context" and `scholarship` is attributed to a named source (Alston 2014, Holman 1988, Popoff 2014, Tulyakova et al. 2018, Bartlett, Hapgood, Emerson, Simmons, Wenzer) and each appears in References / `references.background`.

Specifically as required: the Popoff **"false disciple / under duress"** frame is attributed and is NOT stated as fact in the dive's voice. index.md L139 reads: *"**Popoff (2014)** supplies the contested frame of Chertkov as a controlling editor-censor who extracted the posthumous will «under duress» … The primary record here complicates that reading rather than confirming it."* The "two censors" framing is likewise marked *"Chertkov's … carried here as his attributed idea, not asserted in the dive's voice."* Clean separation of plumbing-confirmed vs design-not-reached.

## Check 4 — Triangulation integrity · PASS

All 6 `scholarship.triangulation[]` entries reference a real `evidenceRef` that exists in `evidence[]` (verified programmatically: `key-sholom-aleichem`, `chan-rule-only-through-you`, `chan-public-sole-node`, `enc-resurrection-survival-sentence`, `chan-chertkov-controls-all`, `comp-put-drops-attributions` — all resolve). Relations used are only `confirms` and `extends` (both valid). The two `confirms` rows (Free Age Press operation; *Resurrection* mutilation) are genuinely corroborated by named scholarship; the **four** `extends` verdicts each pair a named scholarly view that genuinely stops short of the finding and are defensible.

> Minor wording note (M-1): the prompt and the index narrative speak of **three** `extends` findings (genre-as-encryption, the 1900 protocol, compression-as-encryption); the dossier triangulation actually carries **four** `extends` rows — the extra one is `chan-chertkov-controls-all` (the "two censors" framing). Not a defect: the index groups the three *headline* findings and treats "two censors" separately under "Read critically." No fix required; noted for transparency.

## Check 5 — Entities · PASS

All `entities[]` rows use a valid wikiType (person · institution · concept — all within the 12-type vocabulary of wiki-schema v1.4). vaultStatus spot-checked against `website/src/wiki/` AND loose-matched across all of `website/src/` (transliteration gotcha):

- **Vladimir Chertkov** → `vaultStatus: exists` — confirmed (`website/src/wiki/Vladimir Chertkov.md`).
- **Sholom Aleichem**, **Gorbunov-Posadov**, **Stolypin**, **Свободное слово (Free Age Press)**, **Posrednik (Intermediary)** → all `vaultStatus: missing` — confirmed genuinely missing. The loose grep hits for these names are passing mentions inside *other* dives' dev-blog notes or `relatedArticles` lists (e.g. "Posrednik" appears in `Vladimir Chertkov.md` and `Pavel Birukoff.md` only as a mention, not as its own page). No own-page exists for any of the five. No false `missing`.

## Check 6 — Work-records · PASS

All four `workRecord[]` proposals are evidence-anchored (titleRu / dateFirstPublished / relatedWorks carry `evidenceRefs` that resolve; all entity & workRecord evidenceRefs verified programmatically to exist in `evidence[]`). Every proposed `field` name is a real key in the works schema (`titleEn`, `titleRu`, `genre`, `mainCategory`, `dateFirstPublished`, `dateWritingStarted`, `dateWritingCompleted`, `firstPublishedVenue`, `censoredVersionExists`, `relatedWorks`). `genre: anthology` is valid (works schema v7). `relationshipType: revision` is valid (schema enum). Several dates honestly carry `approximate: true` (7 occurrences). The unresolved Non-Fiction subcategory is honestly flagged: recordPaths use `<subcategory-TBD>` and `needsReview` item 1 names the schema shelving gap. No fabricated dates/venues.

## Check 7 — Coverage honesty · PASS

The `coverage[]` ledger is honest. The two `partial` rows are accurately partial — "Scholarly context (… Phase-3 pass pending integration; anthology scholarship is thin in English)" and "Visual & manuscript record (light sweep … no Free Age Press masthead found yet)" — both match the dive (the scholarship section is present but flagged thin; the visuals sweep is explicitly light with a named gap). The two `not-covered` rows (un-dived direct-treatise comparators; the 1905–06 Круг чтения weekly tales-as-tales) match `notCovered[]` and the "Material not covered" section. Nothing marked `covered` is in fact only partial.

## Check 8 — Voice · PASS

No advocacy in the dive's own voice. Working translations all carry the "(working English)" label (verified across the evidence ledger). Contested mainstream labels ("false disciple", "antagonist", "two censors") are attributed and cross-linked (`biryukov-sofia-relationship`, `tolstoyanism`), not asserted. The "Why this matters" close is interpretive synthesis grounded in the assembled evidence (it argues *from* the corpus findings), not editorial advocacy — acceptable as a framing paragraph.

## Check 9 — Rights & hygiene · PASS

- `git check-ignore docs/research/late-voice-encryption-compression/visuals/commons-chertkov-portrait-1883.jpg` → prints the path (= git-ignored). `git ls-files` on `visuals/` returns nothing (no image tracked). PASS.
- No image placed in `website/src/`: the only untracked item under the submodule is the draft dev-blog note `src/posts/notes/2026-06-12-late-voice-encryption-compression.md` (held `draft: true`). No `commons-*` or binary image anywhere in `website/src`.
- `extracts/` holds only `.txt` (Tolstoy PD text) plus the `_*.md/.html` working ledgers — no binaries, no images.
- All 7 `visuals[]` entries carry `licence: PD` (the Sholom Aleichem one additionally flags PD-US / "clear rights before any publication outside the cache" — honest).

---

## Minor items (none blocking)

- **M-1 (cosmetic, no fix needed):** "three `extends`" in the narrative vs four `extends` rows in the dossier triangulation — see Check 4. The fourth (`chan-chertkov-controls-all`, "two censors") is handled separately and correctly under "Read critically." Transparency note only.
- **M-2 (metadata consistency, optional):** `enc-devil-secret` carries `pssTom: 27` (the novella *Дьявол*'s volume) but its `quoteRu` is from a Tom 65 letter to Biryukov (`v65_005`). The quote verifies verbatim against the cited extract, so this is harmless, but `pssTom` here tags the work-subject rather than the citation source — inconsistent with sibling fresh rows where `pssTom` matches the extract's Tom. If ingested, prefer the source Tom (65) or add a note. (Reused row inherited from the-devil dive.)
- **M-3 (already in `needsReview`):** the `fuse-krug-censored-thoughts` row deliberately has no `quoteRu` (file-level pointer); `needsReview` item 2 already commits to anchoring it with the «19-е января» entry. Carrying forward as-is is acceptable for a prototype dive.

All three are honestly pre-flagged or cosmetic. No must-fix.

---

## Verdict

**CLEAN-WITH-MINORS.** All nine checks PASS. Mechanical gate re-confirmed 56/56. Byte-fidelity holds across fresh and reused rows; primary claims anchored; secondary claims attributed (Popoff frame correctly not asserted); triangulation refs resolve with defensible verdicts; entity wikiTypes and vaultStatus accurate (Chertkov exists, the five flagged entities genuinely missing); workRecord fields all valid schema keys with the subcategory gap honestly flagged; coverage ledger honest; voice clean; rights/hygiene clean (visuals git-ignored, no image in `website/src`, extracts PD-only, every visual licensed). 0 must-fix items; 3 cosmetic/pre-flagged minors.
