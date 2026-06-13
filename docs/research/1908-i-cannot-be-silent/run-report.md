# Run report — 1908-i-cannot-be-silent

**Dive:** *Не могу молчать* / *I Cannot Be Silent* (1908), Tolstoy's essay against capital punishment.
**Type:** single-work work-dive (record-creating: no `works/` record existed). NOT `--novel`.
**Run:** 2026-06-13, in-session (accept-edits), from a written scope handoff. Model: Opus (main); sub-sweeps Sonnet; verifier Opus.
**Gates:** `--choice=reg --notes=auto`; `verify_quotes.py` 42/42 PASS (2 facsimiles OK); separate-pass verifier CLEAN-WITH-MINORS (0 critical, 0 major, 3 minor, all addressed or self-documented).

---

## Phase 0 — scope contract (confirmed in prose from the brief; not gated on a picker)

- **Question:** how *Не могу молчать* came to be written (the Kherson hanging, the failed phonograph dictation, the 13 May first draft); what it argues (the symmetric condemnation of state and revolutionary violence; the personal-complicity demand); how its public appearance was itself the story (Russian papers fined, the complete text only illegal/abroad); and how the drafting (draft №1 named Stolypin + Nicholas II; Chertkov's edits cut the most explicit "do the same to me" coda) bears on reading the personal-complicity argument as the centre.
- **Corpus surface:** works (main text `v37_083_096` + variants `v37_391_399`); comments (Eikhenbaum's editorial history `v37_425_427` + manuscript description `v37_427_432`); diaries (Tom 56, May–June 1908). PSS Tom 37 PDF = `jubilee-edition/vol06/vol06.pdf` (verified via `<book-title>`).
- **Marquee:** the personal-complicity argument — tested, not asserted.
- **Slug:** `1908-i-cannot-be-silent` (year-only, per brief).
- **Cross-links:** twin `1908-the-law-of-violence-and-the-law-of-love`; sibling `1908-a-letter-to-a-hindu`. Seeds the planned death-penalty theme-dive.

---

## Coverage ledger

| surface | status |
|---|---|
| The work's own text (all 7 chapters) | covered |
| Genesis & composition (trigger, phonograph, dates, people) | covered |
| Redactions & textual history (named draft, depersonalisation, Chertkov's edits) | covered |
| Publication, censorship & translation | covered |
| Reception & afterlife (Russian society/church first) | **partial** |
| Marquee question (personal complicity) | covered |
| Scholarly context | covered |
| Visual & manuscript record | covered |
| workRecord (record-creating) | covered |
| Independent corroboration of the Kherson execution | **not-covered** |

---

## Entity work-order (ingestion priority → dependency order)

The dossier `entities` block is the plan; wiki ingestion is a separate human-in-the-loop step. Present order:

**Priority 1 (central — write first):**
1. `I Cannot Be Silent` — wikiType `work` → routes to a NEW `works/` record (see workRecord), not a wiki page.
2. `Capital punishment in late-Imperial Russia` (concept, missing) — also the seed of the death-penalty theme-dive.
3. `Vladimir Chertkov` (person, **exists**) — editor/publisher; just needs this essay added.
4. `Pyotr Stolypin` (person, missing) — named in draft №1; field-courts context.
5. `Nicholas II` (person, missing) — named in draft №1.

**Priority 2 (supporting):**
6. `Nikolai Gusev` (person, missing) — secretary, copyist, diary-witness.
7. `Kherson execution of 8 May 1908` (event, missing) — dependsOn the capital-punishment concept. ⚠ no independent corroboration (needsReview) — do not assert as established fact.
8. `Field courts-martial (1906–1907)` (event, missing; could be concept) — dependsOn the capital-punishment concept.
9. `Non-resistance to evil by force` (concept, missing).

**Priority 3 (peripheral):**
10. `Free Age Press` (edition, missing) — dependsOn Chertkov.
11. `Aylmer and Louise Maude` (person/translator role, missing) — dependsOn Free Age Press.
12. `Ivan Ladyzhnikov` (person, missing) — identity unconfirmed (needsReview).
13. `Boris Eikhenbaum` (person, missing) — the PSS editorial-history author.
14. `Yasnaya Polyana` (place, **exists**).

---

## Visuals work-order

- **Committed (PD, in `extracts/`):** opening printed page (PSS Tom 37 p. 83) + first-manuscript autograph plate — both self-rendered from `vol06.pdf`.
- **Cached (PD, in git-ignored `visuals/`):** 7 Wikimedia Commons images — Prokudin-Gorsky colour (23 May 1908) + study shot, two Bulla 1908 portraits, Repin's Chertkov, Stolypin (1906), Nicholas II. Re-fetch: `python3 docs/fetch_visuals.py 1908-i-cannot-be-silent`.
- **To acquire / request (not located):** title-page facsimiles of the Free Age Press English edition, the Ladyzhnikov edition, and the censored Russian newspaper pages of July 1908 (research library / newspaper archive); a period photograph of N. N. Gusev (State Tolstoy Museum / Yasnaya Polyana archive); a manuscript facsimile beyond the first-page plate, incl. Chertkov's red-ink copy рук. №15 (State Tolstoy Museum).

---

## Work-record work-order (record-creating; for human ingestion into `works/`)

Propose a new record at `website/src/works/non-fiction/essays-and-criticism/i-cannot-be-silent/I Cannot Be Silent.md`. Full field set in `dossier.yaml` `workRecord`.

- **High confidence:** titleEn/titleRu, mainCategory (Non-Fiction), subcategory (Essays and Criticism), genre (essay), language (ru), completionStatus (complete), titleAlternatives (working title «О смертной казни»), dateWritingStarted (1908-05-26 NS / 1908-05-13 OS), publishedDuringLifetime (true), firstPublishedVenue + venueType (newspapers), bans[] (imperial-state, passages-cut), the OS sub-flags.
- **Medium/low confidence (flagged):** dateWritingCompleted (31 May OS author's date vs revisions to 15 June); `publishedInRussiaDuringLifetime: true` (only fined fragments were legal — a reviewer may prefer false-with-censorshipNotes); `dateFirstPublished` (OS/NS reconciliation: Russian fragments 4 July OS = 17 July NS vs worldwide 15 July NS); `excommunicationRelated: false`.
- **Ingestion note:** each `oldStyle:` sub-flag maps to the schema's named `<field>OldStyle` sibling key.

---

## notCovered (resume queue)

- Page-by-page collation of the permitted newspaper fragments vs. the censored whole.
- The full Chertkov edit-list as a complete editorial apparatus (~25 line-level changes).
- The 21 abusive + 60 sympathetic reader letters read individually (Gnatyuk covers the abusive set).
- Non-Russian translation lineage beyond the 1908 Maude / Free Age Press English text.
- The other Tolstoy capital-punishment articles → the planned death-penalty theme-dive (this dive seeds it).
- Independent archival confirmation of the Kherson execution.

## needsReview (deferred human judgement)

1. OS/NS publication dates — Russian fragments 4 July OS (=17 July NS) vs. worldwide 15 July (NS); ~2 days apart, sequence unresolved.
2. `publishedInRussiaDuringLifetime: true` edge case (fined fragments legal; whole illegal in Russia).
3. `bans[].scope = passages-cut` vs. complete-ban+confiscation.
4. No independent corroboration of the 8 May 1908 Kherson / Strelbitsky / Lubenko-estate hanging beyond Tolstoy's text + PSS.
5. Ladyzhnikov edition identity/imprint not independently confirmed.
6. "17 manuscripts" read off the description's numbering, not a stated total.
7. A. F. Koni and V. A. Molochnikov surface in the diary but are tangential to this essay (Koni → death-penalty theme-dive).
8. Edition title-page facsimiles not located.

---

## Evaluation self-assessment

- **Interlocutor sweep yielded people?** Yes — Chertkov (editor), Gusev (secretary/witness), Stolypin + Nicholas II (named in draft), Maude (translator), Ladyzhnikov + Eikhenbaum. ✓
- **Russian society/church reception covered?** Partial and honestly marked — censorship-as-reception, the 21+60 letters, Trotsky/Lenin/Kropotkin; no Synod statement on this essay specifically found. ✓ (partial)
- **workRecord fill accurate and provenanced?** Yes — every field evidence-anchored; edge cases flagged; field names/enums schema-checked by the verifier. ✓
- **Coverage honest?** Yes — Reception `partial`, Kherson-corroboration `not-covered`; no `covered` that is really partial (verifier confirmed). ✓
- **`--choice=reg` extracted cleanly?** Yes — no dropped pre-reform pairs, no recovered note-tails needed. ✓
- **Spine stayed bare?** Yes — verifier confirmed bare/factual voice, attributed scholarship, no asserted contested labels. ✓

---

## Outputs

- `docs/research/1908-i-cannot-be-silent/index.md` (+ generated `index.html`)
- `docs/research/1908-i-cannot-be-silent/dossier.yaml` (42 evidence rows, 14 entities, 9 visuals, scholarship, workRecord, coverage)
- `docs/research/1908-i-cannot-be-silent/extracts/` (6 PD txt extracts + 2 PD facsimiles + `_scholarship_reception.md`)
- `docs/research/1908-i-cannot-be-silent/visuals/` (git-ignored; 7 PD images + `_visuals_sweep.md`)
- `docs/research/1908-i-cannot-be-silent/session-log.md`, `_verifier-report.md`, this `run-report.md`
- `website/src/posts/notes/2026-06-13-i-cannot-be-silent.md` (draft: true)

**Rough cost note:** two Sonnet sub-sweeps (~142k subagent tokens combined) + one Opus verifier (~137k). Mechanical steps (extract/verify/render) ran locally at no model cost.
