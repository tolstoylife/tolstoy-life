# Run-report — `1890-1893-the-kingdom-of-god-is-within-you`

Work-dive on Tolstoy's *The Kingdom of God Is Within You* (Царство Божие внутри вас, 1890–93) — the great non-resistance / anti-state synthesis of the Prophet period and the last and largest of the four religious treatises. Run 2026-06-06/07, in-session unattended (the A-Confession-pilot model), medium visual intensity. Followed the handoff from the *On Life* session, which named *Kingdom* the next panel of the chronological march (Confession → Gospel → What I Believe → What Then Must We Do? → On Life → **Kingdom**).

## Scope contract (Phase 0)

- **Subject (work dive):** *The Kingdom of God Is Within You* (Царство Божие внутри вас, full subtitle «…или Христианство не как мистическое учение, а как новое жизнепонимание»). Slug `1890-1893-the-kingdom-of-god-is-within-you` — year-prefixed, slots after `1886-1887-on-life`.
- **The overlap that scoped the dive:** a `christian-anarchism` dive already covers the *doctrine* (non-resistance, anti-state, the *anarchist* label) thematically. This was scoped as the **work** dive it is not: genesis & composition (1890–93), what the work argues, textual history, publication/censorship/translation, reception (Gandhi the headline), and a `workRecord` fill. Doctrine overlaps cross-link to `../christian-anarchism/index.html`; they are not restated.
- **Corpus surface:** PSS Tom 28 — work «Царство божие внутри вас» pp. 1–293 (`v28_001_293…xml`); table of contents pp. 294–306 (the structural spine); variants pp. 309–330; commentary pp. 333–381 (История писания / текстологические примечания / описание рукописей, N. K. Gudzy — the genesis/publication/censorship source). Composition-window **diaries** Toms 51–52 (1890–93, 434 files); **letters** Toms 65–66 and the Chertkov letters Tom 87. Composition window **July 1890 – May 1893** (OS).
- **Works record:** **EXISTS** (`website/src/works/non-fiction/treatises/the-kingdom-of-god-is-within-you/`) — so the `workRecord` block proposes *corrections/refinements* to a live record, not a from-scratch fill.
- **Mode:** in-session unattended; no `AskUserQuestion` gating; judgment calls → `needsReview`; note `draft: true`; medium visual intensity.

## Method note — main context, with a successful foreground verifier

The handoff warned that a monthly spend limit (hit during the *On Life* dive earlier the same day) might still be in effect, emptying background subagents. Accordingly the whole dive — the deep read of the work via its own table of contents, the commentary mine, the diary + letter sweep, the visual sweep, and the scholarship sweep — was run **in the main context** from the start (no background dispatch was attempted/wasted). The Phase-5 **opus verifier ran successfully as a foreground dispatch** (16 tool uses, ~101k tokens) — the limit was evidently not blocking foreground work this session.

## What was covered

- **Deep read** of the work via Tolstoy's own «Оглавление» (twelve chapters + the six-part conclusion), with keystone passages extracted byte-faithful (`--choice=reg`): the three epigraphs; non-resistance as "the chief departure" the churches made from Christ; Christianity as a *new understanding of life* (новое жизнепонимание), not a mysticism; the three understandings of life and the divine one; the state as organised violence whose army "faces inward"; conscription as the last limit; the four means (intimidation, bribery, hypnotization, soldiery); public opinion; freedom as the recognition of truth and the refusal to lie as the one free act; hypocrisy; and the closing Luke 17:21 title-line.
- **Genesis, near-documentary**, from the commentary + byte-checked diaries: the book began (8 July 1890) as a *preface* to Ballou's *Catechism of Non-Resistance* and Garrison's 1838 *Declaration*, and grew over three years into the treatise; the four title-changes; the Strakhov-prompted split of the overgrown chapter VIII into VIII–X; the 9 September 1892 **Uzlovaya punitive-train** encounter that reshaped the conclusion; and the circle of copyists/interlocutors (Chertkov; Strakhov; Biryukov; the daughters M. L. and T. L. Tolstaya; S. A. Tolstaya; E. I. Popov).
- **Chertkov tone-letter** (14 Dec 1891, byte-faithful): Tolstoy's refusal to soften the book — "to soften, with qualifications, is impossible… the tone expresses the feeling, and the feeling infects."
- **Publication/censorship/translation**, from the commentary: the relay abroad by courier; **French first** (*Le salut est en vous*, Paris/Perrin, Oct 1893) and Italian 1893; the **first-printed Russian** (Berlin/August Deubner, Jan 1894, with censorship cuts) and German (Stuttgart/Deutsche Verlags-Anstalt); two English translations (Garnett; Delano) 1894; the foreign-censorship verdict ("the most harmful book it ever banned") and the Feoktistov circular (18 May 1894); first legal Russian printing July 1906.
- **Reception**: Russian (censors; Stasov — "the greatest book of our whole nineteenth century"; Repin — "a thing of terrifying power") from the commentary; then **Gandhi** as the headline afterlife (read it 1894, "overwhelmed" him — Gandhi's *Autobiography*) → *A Letter to a Hindu* (1908) → 1909–10 correspondence → Tolstoy Farm → the Gandhi–King nonviolence lineage.
- **Scholarship triangulation** (5 entries): confirms the Christian-anarcho-pacifist framing; extends the genesis (week-by-week diaries vs "thirty years of thinking"); complicates the publication record (French-first 1893 vs "first published in Germany 1894" / the record's Leipzig venue); contradicts the "mysticism" reading via the subtitle; complicates the "Chertkov softened it" frame (he was refused).
- **Visuals** (medium intensity, 7 PD images cached): keystone Tolstoy 1892 portrait + the **Berlin/Deubner 1894 first-Russian-edition title page**; Chertkov; Gandhi (London 1906); Garrison and Ballou (the ch. I forebears); Tolstoy at famine relief 1891.

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition | covered |
| What the work says | covered |
| Redactions & textual history | partial (Varianty + Afterword summarized, not collated) |
| Publication, censorship & translation | covered |
| Reception & afterlife (society + Gandhi) | covered (M. L. King only sketched) |
| Reception (Church / Synod) | partial (climate, not a documented direct ban) |
| Place in the cluster | covered |
| The author's later verdict | partial (relief + tone-defense; no later retrospective in-window) |
| Visual & manuscript record | covered (French/German title pages + MS facsimile to acquire) |

## Entity work-order (ingestion priority → dependency)

**Priority 1 (central; write first):** Non-resistance to evil by force (непротивление злу насилием) [concept]; Christianity as a new understanding of life (новое жизнепонимание) [concept]; The state as organised violence and the four means [concept]; **M. K. Gandhi** [person — MISSING, the reception headline]. Leo Tolstoy EXISTS.
**Priority 2:** V. G. Chertkov [person — EXISTS]; N. N. Strakhov [person — MISSING, also overdue from On Life/WIB/WTMWD]; P. I. Biryukov [person — **EXISTS as `Pavel Birukoff.md`**, link there]; Adin Ballou, William Lloyd Garrison [persons — MISSING, the ch. I forebears]; Universal military conscription (всеобщая воинская повинность) [concept]; The Uzlovaya punitive-train encounter, 9 Sept 1892 [event].
**Priority 3:** E. I. Popov; M. L. Tolstaya (→ `Maria Tolstaya`, EXISTS, the daughter — verifier-confirmed); T. L. Tolstaya (→ `Tatyana Tolstaya`, EXISTS); S. A. Tolstaya (EXISTS); I. D. Halpérine-Kaminsky; Constance Garnett; Pyotr Chelčický; August Deubner (all MISSING). Yasnaya Polyana EXISTS.

## Visuals work-order

Cached (PD, usable): Tolstoy 1892 (keystone portrait); Berlin/Deubner 1894 first-Russian-edition title page (keystone artefact); Chertkov; Gandhi (London 1906); Garrison; Ballou (low-res, dossier-only); Tolstoy famine relief 1891.
**To acquire:** a clean title-page scan of the 1893 French *Le salut est en vous* (Gallica/IA — digitized); a title page of the 1894 Stuttgart German edition; a manuscript facsimile of the drafts (AЧ 19–35, State Museum of Leo Tolstoy, Moscow).

## Work-record work-order (corrections to the EXISTING record)

**High confidence:** `dateWritingCompletedOldStyle` "1893-04" → **"1893-05"** (completion 14 May 1893 OS; likely OS/NS slip in the record); `dateFirstPublishedInRussia` 1906 confirmed (fill `firstPublishedInRussiaVenue`: «Русское свободное слово», July 1906); `transcriptions` expanded beyond Sophia alone to M. L. + T. L. Tolstaya (principal copyists), S. A. Tolstaya, L. F. Annenkova, E. I. Popov; `authoringLocations` add Begichevka + Moscow; `titleAlternatives` add the two draft titles + the actual French title *Le salut est en vous*; `relatedWorks` add the Prophet-period siblings (it is the **sequel** to *What I Believe*).
**Medium/low:** `firstPublishedVenue` + `dateFirstPublished` — the record's "Wilhelm Friedrich Verlag, Leipzig" / 1894 is **not** supported by the PSS Tom 28 commentary (French Perrin 1893 first; Berlin/Deubner Russian + Stuttgart German Jan 1894) → needsReview; `excommunicationRelated` true kept on the "related/climate" reading only → needsReview.

## needsReview (deferred human judgment)

1. `firstPublishedVenue` / `dateFirstPublished` — the record's Leipzig/1894 is unsupported by the commentary (French Perrin 1893 first; Berlin Deubner Russian + Stuttgart German Jan 1894). Human to choose the field's semantics and correct the venue.
2. `bans[]` Holy Synod complete-ban — not documented in the Tom 28 commentary (which records secular censorship: foreign-publications ban 1893; Feoktistov circular 1894). Verify or reclassify.
3. `excommunicationRelated` (true) — the 1901 Synod edict named no works; a tie of climate, not a direct ban (same caution as On Life).
4. `dateWritingCompletedOldStyle` "1893-04" — likely an error; should be "1893-05".
5. *(Resolved by the verifier)* `Maria Tolstaya.md` confirmed the daughter Maria Lvovna — safe to link.
6. Genesis/publication/censorship facts + Stasov/Repin reception are from the PSS Tom 28 commentary (Gudzy), not byte-extracted PD text — attribute, don't byte-claim.
7. Gandhi reception is from Gandhi's *Autobiography* + scholarship, not the corpus; the 1909–10 correspondence (Toms 80–82) is outside this window.

## Verification

- `verify_quotes.py` → **17/17 verbatim PASS** (after one fix: `kgd-text-12` initially dropped the closing guillemet — «…внутрь вас есть».» — corrected in dossier and index.md).
- Phase-5 verifier (opus, fresh foreground context) → **PASS-WITH-NITS, 0 must-fix, 4 nits**. The verifier independently re-derived the byte-fidelity sample from the original TEI (work, diaries, letter), confirmed every primary claim anchored, the commentary correctly attributed and kept out of `extracts/`, the triangulation valid, the entities resolved (Biryukov→Birukoff correct), and the workRecord corrections sound against the live record's actual values. **Nit 1 applied** (Maria Tolstaya confirmed the daughter); nits 2–4 no-action. Report: `_verifier-report.md` (with a resolution footer).

## Evaluation self-assessment (work-dive gate)

- Interlocutor sweep yielded people? **Yes** — Chertkov, Strakhov, Biryukov, the daughters M. L. and T. L. Tolstaya, S. A. Tolstaya, E. I. Popov as the composition circle; Ballou, Garrison, Chelčický as the forebears; Halpérine-Kaminsky, Garnett, Deubner as the publication chain; Gandhi as the afterlife — all in `entities`.
- Russian society/Church reception covered? **Yes** — the censors, Stasov, Repin (commentary); the Church tie honestly marked `partial` (climate, not a documented ban).
- `workRecord` fill accurate & provenanced? **Yes** — corrections to a live record, each evidence/commentary-anchored, with the unsupported Leipzig venue and the OS-date slip flagged; uncertain calls → `needsReview`.
- `coverage` honest? **Yes** — 3 surfaces graded `partial` with reasons (verifier-accepted).
- `--choice=reg` extracted cleanly? **Yes** — pre-reform resolved across the work, diaries and the Chertkov letter (the letter's body is mixed-orthography but the cited span is clean modern text, verified present with `--notes=off`).
- Spine stayed bare? **Yes** — "mysticism" attributed and rejected via the subtitle; "Christian anarchism"/"anarchist" attributed to the outside and cross-linked; commentary facts attributed throughout; verifier found no endorsing adverbs.

## Models & rough cost

Main loop: Opus (in-session) — did the deep read, the commentary mine, the diary/letter/visual/scholarship sweeps, and the synthesis. Subagents: 1× Opus verifier (~101k tokens, foreground, succeeded). Web: 2 scholarship searches; a main-context Wikimedia Commons fetcher (~14 API/FilePath calls, 7 downloads, with rate-limit backoff). No licence-gated downloads to `website/src/`.

## Output paths

- `docs/research/1890-1893-the-kingdom-of-god-is-within-you/index.md` (+ rendered `index.html`, git-ignored)
- `docs/research/1890-1893-the-kingdom-of-god-is-within-you/dossier.yaml`
- `docs/research/1890-1893-the-kingdom-of-god-is-within-you/extracts/` (PD primary extracts — the work, 5 composition-window diaries, 1 Chertkov letter)
- `docs/research/1890-1893-the-kingdom-of-god-is-within-you/visuals/` (git-ignored cache; 7 PD images)
- `website/src/posts/notes/2026-06-06-the-kingdom-of-god-is-within-you.md` (draft)
- `session-log.md`, `_verifier-report.md`, this `run-report.md`

Wiki ingestion is a separate, human-in-the-loop step — this dossier is the pointer, not the writer.
