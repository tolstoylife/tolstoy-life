---
layer: reference
lastUpdated: 2026-05-30
tags: [research, session-log]
---

# corpus-dive: christian-anarchism — session log

Append-only log for the `christian-anarchism` dive (dive #2 of three:
`tolstoyanism` → `christian-anarchism` → `christian`). Resume from the most recent entry.

---

## Session 1 — 2026-05-30 — built (split + retrofit), Phases 0→6

**Status: dive built; Phase-5 opus verifier pending.** This dive is a **split + retrofit**: it
carves the Christian-anarchism half out of the legacy combined survey
`docs/research/tolstoyanism-christian-anarchism/` (whose extracts are already byte-faithful and
PDF-cross-checked) and back-fills the structured layers the original lacked. No re-sweep, no
re-translation of the locked quotes.

### Scope contract (confirmed with Johan via the Phase-0 picker)

- **Territory:** fresh narrow dive at `docs/research/christian-anarchism/`, reusing the legacy CA
  extracts verbatim. Legacy combined dive → superseded for the CA half once this lands.
- **Spine:** Tolstoy's double move — refuse *anarchist* as a political label (Eltzbacher, 1900),
  affirm the substance as religious; the unique self-voiced «христианский анархизм» (Sacy, 1901);
  the 1894 diary as seed; the phrase-genealogy (Schmitt/Kenworthy/Davidson/Crosby/Ortt → Chertkov
  1905) as a parallel thread.
- **Corpus surface:** post-1880 Prophet period; letters first-class; diaries + polemical works
  (esp. *The Kingdom of God*, Т.28) secondary; editorial `comments/` excluded. Sweep: inline
  (heavy sweep already done). Visuals: **light** (full-retrofit on the structured layers).

### A note on the start of the session

The session opened with an intermittently degraded tool channel (aliased `ls`→colorls / `find`→bfs
produced empty or garbled output, and some file reads returned corrupted tails). An early
exploration of a `primary-sources/pss/tom/**` path under those conditions surfaced apparent
"decoy" lines; that whole branch was **discarded** as unreliable once the channel stabilised — it
is not part of this dive, which works only from the legacy `extracts/` and the real TEI corpus
paths in the handoff. All build steps below ran cleanly and are gated by `verify_quotes.py`.

### What was done

- **Extracts copied** into `extracts/` (+ `extracts/pss-pages/`): `v52_138_140_1894_09_10`,
  `v72_341_…Elcbaxeru…`, `v73_126_…Sasi…`, plus supporting `v67_179_…Davidsonu`,
  `v68_024_…SHmitu`, `v68_060_…SHmitu`, `v78_252_…Germogenu`; PSS page images
  `tom72-eltzbacher-441/442/443.png`, `tom73-sacy-153/154.png`.
- **`dossier.yaml` built** via a fail-loud scripted-slice generator (`/tmp/build_ca_dossier.py`,
  not committed) that slices each `quoteRu` out of its extract by start/end anchor — no hand-typed
  Cyrillic. **`verify_quotes.py` → PASS, 10/10 verbatim, 2 facsimiles ok, exit 0.** Ten evidence
  rows: 3 seed (opener/reframing/dilemma), Eltzbacher (RU praise + RU reject + DE reject), Sacy
  (RU + FR), Davidson, Schmitt. The two bilingual letters are entered twice — Tolstoy's Russian and
  his own French/German original — both byte-checked. Eleven entities (priority + dependsOn), five
  visuals, scholarship / contradictions / notCovered / needsReview layers.
- **`index.md` synthesized** (9-section SKILL spine, one-line paragraphs for nl2br). RU/FR/DE quotes
  copied from the verified dossier.
- **Draft note** `website/src/posts/notes/2026-05-30-christian-anarchism.md` (`draft: true`).
- **Visuals: light.** Two committed PD page facsimiles (Eltzbacher Т.72 p.442, Sacy Т.73 p.154) +
  three PD Commons portraits in the git-ignored `visuals/` cache: Paul Eltzbacher, Eugen Heinrich
  (Jenő) Schmitt, Vladimir Chertkov (Repin, same image as dive #1). **Gabriel Sacy: no portrait
  exists on Commons** (only the unrelated Silvestre de Sacy) — recorded in `needsReview`.
- **Phase 3 scholarship:** light English-first web sweep (sonnet subagent) — received view
  (Christoyannopoulos 2009/2010; Alston 2013; Eltzbacher 1900 / Byington 1908; Marshall);
  triangulation in §5. [Reconcile the subagent's verified citations into §5 + dossier `scholarship`
  before closing.]

### Key ingestion finding (for the separate wiki step)

The vault page `website/src/wiki/Christian Anarchism.md` (recordStatus: draft) carries a
`<!-- NEEDS PRIMARY SOURCE -->` block for **exactly** Tolstoy's rejection of the political label —
which the **Eltzbacher letter (Т.72, 1900)** here anchors — and **lacks** the unique Sacy
self-attestation (Т.73, 1901) and the phrase-genealogy. The dossier `evidence` resolves both. The
page also cites Christoyannopoulos 2009; dive #1 cited 2010 — both exist (same author); pick per use.

### Open / handed forward

- Phase-5 opus verifier — dispatch in a fresh context; fix anything it flags.
- Reconcile the Phase-3 subagent's citations into §5 / dossier `scholarship` (provisional now).
- `extracts/v78_252_EpiskopuGermogenu.txt` — carried over for the clusters mention only (the reply
  is brother-to-brother, no «анархист» in Tolstoy's body voice); not an evidence row.
- `/tmp/build_ca_dossier.py` — scratch generator; delete after the verifier passes.
- Entity work-order (priority-then-dependency): **1** `Christian anarchism` (concept, exists —
  needs the Eltzbacher + Sacy anchors) + `Leo Tolstoy` (exists); **2** `Paul Eltzbacher`,
  `Gabriel Sacy`, `Eugen Heinrich Schmitt`, `Non-resistance` (all missing), `Vladimir Chertkov`
  (exists); **3** `John Coleman Kenworthy`, `John Morrison Davidson`, `Ernest Howard Crosby`,
  `Felix Ortt` (all missing).
- Visuals work-order: a **Gabriel Sacy** portrait (none on Commons) would need an Egyptian/Russian
  archive request; otherwise the visual record is complete.
