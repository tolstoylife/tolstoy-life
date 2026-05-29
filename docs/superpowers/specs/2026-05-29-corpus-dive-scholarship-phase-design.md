---
title: corpus-dive — "Scholarly context & gap-filling" phase — design
layer: reference
date: 2026-05-29
status: draft — design approved 2026-05-29; awaiting spec review
---

# corpus-dive — "Scholarly context & gap-filling" phase

Adds one new phase to the `corpus-dive` skill: after the primary evidence is locked, the dive
web-searches **conventional Tolstoy scholarship** and **related facts**, then triangulates its
own findings against the received view, fills knowledge gaps, and records a *secondary* layer on
top of the primary evidence. Supersedes nothing in the skill's primary-source pipeline — it is
purely additive.

> **Context.** This replaces the (now-shelved) nightly-runner direction: a `launchd`
> nightly-runner was designed and permission-de-risked on 2026-05-29, then deliberately
> shelved so dives stay human-present and interactive (web tools available again).

## Why

A primary-source dive currently stands alone — it never asks how its findings sit against the
established scholarship, and it has no step for filling factual gaps from outside the corpus.
This phase closes that: it lets the dive say *where the corpus confirms, complicates, or
contradicts the received view*, situate itself in the scholarly conversation, and catch themes
or sources that scholars treat as central but the corpus sweep missed.

## Decisions (settled 2026-05-29, via brainstorming)

| Question | Decision |
|---|---|
| Purpose | **All three:** (1) triangulate findings — confirm / complicate / contradict the conventional view; (2) contextualize — situate the dive in the scholarly conversation; (3) completeness — catch what the sweep missed. |
| Sourcing rigor | **Prototype-light.** These dives are *research-as-prototypes*, looser than the wiki. Primary-source rigor (verbatim RU, TEI id, PSS Tom/pages, byte-fidelity) is **unchanged**. Secondary/scholarly claims are drafted from model knowledge + web search and **footnoted when there's a clear source**; genuine uncertainty → `needsReview`. **No** adversarial citation-verification gate. |
| Structure | **Approach A — one dedicated phase**, inserted between Extract (Phase 2) and Synthesize. Gives the scholarship round a clear identity and the completeness loop-back a home. |
| Scholarship scope | **Both, English-first.** Primarily English-language Tolstoy studies (audience + accessibility); Russian-language scholarship when authoritative or decisive. Footnote whichever is the clear source. |

## The new phase — "Scholarly context & gap-filling"

Inserted **after Phase 2 (Extract & verify finalists), before Synthesize.** Phases renumber:
the new phase becomes **Phase 3**; Synthesize → 4, Verify → 5, Handoff → 6. Cross-references in
SKILL.md to "Phase 4 verifier" / "Phase 5" / "the Phase 0 contract" are updated to match.

Inputs: the verified finalists/evidence from Phase 2, the Phase 0 scope contract, and the running
dossier (`notCovered`, `needsReview`, `entities` with `vaultStatus`).

1. **Assemble claims & gaps.** List the dive's main findings/assertions from the extracted
   evidence. Collect the open gaps from the dossier: `needsReview` items, `notCovered`
   candidates worth a quick check, entities with `vaultStatus: missing | stub`, and factual
   unknowns (identities, dates, event context) flagged during extraction.
2. **Web sweep — scholarship + related facts.** English-first (major biographers + academic
   Tolstoy studies), Russian when authoritative/decisive. Two intents:
   - **Scholarship**: the received view on the theme and on the specific findings — who the key
     voices are, what the consensus is, whether mainstream work addresses these findings.
   - **Gap-filling facts**: resolve the assembled factual unknowns and surface related info the
     corpus sweep lacked.
   Capture each source as `author, year, work/title, url`. Use a lightweight fan-out (the
   `deep-research` search-and-triage pattern) — **not** the full adversarial harness.
   This is distinct from Phase 2's *visual-materials* web sweep (images), which stays where it is.
3. **Triangulate.** For each major finding, classify it against the conventional view:
   - `confirms` — scholarship agrees;
   - `complicates` — adds nuance / partial agreement;
   - `contradicts` — the primary source pushes back on the received narrative (**the high-value
     case**).
   Each entry ties to its primary `evidenceRef`, and — *where there is a clear source* — a
   footnoted secondary citation.
4. **Completeness loop (bounded).** Ask: what do scholars treat as central to this theme that the
   corpus sweep didn't surface? If a real gap emerges (a key text, letter, episode, sub-theme),
   loop back for **one bounded** targeted Phase 1→2 mini sweep+extract for it, then return. A gap
   that can't be resolved in-scope → `notCovered` / `needsReview`. The loop runs **once** per
   dive, not open-endedly.

## Ripple changes

### index.md
New section **"Scholarly context"**, placed after *"Where the theme clusters"* and before
*"Material not covered"*. It states the received scholarly view on the theme, then names exactly
where the corpus evidence **confirms / complicates / contradicts** it. Discipline:
- Platform voice — simple, factual, **minimal editorial**.
- **Attribute, don't assert**: "Bartlett (2010) describes… ; the diary entry of 4 May 1898 shows…"
- Markdown footnotes for clear secondary sources (serve.py renders `index.md` → HTML; footnote
  rendering to be confirmed at implementation — see Open questions).
- Working-English translations stay labelled, as elsewhere.

### dossier.yaml
New top-level `scholarship:` block (peer to `evidence` / `entities` / `visuals`):
```yaml
scholarship:
  summary: >          # short prose: the received view on this theme, English-first
  triangulation:      # one entry per major finding compared to scholarship
    - evidenceRef:     # id from the evidence ledger
      conventionalView: # what mainstream scholarship holds on this point
      relation:        # confirms | complicates | contradicts
      source:          # author, year, work, url — when there is a clear one (else omitted)
```
- Secondary sources also accumulate in the existing `references.background`.
- The existing `contradictions` field is **kept distinct** — it remains for *intra-corpus*
  (primary-vs-primary) conflicts, not scholarly triangulation.
- `notCovered` / `needsReview` / `entities` are updated as gaps are filled or newly surfaced.

### Verify phase (light — prototype rigor)
The verifier additionally checks: scholarly claims are *attributed* (not asserted as fact);
footnotes name a real source wherever one is claimed; the "Scholarly context" section holds the
minimal-editorial voice; `scholarship.triangulation` entries reference valid `evidenceRef`s.
It does **not** demand byte-fidelity on secondary sources.

### Model routing (add rows to the routing table)
| Phase / task | Tier |
|---|---|
| Scholarship/gap web search + relevance triage | sonnet |
| Factual gap-fill lookups | sonnet / haiku |
| Triangulation + "Scholarly context" synthesis | opus |

### Modes
- **Interactive (the norm now):** escalate genuine editorial judgment to the user as elsewhere.
- **`--auto`:** the phase still runs (web is available); footnote what's clear, defer judgment
  calls to `needsReview`, never block.

## Out of scope (YAGNI)
- No adversarial citation-verification gate.
- No dependency on the full `deep-research` skill (borrow its search pattern only).
- No wiki-grade source quoting — these are research prototypes.
- No change to the primary-source pipeline (Sweep / Extract / byte-fidelity).

## Open questions to settle at implementation (not blockers)
1. **Footnote rendering** — confirm `docs/serve.py` renders Markdown footnotes in `index.md → .html`;
   if not, fall back to an inline `[source: …]` convention or a References-list anchor.
2. **Phase renumbering** — mechanical; update every in-doc "Phase N" cross-reference when the new
   phase is inserted.
3. **Existing dives** — whether to backfill a "Scholarly context" section into the already-written
   dives (`copyright-renunciation/`, `crisis/`) is a separate, later call; this spec only changes
   the skill going forward.
