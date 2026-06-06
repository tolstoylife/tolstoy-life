# Run report — A Confession (Исповедь) work-dive

**Mode:** autonomous (`--auto`), run **deep / multi-pass** with a **heavy** visual fan-out.
**Date:** 2026-06-06 · **Slug:** `a-confession` · **Work id:** `confession`
**Scope approved once upfront** (the reader chose Heavy visuals + Go-deep), then detached.

## Phase 0 — scope contract (as run)

- **Question.** Document *A Confession* as a *work*: genesis & composition, what the text says, redactions, publication / censorship / translation, reception (Russian society & Church first), and place in the Prophet-period canon — grounded in Tolstoy, the Jubilee apparatus, the composition-window diaries/letters, and prior dives. Propose a `workRecord:` to fill the near-empty `Confession.md`.
- **Corpus surface.** PSS Tom 23: `v23_001_059_Ispoved` (text, pp. 1–59), `v23_488_511_…Plany_i_varianty` (variants, pp. 488–511), `v23_515_537_Ispoved` (commentary, pp. 515–537). Composition-window diaries Tom 48 (1878) + Tom 49 (1881–82); letters Tom 62–63; sibling *В чём моя вера?* (Tom 23); echoes (Tom 26 *Notes of a Madman*, Tom 66 letter to Dumas). Period: post-1880 Prophet years; OS dates.
- **Pins discovered.** Composition ~1879–1882 (roots 1877; complete 1879 treatise reworked into «Исповедь»; finished form ~early July 1881, editor-hedged; type-set 1882). Diary silence 1879–80 (notebooks, not diaries). Title «Исповедь» not Tolstoy's (first in Elpidin 1884).

## Models used (cost note)

- **opus:** work deep-read; Tom-23 commentary mining; Phase-3 scholarship + triangulation; the Phase-5 verifier (fresh context).
- **sonnet:** 4 Phase-1 sweeps (diaries, letters Tom 62, letters Tom 63, broad echo); 3 visual channels (Tolstoy / people-places / editions); the PD facsimile render; the visuals dedup/consolidation.
- Rough order ~1.1M subagent output tokens across ~12 subagents + main-context synthesis. Mechanical steps (extract_tei, verify_quotes, serve.py, build_evidence_index, image download) used no model.

## Verification (Phase 5)

- **Mechanical gate:** `verify_quotes.py docs/research/a-confession/dossier.yaml` → **27/27 quotes verbatim, 0 label warnings — PASS.**
- **Cross-dive aggregation:** `build_evidence_index.py --check` → **exit 0** (0 unresolved refs; entities register cleanly).
- **Render:** `serve.py --build-only` → `index.html` (48 KB) + `INDEX.html` rebuilt, exit 0.
- **Independent verifier (opus, fresh context):** verdict **CLEAN-WITH-MINORS, no must-fix.** Confirmed primary-anchored claims, attributed secondary, valid triangulation refs, accurate `vaultStatus`, the cousin/daughter A. A. Tolstaya distinction, rights hygiene (visuals git-ignored; only PD in `extracts/`; nothing in `website/src/`), honest coverage, evidence-anchored dates. Only minor: `workRecord` value *shapes* (flat vs object arrays) to reshape at human ingestion — already in `needsReview`.

## Evaluation self-assessment (the deferred gate, self-scored; not run live)

1. **Did the composition-years interlocutor sweep yield people as `person` entities?** — **YES.** Strakhov, Fet, Alexandrine (cousin), Fedorov, Sutaev, Alekseev, Engelhardt, Yuryev, Elpidin, Pobedonostsev, Turgenev, Urusov surfaced from the letters/diaries and are routed in `entities` with `ingestionPriority`. Strong.
2. **Is the Russian society & Church reception real and source-confirmed?** — **PARTIAL (honest).** 1880s critics (Gromeka, Ostroumov, Gusev) named via the PSS commentary; the 1882 censorship and the 1901 Synod edict ("names no works") confirmed (commentary + scholarship). A dedicated reception sweep was not run → `coverage: partial`, logged in `notCovered`.
3. **Is the `workRecord` fill accurate and provenanced?** — **YES, with the shape caveat.** Every proposed value is evidence- or commentary-anchored; uncertain ones carry `confidence: medium` + notes; the two record fields that are currently *wrong* (`publishedDuringLifetime`, `publishedInRussiaDuringLifetime` = false) are flagged to flip to true. Value-shape reshaping deferred to ingestion (`needsReview`).
4. **Is `coverage` honest (no `covered` that is really `partial`)?** — **YES.** Verifier spot-checked; `partial`/`not-covered` calls (variants, sibling work, reception, 1901 text, 1879–80 diary) match the prose.
5. **Did `--choice=reg` extract cleanly?** — **YES.** All 18 extractions ran with no dropped-pair warnings; pre-reform orthography resolved to modern.
6. **Did the spine stay bare?** — **YES (with one caution).** Contested labels ("crisis"/"conversion"/"Tolstoyanism") are attributed to biographers, not adopted; the dive leads with «переворот». "crisis" appears in running prose only as the frame being corrected or a neutral descriptor — acceptable, watch on future dives.

## Outputs

- `docs/research/a-confession/index.md` (+ git-ignored `index.html`)
- `docs/research/a-confession/dossier.yaml` (evidence ×27, entities ×24, scholarship, workRecord, coverage, visuals, needsReview)
- `docs/research/a-confession/extracts/` — 18 byte-faithful `.txt` extracts + 1 PD facsimile (`v13_MyConfession_opening_facsimile-019.jpg`, English Wiener 1904)
- `docs/research/a-confession/visuals/` — 27 PD images cached (git-ignored; repopulate with `fetch_visuals.py a-confession`)
- `docs/research/a-confession/session-log.md`, `run-report.md`
- `website/src/posts/notes/2026-06-06-a-confession.md` (`draft: true`)

## For the reader's return (deferred, with Johan)

- **Human evaluation gate** (spec §5): review this self-assessment; decide whether to fold any fixes into `SKILL.md`/`extract_tei.py` before running the rest of the canon.
- **Pending memory updates** (from the handoff): reverse `corpus-dive-human-present` (unattended `--auto` runs are wanted again — confirmed this session); reconfirm in-session `claude -p --allow-dangerously-skip-permissions` is denied by the auto-mode classifier (Johan launches headless, or drives in-session under accept-edits, as here). Left for the with-Johan ritual.
- **`needsReview` highlights:** the 1884 Geneva imprint wording (Genève vs Carouge); identity of the "book exposing the deceivers" in two 1882 letters; the 1884–85 Russkaya-Mysl-ban letters likely concern *What I Believe*, not *A Confession*; the `excommunicationRelated` field intent; the cousin Alexandrine needs a NEW wiki page (not the daughter's).
- **Wiki ingestion is a separate human step** — the dossier is the pointer, not the writer. Entity work-order (priority 1 first): the «переворот» concept page + Strakhov; then Alexandrine (cousin), Fet, Fedorov, Sutaev, Yuryev, Elpidin, Pobedonostsev, Holy Synod, Russkaya Mysl, Optina Pustyn; then Turgenev, Urusov, Alekseev, Engelhardt, Rumyantsev Museum.
