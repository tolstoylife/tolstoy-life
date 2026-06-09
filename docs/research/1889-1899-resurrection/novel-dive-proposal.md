---
layer: reference
lastUpdated: 2026-06-08
tags: [research, meta, corpus-dive, novel-dive, skill-proposal]
---

# Proposal: a `--novel` mode for `corpus-dive`

Written after running the *Resurrection* dive (the first flagship novel-dive). The handoff asked: build a new `novel-dive` skill, or a `--novel` mode of `corpus-dive`? **Recommendation: a `--novel` MODE of `corpus-dive`, not a standalone skill** — it shares all the machinery (extraction, `verify_quotes`, the visuals sweep, render, the verifier, the handoff) and differs only in spine *weighting* and two extra sections. One maintained pipeline; the hard gates stay identical.

This is a written proposal, not a built skill. Building it (via `skill-creator`) should wait for a go, because it touches a schema question (below) that needs a decision first, per the project's explain-schema-before-editing rule.

## What the work-dive spine got wrong for a novel — and what the Resurrection run actually did

The work-dive spine was tuned on the non-fiction treatises, where the textual layer is exhaustive (~12–14 keystone passages, chapter by chapter). For a 500-page novel that is both wrong and impossible. The Resurrection run re-balanced it by hand; the moves that worked:

| Aspect | Work-dive (non-fiction) | What worked for the novel |
|---|---|---|
| **Textual layer** | Exhaustive chapter-by-chapter keystone read | **Light.** Extract the full novel ONCE; grep to *locate* pivotal scenes; close-read only those (here: communion centrepiece + 3 scenes). A thematic map carries the rest. |
| **Centrepiece** | One keystone among many | **One close-read anchor** (the communion scene), treated like the title-saga centrepiece in the Law-of-Violence dive — the scene to quote in full. |
| **Genesis & composition** | Standard section | **Heaviest section.** The composition-years diaries+letters sweep + the «История писания» commentary mine got the most agent budget. This is where a novel's depth lives. |
| **Redactions** | When present | **Rich.** The six-redaction history + the censorship-variant text were first-class (here: the centrepiece's late emergence in the 3rd redaction; the wholesale «Нива» cut). |
| **Reception** | Russian/Church first, incidental | **Heaviest reception.** Censorship-as-reception + the excommunication causal question carried a dedicated pass. |
| **Characters / prototypes** | n/a | **New standing section.** The real-life prototypes (Koni's Rozalia Oni; Toporov = Pobedonostsev; Nekhlyudov's autobiographical core) — a routing source for `person` entities. |
| **Themes** | Folded into "what it says" | **Its own section** (guilt, repentance, resurrection/awakening, justice, land, Church). |

## Concrete changes a `--novel` flag would make

1. **Phase 1 (Sweep):** shift budget to the composition-years witness sweep (diaries + letters for genesis & the people around the work). The novel's title rarely appears in the diaries — sweep for work-mood and the named network, not a title grep.
2. **Phase 2 (Extract):** replace "read the work's own text deeply, chapter by chapter" with **"extract the full text once; locate and close-read 3–5 pivotal scenes; map the rest thematically."** Add the censorship-variant text as a first-class extract.
3. **Standing sections:** add **"Characters & prototypes"** and promote **"Themes"** to its own section. Keep "Genesis & composition" and "Reception & afterlife" as the two heaviest.
4. **Marquee-question framing:** when the dive carries a contested causal claim (here, communion→excommunication), treat it as a **hypothesis to test** and report `confirms` / `complicates` / `extends` — this surfaced a real finding (`complicates`, with the Pobedonostsev-caricature axis) instead of confirming a prior.
5. **Visuals:** default to a **heavy** four-channel fan-out for canonical novels with a rich illustration record (Pasternak here → 85 distinct items). The work-dive default is light.
6. **Hard gates unchanged:** `--choice=reg`, `verify_quotes.py` exit 0, the bare voice, no vault writes, the record-creating `workRecord`, the separate-pass verifier.

## A schema decision the novel-dive forces (needs a go before building)

> **Update 2026-06-09 — RESOLVED (gate cleared).** Decided **option (a)** with the reader: added a `character` wiki type (minted by a *tiering rule* — principal, documented prototype, or recurs across works) carrying a structured `prototypes[]` field (`person` + `name` + `basis`/`certainty` evidence enums — the fiction→life edge), **and** a `group` type for real-world peoples/sects (Doukhobors, Shakers). The reverse direction is left to Obsidian backlinks (no field added to `person`). See `website/schema/wiki-schema.md` v1.4; the *Resurrection* and *Kreutzer* dossiers were re-routed off the `concept` stopgap. The `--novel` skill should emit character rows with `wikiType: character` (+ `prototypes[]`) and sects with `wikiType: group`. Gate (2) — standalone-skill-vs-mode — is still open and belongs to the build session.

Fictional **characters** (Maslova, Nekhlyudov) have no home in the 10-type wiki schema — the Resurrection dossier routed them as `concept`, which the verifier flagged as a stopgap that will mis-shape their eventual pages. Before the `--novel` mode is built (and before these entities are ingested), decide one of:
- **(a)** add a `character` wiki type (and possibly a `group` type — the Doukhobors are a people/sect, also routed as `concept`); or
- **(b)** fold a novel's principal characters into the work's own wiki page rather than giving them standalone pages.

This is the one genuinely new design question the novel format raises. Everything else is re-weighting.

## Recommendation

Build `corpus-dive --novel` via `skill-creator` after: (1) a decision on the character/group schema question; (2) a go on the standalone-vs-mode call (recommend mode). The Resurrection dive is the reference implementation — the spine above is what actually worked on a real 500-page novel, not a guess.
