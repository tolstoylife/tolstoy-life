---
layer: reference
lastUpdated: 2026-06-07
tags: [research, corpus-dive, session-log]
---

# Session log — 1884-1886-the-death-of-ivan-ilyich

A single-session `corpus-dive` work-dive on *The Death of Ivan Ilyich* (Смерть Ивана Ильича), run interactively on 2026-06-07.

## Session 1 — 2026-06-07 (Phases 0–7, complete)

- **Phase 0 (Scope).** Subject fixed as the single work; slug set to the **composition window 1884–1886**. The window was the one genuine decision: the menu offered "1882–1886" (conception-inclusive); a first reading of the PSS Tom 26 commentary's opening surfaced Sreznevsky's "1885–1886" (7 months); reading the *full* commentary showed the PSS editor **rejects** Sreznevsky and dates the literary work to April–May 1884, with Strakhov's title-page note «(1884—1886)». Slug → `1884-1886-the-death-of-ivan-ilyich`. Corpus surface: PSS Tom 26 (text/variants/commentary); diaries Tom 49; letters Toms 63/83/85.
- **Phase 1–2 (Sweep / extract).** Extracted the three Tom 26 files (`--choice=reg`, clean). Two opus subagents: a structural deep-read of the novella (12 chapters, 24 keystones → `_deepread.md`) and a composition-window witness sweep of diaries + letters (12 genesis quotes, 11 people → `_witness_sweep.md`, individual extracts saved). Visual sweep (sonnet): 4 PD portraits cached in git-ignored `visuals/`, 1 PD facsimile rendered to `extracts/` (PSS Tom 26 p. 61), 1 gap (1886 title page).
- **Phase 3 (Scholarship).** Sonnet sweep → `_scholarship.md`: received view, reception (thin for 1886), Heidegger §51 precision-graded, 8 triangulation rows, 20 sources. Framing watch applied (resists the "didactic Tolstoy" slide).
- **Phase 4 (Synthesize).** `index.md` (full work-dive spine), `dossier.yaml` (22 evidence rows, 13 entities, 6 visuals, 8 triangulations, a NEW-record `workRecord` proposal, coverage ledger, contradictions, notCovered, needsReview), draft note (`website/src/posts/notes/2026-06-07-the-death-of-ivan-ilyich.md`, draft:true), HTML via `serve.py`.
- **Phase 5 (Verify).** `verify_quotes.py` PASS 22/22 (0 warnings after adding "(working English)" labels). Independent opus verifier: **CLEAN-WITH-NOTES**, 0 must-fix, 4 nice-to-fix; 3 fixed (stale `_visuals.md` facsimile ref; `titleAlternatives.type` working-title→working; removed invalid `wikiType: work` entity → routed via workRecord), re-verified green.

### Key decisions (don't re-derive)
- **Slug = 1884–1886** (literary-work window per PSS Tom 26 + Strakhov), NOT 1885–86 (Sreznevsky, rebutted by the PSS editor) and NOT 1882–86 (conception). Conception/prototype (1881) lives in Genesis.
- **Diary-year artifact:** the genesis diary files are named `…1883_04_27/30`, `…1883_05_01` in the TEI but are **1884** (each `# bibl` = "Дневник 1884 г."; commentary dates them 1884; Tolstoy's diary was in a gap through early 1884). Adopted 1884; flagged in `needsReview`.
- **S. A. Tolstaya 1885 letters are in Tom 83**, not Tom 84 (Tom 84 begins 1891).
- **The March 1886 Ge letter** naming the novella (quoted in the commentary) is **absent from the TEI corpus** — do not re-hunt; source from PDF if needed.
- **No works/ record exists** — the `workRecord` proposes a NEW record at `…/novellas/the-death-of-ivan-ilyich/`.

### Follow-up queued (separate steps)
- Wiki/works ingestion: priority-1 entities are the prototype **Ivan Ilyich Mechnikov**, the concept **the false life («не то»)**, and the **work record** itself (apply the `workRecord` proposal). Priority-2: Kuzminskaya, Urusov, the decorous-lie concept.
- `needsReview`: diary-year PDF check; Stasov "seventy pages" primary source; the What Is Art? footnote include/exclude question; Heidegger §51 German wording; cluster relatedWorks ids.
- `notCovered`: redaction collation; Maude/translation lineage; full 1886 periodical reception; 1886 title-page facsimile.
