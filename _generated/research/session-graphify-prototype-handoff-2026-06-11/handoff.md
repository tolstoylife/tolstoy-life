# Handoff — PLANNING session: Tolstoy-Graphify-Spike → full prototype

**Date:** 2026-06-11 · **From:** Graphify-evaluation continuation session (LightRAG e2e verify + planning-trail reconstruction)
**Next session type:** brainstorming + planning. **PLAN ONLY — no execution.** Per memory `feedback_plan_then_execute_separately`: the session ends when the plan is approved and saved; execution happens in a *later* fresh session. Plan approval ≠ "go".

## The ask

Turn `/Volumes/Graugear/Tolstoy-Graphify-Spike/` into a **full prototype of the Tolstoy production setup** — same folder structure as `website/src/` (wiki/ + works/ pages, Obsidian vault) — but populated **from the Graphify graph** instead of the deliberate human-in-the-loop ingestion used for production. A sandbox that "simulates and tests how the live site will function" (Johan's phrase).

This picks up **thread 2** of the 2026-06-10 brainstorm, which was voiced but never planned. Johan's original words (session `192dc3f9`, answer at line 164):

> "Perhaps we should divide the förstudie (Feasibility study) research/ folder to the same folder structure as the production website/src/? This would be a good way to simulate and test how the live site will function. Perhaps we even should make a clone of the current repo to test this out? I'm here also thinking of instead of ingesting the works to LightRAG, use graphify to create a graph and Obsidian vault from that."

## Prior artifacts (reference, don't re-derive)

- **Spike plan (executed):** `~/.claude/plans/before-doing-another-corpus-dive-rosy-gray.md` — the three-backend evaluation spike, corpus/cost figures (~1.5–2M tokens, ~210 files), workspace layout, and an "Execution-session notes" section with the verified CLI shape: `cd ~/Projects/graphify-8 && uv run graphify extract <path> --backend claude-cli [--out DIR]` then `graphify export obsidian` (vault export is a deterministic no-LLM post-step). Its follow-up bullet — "decide where a Graphify-derived vault/graph fits alongside LightRAG, and whether to fold a `_staging`-style Karpathy ingestion folder into the regular workflow" — is part of what this planning session resolves.
- **Spike verdict:** `_generated/research/session-graphify-spike-2026-06-10/index.html` + memory `project_graphify_spike_verdict` — KEEP the Opus auto-vault as a **complementary nav aid** (cross-dive "surprising connections" + community map), **NOT a typed entity store**; backend = claude-cli ($0 marginal on subscription); Ollama leg infeasible on the 24 GB M4.
- **Brainstorm transcript:** session `192dc3f9-168a-4c50-a1ad-f5af5adcaea1` (2026-06-10). Three threads emerged: (1) works-timeline index page — deferred, still open; (2) mirror-`website/src/` sandbox — **this session's subject, never planned**; (3) Graphify spike — done. Also on record there: Johan's idea to rename the ingestion folder `_staging` → `_raw` (Karpathy-style); the spike plan dropped the rename for the *production* folder, but it's a live option for the prototype workspace.

## Current state (verified 2026-06-11)

- **Workspace** `/Volumes/Graugear/Tolstoy-Graphify-Spike/` (NOT a git repo):
  - `_staging/` — the ingestion corpus: copy of `docs/research/` (all dives) + curated `wiki/` + `works/`.
  - `graphify-out-claude/graphify-out/` — **the Opus run, the quality benchmark**: 299 nodes / 398 edges / 15 named communities; `obsidian/` vault (315 notes incl. `_COMMUNITY_*` hub notes); `graph.json` (NetworkX node-link), `GRAPH_REPORT.md`, `graph.html`, `manifest.json`.
  - `graphify-out-haiku/graphify-out/` — Haiku comparison run (~540 notes, noisier).
  - `graphify-out-ollama/`, `ollama-validate-out/`, `pilot-out/` — Ollama leg remnants (infeasible on this hardware) + the calibration pilot; plus run logs.
- **Graphify tool:** `~/Projects/graphify-8` (v8, local checkout), run via `uv run graphify`. Unexplored capabilities flagged in the verdict: MCP serve, global graph, benchmark.
- **LightRAG (production Layer 2) verified e2e same day** — query + ingest + incremental sync all pass (TODO #1 closed, commit `c0d969f0`). It indexes only the 29 curated vault docs; **unaffected by and orthogonal to this prototype**. Nightly-cron sub-item still open (sync.py retry footgun noted in TODO.md #1).
- **Schemas the generated pages would target:** `website/schema/` — works schema **v9** (incl. the new `stage-ban` bans scope), wiki-schema **v1.4** (12 types incl. `character` + `group`). Frontmatter validator: `cd website && node .github/scripts/validate-frontmatter.mjs`.
- **Pending small decision from 2026-06-11 session:** recommendation to move the Opus `graphify-out/` to `_generated/graphify/` (gitignored) as the standing nav-aid home — **not yet acted on**; if the prototype workspace becomes its home instead, that recommendation is superseded.

## Open design questions the plan must answer

0. **Framing: throwaway or evolutionary prototype?** (clarified with Johan 2026-06-11) — this is a *prototype*, not another spike: the deliverable is a working model of the graph-populated site, not a verdict. Decide up front whether it's **throwaway** (built purely to learn, sandbox discarded after evaluation) or **evolutionary** (could become a standing preview/staging layer that regenerates as dives land). The answer reshapes Q1 (workspace shape) and Q7 (regeneration story).
1. **Workspace shape** — extend `Tolstoy-Graphify-Spike/` in place, or a true clone of the repo (Johan's original instinct)? Does the prototype get its own git repo? Mirror `website/src/` how literally — folder structure only, or a runnable eleventy build (the production site is Eleventy Excellent-based) so "simulate the live site" is real?
2. **Graph → page generation** — what does a `works/`/`wiki/` page generated from `graph.json` + the dive dossiers actually look like? Schema-conformant frontmatter or a looser prototype shape? Generator: deterministic script over `graph.json`+`dossier.yaml`, a claude-cli synthesis pass, or hybrid? How do the 315 auto-vault notes relate to the generated pages (same files? two layers?)?
3. **The verdict tension (must be named in the plan)** — the spike verdict says the graph is a nav aid, *not* a typed entity store; generating typed pages from it uses it as exactly that. The prototype should frame page generation as **the experiment that tests this boundary**, with explicit quality criteria for judging the result against hand-curated pages (the 29 curated vault docs are the natural control group).
4. **Isolation guarantees** — read-only on all sources; never points at production; output never flows back into `website/src/` (memory `feedback_llm_wiki_ingestion`: the curated vault grows by source-ingestion only). State this in the plan's "explicitly NOT" section.
5. **The deferred works-timeline index page** — the original 2026-06-10 ask; in the brainstorm it was noted it "would naturally become the `works/` index of that sandbox". Fold it in here or keep it a separate follow-up?
6. **Ingestion-folder convention** — `_staging/` vs `_raw/` naming for the prototype's Karpathy-style folder; and whether the pattern is worth folding into the regular workflow (the spike plan's open follow-up).
7. **Regeneration story** — corpus changes (new dives) → re-extract → re-export: full re-run vs incremental; backend claude-cli/Opus ($0); rough token/time budget per re-run (spike figures: ~1.7M input, 10–20 min).

## Constraints

- **Plan only** — end the session at an approved, saved plan (`~/.claude/plans/` auto-save; consider also copying into `_generated/` per the artifact convention if Johan wants it in-repo).
- **Schema/design changes need Johan's explicit nod before writing** (memory `feedback_explain_schema_before_edit`) — applies to any new page-shape or folder-convention proposals.
- Production repo zones untouched: `website/src/**` (incl. `_staging/`), `primary-sources/**`.
- No `git push` / `gh pr create` — committing in the Tolstoy repo is fine, pushing is Johan's.
- Hardware: 24 GB M4 — no local-LLM extraction legs (parked until ≥36–48 GB); claude-cli is the backend.
- Docs in English.

## Suggested skills for the next session

- `superpowers:brainstorming` — open with it; this is a design-exploration session (and what Johan will likely invoke himself).
- `superpowers:writing-plans` — to produce the implementation plan once the design settles.
- `eleventy-excellent` / `eleventy` — only if Q1 lands on a runnable site build.
- `obsidian-markdown` + `nice-permalinks` — if page templates / filename-permalink conventions get sketched in the plan.

## Verification for the planning session itself

1. Every open question above has a decided answer (or an explicit "deferred" with reason) in the plan.
2. The plan has an "Explicitly NOT in scope" section covering the isolation guarantees (Q4) and no-execution.
3. The verdict tension (Q3) is addressed with concrete quality criteria, not glossed.
4. Plan saved; session ends without executing anything.
