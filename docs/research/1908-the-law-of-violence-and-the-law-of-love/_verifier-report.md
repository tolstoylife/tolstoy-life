# Verifier report — *The Law of Violence and the Law of Love* (Закон насилия и закон любви, 1908) work-dive

**Verdict: CLEAN** — 0 must-fix, 3 minor notes.

Fresh-context independent verification, 2026-06-08. Mechanical gate re-run by the verifier:
`verify_quotes.py` → **33/33 quotes verbatim, 1 facsimile OK, PASS**. The judgement-level checklist below is all PASS.

---

## 1. Byte-fidelity sample — PASS
Spot-checked 6 quotes across all four genres by grep against the named extract:

- **Work-text (epigraph, the load-bearing one):** `zakon-dry-wood` «...как огонь в сухом дереве, прожгла свою оболочку и выбилась наружу.» appears verbatim at lines **173 and 399** of `v37_149_221_…txt`, each followed by «Сольтер.» at lines 177/403 — i.e. it IS a Salter epigraph at chs VI and X, exactly as the dossier claims (see item 8d).
- **Work-text (Tolstoy's own):** `zakon-cold-fire` «...как холодный огонь или горячий лед.» at line 255, embedded inside Tolstoy's running sentence — confirmed his own prose, not an epigraph.
- **Diary:** `zakon-diary-finished` «...и мне понравилось, и я кончил ее.» verbatim in `v56_117_117_1908_05_12.txt` (neuter «понравилось» — matches the dossier's `needsReview` correction of the brief's «понравилась»).
- **Letter:** `zakon-ikonnikov` «В статье этой я говорю об отказах от военной службы и о вас...» verbatim in `v78_138_A_I_Ikonnikovu.txt`.
- **Editorial commentary:** `zakon-ms-58` «...исчисляется в 1536 листов разного размера» and `zakon-gusev-chepukha` «Теперь я буду свою чепуху кончать» both verbatim in `v37_436_438_…txt` — the чепуха line correctly sits inside a Gusev-diary quotation embedded in Serebrovskaya's apparatus.
- **Facsimile:** `extracts/v37_149_Zakon_nasilija_opening_facsimile.png` exists, valid PNG (1221×1856 RGB).

## 2. Primary claims source-anchored — PASS
Every factual claim in the primary sections (Genesis, What the work says, Redactions, Publication, The author's verdict) ties to an evidence row with a verified extract. Composition dates, the title saga, the demoted chapters, the 1909 censored/abroad publication split, and the verdict swing all trace to diary/notebook/letter/editorial extracts. No unanchored primary assertion found. Programmatic check: all entity, triangulation, and workRecord `evidenceRefs` resolve to real evidence ids (0 dangling).

## 3. Secondary claims attributed, not asserted — PASS
Scholarly/reception claims are consistently attributed: "Tseitlin's 2025 Davis Center essay," "the editorial history," "Reading Russia, vol. 2," "Green 1986," Trotsky's 1908 tribute, etc. The Scholarly-context and Reception sections carry explicit attributions and a "received view is attributed, not asserted" preface. No byte-fidelity demanded on secondary sources (correct for prototype rigor).

## 4. Translations labelled — PASS
All **33/33** dossier `quoteEn` carry "(working English)". index.md shows the marker on every displayed quote (25 inline occurrences) and the Method section states translations "are labelled and are the dive's own." No unlabelled translation found.

## 5. No editorializing voice / contested labels not asserted — PASS
"Christian anarchist" / "Tolstoyan" appear only as the mainstream's contested label — flagged as such ("Where the mainstream uses a contested label…"), cross-linked to the project's Christian Anarchism and Tolstoyanism dives, and explicitly "labels this dive points at rather than asserts." Christoyannopoulos is named as the source of the "Christian anarchist" framing. Voice is simple and factual throughout.

## 6. scholarship.triangulation — PASS
All 5 entries reference valid evidence ids and use valid relations: `extends`, `confirms`, `extends`, `confirms`, `complicates` — all within {confirms/complicates/contradicts/extends}. The Gandhi-lineage row is correctly `complicates` (no source documents Gandhi engaging this text).

## 7. Entities resolve — PASS
All 13 entities carry a valid `wikiType` (person/concept/institution/event). vaultStatus spot-checked against `website/src/wiki` + `website/src/works`, and **every value matches the filesystem**:
- `exists` (confirmed present): Leo Tolstoy, Vladimir Chertkov, Pavel Birukoff, Christian Anarchism. (Tolstoyanism also exists — referenced in index, not a separate entity row, fine.)
- `missing` (confirmed absent): Nikolai Gusev, Free Age Press, Mahatma Gandhi, A. I. Ikonnikov, Holy Synod, Kievskie Vesti, the two non-resistance/law concept pages, the 1908 jubilee event.
Matches the known-true list in the brief exactly.

## 8. WORK-DIVE specifics
- **8a — workRecord fields / record-creating — PASS.** No record exists under `website/src/works/**` for this treatise (verified) — confirms RECORD-CREATING; nothing was written to `works/`. Field names match the works schema. `mainCategory: Non-Fiction` / `subcategory: Treatises` are not in the schema doc's field table but ARE the live field names in the sibling record (`The Kingdom of God Is Within You.md`, frontmatter lines 20–21) — so they're correct, the schema-doc grep simply didn't list them as table rows. `identifiers.jubileeEdition.volumes` matches the nested schema key. Proposals are evidence-anchored (no fabricated dates/venues); the `dateFirstPublished` = censored Kievskie Vesti is honestly flagged.
- **8b — OS/NS conversions — PASS.** Verified by computation (+13 days in 1908/1909): 20 Jan 1908 OS = 2 Feb NS ✓; 2 Jul 1908 OS = 15 Jul NS ✓; 17 Feb 1909 OS = 2 Mar NS ✓. All match the dossier.
- **8c — coverage ledger honest — PASS.** Reception is marked `partial` (text-specific contemporary reception thin because censored + author died Nov 1910) and Visual record `partial` (no manuscript facsimile / Gusev portrait / first-edition title pages openly available). No inflated `covered`.
- **8d — fire "dry wood" attribution — PASS (the key cross-dive correction is correct).** «огонь в сухом дереве» appears verbatim twice (lines 173, 399), each immediately followed by «Сольтер.» (lines 177, 403) — confirming it is a **Salter epigraph at the head of chs VI and X**, not Tolstoy's own prose, exactly as the dossier/index/`needsReview`/`contradictions` blocks state. The «холодный огонь / горячий лед» image (line 255) is correctly identified as Tolstoy's own running sentence. This refinement over the fire-metaphor dive is sound and well-documented.

## 9. File hygiene — PASS
`extracts/` holds only PD material: Tolstoy-text `.txt` extracts, the self-rendered PD `.png` facsimile, and the dive's own analysis `.md`/`.html` files (`_deepread`, `_scholarship`, `_sweep_composition`, `_visuals`). No rights-reserved raster image committed (no jpg/jpeg/gif/etc. in `extracts/`). `visuals/` is git-ignored (`docs/.gitignore` rule `research/*/visuals/`; `git check-ignore` confirms; `git ls-files` lists nothing under it). The dev-blog note `website/src/posts/notes/2026-06-08-…md` has `draft: true`.

---

## Must-fix
None.

## Minor notes
1. **index.md inline working-English count (25) < dossier evidence rows (33).** Expected and correct — several work-text quotes share one displayed passage and the krug-cognate quote is referenced not displayed; every *displayed* quote in index.md carries the marker, and the dossier is 33/33. No action needed; noted only so a future reader doesn't read the gap as a missing label.
2. **`mainCategory`/`subcategory` absent from the schema doc's field-table.** They're real (used verbatim in the sibling Kingdom-of-God record), so the dossier is right — but the schema doc `tolstoy-works-schema.md` would be clearer if it listed them as rows. A docs nicety, outside this dive's scope.
3. **`needsReview` is long (12 items) but all are genuine forward-looking ingestion flags** (OS/NS care, the Salter first-name identification, relatedWorks slug existence, the publishedInRussiaDuringLifetime edge case). None is an unresolved error in the dive itself; they correctly defer schema-boundary judgments to the human ingestion pass.
