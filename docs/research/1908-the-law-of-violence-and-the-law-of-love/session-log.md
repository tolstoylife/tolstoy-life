# Session log — 1908-the-law-of-violence-and-the-law-of-love

## 2026-06-08 — Session 1 (full dive, in-session accept-edits)

Ran the complete corpus work-dive from the scope handoff
(`_generated/sessions/2026-06-08-the-law-of-violence-dive-scope-handoff.md`).

- **Phase 0–1.** Confirmed corpus facts; no existing slug dir, no existing `works/` record (record-creating dive). Tom mapping: 37→vol06, 56→vol22, 78→vol56, 89→vol59, 41→vol09.
- **Phase 2.** Extracted the treatise (`--choice=reg --notes=auto`, 870 lines), the editorial history (`v37_436_438`), and the Krug Chtenija cognate (`v41_334_336`). Three parallel sub-sweeps:
  - Treatise structural deep-read (opus) → `extracts/_deepread.md` (14 keystones).
  - Composition-years witness sweep (opus) → `extracts/_sweep_composition.md` (+ saved diary/notebook/letter extracts). Caught two corrections: the 12 May verb is «понравилось» not «понравилась»; the «чепуха» lines are Gusev's diary, not a Tolstoy autograph.
  - Visual-materials sweep (sonnet) → `extracts/_visuals.md` (10 PD images downloaded, incl. Prokudin-Gorsky 23 May 1908).
  - Rendered the opening-page PD facsimile (PSS vol06 p.165) → `extracts/v37_149_Zakon_nasilija_opening_facsimile.png`.
  - Refinement found in the text: the "fire in dry wood" image is a Salter («Сольтер») epigraph at the head of chs VI & X, not Tolstoy's prose; the "cold fire / hot ice" image is his own.
- **Phase 3.** Scholarship + reception web sweep (opus) → `extracts/_scholarship.md` (21 sources, 5 triangulation entries). Key: the Gandhi lineage runs through the 1908 *siblings* (A Letter to a Hindu, Kingdom of God), not this text (`complicates`); the 1908 jubilee / Synod hostility is the dominant reception context.
- **Phase 4.** Wrote `dossier.yaml` (33 evidence rows), `index.md`, and the `draft:true` note. `verify_quotes.py` → **33/33 PASS, 1 facsimile OK** (fixed 3 footnote-superscript / OCR-space mismatches). Rendered HTML with `serve.py --build-only`.
- **Phase 5.** Verifier pass (separate context).

Status at session end: dive complete; primary layer + scholarship + visuals + record-creating workRecord all in place. Not pushed (Johan pushes himself).
