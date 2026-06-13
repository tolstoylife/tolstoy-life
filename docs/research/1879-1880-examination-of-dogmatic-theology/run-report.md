# Run-report — `1879-1880-examination-of-dogmatic-theology`

Work-dive on Tolstoy's *Examination of Dogmatic Theology* («Исследование догматического богословия», 1879–80) — the demolishing second panel of the four-part religious project (A Confession → this work → the Gospel harmony → What I Believe), and the only un-dived member of that quartet. Run 2026-06-07, in-session unattended (the A-Confession-pilot model), medium visual intensity. Followed the handoff from the *Kingdom of God Is Within You* session, which named this as the "missing foundation stone."

## Scope contract (Phase 0)

- **Subject (work dive):** *Examination of Dogmatic Theology* (Исследование догматического богословия; émigré/English title «Критика догматического богословия» / *A Critique of Dogmatic Theology*). Slug `1879-1880-examination-of-dogmatic-theology` — year-prefixed by composition window; sorts before `1879-1882-a-confession`.
- **Corpus surface:** PSS Tom 23 — work pp. 60–303 (`v23_060_303_…xml`); commentary by V. F. Savodnik pp. 538–547 (`texts/comments/…`, the handoff's `texts/works/comments/` path was wrong). Composition-window letters Tom 63 (to N. N. Strakhov). **No diaries survive for 1879–80** (Tom 48 ends 1878-06-03; Tom 49 begins 1881-04-17) — verified, documented as a gap.
- **Composition window:** late 1879 – March 1880 (Old Style); substantial final revision Sept–Nov 1884.
- **Works record:** missing — the dive is the source-grounded basis to create it (cf. On Life).
- **Mode:** in-session unattended; no `AskUserQuestion` gating; judgment calls → `needsReview`; note `draft: true`; medium visual intensity.

## Headline event this run — an extract_tei.py byte-fidelity bug found and fixed

While extracting the genesis letters, the diff against the agent's output exposed a real bug in the shared extractor `docs/research/lib/extract_tei.py`: in `normalise_paragraph`, the pre-pass `node.clear()` on inline `<note>` elements also wiped each note's `.tail` (lxml `.clear()` clears tail), **silently dropping the Tolstoy prose that immediately follows a footnote anchor**. In THIS work alone it had been dropping **7 passages** of Tolstoy's own text (e.g. l.523 «И в самом деле, из того, что бог един, и неизмерим, и дух, и троичен, какое может быть нравственное приложение?»). Fixed surgically (preserve `node.tail` across the clear). Re-extraction of the work diffed as **purely additive** (7 recovered tails, same line count, no note bodies leaked); all committed extracts regenerated with the fix; verifier independently confirmed the fix is additive with 0 note-body leaks. **This is a shared-tool change — flag to Johan.** A background task (`task_39e6c20b`) was spawned to backfill the fix across prior dives' committed extracts (additive; verify_quotes should still pass for them).

## What was covered

- **Deep read** of the Вступление, all 17 chapters, and the Заключение — the demolition follows Makary's dogma order (knowability of God, Trinity, the divine attributes, creation/angels/Fall, original sin, providence, the divinity of Christ, redemption, the Church, grace, sanctification, the sacraments, relics/judgment). 20 keystone passages extracted byte-faithful, including the method ("learned it like a good seminarian"), the «сознательная ложь» charge, the recurring «бред сумасшедшего», the God "who fears men" (Zeus/Prometheus), the "how shall I live / why am I bad" substitution, the church as "a self-instituted hierarchy", the madman-with-a-tower-on-his-nose, the sacraments as "spells against toothache", the Chuvash-with-sour-cream, the horror at his own «кощунство», the conclusion's deadpan paraphrase, the censored Catherine/Peter passage, and the positive turn («Дело веры есть только жизнь по вере»).
- **Genesis** grounded despite the 1879–80 diary gap: the four-part-project origin (one treatise begun late 1879); the two 1880 Strakhov letters (29 Feb, 23 Mar — the only firm dateable witnesses, both extracted byte-faithful); the 1882 Solovyov-prompted inserted article folded into ch. XIII; the Sept–Nov 1884 revision provoked by Chertkov. All from the PSS Tom 23 commentary + Tom 63 letters.
- **Redactions:** the four manuscript witnesses (the personal first autograph; the chapter-divided third copy with Strakhov's marginalia; the base fourth copy once owned by M. A. Schmidt) summarized from the commentary; the title history («Исследование» restored vs the émigré «Критика»).
- **Publication/censorship:** Elpidine (Geneva 1891 / Carouge 1896, as «Критика»); «Свободное слово» Christchurch 1903; Russian printings Askarkhanov (partial) and Gertsik 1908; the 1911 S. A. Tolstaya / 1913 Sytin-Biryukov censorship cuts (the Catherine/Peter passage to dots, phrase softenings); Wiener's English (Boston 1904).
- **Scholarship** triangulated (5 entries) against Simmons ("least read … undeservedly"), Pål Kolstø's *Heretical Orthodoxy* (2022, ch. 3 — the only full study, an "against the grain" reading), Britannica, Wikipedia; the headline being that the "merely negative" framing is *complicated* by the book's own positive conclusion, and that the inherited English title "Critique" *contradicts* Tolstoy's «Исследование».
- **Visuals:** 6 PD images cached (keystone = Metropolitan Makary Bulgakov, the antagonist-text author; period Tolstoy 1880s + Kramskoy 1873; Strakhov; Chertkov; Filaret) + a committed PD English facsimile (Wiener 1904 vol. XIII title page + frontispiece, rendered from the local archive-org scan).

## Coverage ledger

| Surface | Status |
|---|---|
| Genesis & composition | covered (no 1879–80 diary; leaned on letters + commentary) |
| What the work says | covered |
| Redactions & textual history | partial (4 mss summarized from commentary; no «варианты» file collated) |
| Publication, censorship & translation | covered (1903 Christchurch ed. rests on commentary) |
| Reception & afterlife (Russian society + Church) | partial (no contemporary RU reception in corpus; not separately swept) |
| Place in the cluster | covered |
| The author's later verdict | partial (1902–03 reissue corrections; no separate later self-assessment swept) |
| Visual & manuscript record | covered (Elpidine «Критика» title page not openly found) |

## Entity work-order (ingestion priority → dependency)

**Priority 1 (central; write first):** Metropolitan Makary (Bulgakov) [person] — the antagonist-text author, MISSING. Leo Tolstoy EXISTS.
**Priority 2:** Tolstoy's four-part religious project (1879–84) [concept] — MISSING (ties the quartet + its dives together); N. N. Strakhov [person] — MISSING (genesis correspondent; overdue across A Confession / What I Believe / On Life dives). V. G. Chertkov [person] EXISTS (add the 1884-revision + 1903-edition roles).
**Priority 3:** Metropolitan Filaret (Drozdov) [person]; M. K. Elpidine [person]; Leo Wiener [translator]; Holy Synod [institution]; Vladimir Solovyov [person] — all MISSING. Yasnaya Polyana [place] EXISTS.

## Visuals work-order

Cached (PD, usable): Makary Bulgakov (keystone); Tolstoy 1880s photo; Tolstoy (Kramskoy 1873); Strakhov; Chertkov (Kramskoy); Filaret Drozdov. Committed PD facsimile (extracts/): Wiener 1904 vol. XIII title page + frontispiece ("A Russian Pope in Full Canonicals").
**To acquire (request from holdings):** a title-page facsimile of the **Elpidine «Критика» 1891 first edition** (the keystone publication artefact; PD by age, no open scan located — PY Rare Books has a catalogue image); an **M. K. Elpidine portrait** (none on Commons; try vtoraya-literatura.com / imwerden.de / Geneva archives).

## Work-record work-order (proposed fills for a NEW record)

**High confidence:** titleRu «Исследование догматического богословия» (Tolstoy's autograph title, restored by PSS); titleAlternatives («Критика…» variant; "A Critique of Dogmatic Theology" Wiener EN; "An Examination…" Britannica EN); dateFirstPublished 1891 + firstPublishedVenue (Elpidine, Geneva/Carouge, as «Критика»); publishedDuringLifetime true; censoredVersionExists true (+ censorshipNotes); samizdatCirculation true; identifiers.jubileeEdition.volumes 23.
**Medium/low:** titleEn "Examination of Dogmatic Theology" (or Wiener's "Critique" — human call); genre (proposed `religious`; Confession uses `essay` — needsReview); dateWritingStarted 1879 / dateWritingCompleted 1880-vs-1884 (needsReview); dateFirstPublishedInRussia 1908 Gertsik (vs Askarkhanov partial — needsReview); publishedInRussiaDuringLifetime true (censored only); bans (single imperial-censorship complete-ban; holy-synod entry arguable — needsReview); excommunicationRelated false (needsReview); relatedWorks [confession, what-i-believe, gospel-harmony] companion; manuscripts (4, summary). Folder (treatises) → human decision.

## needsReview (deferred human judgment)

1. `genre` — proposed `religious`; sibling Confession uses `essay` (schema enum has both + `philosophical`). Consistency call.
2. `dateWritingCompleted` — 1880 (composition) vs 1884 (final revision).
3. `dateFirstPublishedInRussia` — Askarkhanov (partial) vs Gertsik 1908 (fuller).
4. `bans[]` encoding — single imperial-censorship complete-ban vs adding a holy-synod entry (the work was never submitted in Russia; the "ban" is a standing unpublishability).
5. `excommunicationRelated` (proposed false) — the 1901 edict names no works; this is its fullest doctrinal target but not a named cause.
6. Makary's dogmatics — 5 vols 1849–53 (PSS commentary) vs 6 vols 1847–53 (web reference works); attribute to the commentary, note the divergence.
7. The genesis/publication/censorship/manuscript facts are from the PSS Tom 23 commentary (Savodnik), not byte-extracted PD documents — attribute, don't byte-claim.
8. The 23 March 1880 Strakhov letter's subject — the corpus TEI note reads its "work" as the Gospel examination; the Tom 23 commentary reads it (with a caveat) as the dogmatic theology. Logged in `contradictions`; index.md now carries the caveat at point of use.
9. **extract_tei.py note-tail fix (2026-06-07)** — a shared-tool change (see headline above); prior dives' extracts predate it (backfill task `task_39e6c20b` spawned). Flag to Johan.

## Verification

- `verify_quotes.py` → **22/22 verbatim PASS** (re-run after the nit edits). No superscript-marker or guillemet issues; the genesis-letter quotes avoid the footnote-anchor positions.
- Phase-5 verifier (opus, fresh context) → **PASS-WITH-NITS, 0 must-fix, 3 nits**, all resolved before commit. It re-ran verify_quotes, re-extracted the source XML from scratch and diffed IDENTICAL, loose-matched every entity's vaultStatus (3 exists / 8 missing all confirmed, transliteration gotcha checked), validated all 18 workRecord field names + enum values against the works schema, and confirmed the extract_tei.py fix is additive with 0 note-body leaks. **Nits applied:** (1) softened "COMMITTED PD facsimile" wording (now committed, so true); (2) Wiener wikiType `person` → `translator` (the schema has a dedicated translator type — Maude/Garnett's category); (3) added the 23-March-letter subject caveat at point of use in index.md (was only in the dossier). Report: `_verifier-report.md`.

## Evaluation self-assessment (work-dive gate)

- Interlocutor sweep yielded people? **Yes** — Metropolitan Makary (the central new figure, the antagonist-text author), Strakhov, Chertkov, Filaret, Elpidine, Wiener, Solovyov, plus the Holy Synod and the four-part-project concept, all carried into `entities`. (Genesis was people-thin by nature — a solitary, polemical work written in a diary-less period.)
- Russian society/Church reception covered? **Partial, honestly** — the censorship history (the cut Catherine/Peter passage; the unpublishability) is covered; contemporary Russian critical reception is genuinely absent from the corpus (the work circulated abroad / in manuscript) and was not separately swept — marked `partial`, not padded.
- `workRecord` fill accurate & provenanced? **Yes** — every field evidence- or commentary-anchored; the title restoration, the bans/censorship, and the publication chain attributed; uncertain fields → `needsReview`. Verifier-confirmed against the works schema.
- `coverage` honest? **Yes** — three surfaces marked `partial` with candid reasons (verifier-confirmed nothing over-graded).
- `--choice=reg` extracted cleanly? **Yes** — pre-reform resolved across the work and the two letters; `--notes=auto` used. AND a latent `.tail`-dropping bug in the extractor was caught and fixed here (see headline).
- Spine stayed bare? **Yes** — "merely negative" and the 1901-excommunication link attributed to the mainstream and complicated by the primary text; commentary facts attributed throughout (verifier-confirmed no editorializing voice).

## Models & rough cost

Main loop: Opus (in-session) — Phase 0 recon, the Вступление/Заключение close read, the dossier + index.md synthesis, the extract_tei.py bug diagnosis/fix, and the nit fixes. Subagents: deep-read (opus, ~272k tokens — the 17-chapter map); genesis-letters (sonnet, ~42k); visuals (sonnet, ~27k — 6 Commons fetches); scholarship (sonnet, ~59k — 15 sources, web); verifier (opus, ~100k). No spend-limit interruption this run (unlike On Life). No licence-gated downloads to `website/src/`.

## Output paths

- `docs/research/1879-1880-examination-of-dogmatic-theology/index.md` (+ rendered `index.html`, git-ignored)
- `docs/research/1879-1880-examination-of-dogmatic-theology/dossier.yaml`
- `docs/research/1879-1880-examination-of-dogmatic-theology/extracts/` (PD only — work text; Strakhov letters 29 Feb & 23 Mar 1880; 2 Wiener-1904 PD facsimiles)
- `docs/research/1879-1880-examination-of-dogmatic-theology/visuals/` (git-ignored cache; 6 PD images)
- `website/src/posts/notes/2026-06-07-examination-of-dogmatic-theology.md` (draft)
- `_verifier-report.md`, this `run-report.md`
- `docs/research/lib/extract_tei.py` (note-tail byte-fidelity fix — shared tool, flag to Johan)

Wiki ingestion is a separate, human-in-the-loop step — this dossier is the pointer, not the writer.
