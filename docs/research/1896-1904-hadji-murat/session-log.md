# Session log — Hadji Murat novel-dive (`1896-1904-hadji-murat`)

Append-only. Resume reads this + `dossier.yaml` `coverage:` + `notCovered:`.

## [2026-06-09] session 1 — full novel-dive (in-session, accept-edits)

**Origin:** the scope handoff `_generated/sessions/2026-06-08-hadji-murat-dive-scope-handoff.md`
(written at the end of the Kreutzer Sonata dive). Run as the third flagship **novel-dive**,
re-weighting the work-dive spine per `docs/research/1889-1899-resurrection/novel-dive-proposal.md`.

### Phase 0 — scope contract (confirmed by the handoff; not re-gated)

- **Question / marquee hypothesis:** Is *Hadji Murat* a **betrayal or a fulfilment of *What Is Art?***?
  Tolstoy wrote his most sensuous late fiction in secret (1896–1904) while publicly teaching
  (in *What Is Art?*, 1897–98) that art must be moral, universal, "infectious" of the highest
  religious feeling — and he called writing it self-indulgence («озорство»). Test the relation:
  `confirms` / `complicates` / `extends`. Standing secondary theme: the **mirrored** critique of
  state violence (Nicholas I ‖ Shamil), attributing the "anti-imperialist" label, not asserting it.
- **Corpus surface:** PSS **Tom 35** holds the work + an unusually full apparatus (the novella
  `v35_005_118`; working notes `v35_275_283`; variants `v35_284_556`; «История писания»
  `v35_583_629`; «История печатания» `v35_629_631`; **«Список источников»** `v35_631_633`;
  «Примечания» `v35_634_643`; glossary of mountaineer words `v35_644_647`; «Описание рукописей»
  `v35_648_666`). Genesis sweep: **diaries Tom 53–55** (1895–1904; 796 files present) and
  **letters Tom 69–75** (1896–1904; 1,960 files present). Tom 35 → local PDF `vol04`;
  diaries 53→vol19 / 54→vol20 / 55→vol21; letters 69→vol52 / 70→vol35 / 71→vol53 / 72→vol36 /
  73→vol37 / 74→vol54 / 75→vol38.
- **Spine re-weighting (novel):** textual layer LIGHT (extract once, scene-led close-read of the
  pivotal nodes + a thematic map — *Hadji Murat* is short, ~110pp/25 chs, so a fuller structural
  pass is affordable); **genesis & composition is the HEAVIEST** and carries an extra
  **SOURCE-research layer** (the «Список источников» + the Stasov archive requests — distinctive to
  this work); redactions rich (~10 across 1896→1904 — sample, don't collate the ~270pp variants);
  reception is **POSTHUMOUS** (first published 1912, Berlin uncensored / Russian censored — the
  Nicholas I material; posthumous state/Romanov-dynasty censorship, not a living-author ban);
  standing sections "Characters & prototypes" and "Themes".
- **Stop-condition:** the Definition-of-Done in the handoff §7.

### Schema update applied (supersedes the handoff's §0/§17 "concept stopgap" instruction)

The `character`/`group` wiki-schema gap the handoff flagged as "overdue (3 dives)" was **RESOLVED
2026-06-09** — `website/schema/wiki-schema.md` **v1.4** added the `character` type (with a
structured `prototypes[]` fiction→life edge: `person` + `name` + `basis`/`certainty` enums) and the
`group` type (the schema even names "Caucasus highlanders" as the worked `group` example). The
Resurrection + Kreutzer dossiers were re-routed off the `concept` stopgap. This dive applies v1.4:
- **Hadji Murat** → `character` (titular; tiering rule) with `prototypes[]` → the historical Hadji Murat (`person`).
- **Nicholas I, Shamil, Vorontsov, Loris-Melikov, Chernyshov** → `person` (historical figures who appear in the novel; reverse life→fiction edge via Obsidian backlinks).
- **Butler, Marya Dmitrievna** → `character` (invented; tiering-rule judgment calls → `needsReview`).
- **The Caucasus highlanders / mountaineers** → `group` (`groupType: ethnic-group`).

### Phases 1–7 — completed in one session (2026-06-09)

Dispatched 6 parallel subagents (write-to-file, return-a-line): work-text close-read (opus),
genesis-commentary mine (opus), genesis-diaries sweep (opus), genesis-letters sweep (sonnet),
heavy visuals sweep (sonnet), and the Phase-3 scholarship web-sweep (sonnet). All deliverables
in `extracts/` + `visuals/_sweep.md`.

**Outputs shipped:**
- `dossier.yaml` — 34 evidence rows (12 work-text + 8 diary + 6 letter + 8 commentary), 18 entities
  (wiki-schema v1.4: 12 person, 3 character, 1 group, 1 event, 1 concept), 12 visuals, 5-entry
  scholarship triangulation, a record-CREATING single `workRecord`, coverage ledger, 2 intra-corpus
  contradictions, 7 needsReview items.
- `index.md` (+ rendered `index.html`) — the full novel-dive spine.
- `website/src/posts/notes/2026-06-09-hadji-murat.md` — draft dev-blog note (`draft: true`).
- `extracts/` — verbatim TEI extracts (work + 6 commentary files + 26 diary + ~40 letter) + the
  5 provenance briefs; `visuals/` — 24 PD images cached (git-ignored).

**Gates:** `verify_quotes.py` 34/34 PASS; a separate-pass opus verifier returned CLEAN (0 blocking,
5 minor — 2 addressed: the «два полюса» Shulgin-provenance flag + a doubled-Tom citation; 3 cosmetic
left, consistent with sibling-dive convention). `_verifier-report.md` holds the full report.

**Marquee finding:** the What-Is-Art contradiction was LIVED, not reconciled — Tolstoy never argued
the work fulfilled his theory; he experienced writing it as ascetic shame and refused to publish,
yet the text's withholding of all moralizing is the closest it comes to obeying the treatise's own
attack on didacticism. Reported `extends` against Simmons (fulfilment) / Herman (violation) /
biographical (relapse). The Nicholas ‖ Shamil mirror is Tolstoy's own stated design (`confirms`);
the "anti-imperialist" label stays the mainstream's (`complicates`, per Bojanowska/Gould/Kokobobo).

**Schema:** applied wiki-schema v1.4 (`character` + `group`), which RESOLVED the gap the handoff
flagged as overdue — Hadji Murat → character (+ prototype = the historical figure); Nicholas I /
Shamil / Vorontsov / Loris-Melikov → person; Butler (prototype F. F. Kutler) / Marya Dmitrievna →
character; Caucasus highlanders → group. The genuine routing judgment calls are in `needsReview`.

Dive complete. Wiki ingestion (the LLM wiki-ingestion method) is the separate downstream step.
