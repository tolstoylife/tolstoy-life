# Run report — The Living Corpse (Живой труп) dive

**Slug:** `1900-the-living-corpse` · **Mode:** interactive, `--novel` (drama flex) · **Date:** 2026-06-12
**Subject:** Tolstoy's unfinished 1900 drama, PSS Tom 34. Record-creating workRecord (plays/drama).

## Scope contract (as run)

- **Question:** Is *The Living Corpse* an indictment of legal/church marriage and the divorce machinery — honesty against the institution — and was its abandonment driven mainly by Tolstoy's reluctance to wound the real Gimers?
- **Corpus surface:** PSS Tom 34 (play `v34_007_099`; plans `v34_407_410`; variants `v34_411_483`; commentary `v34_533_543` + `v34_543_545`); diaries Tom 53 (1897 seed) + Tom 54 (1900); letters Tom 72 (Posse) + Tom 88 (Chertkov).
- **Marquee (named up front):** two-pronged (institutional indictment; reason for abandonment), tested as hypothesis.
- **Visuals intensity:** heavy. **Companion text:** none.
- **Gates:** `--choice=reg --notes=auto`; `verify_quotes.py` exit 0; separate-pass verifier; commit, don't push.

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition | covered |
| Witness/interlocutor network | covered |
| What the work says (close-read) | covered |
| Redactions & textual history | covered (sampled) |
| Characters & prototypes | covered |
| Themes | covered |
| Marquee (hypothesis tested) | covered |
| Reception & afterlife (1911 staging story) | covered |
| Contemporary Russian/church reaction (pre-1911) | partial (none existed — withheld until 1911) |
| Scholarly context | covered |
| Manuscript facsimile (PD, committed) | not-covered |
| Full variant collation | partial |

## Marquee outcome

**confirms + complicates + extends.** (1) Institutional indictment — `confirms` (scholarship agrees) + `extends` (the primary text shows it is *structural*, no villain, and legal-circle sourced like *Resurrection*). (2) Abandonment — `complicates` (the "spared the Gimers" account is real but partial) + `extends` (the diary names the conscience-turn the scholarship only infers). Sub-claim: the "about-face from *Kreutzer*" reading is `complicates` (Tolstoy grouped the play *with* *Kreutzer*).

## Work-orders for the (later, human-in-the-loop) ingestion

**Entity work-order** (by ingestionPriority, then dependency):
- **Priority 1:** Fyodor Protasov (`character`), Liza Protasova (`character`), N. S. Gimer (`person`), E. P. Gimer (`person`), + the record-creating workRecord.
- **Priority 2:** Viktor Karenin, Masha (`character`); N. V. Davydov, A. F. Koni, Nemirovich-Danchenko, Stanislavski, Chertkov (`person`, Chertkov exists); the 1911 MAT premiere + Gimer-trial (`event`).
- **Priority 3:** Anna Pavlovna, Ivan Petrovich Aleksandrov, Afremov (`character`); E. A. Simon, A. P. Ivanov, Moskvin, Chekhov, Biryukov (exists), Posse (`person`); Moscow gypsy choirs (`group`); Moscow Art Theatre (`institution`); Redemption-1918 + Otsep-1929 (`adaptation`).
- All `missing` except **Vladimir Chertkov** and **Pavel Birukoff** (exist).

**Work-record work-order** (record-creating proposal → `website/src/works/plays/drama/the-living-corpse/The Living Corpse.md`):
- *High confidence:* id, titles (+ alternatives Труп / Redemption / The Man Who Was Dead / The Live Corpse), Plays/Drama, genre play, language ru, completionStatus incomplete, publishedDuringLifetime/InRussia false, dateFirstPublished 1911-10-06 NS / 1911-09-23 OS (Russkoe Slovo), dateWritingStarted 1900-02-08 NS / 1900-01-27 OS, themes, synopsis, jubileeEdition vol 34, bans [] (author-withheld), censorshipNotes.
- *Medium:* dateWritingCompleted 1900-08-28 NS (first draft; approximate), authoringLocations (Moscow / Pirogovo / Yasnaya Polyana).
- *Low / deferred:* relatedWorks [] (no enum value fits the Kreutzer/PoD/Resurrection thematic grouping — human call); wordCount 0.
- **At ingestion:** expand the dossier date sub-flags `oldStyle:`/`approximate:` to the schema's per-field keys (`<field>OldStyle` / `<field>Approximate`).

**Visuals work-order:** 12 PD images cached (git-ignored `visuals/`; metadata in dossier). Acquire: a PD manuscript / 1911 first-edition facsimile (try GMT / RGB / State Tolstoy Museum); a photo of Moskvin *as Fedya*; an N. V. Davydov portrait; a Barrymore *Redemption* production still.

## notCovered queue

Full variant collation (рук. №№ 1–14); the Meyerhold/Alexandrinsky production + European tour in depth; the full English-translation lineage; the 11–12 Oct 1887 Tolstoy→Biryukov letter (Tom 64); the separate «большая драма» of the 7 Sept 1900 diary.

## needsReview (human-judgment deferred)

Karenin←Chistov (conjectural, not in PSS); Masha prototype (milieu, not a model); the unverified Koni "14 Jan 1900 self-sacrifice letter" web claim; any incidental 1911 stage-censorship (bans [] proposed); whether Kryukova/Afremov earn their own character nodes; wordCount.

## Evaluation self-assessment (work-dive checks)

- **Interlocutor sweep yielded people?** YES — the prototype + witness network is dense (Davydov, Koni, the Gimers/Simon, Ivanov, Nemirovich-Danchenko, Chertkov, Posse, Gnedich).
- **Russian society/church reception covered?** PARTIAL-BY-NATURE — none existed pre-1911 (withheld); the posthumous 1911 staging reception is covered. Honestly marked `partial`.
- **workRecord fill accurate & provenanced?** YES — record-creating; every field evidence-anchored; OS/NS dates correct (incl. the leap-century gap); verifier confirmed.
- **coverage honest?** YES — verifier confirmed no `covered` overstating a `partial`.
- **`--choice=reg` extracted cleanly?** YES — no stderr warnings.
- **Spine stayed bare?** YES — attribute-don't-assert; verifier PASS on voice.

## Gates & models

- `verify_quotes.py`: **40/40 verbatim, exit 0 (PASS).**
- Separate-pass verifier (opus): **CLEAN-WITH-MINORS** (0 blockers, 5 minor/note); 2 minor text fixes applied (reception-figure attribution; stale comment 43→40).
- Models: orchestration + close-read + synthesis + marquee on the main (opus) context; reception/scholarship sweep + visuals sweep on sonnet sub-agents; verifier on opus.

## Output paths

- `docs/research/1900-the-living-corpse/index.md` (+ rendered `index.html`)
- `docs/research/1900-the-living-corpse/dossier.yaml`
- `docs/research/1900-the-living-corpse/extracts/*.txt` (PD, committed)
- `docs/research/1900-the-living-corpse/visuals/*` (git-ignored cache; `_visuals-sweep.md` catalogue)
- `docs/research/1900-the-living-corpse/{_scholarship-sweep.md, _verifier-report.md, session-log.md}`
- `website/src/posts/notes/2026-06-12-the-living-corpse.md` (`draft: true`)

**Reminder:** wiki ingestion is a separate, human-in-the-loop step. This dive is the plan and the pointer, not the writer — no vault pages were created.
