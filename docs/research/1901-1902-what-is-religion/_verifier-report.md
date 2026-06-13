# Phase-5 Verifier Report — `1901-1902-what-is-religion`

**VERDICT: NEEDS-FIXES** (1 factual FAIL, 3 schema FAILs; 3 CONCERNs). All are surgical fixes; the dive's scholarship, byte-fidelity, claim-anchoring, framing, and chapter-count handling are sound.

Verifier: independent Phase-5 pass, 2026-06-08. Adversarial re-derivation against the extract files and the two schema documents.

---

## Check-by-check

### 1. BYTE-FIDELITY — PASS
Re-derived 13 quotes (6 work-text, 7 diary/letter) verbatim against the named extract files by exact substring match — all FOUND. Additionally mapped all 7 keystone work-text quotes to their actual `[head]` chapter and confirmed each sits under exactly the chapter the dive attributes it to:
- ev-main-text → head III (claimed III) ✓
- ev-equality-core → head IV (claimed IV) ✓
- ev-corruption-three-means → head V (claimed V) ✓
- ev-church-truc → head VI (claimed VI) ✓
- ev-faith-definition → head VІІ (claimed VII) ✓
- ev-universal-religion-ch14 → head ХІV (claimed XIV) ✓
- ev-religious-people-break-circle → head XVII (claimed XVII) ✓

Chapter/date attributions are plausible and internally consistent. (Note: heads VII, XIV, XVI render with Cyrillic homoglyphs — `VІІ`, `ХІV`, `ХVІ` — an OCR/encoding artifact in the TEI, not an error in the dive.) `verify_quotes.py` 25/25 corroborated.

### 2. CLAIM-ANCHORING — PASS
Every primary claim in `index.md` traces to an evidence row / extract. The composition narrative (Genesis section) cites the diary/letter extracts inline; the "What the work says" section anchors each block to a chapter-located quote; the textual-history numbers (82 MSS / 1,449 units) anchor to ev-manuscript-description. All 25 evidence ids are defined; every entity `evidenceRef` resolves to a real id (0 dangling).

### 3. SCHOLARSHIP ATTRIBUTION — PASS
All four secondary sources present and correctly attributed, never asserted as fact:
- **Simmons 1968** — "perhaps his most conclusive, best-tempered…" attributed to Simmons, with the ourcivilisation.com URL in References. The "most conclusive" judgement is explicitly flagged (index.md ~line 290) as "an external attribution, not a finding." ✓
- **Moulin 2017** — `Journal of Ecclesiastical History` 68:3, 2017 in all four occurrences across index.md + dossier.yaml. **No "2021" anywhere** in either file. ✓
- **Bartlett 2010** — attributed for the excommunication-context framing. ✓
- **Maude 1911** — attributed for the A-Confession-to-here arc. ✓

### 4. SCHOLARSHIP TRIANGULATION — PASS
5 triangulation entries. All `relation` values are in the valid set (`confirms` ×1, `extends` ×3, `complicates` ×1 — no `contradicts`, which is fine). All 5 `evidenceRef` values (ev-definition-ch2, ev-corruption-three-means, ev-church-truc, ev-universal-religion-ch14, ev-diary-1901-02-08) match defined evidence ids.

### 5. ENTITIES — PASS
12 entities. All `wikiType` values valid: person ×7, event ×1, institution ×1, place ×1, work ×1. `institution` correctly used for «Свободное слово» / Free Word Press (NOT `organisation`/`organization`). `vaultStatus` values plausible; Chertkov & Birukoff marked `exists` (consistent with known vault pages incl. the `Pavel Birukoff` transliteration), the rest `missing`/contextual. Every entity `evidenceRefs` resolves.
- **Pobedonostsev** — `evidenceRefs: []`, role text states plainly: "Contextual to the dive's excommunication frame only — NOT named in the treatise or in the corpus extracts; included for the reception/biographical surround." Correctly NOT overclaimed. ✓
- **Holy Synod excommunication (1901)** event — role text: "the treatise's critique … bears on it but is not a formal reply, and the decree is nowhere named in the text — attributed, not asserted." Correct framing. ✓

### 6. EXCOMMUNICATION FRAMING — **FAIL** (one isolated day-count error)
The dive does NOT assert the treatise is a response to the excommunication: index.md:266 states "the Synod's action was not a response to this text"; line 276 attributes the "direct response" reading to scholarship (Bartlett/Maude); line 285 *complicates* it. The definitional formula's precedence (diary 8 Feb 1901 OS; decree 22–24 Feb 1901 OS) is correctly framed as "about two weeks before" in **6 of 7 places** (index.md:9, 17, 58; dossier.yaml:130; note line 12). Framing is otherwise clean.

**THE ONE ERROR:** `index.md:285` says the kernel formed "**nine days** *before* the decree." This is wrong and self-contradictory with the rest of the dive. 8 Feb OS → 22–24 Feb OS = **14–16 days** (≈ two weeks). This is exactly the wrong day-count the verifier brief warns about. Note: the parallel dossier triangulation note (dossier.yaml:613) correctly says "five months before the first dated manuscripts" (a different, correct claim) and contains NO "nine days." The error is isolated to index.md line 285 (and its mirror in the generated index.html:632).

### 7. CHAPTER COUNT — PASS
Handled honestly. The TEI extract carries exactly **17 numbered heads (I–XVII)** — confirmed by direct count (including the 3 Cyrillic-homoglyph heads VІІ/ХІV/ХVІ that a naive Latin-only count would miss). index.md "Textual history" and dossier `needsReview` both state the discrepancy openly: PSS manuscript description = главы I—XVIII (18), TEI = 17 heads, cause unresolved from the corpus, quotes byte-faithful to the TEI and chapter numbers follow the TEI. No number is silently asserted as definitive. This is the expected documented discrepancy, correctly surfaced.

### 8. CROSS-LINKS — PASS
All 10 sibling slugs linked from index.md resolve to real directories under `docs/research/`: `1879-1880-examination-of-dogmatic-theology`, `1879-1882-a-confession`, `1882-1884-what-i-believe`, `1890-1893-the-kingdom-of-god-is-within-you`, `1893-1894-christianity-and-patriotism`, `1897-1898-what-is-art`, `1900-the-slavery-of-our-times`, `christian`, `christian-anarchism`, `christian-communism-socialism`. No broken slug.

### 9. WORKRECORD — **FAIL** (3 controlled-vocabulary value violations; field NAMES are OK)
All 21 workRecord `field:` names are real keys. `mainCategory`/`subcategory` are NOT in `tolstoy-works-schema.md` but ARE a live convention in real records (`what-is-art/What Is Art?.md`, `confession/Confession.md`, etc.) — so they are legitimate, not invented. No fabricated venues/dates: Free Word No. 75 (Christchurch, 1902), 1906 Zemlya i Trud, and the OS/approximate sub-flags all check out.

**However, three controlled-vocabulary VALUES are invalid** (confirmed by diffing against the schema enums AND against real records such as `the-kingdom-of-god-is-within-you/…md`):
1. `firstPublishedVenueType: "publisher"` (dossier.yaml:739–740) — schema enum is `journal · newspaper · book · samizdat`. "publisher" is not a member. (Real records use `book` for a press-published treatise, e.g. KoG.)
2. `bans[].authorityType: "state"` (dossier.yaml:797) — schema enum is `imperial-state · holy-synod · foreign-government · periodical-editor · other`. Should be `imperial-state` (as in the KoG record).
3. `bans[].scope: "full publication ban"` (dossier.yaml:799) — schema enum is `complete-ban · passages-cut · serialization-refused · confiscation · pre-publication-rejected`. Should be `complete-ban`.

These are proposed-record values, not yet a live frontmatter file, so they would be caught at ingestion — but they are schema-invalid as written and should be corrected in the dossier so the proposal is clean.

### 10. COVERAGE HONESTY — PASS
No inflated `covered`. Genuine partials are marked `partial` (Redactions & textual history; Reception; Author's later verdict; Scholarly context). The "Place in the cluster" note (coverage line ~847) explicitly states *On Religious Tolerance* (О веротерпимости) and *On Freedom of Conscience* are sibling works with **NO dedicated dive yet** ("mentioned, not linked") — does not falsely claim dives exist. index.md:34 likewise: "(no dedicated dive yet)." Reception correctly marked a `notCovered` gap with no fabricated reactions.

### 11. RIGHTS/FILES — CONCERN (bookkeeping mismatch, low rights risk)
- `docs/.gitignore` line 18 confirms `research/*/visuals/` is git-ignored — third-party images not committed. ✓
- `extracts/` holds only PD text (Tolstoy + PSS editorial apparatus). ✓
- **Mismatch:** index.md (lines 330, 342) states "**Nine** public-domain images were cached locally" and lists `commons-biryukov-pavel-portrait.jpg` as the 9th. The `visuals/` dir does contain **9** image files, but the dossier `visuals:` block has only **8** entries (8 `localPath`, 8 `licence: PD`). The 9th file (`commons-biryukov-pavel-portrait.jpg`) has **no dossier `visuals[]` entry and therefore no recorded licence** — it is only name-dropped in another entry's `note` (dossier.yaml:566) and in the index prose. All 8 *recorded* visuals carry `licence: PD`. Because the file is git-ignored, this is a provenance-bookkeeping gap, not a redistribution risk; but index "9" vs dossier "8" should be reconciled (either add the 9th dossier entry with its licence, or drop the 9th from the index list).

### 12. VOICE — PASS
Minimal editorial; all Russian renderings labelled "(working English)"; mainstream scholarship consistently used as a foil and attributed, never asserted as baseline. A few evaluative phrases ("rare moment of eschatological confidence," "the rarest register") are interpretive but clearly framed as reading-of-the-text, not asserted fact, and are within the looser dive register. No purple overclaim.

---

## Prioritized fix-list

1. **[FAIL · factual]** `index.md:285` — change "nine days *before* the decree" to "about two weeks before the decree" (8 Feb OS → 22–24 Feb OS ≈ 14–16 days), matching the other 6 occurrences. Regenerate `index.html` (mirror error at index.html:632).
2. **[FAIL · schema]** `dossier.yaml:740` — `firstPublishedVenueType: "publisher"` → `book` (or a valid enum member).
3. **[FAIL · schema]** `dossier.yaml:797` — `bans[].authorityType: "state"` → `imperial-state`.
4. **[FAIL · schema]** `dossier.yaml:799` — `bans[].scope: "full publication ban"` → `complete-ban`.
5. **[CONCERN]** Reconcile visuals count: index.md says 9, dossier records 8. Either add a `visuals[]` entry (with `licence: PD`) for `commons-biryukov-pavel-portrait.jpg`, or remove it from the index list of nine.
6. **[CONCERN · already flagged, not a defect]** Subcategory `Essays and Criticism` vs `Treatises`/`religious` — the dossier `needsReview` already flags this as a Johan judgment call (the KoG record uses `subcategory: Treatises`, which may fit better). No action required from the verifier's side; noted for the author.
7. **[CONCERN · already flagged, not a defect]** Title `назначение` vs `сущность` and Biryukov co-translator-vs-reviser — both already in `needsReview`. Honest.

No fabrication, no unanchored primary claim, no byte-fidelity failure, no broken cross-link, no wikiType violation, no excommunication causal-overclaim (beyond the isolated day-count number), and the chapter-count discrepancy is handled honestly.

---

## Resolution (2026-06-08)

All four FAILs and the visuals CONCERN were fixed in the reviewing pass:

1. **[FAIL · factual]** `index.md` Scholarly-context bullet "nine days" → "about two weeks" — the one remaining straggler; the other six occurrences had already been corrected.
2. **[FAIL · schema]** `dossier.yaml` `firstPublishedVenueType: publisher` → `book`.
3. **[FAIL · schema]** `dossier.yaml` `bans[].authorityType: state` → `imperial-state`.
4. **[FAIL · schema]** `dossier.yaml` `bans[].scope: "full publication ban"` → `complete-ban`.
5. **[CONCERN]** Visuals reconciled to **8 catalogued**: the duplicate undated Biryukov portrait was dropped from the index list (the dated 1916 portrait is the canonical Biryukov entry), and the unsupported "6 additional catalogued" claim was removed from the Method section.

The two remaining CONCERNs — subcategory (`Essays and Criticism` vs `Treatises`) and the title `назначение`/`сущность` + Biryukov co-translator-vs-reviser question — are Johan judgment-calls already recorded in the dossier `needsReview`, left for human ingestion.

Post-fix: `verify_quotes.py` re-run **25/25 PASS**; straggler grep clean (no "nine days", "2021", broken slugs, `organisation`, or invalid enum values remain); HTML regenerated.
