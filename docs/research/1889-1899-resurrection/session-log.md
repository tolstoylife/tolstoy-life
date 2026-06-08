---
layer: reference
lastUpdated: 2026-06-08
tags: [research, session-log]
---

# Session log — `1889-1899-resurrection` (novel-dive)

Append-only record of what each session covered. The dossier `coverage:` ledger is the
structured surface map; this is the narrative companion.

## 2026-06-08 — Session 1 (core, to checkpoint)

**Mode:** autonomous in-session, checkpoint after the core (genesis layer + communion
centrepiece + excommunication hypothesis), per the [scope handoff](../../../_generated/sessions/2026-06-08-resurrection-dive-scope-handoff.md).
This is a **novel-dive** — the work-dive spine re-balanced for fiction (genesis-heaviest,
textually light, communion centrepiece, excommunication as a hypothesis to test).

**Corpus surface verified.** Tom 32 (→vol01) holds the novel + variants; Tom 33 (→vol02)
the 6 redactions + the «История писания» commentary (`comments/v33_329_422`); Reply to the
Synod in Tom 34 (`works/v34_245_253` + `comments/v34_575_577`). Diaries Tom 53 (1898–99) +
Tom 54 (Feb–Mar 1901); letters Toms 71/72 + Chertkov 88/89. No `works/` record exists →
`workRecord` is record-CREATING.

**Mechanical extractions (all `--choice=reg --notes=auto`, clean, no drop-warnings):**
- `extracts/v32_003_445_Voskresenie.txt` (the novel, 8022 lines)
- `extracts/v32_471_505_Tsenzurnye_varianty.txt` (censorship variants)
- `extracts/v33_329_422_Istorija_pisanija.txt` (genesis commentary, 548 lines)
- `extracts/v34_245_253_Otvet_Sinodu.txt` (Reply to the Synod)
- `extracts/v34_575_577_Otvet_commentary.txt` (Reply commentary)

**Centrepiece located precisely:** the prison-church liturgy is **Part I, chs XXXIX–XL**
(extract lines 2355–2388), with the hammer-blow in **ch XLI** (the city's bells call people
«к присутствованию при таком же служении, какое совершалось теперь в тюрьме»). Confirms the
handoff's "~39–40".

**Core deliverables (6 subagents, each persisted to a file):**
- `extracts/_communion_centrepiece.md` — 9 verbatim passages + working-EN, byte-verified.
- `extracts/_censorship_variants.md` — 4 variant passages.
- `extracts/_genesis_commentary.md` — ~70 dated facts (Koni seed 1887; the 6 redactions;
  Doukhobor-funding engine; Marks/Нива contract + serialisation map; censorship by the
  numbers — 497 distortions / 10,240 words, only 25 of 123 chapters undistorted, chs XXXIX–XL
  cut WHOLESALE from Нива; Chertkov/Свободное слово; Pasternak illustrations; full prototypes
  table incl. Toporov = Pobedonostsev).
- `extracts/_sweep_diaries.md` — 18 hits, 5 full passages (the 17 Jul 1898 decision; the
  2 Nov 1898 immersion + 12,000 r.; the 18 Dec 1899 completion verdict).
- `extracts/_sweep_letters.md` — 20 candidates, 6 full (Marks contract 12 Oct 1898; censorship
  strategy 7 Nov 1898; fees→Chertkov routing 2 Mar 1899; Doukhobor ships).
- `extracts/_excommunication.md` — **verdict: COMPLICATES** (with an *extends* component).
  The Synod decree's indictment is doctrinally broad; the Eucharist is named but as the
  «последняя и высшая степень» (rhetorical climax), not the basis. The PSS editor names
  *Resurrection* as the «толчок» to PUBLISH a long-prepared act, and locates its sting as much
  in the **Toporov caricature of Pobedonostsev** as in the Mass scene. Tolstoy's own diary reads
  it as doctrinal/systemic («странное отлучение»). Connective fact: chs XXXIX–XL were cut
  entirely from Нива, so Russian serial readers never saw the communion satire.

**CHECKPOINT REACHED** — reader reviewed; approved the "complicates" framing and asked for a HEAVY visuals sweep. Continued autonomously.

## 2026-06-08 — Session 1 (continued, lighter layers → completion)

**Lighter layers (6 more subagents + 1 consolidator):**
- `extracts/_thematic_map.md` — 3 pivotal scenes (verdict error / land / ending) + thematic map, 7 byte-verified passages.
- `extracts/_redactions.md` — light redaction sampling; CONFIRMED the church service first appears in the 3rd redaction (Aug 1898) as two adjacent drafts.
- `extracts/_scholarship.md` — 7 triangulations / 14 refs; flags the money-total inconsistency (≈30k–34.2k secondary, NOT corpus-anchored — corpus fixes only the 12,000 r. advance).
- `extracts/_reception.md` — 12 sources; Russian/Church reception first; named RU press reviews = a gap.
- Visuals HEAVY 4-channel sweep → 90 files / 38 MB, deduped to **85 distinct** in `extracts/_visuals_consolidated.md` (19 Pasternak illustrations PD-usable; Repin 1901; Pobedonostsev; the censored-chapters autograph is request-only at ГМТ).

**Synthesis:** `index.md` (novel-dive spine, 12 figures embedded), `dossier.yaml` (31 evidence rows, 13 entities, 101 visuals, 7 triangulations, 17-field record-CREATING `workRecord` at `website/src/works/fiction/novels/resurrection/Resurrection.md`, 8-row coverage), draft note `website/src/posts/notes/2026-06-08-resurrection.md` (draft:true). Rendered via `serve.py --build-only`.

**Phase 5 — verify:** `verify_quotes.py` PASS (31/31 byte-verbatim). Independent opus verifier: **CLEAN-WITH-NITS** (0 blockers / 2 should-fix / 4 nits) → `_verifier-report.md`. Nits N-1 (Chekhov attribution) + N-2 (imperial-censor → «Нива» censorship precision) fixed in index.md and re-rendered. SF-2 (no `character` wikiType for Maslova/Nekhlyudov) → deferred schema decision (see `novel-dive-proposal.md`).

**Phase 6 — research handoff / work-orders:**
- *Entity work-order* (ingestion order): P1 — Resurrection (work), Excommunication-1901 (event), Koni, Doukhobors; P2 — Chertkov (present), Birukoff (present), Marks, Pobedonostsev, Pasternak; P3 — Maslova, Nekhlyudov, communion/Eucharist theme, Henry George. (13 entities; Chertkov + Pavel Birukoff already in the vault.)
- *Visuals work-order*: 66/85 PD-usable + cached; request-only = the ГМТ censored-chapters proofs (highest value), the 1899 «Нива» run, the «Свободное слово» editions.
- *Work-record work-order*: record-CREATING — propose the full `workRecord` block (high-confidence on dates/genre/censorship/excommunicationRelated; `relatedWorks` slugs need confirming — in needsReview).
- *Coverage*: covered = genesis, communion, publication/censorship, excommunication, visuals, scholarship; partial = reception (no named RU press reviews), redactions (sampled only).

**Novel-dive skill proposal:** written to `novel-dive-proposal.md` (recommend a `--novel` MODE, not a standalone skill; flags the character/group schema gap as the one new design decision).

### ⚠️ ANOMALY for the reader (needs a decision — NOT resolved autonomously)
A commit **`8fe5e056` "feat(corpus-dive): Resurrection … work-dive"** (Johan Edlund, Mon 8 Jun 20:22, now an ancestor of HEAD on `feat/corpus-dive-skill`) was made MID-SESSION and committed: this session's `extracts/` + `session-log.md` **plus a `resurrection-dive.md` (357-line OLD work-dive format) that THIS session did not author** (this session wrote `index.md`, the novel-dive). Result: two divergent narratives in one dive folder, sharing the same extracts. Likely a concurrent/automated `--auto` run on the same repo. **Not deleted** (committed work I didn't create). Decision for the reader: which narrative is canonical (recommend `index.md` — it is the novel-dive the handoff asked for) and whether to remove `resurrection-dive.md` + `resurrection-dive.html`. My new work (`index.md`, `dossier.yaml`, `_verifier-report.md`, `novel-dive-proposal.md`, per-entry extracts) is **uncommitted** pending this decision.

**STATUS: dive complete** (definition-of-done met) pending (1) the duplicate-narrative decision and (2) commit.

### Remaining after checkpoint (Phase 2-light → 7)
- Thematic map + the other pivotal scenes read lightly (courtroom/verdict, the prison, the
  land-giving) — NOT a chapter-by-chapter read.
- Redactions: sample (not collate all six) for the centrepiece scenes.
- Visual-materials sweep (Pasternak illustrations; Tolstoy ~1898–99 photos; censored Нива).
- Phase 3 scholarship + triangulation; reception pass (Church/press).
- Synthesize `index.md` + `dossier.yaml` (record-CREATING `workRecord`) + draft note; render.
- Phase 5 verify (`verify_quotes.py` gate + opus verifier); Phase 6/7 handoffs.
- THEN: the `novel-dive` skill proposal (what the re-balancing actually needed).

### needsReview / follow-ups noted
- Koni genesis letter is in Tom 64 (1887), outside the swept Toms — fetch for the seed quote.
- Targeted `Свободн`+`Воскресен` search in v88 for the explicit Свободное слово correspondence.
- Pobedonostsev's exact role (author/prime-mover vs reluctant) is contested between the Soviet
  PSS commentary and later accounts — report attributed, don't adjudicate.
- Decree text is partly web-sourced (Skvortsov 1901 via azbyka.ru); mark as such, not corpus-verified.
</content>
</invoke>
