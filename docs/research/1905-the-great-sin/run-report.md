# Run-report — The Great Sin (Великий грех, 1905) corpus-dive

**Mode:** interactive (in-session, accept-edits). **Date:** 2026-06-21. **Kind:** work-subject dive (single work → one proposed `workRecord`), NOT `--novel`. **Slug:** `1905-the-great-sin` (composition window 1905).

## Scope contract (as run)

- **Question:** Does The Great Sin confirm, complicate, or contradict Tolstoy's Christian-anarchist anti-statism, given that he endorses Henry George's state-administered single tax as the remedy for the land-monopoly «великий грех»?
- **Corpus surface:** the essay + variants + composition-history commentary (PSS Tom 36); the 1905 diaries (Tom 55) and the 17 Apr 1905 letter to Chertkov (Tom 89); prior sibling dives; English-first scholarship; light Commons visuals sweep.
- **Gates:** `--choice=reg --notes=auto` extraction; `verify_quotes.py` exit 0; record-creating `workRecord`; Genesis + reception + marquee sections; bare voice; no vault writes; separate-pass verifier; commit not push; plain language. **All met.**

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition | covered |
| What the work says | covered |
| Redactions & textual history | covered |
| Publication, censorship & translation | covered |
| Reception & afterlife (Russia/foreign) | partial (named Russian critical replies not found) |
| Scholarly context | covered (Wenzer 1997 anchor) |
| Place in the cluster | covered |
| The author's later verdict | partial |
| Visual & manuscript record | covered (manuscript facsimile not pursued) |
| Characters & prototypes | not-covered (non-fiction) |

## Marquee verdict

**Complicates, not contradicts.** Tolstoy endorses the single tax conditionally («при существующем государственном строе и обязательных податях»), and Chertkov physically cut the anarchist sentence (variant № 15) from the introduction because it contradicted the reform argument — the commentary records Chertkov's own motivation («стоит в противоречии со всем предыдущим»). The remedy stays conscience-not-legislation (the serfdom analogy). Scholarship (Wenzer 1997) independently reads a "concession/weakness" Tolstoy "compartmentalized."

## Work-orders for the separate, human-in-the-loop ingestion step

**Entity work-order (ingestionPriority then dependsOn):**

1. **Henry George** (person, *missing*) — the central figure; 1839–1897, Progress and Poverty 1879, the single tax. Write first.
2. **The Great Sin** (work record, *missing*) — see the workRecord proposal below.
3. **Private property in land / the great sin** (concept, *missing*) — dependsOn Henry George.
4. **The single tax / единый налог** (concept, *missing*) — dependsOn Henry George.
5. **S. D. Nikolaev** (person, *missing*) — George's Russian translator; Tolstoy's source.
6. **Vladimir Chertkov** (person, *exists*) — augment with the cuts episode.
7. Peripheral, *missing* (loose-match the vault first — transliteration gotcha): **Dušan Makovický**, **Giuseppe Mazzini**, **A. S. Buturlin**. **Maria Lvovna Obolenskaya** routes to the existing `Maria Tolstaya.md` — confirm daughter-not-sister first.

**Work-record work-order:** create `website/src/works/non-fiction/essays-and-criticism/the-great-sin/The Great Sin.md` from the dossier `workRecord` block (26 proposed fields, mostly high-confidence; genre `essay`, subcategory `Essays and Criticism`; `publishedInRussiaDuringLifetime: true`; venueType `journal`). Shape list-typed fields to the works schema object arrays on application.

**Visuals work-order:** 8 PD images cached (git-ignored). Keystones: Henry George 1888 portrait; Tolstoy c.1905 (from the *A Great Iniquity* pamphlet); Progress and Poverty title page; Chertkov (Repin). Gaps to chase if a page needs them: Nikolaev's Russian George translation title page; a PD Russian-peasant photo c.1905.

## notCovered (resume queue)

- The P9 cluster satellites (To the Working People, The First Step, the George prefaces, etc.) — this dive seeds `land-question-henry-george`.
- Variant collation beyond the cut chapters.
- Named contemporary Russian critical replies (deeper Russian-language reception pass).
- Whether Joseph Fels / a "Land Values Publication Dept" issued the "A Great Iniquity" pamphlet (only Free Age Press + The Public confirmed).
- The Gandhi / Indian land-reform afterlife (belongs with the Letter to a Hindu material).

## needsReview (deferred human judgment)

`publishedInRussiaDuringLifetime` confirm-no-journal-censorship; `Maria Tolstaya.md` daughter-vs-sister disambiguation; vault transliterations for Makovitsky/Mazzini/Nikolaev/Buturlin; relatedWorks id-slug existence. (firstPublishedVenueType and the 'A Great Iniquity' translator items: RESOLVED.)

## Models / cost

Main synthesis + edits: Opus (this session). Two background subagents: scholarship sweep (general-purpose, ~74k tokens) and visuals sweep (general-purpose, ~58k tokens). Verifier: Opus (~121k tokens), separate pass. Rough order: a few hundred k tokens total.

## Self-assessment (gates)

- Interlocutor sweep yielded people: ✓ (George, Nikolaev, Chertkov, Makovitsky, Mazzini, Buturlin, Obolenskaya).
- Russian-society reception covered: partial (editors' disclaimer + SR/Marxist contrast; named replies open).
- workRecord fill accurate & provenanced: ✓ (evidence-anchored; one enum fixed post-verify).
- coverage honest: ✓ (two surfaces honestly `partial`).
- `--choice=reg` extracted cleanly: ✓.
- Spine stayed bare: ✓ (verifier confirmed).

## Outputs

- `index.md` (+ generated `index.html`), `dossier.yaml`, `extracts/` (10 PD verbatim + `_scholarship.md`), `visuals/` (8 PD, git-ignored, + `_visuals.md`), `_verifier-report.md`, this `run-report.md`, `session-log.md`.
- Draft note: `website/src/posts/notes/2026-06-21-the-great-sin.md` (`draft: true`, submodule).
