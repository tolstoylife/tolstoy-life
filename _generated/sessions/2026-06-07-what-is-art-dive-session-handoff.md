# Handoff — corpus work-dive: *What Is Art?* (`1897-1898-what-is-art`)

**Status: COMPLETE this session (Phases 0–7).** A fresh agent does **not** need to redo anything. This doc is for (a) the optional commit/push, and (b) the follow-up work the dive itself queued.

## What was done

A `corpus-dive` work-dive on Tolstoy's *What Is Art?* (Что такое искусство?, 1897–1898), run interactively from the scope handoff at `_generated/sessions/2026-06-07-what-is-art-dive-scope-handoff.md`. All outputs live in `docs/research/1897-1898-what-is-art/`:

- `index.md` (+ rendered `index.html`) — full spine: Key findings, Genesis & composition (with the people), What the work says (18 keystones), the **Mainstream-aesthetics-vs-Tolstoy concept/philosopher map** (the §3 centrepiece), Redactions, Publication/censorship (keystone), Reception, Scholarly context, cluster cross-links, the author's verdict, Method, References.
- `dossier.yaml` — 23 byte-faithful evidence rows, 18 entities (routing map), 7 visuals, 5 scholarship triangulations, a workRecord proposal, a coverage ledger, contradictions, notCovered, needsReview.
- `extracts/` (152 files, committed, PD-only) — the Tom 30 cluster + 151 per-file diary/letter extracts + the agent deliverables (`_deepread.md`, `_concept_map.md`, `_witness_sweep.md`, `_scholarship.md`, `_visuals.md`) + `_recover_notes.py` (the one-off helper that recovered the self-condemnation footnote).
- `visuals/` (5 PD images, **git-ignored** cache).
- `session-log.md`, `_verifier-report.md`.
- Draft dev-blog note: `website/src/posts/notes/2026-06-07-what-is-art.md` (`draft: true`).

**Verification:** `verify_quotes.py` PASS 23/23; opus verifier verdict CLEAN-WITH-NOTES — both should-fix items + 1 nit fixed and re-checked.

## Don't re-derive these decisions

- **Slug = composition window** `1897-1898-what-is-art`; the 1882–1896 art-essays are *preparatory redactions*, not the work's window (confirmed from Gudzy's PSS Tom 30 history).
- **Self-condemnation footnote** ("свои художественные произведения я причисляю к области дурного искусства…") is an inline `<note>` that `extract_tei.py` **strips**; recovered into `extracts/v30_027_203_notes.txt` via `extracts/_recover_notes.py`. Don't re-hunt it.
- **Taneyev the composer cannot be tied to the treatise** via this corpus; the «А. С. Танеев» letters are to a court official. The dive deliberately does **not** assert a tie.
- **Church reaction is thin** — the 1901 excommunication was driven by *Resurrection* + the religious works, NOT this treatise. Do not overstate it.

## Follow-up work the dive queued (for a *later, separate* step — not this dive)

1. **Wiki/works ingestion** (the separate human-in-the-loop LLM-wiki-ingestion method, NOT corpus-dive): the dossier `entities` map is the plan. Priority-1 missing pages: **Aylmer Maude, Nikolai Grot, Vladimir Stasov**, the concept **art as infection (заражение)**, and the **What Is Art? work record** (apply the `workRecord` proposal — note the `publishedInRussiaDuringLifetime: false → true` correction and OS→NS date finalization).
2. **`needsReview` items** (`dossier.yaml`): an `extract_tei.py --notes=inline` tooling enhancement (authorial-footnote recovery); a named scholarly backer for the "Tolstoy flattens Kant/Schopenhauer" charge; Stasov's *published* reaction (archival); a PD Russian 1898 first-edition title page.
3. **`notCovered`**: variant-draft collation (`v30_303_426`); chapter-by-chapter censored-vs-uncensored collation; a Maude translator/edition follow-up.

## Optional: commit + push (Johan pushes himself — provide, don't run)

The dive touches **two repos** (parent + the `website` submodule for the draft note). HTML is git-ignored. Suggested sequence (per `reference_push_command_sequence`): submodule first, then parent pointer bump, then parent. Draft the exact commands for Johan; do **not** run `git push` / `gh pr create`.

## Suggested skills for the next session

- **LLM wiki ingestion** (per memory `feedback_llm_wiki_ingestion`) — to turn the dossier `entities`/`workRecord` into vault pages. Mind `reference_vault_transliteration_gotcha` (loose-match surnames before marking `missing`).
- `end-of-day` — if wrapping the work day (LOG/AGENTS/TODO/memory + commit).
- `corpus-dive` only if starting a *different* work/theme — this one is done.
