# Run report — The Law of Violence and the Law of Love (Закон насилия и закон любви, 1908)

**Dive:** `docs/research/1908-the-law-of-violence-and-the-law-of-love/`
**Run:** 2026-06-08, in-session (accept-edits), from the scope handoff `_generated/sessions/2026-06-08-the-law-of-violence-dive-scope-handoff.md`.
**Type:** single-work Prophet-period dive · **record-creating** (no `works/` record existed).
**Verdict:** verifier CLEAN (0 must-fix); `verify_quotes.py` 33/33 PASS, 1 facsimile OK.

---

## Scope contract (Phase 0)

- **Question:** how the 1908 treatise states, for the last time and systematically, non-resistance as the form of the law of love; how it was composed Jan–Jul 1908 (the title saga, the abandon-it struggle, the moved chapters); and how its censored partial appearance in Russia + complete publication abroad carried it into the final, Gandhi-adjacent year.
- **Corpus surface:** works (Tom 37 treatise + Tom 41 cognate), 1908 diaries + notebooks (Tom 56), letters (Toms 78, 89), editorial commentary (Tom 37 «История писания»).
- **Centrepiece (per handoff):** the redaction / textual history (the unstable title + the chapters moved in and out).
- **Reuse:** the two fire quotes from the fire-metaphor dive, re-verified (with a Salter-epigraph attribution refinement on the "dry wood" one).
- **Time-box:** one session. **Sweep mode:** targeted inline + 3 parallel sub-sweeps.

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition (incl. people) | covered |
| What the work says (structural map) | covered |
| Redactions & textual history (centrepiece) | covered |
| Publication, censorship & translation | covered |
| Reception & afterlife (Russian/Church first) | partial |
| Place in the cluster | covered |
| The author's later verdict | covered |
| Visual & manuscript record | partial |

`partial` reasons: Reception — text-specific contemporary reception is thin (censored; author died Nov 1910); the jubilee/Synod/Trotsky context is covered, and the Gandhi lineage runs through the 1908 *siblings*, not this text. Visual — manuscript facsimile, Gusev portrait, and first-edition title pages are not openly available.

## Entity work-order (for the later wiki-ingestion step — priority then dependency)

**Priority 1 (central):**
- *Leo Tolstoy* — exists.
- *non-resistance (непротивление злу насилием)* — **missing** (concept). Currently only inside Christian Anarchism / Tolstoyanism / Leo Tolstoy; a dedicated page is the single biggest gap this dive surfaces.
- *Vladimir Chertkov* — exists.

**Priority 2 (supporting):**
- *the law of love / the law of violence* — missing (concept; depends on the non-resistance page).
- *Nikolai Gusev* — **missing** (person; the secretary/diary-witness — recurs across the Prophet-period dives, worth creating).
- *Pavel Birukoff* — exists (vault transliteration "Pavel Birukoff").
- *A. I. Ikonnikov* — missing (person; conscientious objector quoted in the work).
- *Free Age Press* — missing (institution; shared with the Bethink dive).
- *Tolstoy's 80th-birthday jubilee (1908)* — missing (event; the dominant reception context).

**Priority 3 (peripheral):**
- *Kievskie Vesti* — missing (institution). *Holy Synod* — missing (institution). *Mahatma Gandhi* — missing (person; lineage endpoint, NOT a reader of this text). *Christian Anarchism* — exists (cross-link only).

## Work-record work-order (RECORD-CREATING — propose a NEW `works/` record)

Target path (proposed): `website/src/works/non-fiction/treatises/the-law-of-violence-and-the-law-of-love/The Law of Violence and the Law of Love.md`. Field set proposed in `dossier.yaml` → `workRecord`. Grouped by confidence:

- **High:** titleEn, titleRu, titleAlternatives, mainCategory (Non-Fiction), language, completionStatus, publishedDuringLifetime, dateWritingStarted (1908-02-02 NS / 1908-01-20 OS), firstPublishedVenue/Type (Kievskie Vesti / newspaper), bans (passages-cut, imperial-state, 1909), censoredVersionExists, censorshipNotes, identifiers.jubileeEdition.volumes (37), epigraph + epigraphSource (Mt 10:28), authoringLocations (Yasnaya Polyana).
- **Medium (verify before applying):** subcategory (Treatises), genre (philosophical), dateWritingCompleted (1908-07-15 NS / 1908-07-02 OS — corrections to 6 Aug), dateFirstPublished (1909-03-02 NS / 1909-02-17 OS), **publishedInRussiaDuringLifetime** (proposed `true` but partial+censored — reviewer may prefer `false`+note), excommunicationRelated (false), relatedWorks (6 proposed; only `the-kingdom-of-god-is-within-you` has a confirmed record — verify/create the others).

## Visuals work-order

- **Cached & usable (10 PD photos in git-ignored `visuals/`):** keystone Prokudin-Gorsky colour portrait (23 May 1908), Chertkov-photographed Tolstoy (1908), Repin's Chertkov portrait, Bulla 1908 portraits, Tolstoy+Alexandra (1908), etc. + 1 self-rendered PD page facsimile in `extracts/`.
- **To acquire (requests):** a manuscript facsimile of рук. № 58 (State Museum of L. N. Tolstoy, рукописный отдел); a period N. N. Gusev portrait; title pages of «Свободное слово» (1909) and «Киевские вести» (1909).

## notCovered (resume queue)

Full epigraph apparatus (mapped, not sourced individually); page-by-page collation of the censored Kievskie Vesti text vs the complete Svobodnoe Slovo edition; the spun-off «Номер газеты» (Tom 38) and absorbed «Христианство и воинская повинность» as full texts; the Krug Chtenija cognate read as a separate piece; the non-Russian translation lineage.

## needsReview (deferred human judgement — see dossier for all 12)

Headline items: the «понравилось» (not «понравилась») verb correction; «чепуха» is Gusev-via-apparatus not a Tolstoy autograph; the dry-wood fire image is a Salter epigraph (cross-dive correction to fire-metaphor); OS/NS colophon-date care; the `publishedInRussiaDuringLifetime` edge case; relatedWorks slug existence; Gandhi did not (on the record) read this specific text.

## Evaluation self-assessment

- Interlocutor sweep yielded people? **Yes** — Chertkov, Gusev, Biryukov, Ikonnikov, each with first-hand evidence.
- Russian society/church reception covered? **Partial-honest** — censorship + jubilee/Synod/Trotsky context covered; text-specific reception genuinely thin (stated, not padded).
- workRecord fill accurate & provenanced? **Yes** — every field evidence-anchored; record-creating status flagged; edge cases in needsReview.
- coverage honest? **Yes** — two `partial`s justified, no inflated `covered` (verifier confirmed).
- `--choice=reg` extracted cleanly? **Yes** — no stderr warnings; `--notes=auto` recovered the 12 May line + Notebook No. 3 chapter-note.
- Spine stayed bare? **Yes** — verifier PASS on voice / contested-label cross-linking.

## Models & rough cost

Main loop opus. Sub-sweeps: treatise deep-read (opus), composition sweep (opus), scholarship (opus), visuals (sonnet), verifier (opus). ~5 subagent dispatches; ~0.4–0.5M subagent tokens total. Mechanical steps (extract/verify/render/facsimile) ran no-model in Bash.

## Output paths

`index.md` (+ git-ignored `index.html`), `dossier.yaml`, `session-log.md`, `run-report.md`, `_verifier-report.md`, `extracts/` (PD text + facsimile + analysis files), `visuals/` (10 PD images, git-ignored). Draft note: `website/src/posts/notes/2026-06-08-the-law-of-violence-and-the-law-of-love.md` (`draft: true`).

**Not pushed** — Johan pushes himself. No vault pages or works records created (the dive plans them).
