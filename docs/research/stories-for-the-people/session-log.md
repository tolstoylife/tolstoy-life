# Session log — stories-for-the-people

## Session 1 — 2026-06-11

**Scope contract (Phase 0):**
- Question: Tolstoy's народные рассказы (1881–1887) as a project — genesis, the Posrednik machinery (Chertkov, Sytin), the shared moral core of the tales, their reach into the popular readership, and the arc to What Is Art? + the two drama dives.
- Corpus surface: Tom 25 tale TEIs (18 tales + Речь о народных изданиях + variants); per-tale История писания commentary TEIs (v25_665–890); letters Toms 63–64, 85–86; diaries/notebooks Tom 49 (1881–87).
- Keystone workRecords (~6): What Men Live By; Where Love Is, God Is; Two Old Men; How Much Land Does a Man Need? (record exists → fill); Ivan the Fool; Three Hermits.
- Keywords: Посредник / народны* издани* / лубочн* / Сытин / Чертков / для народа / дешев* издани* + tale titles.
- Stop: one session; 1903–06 late tales → notCovered; What Is Art? via its existing dive.
- Mode: plain theme-dive (NOT --novel, NOT --cluster), in-session interactive; fan-out sweep; medium visuals.

**Session 1 outcome (all phases complete):**
- Sweep: 777 anchor-hit letters triaged in 3 parallel lanes (Toms 63–64, 85–87 Chertkov, late/diaries); per-tale Tom 25 «История писания» commentary mined (32 works); 66 extracts via extract_tei.py --choice=reg --notes=auto.
- Completeness loop (once): added the Цветник preface (Tom 26) after the Zheltov letter named it.
- Outputs: dossier.yaml (50 evidence rows, 23 entities, 12 visuals, 8 triangulations, 6 workRecords incl. 2 corrections to the existing How Much Land record), index.md (+ generated index.html), draft note (draft: true).
- Gates: verify_quotes.py 50/50 PASS (exit 0); opus verifier — all 10 checks PASS, 2 minor issues found and fixed (facsimile localPath zero; stray .omc telemetry dir).
- Marquee finding: the What Is Art? footnote (1898) silently condemns the tales; the 24 Oct 1910 grading letter (PSS 82, № 278) puts nine of them in Tolstoy's own top grade — unreconciled, and uncited in anglophone scholarship.
- Key needsReview: Pobedonostsev instigation not anchored in the Tom 25 apparatus extract; 60,000-vs-600,000 print-run arithmetic on the 1885 Sytin transfer.
