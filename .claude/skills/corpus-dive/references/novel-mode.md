# corpus-dive — novel mode (`--novel`)

This file governs a dive run with `--novel`. Read it once at the start of such a dive and treat it
as an **overlay on the work-dive spine in `SKILL.md`**: every hard gate, boundary, and phase still
applies; this file only re-weights *where the effort goes* and adds three index sections. It does not
replace `SKILL.md` — read both.

`--novel` is a **work-subject dive** (the subject is one work, so the dive carries a `workRecord:`
block) tuned for a long narrative work — a novel or a substantial novella. The work-dive spine was
tuned on the non-fiction treatises, where the textual layer is exhaustive (~12–14 keystone passages,
chapter by chapter). For a 300–500-page novel that is both wrong and impossible: the genesis,
redaction history, and reception are where a novel's depth lives, and the text is read by *locating*
its pivotal scenes, not marching through it. This overlay is the distillation of three flagship
novel-dives that re-balanced the spine by hand and converged on the same shape (see *Reference
implementations*).

**One run at a time.** Never start an `--auto` pass while an in-session run of the same dive is
live — a concurrent `--auto` run on *Resurrection* committed a duplicate narrative mid-session. Pick
one mode and finish it.

## What `--novel` changes (overlay on the work-dive spine)

| Layer | Work-dive (base) | Novel mode |
|---|---|---|
| **Close-read of the text** | exhaustive, chapter-by-chapter keystones | **Light.** Extract the full text ONCE; grep to *locate* the pivotal scenes; close-read 3–5 (one centrepiece quoted in full); a thematic map carries the rest. |
| **Genesis & composition** | standard section | **Heaviest layer.** The composition-years diaries + letters sweep (work-mood AND the named network) and the «История писания» commentary mine get the most budget. |
| **Redactions** | when present | **Sample, don't collate.** Summarise the redaction history; extract the single *keystone* variant as a first-class text only when it changes the reading. |
| **Reception** | Russian/Church first, incidental | **Heaviest reception.** Censorship-as-reception earns a dedicated pass. The era flexes (see *Flex*) — do not assume a living-author ban. |
| **Characters / prototypes** | n/a | **New standing section** → routes `character` (+ `prototypes[]`), `person`, and `group` entities. |
| **Themes** | folded into "what it says" | **Promoted to its own section.** |
| **Marquee question** | n/a | **New standing section.** The dive's central contested claim is stated up front and *tested as a hypothesis* (`confirms` / `complicates` / `extends`). |
| **Visuals** | light default | **Heavy** four-channel fan-out is the default for a canonical novel with a rich illustration record. |

## Phase-by-phase overlay

**Phase 0 — Scope.** Pin the work-subject contract exactly as the base requires (the PSS Tom(s)
holding the work and each redaction; the composition window; the path to the `works/` record — or,
when no record exists yet, the path it *should* live at: **most un-dived novels have no `works/`
record**, so the `workRecord` is a record-*creating* proposal from scratch, not a fill — don't stall
hunting for a record that isn't there). Additionally: (1) **name the marquee question** — the one
contested claim this dive will test, framed as a hypothesis rather than discovered late. For the
doctrinal late works it is usually a **causal** claim (did the communion scene cause the
excommunication); for the early/aesthetic works it is more often **interpretive/developmental** (is
this the pivot where a lifelong thesis first appears). Both are valid marquees — don't force a causal
claim onto a work that has none. (2) set **visuals intensity** (heavy is the novel default; drop to
light only if the illustration record is thin);
(3) **flag any companion text** (an afterword, epilogue, or framing essay the PSS catalogues
separately) — it becomes a *second* `workRecord` proposal (see *Flex*).

**Phase 1 — Sweep.** Shift the budget to the **composition-years witness sweep** (the base already
defines it). The novel's *title* rarely appears in the diaries, so do **not** lead with a title grep —
sweep the composition window's diaries + letters for two things: Tolstoy's own work-mood (strain,
urgency, self-understanding while writing) and **the people around the work** (visitors,
correspondents, named draft-readers, conversation partners), surfacing each as a `person` entity. The
always-on post-1880 letter pass still runs.

**Phase 2 — Extract & close-read.** This **replaces** the base "read the work's own text deeply,
chapter by chapter." Instead:
1. Extract the full text **once** — `extract_tei.py --choice=reg --notes=auto` (every Prophet-period
   novel is pre-1918; the flag is non-negotiable).
2. **Locate** the pivotal scenes by grepping the extract for the marquee threads and the keystone
   moments.
3. **Close-read 3–5 scenes.** One is the **centrepiece**, quoted in full with a working-EN
   translation (the communion scene in *Resurrection*; the doctrine chapters in *Kreutzer*; Hadji
   Murat's death). The other 2–4 are read more lightly.
4. **Map the rest thematically** — do not transcribe the whole novel.
5. Add the **censorship-variant / keystone-redaction text** as a first-class extract *when it exists*
   and changes the reading (*Kreutzer*'s lithographed 8th redaction did; *Hadji Murat*'s fuller
   pre-censorship Nicholas-I chapter is the open follow-up).
6. **Source-research sub-layer (optional).** For a *historically sourced* work — built from an
   archive rather than invented — add a genesis sub-step that traces the source campaign (*Hadji
   Murat*'s 82-item «Список источников» and the Stasov / Grand-Duke / Tiflis-archive network). Most
   Tolstoy fiction has no such layer; add it only when the evidence shows one.

**Phase 3 — Scholarly context & reception.** Unchanged in mechanism (ground in the project before the
mainstream; attribute, don't assert; `confirms`/`complicates`/`contradicts`/`extends` triangulation).
Two novel emphases: run the **reception pass heavy**, and **test the marquee hypothesis here** against
the scholarship. **Reception flexes by era** — see *Flex* (for an uncensored early work, "heavy"
reweights toward **literary-critical** reception, not censorship-as-reception).

**Phase 4 — Synthesize.** Build the novel spine below. Emit the new entity types in the dossier
(`character` + `prototypes[]`, `group`, and the companion-text second `workRecord` where applicable).

**Phases 5–7 — gates unchanged.** `verify_quotes.py` exit 0 before the verifier; the separate-pass
opus verifier (it additionally checks the `workRecord` proposals, the `coverage` honesty, the
bare-voice standing sections — and, for novels, that `character`/`group`/`person` routing is correct
and `prototypes[]` certainty is not over-claimed); Phase 6 research handoff (+ `run-report.md` under
`--auto`); Phase 7 `handoff`-skill session compaction.

## The novel index spine (realized across all three runs)

Insert each section where the narrative wants it; drop and log in `coverage` any the evidence can't
support (never pad). The marquee section's *placement* flexes — early (right after *Why this matters*,
as in *Hadji Murat*) or mid-spine (after *Publication & censorship*, as in *Resurrection* and
*Kreutzer*) — pick what the argument needs.

1. **Key findings** — tight bulleted exec-summary; no new claims.
2. **Why this matters**
3. **The marquee question (hypothesis tested)** — state the contested claim, stage the evidence
   (verbatim RU + working-EN + TEI id / PSS Tom), report the outcome as `confirms` / `complicates` /
   `extends`.
4. **Genesis & composition** *(heaviest)* — the seed; the gestation / redaction history; **the people
   around the work**; + the optional **source-research** sub-section.
5. **What the work says** — the centrepiece (quoted in full) + 3–5 pivotal scenes (mapped lightly).
6. **Redactions & textual history** — sampled; the keystone variant first-class when it earns it.
7. **Publication, censorship & translation/afterlife**
8. **Characters & prototypes** *(new)* — see below.
9. **Themes** *(promoted)*
10. **Reception & afterlife** — the Russian society & church reaction first, then wider influence.
11. **Scholarly context** — a divergence map, not corroboration.
12. **Where the material clusters** — the genre tables (diaries / letters / works & commentary).
13. **The author's later verdict**
14. **Material not covered** · **Visual & manuscript record** · **Method** · **References**

## Characters & prototypes (the entity routing)

Apply the wiki-schema v1.4 **tiering rule** (`website/schema/wiki-schema.md` → *Character*): mint a
standalone node only for a figure that is **principal/titular**, carries a **documented or attributed
prototype**, or **recurs across works**. Everyone else folds into the work's overview prose or a
principal's page; record borderline calls in `needsReview`.

Route by **what the figure actually is** — the leads are *not* always fictional:
- **Fictional figure** → `wikiType: character`, with a structured `prototypes[]` edge
  (`person` slug-or-`""` · `name` · `basis` ∈ author-stated/autobiographical/editorial/scholarly/contemporary
  · `certainty` ∈ documented/probable/conjectured · `note` · `sourceId`). Never flatten a conjecture
  into a fact (Levin ↔ Tolstoy is `autobiographical` + `probable`, never `author-stated`).
- **Historical person appearing as themselves** → `wikiType: person`, **not** `character`. *Hadji
  Murat*'s Nicholas I, Shamil, Vorontsov, and Loris-Melikov are `person`; only the invented Butler and
  Marya Dmitrievna are `character` — a far smaller `character` blast radius than the wholly-invented
  casts of *Resurrection* and *Kreutzer*. The same holds for the **middle case** between those poles: a
  *single* real figure appearing as himself inside an *otherwise wholly-fictional* cast still routes
  `person`, not `character` — *Father Sergius*'s Nicholas I (the censored love-affairs strand) is
  `person`, while Kasatsky/Sergius, Mary, and Pashenka remain `character`. The presence of one
  historical walk-on does not make the cast "historical"; route each figure by what it is.
- **Real-world people / sect / ethnic group** → `wikiType: group` (the Doukhobors, the Shakers, the
  Caucasus highlanders), distinct from a `concept` (an idea) or `institution` (an organisation).

The reverse life→fiction direction is left to Obsidian backlinks — there is deliberately no
reciprocal field on `person`.

## Flex, don't hard-code

The three runs surfaced variations the mode must **flex** to, not bake in:

1. **Principals are not always fictional** — route each lead by what it is (see above). Do not assume
   a fictional protagonist.
2. **Companion text → its own record.** A separately-catalogued afterword/epilogue gets its **own**
   record-creating `workRecord` (`relatedWorks: companion`), mirroring the PSS. *Kreutzer*'s Afterword
   did. Handle a work-with-companion-text as a **two-record proposal**.
3. **Reception flexes by era.** Observed shapes (not exhaustive): a **living-author ban** (*Kreutzer*,
   1889 — Pobedonostsev / Feoktistov); **excommunication-adjacent** (*Resurrection*, 1901);
   **posthumous state/dynasty censorship** (*Hadji Murat*, 1912 — `bans[].scope: passages-cut`); and —
   the **pre-Prophet / early-fiction default** — **acclaimed legal publication, censorship not a
   factor** (*The Cossacks*, the early fiction), where reception means **literary-critical** reception
   and `bans: []`. Don't default the section to a living-author ban, and don't force a censorship frame
   onto an uncensored work.
4. **Genesis may carry a source-research sub-layer** — only for historically-sourced works (see
   Phase 2.6). Most fiction has none.
5. **Redactions: sample, don't collate** — but extract the single keystone variant first-class when it
   changes the reading.
6. **The marquee is a hypothesis, not a foregone conclusion.** Report what the evidence actually does.
   The three runs each produced a *real* outcome this way, not a confirmation of a prior.

## Reference implementations

The first three were run **by hand**, applying this re-weighting manually; the mode codifies what they
share. *Father Sergius* (2026-06-09) was the **first run under the codified mode** — a validation, not
a derivation — and it held up with no overlay change needed. Read the nearest analogue when scoping a
new novel-dive.

- `docs/research/1889-1899-resurrection/` — wholly-invented cast; marquee = **`complicates`**
  (communion → excommunication, with the Pobedonostsev-caricature axis). Pre-schema-v1.4 run: its
  characters were routed as `concept` stopgaps and later re-routed.
- `docs/research/1887-1889-the-kreutzer-sonata/` — companion-text precedent (the Afterword's own
  record); marquee = **`extends`** (Tolstoy owns the doctrine but withholds the modality —
  ideal-not-rule).
- `docs/research/1896-1904-hadji-murat/` — first to apply v1.4 natively (historical principals →
  `person`; Butler/Marya Dmitrievna → `character`); heaviest genesis (the source-research campaign);
  posthumous passages-cut censorship; marquee = **`extends`** (the *What Is Art?* contradiction was
  lived, not reconciled).
- `docs/research/1890-1898-father-sergius/` — **the mode's first validation run** (above three
  *derived* it; this one ran under the codified overlay). Wholly-fictional cast with one historical
  walk-on → the **person-in-a-fictional-cast middle case** (Nicholas I, the censored love-affairs
  strand → `person`); marquee = **`confirms` + `extends`** (the driver is слава людская / vanity, not
  lust; the cure is anonymity, not asceticism); finished 1898 for the Doukhobor emigration fund.

The written proposal that specced this mode: `docs/research/1889-1899-resurrection/novel-dive-proposal.md`.
