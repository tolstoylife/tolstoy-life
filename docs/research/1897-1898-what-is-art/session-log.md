# Session log — 1897-1898-what-is-art

## 2026-06-07 — initial dive (interactive, complete)

A single-session `corpus-dive` work-dive on *What Is Art?* (Что такое искусство?), run from the scope handoff at `_generated/sessions/2026-06-07-what-is-art-dive-scope-handoff.md`.

**Covered:**
- Phase 0–2: extracted the full Tom 30 treatise cluster (treatise, English-edition preface, Maupassant preface, 7 precursor art-essays, Gudzy's commentary) with `--choice=reg`; structural deep-read of all 20 chapters; concept/philosopher map (17 thinkers + 5 concepts); composition-window witness sweep (Tom 53 diaries + Toms 69–71/88 letters → 25 genesis passages, 8 people); light visual sweep (5 PD images).
- Recovered the self-condemnation footnote (stripped by `extract_tei.py`) byte-faithfully via `extracts/_recover_notes.py` → `extracts/v30_027_203_notes.txt`.
- Phase 3: scholarship + reception (English-first; Russian society/church first, with the caution that the 1901 excommunication was NOT driven by this work).
- Phase 4: `index.md` (+ `index.html`), `dossier.yaml` (23 evidence rows, 18 entities, 7 visuals, 5 triangulations, workRecord, coverage), draft note `website/src/posts/notes/2026-06-07-what-is-art.md`.
- Phase 5: `verify_quotes.py` PASS 23/23; opus verifier verdict CLEAN-WITH-NOTES (2 should-fix + 1 nit, all fixed: Chekhov anecdote anchored, `bans[].scope` → `passages-cut`, ё/е normalised).

**Key decisions:**
- Slug = composition window `1897-1898-what-is-art`; the 1882–1896 art-essays are preparatory redactions, not the work's window.
- workRecord proposes correcting the stub's `publishedInRussiaDuringLifetime: false` → `true` (censored serial 1897–98 + Tolstaya's 1898 Collected Works).

**Resume queue:** see `dossier.yaml → notCovered` and `needsReview` (variant-draft collation; Stasov's published reaction; a named scholarly backer for the "flattening" charge; Russian 1898 first-edition title page; OS→NS date finalization at ingestion; an `extract_tei.py --notes=inline` tooling enhancement).
