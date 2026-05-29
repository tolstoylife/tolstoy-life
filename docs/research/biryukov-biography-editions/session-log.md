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

- **Scanning plan.** Johan to V850 full-scan Andra delen first (decided this turn). The 51 iPhone photos already cover textual-transcription needs; V850 scans give archive-grade text and OCR substrate. Further scans of the two Första delen häften are a likely follow-up but not committed. *(Reversed 2026-05-28 at session 3 close — see session 3 entry below: full workflow re-costed at 30–40 h, scan is parked.)*
- **Yellow-highlighted IMG_0605 passage:** Johan's own marking, not a textual signal. Disregard as a transcription priority.
- **Norstedt 1906/1909 Swedish edition is not rare on the second-hand market.** Johan acquired his copies that way; the witness value is functional (cross-check) not bibliographic-scarcity.
- **All §6 / §7 framing accepted** for inclusion in the working-zone `index.md`.

Edits this turn (all to `_generated/research/biryukov-biography-editions/index.md`):

1. **§0 framing:** explicit statement that all four volumes are complete authorial work, Birukoff lived nine more years after Vol IV without revising.
2. **§1.4 (Vol IV):** added explicit completion status — 15 December 1922 foreword, project's English translation done at commit `b90cb207`, no source revision implied by this research project.
3. **§2.1 (Swedish):** added availability note (non-rare on Swedish second-hand market, Johan's V850 scan of Andra delen queued). *(Note revised at session 3 close — scan now parked, see below.)*
4. **§3.4 → §3.5 split.** §3.4 stays as the per-volume scope-and-chronology bullet list; new §3.5 ("The Slutord forward-flag: Vol III was memoir-inflected by design") folds in the 27 August 1908 closing statement, with implications: Vol III's "different character" was planned in 1908 (Tolstoy still alive); the 1915 "raw form" admission therefore reads as a confession of editorial incompleteness, not of evidentiary weakness; Aldanov's qualified verdict on Vol III is consistent with the work still being authoritative; "Truth and love" is Birukoff's only on-the-record methodological statement across all three volumes. The original §3.5 ("Open §3 work") renumbered to §3.6.
5. **New §6 ("Censorship and translation validity"):** four-layer table (tsarist censorship, S.A.T. deference, émigré-press freedom, modern-reprint and OCR noise) with cross-check witnesses for each; explicit Scenario A vs. B for the Swedish edition's position (identical-manuscript-and-censorship vs. fuller-Swedish-manuscript); Cassell 1911 status as simultaneously translation, condensation, and original supplement; four standard footnote types for the project's English citation practice (source-of-record, censorship cross-check, validity cross-check, honesty footnote).
6. **New §7 ("Roadmap: a suitable English Birukoff for the LLM-wiki vault"):** eight-phase ladder (Vol IV translation done, Vol III translation done with chs 1–18 gap, this research project in progress, Vol III gap-recapture, Vol I/II RU audit, Vol I/II English translation, Swedish cross-check pass, vault ingestion); sequencing and parallelism notes; open questions that gate phases vs. parking-lot questions; budget summary (≈ 50–80 sessions for the new English translation effort, 3–6 months at one session per working day for the full ladder).

Headings now run §0, §1.1–1.8, §2.1–2.5, §3.1–3.6, §4, §5, §6.1–6.4, §7.1–7.4. Source-list and Related sections preserved at the end.

**Next:** bring the whole document (§5 verdict + the new §3.5 / §6 / §7 material) back to Johan for the sign-off checkpoint. Only then is promotion to `docs/research/biryukov-biography-editions/index.md` legitimate. *(See session 3 close: scan plan reversed; Phase 7 / §6.2 disambiguation now blocked on Swedish text capture by a route other than the V850 full scan.)*

---

## 2026-05-28 — session 3 close: V850 scan of Andra delen deferred

Late in the session Johan reversed the scan commitment from session 2.

- **Decision.** Andra delen will *not* be V850-scanned at this time.
- **Reason — corrected time estimate.** The session-3 handoff arrived at "~3 hours of scanner-active time across 2–3 sessions" — that figure covered only the scanner operating. Full workflow including post-production (Photoshop deskew / levels / dust pass, spread-to-singles split, Tesseract Swedish OCR with the ~5–10% pre-1906-orthography manual-correction pass, file organisation and metadata) lands at an estimated **30–40 hours** end to end. The earlier 3 h figure was therefore mis-leading as a planning number; the real cost is an order of magnitude higher.
- **Downstream impact.**
  - **§2.1 availability note** rewritten to flag the deferral and the corrected cost.
  - **§6.2 Scenario A vs B** marked as blocked on Swedish text capture (the disambiguation does not become wrong, only unreachable until text is in hand by some route).
  - **§7 Phase 7** Swedish cross-check pass: source column now flags "capture route TBD; V850 full scan deferred", and the §7.2 sequencing note that Phase 7 begins "once the V850 scan is in hand" is corrected to "once a clean Andra delen Swedish text is in hand."
  - **TODO.md** §8 and §9 unaffected (they were never premised on the Swedish scan).
  - **LOG.md** session-3 closing entry corrected: the recommended-workflow paragraph now records the deferral and the 30–40 h figure.
  - **`extracts/swedish-andra-delen-v850/` directory** (proposed under `_generated/...`) does **not** get created. The session-3 handoff's full settings + naming-convention block remains a usable blueprint if the scan is later un-parked, but is no longer an active work item.
- **What the 51 iPhone photos still cover.** Textual transcription for sample-scale work (Slutord, title page, any other page Johan re-photographs for a specific question). They do not cover a passage-level Swedish ↔ Russian diff at Vol II's full length; that's the part Phase 7 needs and that's the part now waiting on text capture.

**No new commit this turn.** Edits to this session-log, `index.md` (4 spots), and LOG.md (the existing session-3 entry's last paragraph) made directly; HTML rebuild via `docs/serve.py --build-only` to follow.

---

## 2026-05-29 — sign-off + Phase 7 path + Glava 10 batching

Johan worked through the four next-steps blocks the previous session had queued for him.

### Sign-off pass on the editions document

All four review blocks cleared on first read:
- **§5 verdict per volume** (per-volume disposition: az.lib.ru authoritative for III and IV; az.lib.ru working source for I–II with Aldanov reconciliation (3) flagged but not blocking; Swedish as cross-check, not replacement).
- **§3.5 Slutord reframing** (1915 "raw form" admission = editorial incompleteness, not evidentiary weakness, because the design was announced in the 1908 Slutord with Tolstoy alive).
- **§6.4 four footnote types** (source-of-record / censorship cross-check / validity cross-check / honesty footnote — to become standard in `translation-notes.md` files going forward).
- **§7 budget** (50–80 new translation-cadence sessions; 3–6 calendar months at one session/day).

Frontmatter flipped: `layer: draft` → `layer: reference`, `status: in-progress` → `status: settled`, `lastUpdated: 2026-05-28` → `2026-05-29`. Hedge wording softened in §0, §3, §3.6, §4, §5, §7.1 intro, §7.1 phase-3 table row, and §7.3 sign-off block. Grep-verified no stale "draft / reserved for human checkpoint / in progress" refs remain in the editorial surface (only substantive uses of "drafted" referring to Birukoff drafting his volumes in exile).

### Phase 7 path now that V850 is deferred

Decision: **digital-surrogate hunt first** (Project Runeberg, Litteraturbanken, Libris, Swedish second-hand digital stores) — 1–2 h catalogue probing. If it surfaces a usable Swedish digital surrogate of Andra delen, Phase 7 unblocks for free. If not, accept Phase 7 starts late; the partial-scope V850 scan (post-1880 chapters only, ~8–10 h end-to-end) stays as fallback only if Scenario A/B (§6.2) becomes a real downstream question.

Recorded in §7.2 of the index.

### Glava 10 / Aldanov reconciliation residual

Decision: **batch with the Phase 7 catalogue probe.** Same kind of motion (search Staatsbibliothek zu Berlin / DNB / archive.org Russian émigré collections / RGB-RNB for a 1921 Berlin Ladyzhnikov scan). One session, two open items closed; the Berlin 1921 hunt could surface useful side-evidence for §1's other open questions (1923 reissue, 1922–24 4-vol set, Diederichs German source-edition).

Recorded in §7.2 alongside the Phase 7 sequencing.

### Downstream unblocks

- **TODO §8 Step 1** (ch18 RU↔RU probe) unblocked. No source change required; az.lib.ru `text_1905_tolstoy05.shtml` is confirmed authoritative.
- **TODO §9** (Vol I/II audit) unblocked. az.lib.ru `text_1905_tolstoy01.shtml`–`04.shtml` is the working source; Aldanov reconciliation (3) flagged as known-open, not blocking.

### Memory + commit

Memory written: `project_birukoff_editions_verdict.md` (new) + MEMORY.md index entry. Captures the per-volume verdict + the location of the long form, so future sessions don't re-derive.

**Commit held** at Johan's request — changes staged in working tree but uncommitted, to bundle with whatever else lands later in the session or at end-of-day. The Phase 7 / Glava 10 catalogue-probing session is the natural next executable piece if Johan wants to keep going.

---

## 2026-05-29 — session 4: catalogue probe (Phase 7 + Glava 10 batched)

Johan picked path A from the post-sign-off handoff: the batched Phase 7 Swedish digital-surrogate hunt + the §1.6 Berlin 1921 Russian-scan hunt. Lean-execution mode. Scope discipline: locate-and-confirm, not capture-and-diff.

### Russian side — Berlin 1921 fully located, two new editions surfaced

- **All three Berlin 1921 Ladyzhnikov volumes** are OCR'd PDFs on vtoraya-literatura.com — publ-5548 (Vol I, 576 pp), publ-5598 (Vol II, 680 pp), publ-5599 (Vol III, 616 pp). Page counts vs. Egorov's lot 192 photographs (572 + 675 + 611 pp) drift by +4 / +5 / +5 pp, consistent across all three — front-matter / title-leaf counting variance, same edition with high confidence. Total ~109 MB; electronic editions by Andrey Nikitin-Perensky and Stanislav Lvovskiy.
- **1911 Moscow Кушнерёв second edition Vol I** at imwerden.de/publ-18037 — 544 pp, OCR PDF 24.86 MB, scan prepared by Алексей Балакин (acquisition 2026-01-24). Pre-S. A. Tolstaya death (1919), suppression layer still applies. Adds a third witness to the §1.6 Aldanov reconciliation probe.
- **1923 Moscow + Petrograd Госиздат third edition Vol I** at prlib.ru/item/1163574 — XX + 243 pp + 18 plates, «Издание 3-е, исправленное и дополненное». Anomalously small page count (vs. 576 pp Berlin 1921 Vol I) suggests partial-scope or split-volume; disambiguation against the actual title page is pending. Probable referent of the rumoured "1923 Berlin reissue" (§1.8) — misattribution candidate.

### Swedish side — clean negative at standard digital archives

No digital surrogate of *Hans lif och hans verk* at Project Runeberg, Litteraturbanken, Libris/KB, HathiTrust, archive.org, or Bokbörsen/hstrom. **Phase 7 stays parked** on Johan's physical books or the partial-scope V850 scan if/when Scenario A/B (§6.2) becomes a real downstream question. Remaining surrogate routes (Lund / Stockholm / Uppsala university digital collections, KB digitisation-on-demand) are out of scope for a 1–2 h probe and not on the critical path.

### Side refinements

- **§1.7** — two independent digital surrogates of the 2000 Алгоритм print: az.lib.ru (Adamenko 2003) and imwerden.de/publ-16339 (Nikitin-Perensky + Lvovskiy). Either can serve as an OCR-noise cross-check.
- **§2.1** — Erik Nordenström identified as artillery captain via Litteraturbanken's Rydström article. The "highly questionable 1910 translation" mentioned in passing in the same article concerns Gogol's *Döda själar*, **not** Birukoff — quality judgement does not transfer.
- **§1.1** — Swedish Norstedt edition year range locked to 1906–1909 (Erik Oskarsson Antikvariat Lund snippet).

### Plan deviations from session open

- Plan expected a 1–2 hit Berlin 1921 catalogue probe. Reality: full three-volume set located on a single archive, PLUS two unknown editions (1911 Кушнерёв, 1923 Госиздат) surfaced. Catalogue space is materially bigger than the §1.1 table reflected; positive plan-deviation.
- Plan expected an uncertain-yield Swedish surrogate hunt. Reality: clean negative at all easy targets. Phase 7 disposition firmed up.
- Plan said "no PDF downloads, locate-only." Held — no PDFs downloaded; the chapter-level Glava 10 diff is parked as a focused 1-session next-executable.

### Writeup

- New extract file: [`extracts/digital-surrogate-hunt-2026-05-29.md`](extracts/digital-surrogate-hunt-2026-05-29.md) — full probe transcript, URL table, negative-result table, next-session executable.
- `index.md` updates: §1.1 (table gains 1911 + 1923 rows, +5pp / Berlin URL annotations, "candidate-for-retirement" wording on the rumoured 1923 Berlin reissue, second-digital-surrogate note on the OCR row); §1.6 (Aldanov-reconciliation update note); §1.7 (two independent digital surrogates); §1.8 (Aldanov question marked executable; 1923 Berlin question downgraded; new questions on 1911 Кушнерёв Vol II/III and 1923 Госиздат scope); §2.1 (Nordenström translator profile); §7.2 (Phase 7 path / outcome / parking language); Sources list expanded with five new entries.
- Frontmatter `lastUpdated: 2026-05-29` unchanged (already from session 3).

**Commit still held** at Johan's request. The working tree now bundles session 3's sign-off + session 4's catalogue-probe edits in one atomic commit, to land when Johan calls it.

---
