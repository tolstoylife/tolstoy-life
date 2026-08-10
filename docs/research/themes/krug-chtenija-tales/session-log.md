# Session log — 1905-1906-krug-chtenija-tales

## Session 1 — 2026-06-12 (build + ship)

Built the whole dive in one in-session pass (interactive, not `--auto`). The third movement of the народный рассказ project after `stories-for-the-people` (1880s) and `1903-folk-tales`.

**Scope (Phase 0, Johan-confirmed via picker):** all six tales; genre decided per-tale after reading (not a blanket call); medium visuals; slug `1905-1906-krug-chtenija-tales`.

**What was done:**
- Extracted all 6 tales + the reversed-title draft (Tom 54) + 7 commentary files (`--choice=reg --notes=auto`, no dropped pairs).
- Read the 4 short tales + draft in the main context; delegated the 3 long tales' close read to an opus subagent (`_deepread_long.md`).
- Mined the «История писания» apparatus (`_commentary.md`) + the Круг чтения general history (the недельное чтение slot, the encryption statement, the месячные-чтения German-only fact, the Gorbunov-Posadov prosecution).
- Swept the 1904–06 diary (`_sweep_diary.md`, 15 relevant) + the 1905–06 letters Toms 75/76/89 (`_sweep_letters.md`, 17 relevant) — the composition-amid-revolution record + the Chertkov/Gorbunov channel.
- Medium visuals sweep (`_visuals-sweep.md`): 8 PD downloads + 5 work-orders + sibling-dive cross-refs (Shchegolenok, Chertkov). Keystone facsimile = the Алёша autograph plate rendered from vol05.pdf.
- English-first scholarship sweep (`_scholarship.md`): 4 findings triangulated (3 `extends`, 1 `confirms`); per-tale English translation status (the key correction: only Алёша had a pre-2000 translation; the other five = Sekirin/Spence 2000).
- 36 evidence rows; `verify_quotes.py` PASS (36/36, exit 0). Separate-pass opus verifier = CLEAN-WITH-MINORS (0 blockers, 1 should-fix). Fixed: Молитва censor cut is POSTHUMOUS (2nd ed. 1910–1912 Sytin/Biryukov, not 1908); hedged За что? vol-II inference; trimmed two editorial touches.

**Marquee:** the народный рассказ turns back to realist fiction and aims at the 1905 moment; За что? + Божеское carry the anti-autocracy / anti-capital-punishment / anti-church-as-state-servant critique a treatise could not legally print, inside the anthology Tolstoy built «имея в виду именно нецензурное» — and the editor was jailed for it a year after Tolstoy's death.

**Open items (see dossier needsReview):** anthology-subcategory <TBD> shelving (spans the sibling tale-dives); Молитва genre (short_story vs parable); Божеское genre (short_story vs novella); the English-title variants across the two 2000 editions; Круг чтения's own anthology works record (out of scope); За что? exact Круг чтения volume; the dangling `resurrection` relatedWorks forward-ref.

**Status:** committed (not pushed — Johan pushes). All gates green.
