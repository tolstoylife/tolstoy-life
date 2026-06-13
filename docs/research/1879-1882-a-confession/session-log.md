# Session log — A Confession (Исповедь) work-dive

Append-only record of what each session covered. Resume reads this + `dossier.yaml` `coverage:` + `notCovered`.

## Session 1 — 2026-06-06 (`--auto`, deep + heavy-visuals)

**Scope (Phase 0 contract).** Work-subject dive of *A Confession* (Исповедь). Subject text in PSS **Tom 23**: `v23_001_059_Ispoved` (text, pp.1–59), `v23_488_511_Ispoved_Plany_i_varianty` (redactions, pp.488–511), `v23_515_537_Ispoved` (editorial commentary, pp.515–537). Sibling *V chem moya vera* (What I Believe) same Tom. Composition window ~1879–1882 (to pin from commentary + corpus). Depth: **go deep / multi-pass**. Visuals: **heavy fan-out**. Grounded in Tolstoy / Biryukov / Chertkov + prior dives (`crisis`, `gospel-translation`, `tolstoyanism`). Outputs to `docs/research/1879-1882-a-confession/` + draft note. No vault writes, no push.

**Corpus facts pinned (Phase 0/1 recon).**
- Diary gap: Tom 48 has 5 entries for 1878, then the diary goes quiet through 1879–80 and resumes in Tom 49 at **April 1881** (Tolstoy kept notebooks, not diaries, through the acute crisis). The composition-years diary sweep targets Tom 48 (1878) + Tom 49 (1881–82); the 1879–80 silence is itself a finding.
- Letters: composition-window letters in **Tom 62 (→1879)** and **Tom 63 (1880–86)**.
- `extract_tei.py --choice=reg` ran clean on all three Tom-23 files (no dropped pre-reform pairs).

**Progress.**
- [x] Phase 0 scope contract (this entry + run-report.md).
- [x] Scaffolded `extracts/`, `visuals/`; extracted the 3 Tom-23 files with `--choice=reg`.
- [x] Phase 1 fan-out sweep (diaries Tom 48–49 + letters Tom 62–63 + broad echo + sibling).
- [x] Phase 2 deep-read (16-ch map + 13 keystones) + extracted 18 finalists (`--choice=reg`, clean) + heavy visuals fan-out (27 PD images cached, deduped) + PD facsimile (English Wiener 1904).
- [x] Phase 3 scholarship + gap-filling (Geneva-1884 confirmed; 1901 Synod names no works; English translation lineage; Medzhibovskaya long-conversion triangulation).
- [x] Phase 4 synthesize — `index.md`, `dossier.yaml` (27 evidence / 24 entities / scholarship / workRecord / coverage / visuals / needsReview), draft note, `index.html`.
- [x] Phase 5 verify — `verify_quotes.py` 27/27 PASS; `build_evidence_index.py --check` exit 0; opus verifier (fresh context) CLEAN-WITH-MINORS, no must-fix.
- [x] Phase 6 handoff — `run-report.md` with the six-point self-assessment; intermediate working `_*.md` deliverables folded into index/dossier/run-report and removed (extracts/ kept PD-only). Committed (not pushed).

**Session 1 complete.** Deferred to the reader's return: the human evaluation gate (spec §5) + the pending memory updates (reverse `corpus-dive-human-present`; reconfirm the in-session `claude -p` deny). Wiki ingestion is a separate human step — see run-report entity work-order.
