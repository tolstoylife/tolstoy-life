# Verifier report — Examination of Dogmatic Theology («Исследование догматического богословия») work-dive

- **Verdict: PASS-WITH-NITS**
- **MUST-FIX: 0**
- **NITS: 3**
- Verified independently in a fresh context on 2026-06-07. The dive is sound, source-anchored, honestly scoped, and schema-compliant. The three nits are cosmetic/forward-looking and do not block ingestion.

---

## 1. Byte-fidelity (belt-and-braces) — PASS

- Re-ran `python3 docs/research/lib/verify_quotes.py docs/research/1879-1880-examination-of-dogmatic-theology/dossier.yaml`: **22/22 quotes verbatim, 0 facsimile missing, 0 skipped, 0 label warnings — PASS**.
- Independently re-derived the requested sample by grep against the extract files; each appears exactly once:
  - `dogmth-text-09` («Бог этих первых глав есть не бог христианский …») — 1 hit in the work extract.
  - `dogmth-text-19` (Catherine/Peter, «благочестивой блуднице Екатерине II …») — 1 hit.
  - `dogmth-let-01` (genesis letter, «я отдел обзора православного богословия должен был расширить») — 1 hit in `v63_011_H_H_Straxovu.txt`.
- **Re-extracted the source XML from scratch** (`extract_tei.py --choice=reg --notes=auto` on `v23_060_303_…xml`) and `diff`'d against the committed extract: **IDENTICAL** (byte-for-byte, 1,029,835 bytes). The Catherine/Peter quote and the recovered tail passage are both present in the fresh re-extract.
- All 22 `quoteEn` rows carry the `(working English)` label (22/22 — confirmed by count). Working-English renderings in index.md are likewise labelled `*(working English — …)*`.

## 2. Every primary claim in index.md is source-anchored — PASS

Spot-checked the vivid claims; each traces to an evidence row or to attributed PSS Tom 23 commentary:
- "like a good seminarian" → `dogmth-text-04` (quoted verbatim at index L43–45).
- "conscious lie" / «сознательная ложь» → `dogmth-text-02`; "deception built up over centuries … base aim" → `dogmth-text-05`.
- four-part project → `dogmth-text-20` + `dogmth-let-01` (and attributed to the 1884 Gospel preface).
- title «Исследование» vs «Критика» → `dogmth-text-01` + attributed Jubilee-editor restoration.
- Catherine/Peter censorship → `dogmth-text-19` + commentary (publication section).
- positive conclusion → `dogmth-text-20`.

Commentary-only facts (genesis chronology, four manuscripts, censorship history, 1882 Solovyov insertion) are consistently attributed in the dive's own voice — "the Jubilee commentary (Savodnik)", "the commentary notes", "the Jubilee editors" — never presented as primary-verified fact. No assertion of a commentary/scholarship claim as bare fact was found.

## 3. Scholarship is attributed, not asserted — PASS

- "Scholarly context" names every secondary source: Simmons (1968), Kolstø (2022), A. N. Wilson, Rosamund Bartlett, Medzhibovskaya, Britannica.
- `scholarship.triangulation`: 5 entries. All relations are in the valid set — `complicates`, `extends`, `contradicts`, `complicates`, `confirms`. All `evidenceRef`s point to defined evidence ids (`dogmth-text-20`, `-text-13`, `-text-01`, `-text-19`, `-let-01`). Each entry names a source.
- No byte-fidelity claimed on secondary sources (dossier header is explicit about this).

## 4. Entities & vaultStatus accuracy — PASS

Loose-matched every surname against `website/src/wiki/` (14 pages total) and `website/src/works/`:
- **Claimed `exists`** — all three present: `Leo Tolstoy.md`, `Vladimir Chertkov.md`, `Yasnaya Polyana.md`. Correct.
- **Claimed `missing`** — all eight have **no** loose match in the vault (Makary/Bulgakov, Strakhov, Filaret/Drozdov, Elpidine, Wiener, Solovyov, Holy Synod, plus the four-part-project concept). Correct. No wrong "missing" verdict found; transliteration gotcha checked (no Birukoff-style hidden page exists for any of these).
- `wikiType` values used: `person`, `concept`, `institution`, `place` — all valid per `website/schema/wiki-schema.md`.
  - **Note for the prompt's own checklist:** the wiki schema (v1.3) defines **TEN** types — person, place, event, concept, translator, institution, adaptation, criticalWork, archivalFond, edition. The prompt's stated 9-type set (`…work/object/source/group`) is inaccurate; `work`/`object`/`source`/`group` are NOT wiki types. The dossier's four types are all genuinely valid regardless.

## 5. workRecord soundness — PASS

- All 18 proposed field names validate against `website/schema/tolstoy-works-schema.md` (titleRu, titleEn, titleAlternatives, genre, completionStatus, dateWritingStarted/Completed, dateFirstPublished, firstPublishedVenue, dateFirstPublishedInRussia, publishedDuringLifetime, bans, censoredVersionExists, censorshipNotes, samizdatCirculation, excommunicationRelated, relatedWorks, manuscripts).
- Enum values check out: `bans[].authorityType: imperial-state` ✓, `scope: complete-ban` ✓; `relatedWorks[].relationshipType: companion` ✓; `firstPublishedVenueType: book` ✓; `genre` enum includes both `religious` and `essay` ✓.
- Proposed `recordPath` under `non-fiction/treatises/` matches the existing convention (sibling The Kingdom of God Is Within You lives there).
- No fabricated dates/venues: 1891 Elpidine first edition (PY Rare Books catalogue), 1908 Gertsik, Wiener 1904 — all attributed; none asserted beyond source.
- Uncertain calls correctly routed to `needsReview`: genre, dateWritingCompleted (1880 vs 1884), dateFirstPublishedInRussia (Askarkhanov vs Gertsik), bans[] encoding, excommunicationRelated, Makary-bibliography discrepancy. None of these is asserted in the prose as settled.

## 6. Coverage honesty — PASS

Ledger statuses are honest. Three surfaces marked `partial`, each with a candid reason:
- **Reception & afterlife** — `partial`; note states the contemporary Russian reception sweep was not run and the corpus carries none. Honest (index.md L171/L196 say the same).
- **Redactions & textual history** — `partial`; variants summarized from commentary, not collated (no «варианты» file). Honest.
- **The author's later verdict** — `partial`; no separate later self-assessment swept. Honest.
The four `covered` surfaces (Genesis, What the work says, Publication, Place in cluster, Visual record) are genuinely deep. Nothing marked "covered" that the evidence shows is really partial.

## 7. Voice & hygiene — PASS

- No endorsing/editorializing voice in the dive's own register. Contested labels are attributed to the mainstream or complicated: the 1901-excommunication link is explicitly complicated ("the edict should not be tied to it directly… names no individual works"); "merely negative" is attributed to Simmons/general framing and then complicated by the primary text.
- `extracts/` holds only PD material: the work text, the two PD Strakhov letters, and two PD Wiener-1904 facsimile PNGs (titlepage + frontispiece). `git ls-files` confirms nothing is committed yet (whole dive dir is untracked `??`), so **no rights-reserved/unknown image is committed**. The Elpidine «Критика» title page (rights `unknown`, `usable: no`) is correctly left unfetched (empty `localPath`).
- `visuals/` (the 6 Commons portraits) is correctly git-ignored via `docs/.gitignore:18 research/*/visuals/`. Nothing placed under `website/src/` except the draft note.
- Draft note `website/src/posts/notes/2026-06-07-examination-of-dogmatic-theology.md` has **`draft: true`** (frontmatter L9). Confirmed.

## 8. The extract_tei.py fix — PASS

- The recovered tail passage «И в самом деле, из того, что бог един …» is present in both the committed extract and the fresh re-extract (1 hit each), at line 523, immediately following footnote anchor ²¹ — genuine Tolstoy prose, exactly the class of text the old `node.clear()` pre-pass was dropping.
- The fix is in the code: `extract_tei.py` L57–63 now captures `tail = node.tail` before clearing and restores `node.tail = tail`. Additive.
- **No note BODIES leaked**: `[note]` tag count in the work extract is **0**; a search for Savodnik/commentary phrasing returns 0. The single hit on the broad page-marker regex was `(стр. 567 — 571)` inside Makary's *quoted dogmatics* (legitimate work content Tolstoy is transcribing), not editorial apparatus.
- Honesty note: the fix has an uncommitted working-tree modification (`M docs/research/lib/extract_tei.py`) layered on committed fix `527cef87`; the dossier flags this shared-tool change for Johan in `needsReview`. Appropriate.

---

## NITS (non-blocking)

1. **"COMMITTED PD facsimile" wording is ahead of reality.** index.md L213 and dossier `vis-wiener-1904-titlepage.note` describe the Wiener facsimiles as "COMMITTED". They are present in `extracts/` and are PD, but `git ls-files` shows the entire dive directory is still untracked. The claim is true in intent (they WILL be committed and are PD), but at verification time nothing is committed. Cosmetic — reword to "to be committed" or simply commit the dive. No rights issue.

2. **Prompt's 9-type wiki list is stale, not the dive's problem.** The canonical schema set is the TEN types in `wiki-schema.md` v1.3. Flagged here only so the next verifier/ingestor uses the right list; the dossier's `wikiType` values are all valid.

3. **`dogmth-let-02` (23 March 1880) subject is genuinely ambiguous** and is correctly logged: the corpus TEI editorial note attributes its "work" to the Gospel examination, while the Tom 23 commentary reads it (with a caveat) as the dogmatic theology. The dive routes this to `needsReview`/`contradictions` rather than resolving it — correct handling. Noting it so the ingestor does not silently harden the attribution; the index.md prose (L63–67) leans toward "the work" without restating the caveat at point of use, though the caveat is present in the dossier.

---

## Evidence summary

- `verify_quotes.py`: 22/22 PASS (re-run).
- Fresh XML re-extraction `diff` vs committed extract: IDENTICAL.
- Sample quotes (text-09, text-19, let-01): 1 grep hit each, verbatim.
- vaultStatus: 3 `exists` confirmed present, 8 `missing` confirmed absent (loose-matched).
- All 18 workRecord field names + all enum values validate against the works schema.
- All 5 triangulation relations valid; all evidenceRefs resolve.
- Draft note `draft: true`; visuals git-ignored; no committed rights-reserved image.
- extract_tei tail fix present, additive; 0 note-body leaks.
