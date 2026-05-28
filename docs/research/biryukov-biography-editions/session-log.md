# Session log — Biryukov biography editions

Working zone: `_generated/research/biryukov-biography-editions/`.
Polished output target: `docs/research/biryukov-biography-editions/` (created when content is ready to share).

---

## 2026-05-28 — open the project

Triggered by the TODO §8 "ch18 probe" session. The probe surfaced three things big enough to pause the mechanical recapture work and answer a higher-order question first: which edition of Biryukov's biography should be the citation reference, and what weight does the Swedish edition Johan owns (authorised, examined by Tolstoy) carry against the post-mortem Russian editions?

Background, source-of-record list of what was already established before this session opened, and the five buckets the session has to fill: see [handoff-2026-05-28.md](handoff-2026-05-28.md) (the orientation document for this whole project — written at the close of the previous session).

### Today's actions

1. **Scaffold the working zone** at `_generated/research/biryukov-biography-editions/`. Skeleton `index.md` with the six sections from the handoff (intro, Russian editions, Translations, Tolstoy's review involvement, Per-edition quality, Verdict). No published zone yet — born when content lands.
2. **Anchor the Swedish witness from photographs.** Johan presented two photographs at the start of this session: the title page of *Andra delen* and the closing page (Slutord, p. 453). Both transcribed and filed under `extracts/`. The rest of the bibliographic surface in Johan's three physical books still needs photographing.
3. **Direction set:** scaffold + Swedish first, then library catalogues. Execution mode: direct, escalating §3 (Tolstoy review involvement) and §5 (verdict) to Johan before they enter `index.md`. Per the lean-execution feedback and the handoff's explicit "do not auto-delegate the judgement calls."

### Open at end-of-session-1

- Photographs of Första delen 1 + 2 title pages, prefaces, TOCs, colophons.
- Photograph of Andra delen TOC and preface (if any beyond the Slutord already captured).
- Whether a Tredje delen exists in Swedish at all (Russian Vol III is post-Tolstoy, 1915; a Swedish translation would have been post-mortem). Libris is anti-bot blocked from WebFetch; a manual Libris check is the remaining cheap path.
- Library-catalogue sweep for the Russian first editions (§1 of the handoff).
- Translations catalogue (§2).

---

## 2026-05-28 — second half: WebFetch sweep + decisive findings

Six WebFetch / curl probes while Johan photographed. The big wins:

1. **Aldanov 1921 review of the Berlin Ladyzhnikov reissue** (text on az.lib.ru) — confirms Berlin 1921 = first-edition Vols I–III + one new chapter on Tolstoy's pre-marriage romance with a society lady whose surname was withheld. Otherwise no revision. Captured at [`extracts/aldanov-1921-review-berlin-ladyzhnikov.md`](extracts/aldanov-1921-review-berlin-ladyzhnikov.md).
2. **az.lib.ru Vol III preface** — two-layer text. Layer 1: 24 July 1909 from Ivanovskoye, three-volume plan, Tolstoy alive. Layer 2: 1 November 1915 from Onex près Genève, explicit decision to expand to four volumes with *Resurrection* (1899) as the III/IV boundary, "raw form" admission applies specifically to Vol III. Captured at [`extracts/az-lib-vol3-front-matter.md`](extracts/az-lib-vol3-front-matter.md).
3. **az.lib.ru Vol I preface (1906 first edition)** — Tolstoy's 2 December 1901 letter committing to "categorically answer" Birukoff's questions; S. A. Tolstaya's 19 July 1901 authorisation; the seven-year-period scheme as Tolstoy's own conception. The documentary base of the "granskade af Leo Tolstoj" claim. Captured at [`extracts/az-lib-vol1-roman-chapter-probe.md`](extracts/az-lib-vol1-roman-chapter-probe.md).
4. **"Глава 10. Роман" probe** — az.lib.ru Vol I part 2 already contains the pre-marriage-romance chapter with full Arsenyeva correspondence, regardless of edition source. Settles §1.5.

The §5 verdict crystallised by volume:
- Vol III: 1915 first edition is Birukoff's last word. az.lib.ru authoritative.
- Vol IV: 1922 Berlin is the only authorial edition. az.lib.ru authoritative.
- Vols I–II: az.lib.ru carries the Arsenyeva material regardless of provenance; minor residual risk that Berlin 1921 had a separate chapter on a different woman, not blocking.

Index updated to reflect the synthesis. Verdict in §5 is now draft-ready but still flagged "reserved for human checkpoint before promotion to `docs/research/`."

Blocked tools this session:
- WebFetch on `az.lib.ru` (TLS upgrade fails; fell back to `curl | iconv`).
- Libris (`libris.kb.se` returned access-denied to WebFetch — anti-bot).
- WorldCat (`worldcat.org` 403).
- Litres (`litres.ru` 404 on the author URL pattern).
- Google search (consent-page redirect from Sweden IP).

Surfaces remaining that should be cheap:
- RGB (`search.rsl.ru`) for Russian first-edition publisher and printing location.
- A Berlin 1921 scan (German national library / archive.org / a Russian émigré-archive index).
- The Cassell 1911 English edition full Publishers' Note (Internet Archive scan, readable).
- Once Johan's Swedish photos land: the title-page versos for years, prefaces for the authorisation phrasing, TOCs for chapter mapping, colophons for printer.

### End-of-session-2 status

- Scaffold and Swedish-witness extracts: done.
- Russian-editions catalogue (§1): substantially populated, one Aldanov-claim residual.
- Translations catalogue (§2): Swedish settled at the surfaces seen; English/Dutch sketched; German/French/Italian/Czech/Polish still pending.
- Tolstoy review involvement (§3): documentary base established from Vol I preface; ready for Johan-checkpoint review of the draft framing.
- Per-edition quality (§4): provisional table populated.
- Verdict (§5): draft state, per-volume, ready for Johan-checkpoint review before promotion to `docs/research/`.

---

## 2026-05-28 — session 2: scope expansion before verdict checkpoint

Johan re-framed the deliverable at session 2 open. The previous deliverable shape (an editions catalogue + per-volume verdict) was insufficient: he wants the overview document to also cover **(a)** the censorship / translation-validity question explicitly, **(b)** the roadmap to a "suitable English version of the biography for LLM-wiki ingestion," and **(c)** clarification of Vol IV's completion status (he was unsure whether Vol IV was ever finished — it was, 1922 Berlin, and the project has already translated it). He also paste-quoted the Slutord forward-flag from Andra delen p. 453, which contextualises Vol III's "raw form" 1915 admission as a literary-form issue rather than an evidentiary-weakness issue.

Decisions captured:

- **Scanning plan.** Johan to V850 full-scan Andra delen first (decided this turn). The 51 iPhone photos already cover textual-transcription needs; V850 scans give archive-grade text and OCR substrate. Further scans of the two Första delen häften are a likely follow-up but not committed.
- **Yellow-highlighted IMG_0605 passage:** Johan's own marking, not a textual signal. Disregard as a transcription priority.
- **Norstedt 1906/1909 Swedish edition is not rare on the second-hand market.** Johan acquired his copies that way; the witness value is functional (cross-check) not bibliographic-scarcity.
- **All §6 / §7 framing accepted** for inclusion in the working-zone `index.md`.

Edits this turn (all to `_generated/research/biryukov-biography-editions/index.md`):

1. **§0 framing:** explicit statement that all four volumes are complete authorial work, Birukoff lived nine more years after Vol IV without revising.
2. **§1.4 (Vol IV):** added explicit completion status — 15 December 1922 foreword, project's English translation done at commit `b90cb207`, no source revision implied by this research project.
3. **§2.1 (Swedish):** added availability note (non-rare on Swedish second-hand market, Johan's V850 scan of Andra delen queued).
4. **§3.4 → §3.5 split.** §3.4 stays as the per-volume scope-and-chronology bullet list; new §3.5 ("The Slutord forward-flag: Vol III was memoir-inflected by design") folds in the 27 August 1908 closing statement, with implications: Vol III's "different character" was planned in 1908 (Tolstoy still alive); the 1915 "raw form" admission therefore reads as a confession of editorial incompleteness, not of evidentiary weakness; Aldanov's qualified verdict on Vol III is consistent with the work still being authoritative; "Truth and love" is Birukoff's only on-the-record methodological statement across all three volumes. The original §3.5 ("Open §3 work") renumbered to §3.6.
5. **New §6 ("Censorship and translation validity"):** four-layer table (tsarist censorship, S.A.T. deference, émigré-press freedom, modern-reprint and OCR noise) with cross-check witnesses for each; explicit Scenario A vs. B for the Swedish edition's position (identical-manuscript-and-censorship vs. fuller-Swedish-manuscript); Cassell 1911 status as simultaneously translation, condensation, and original supplement; four standard footnote types for the project's English citation practice (source-of-record, censorship cross-check, validity cross-check, honesty footnote).
6. **New §7 ("Roadmap: a suitable English Birukoff for the LLM-wiki vault"):** eight-phase ladder (Vol IV translation done, Vol III translation done with chs 1–18 gap, this research project in progress, Vol III gap-recapture, Vol I/II RU audit, Vol I/II English translation, Swedish cross-check pass, vault ingestion); sequencing and parallelism notes; open questions that gate phases vs. parking-lot questions; budget summary (≈ 50–80 sessions for the new English translation effort, 3–6 months at one session per working day for the full ladder).

Headings now run §0, §1.1–1.8, §2.1–2.5, §3.1–3.6, §4, §5, §6.1–6.4, §7.1–7.4. Source-list and Related sections preserved at the end.

**Next:** bring the whole document (§5 verdict + the new §3.5 / §6 / §7 material) back to Johan for the sign-off checkpoint. Only then is promotion to `docs/research/biryukov-biography-editions/index.md` legitimate. Johan's V850 scan of Andra delen will produce its own follow-up extracts (under `extracts/swedish-andra-delen-v850/` probably) once it lands; the Scenario A/B disambiguation in §6.2 is the highest single research yield from it.

---
