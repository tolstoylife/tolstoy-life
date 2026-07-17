# Handoff — A Confession, Stage B: build the reader edition (Wiener, 16)

Johan decided on 2026-07-17: **Wiener 1904 is the English reading text; 16
sections.** The planning is done (Stage A complete, plan referenced below) —
this session builds. Don't re-plan, don't re-open the two decisions.

**Branch: `great-sin-redive-pass2`** — the road kit, the decisions, and all of
July's work live here, not on `main`. A cloud session must select this branch
when opening the repo.

**Where you are running matters:**

- **Cloud session (GitHub clone):** everything needed for the *text* work is
  tracked and pushed — see Materials. Audio and anything under
  `primary-sources/` are out of reach; leave those steps for a Mac session.
- **On the Mac (Dispatch or local):** everything is available, including audio.

## The two decisions, and one lucky fit

- **Wiener 1904** — "My Confession", *The Complete Works of Count Tolstoy*
  vol. XIII, Dana Estes & Co., Boston. The decision sheet
  (`_generated/research/session-confession-prep-2026-07-11/decision-sheet.html`,
  local-only) had recommended Maude for source cleanliness; Johan chose Wiener
  for historical closeness — it appeared in Tolstoy's lifetime, and Tolstoy
  corresponded with Wiener about the edition (see the record below).
- **16 sections**, matching the Russian: the 1882 dream stays inside ch. XVI.
- Verified during prep: **Wiener also prints the dream as the tail of XVI with
  no separate heading** — the same shape as the Russian. The "fold Maude's
  Afterword back" step from the decision sheet is moot; both texts are
  natively 16. Alignment should be natural.

## Materials (tracked & pushed)

- **Russian backbone:** `docs/research/works/non-fiction/personal-papers/1879-1882-a-confession/extracts/v23_001_059_Ispoved.txt`
  — PSS 23, pp. 1–59, `[head]`-marked chapters I–XVI. The 2026-07-11 prep
  re-extracted with current settings and got a byte-identical result, so this
  tracked copy is the verified current text.
- **Wiener English:** `_generated/research/session-confession-road-prep-2026-07-17/wiener-1904-my-confession.md`
  — full capture from the local site-mirror epub, 16 chapters, provenance +
  fidelity header. **One repair, clearly marked:** the e-text lacked the "XI."
  heading (X and XI ran together); it was restored at the paragraph matching
  the Russian XI opening. Collate against the printed page when back on the
  Mac (or via archive.org) — a capture note sits at `## XI` in the body.
- **The plan:** `_generated/Fable-plan-a-confession-reader-edition.md` —
  Stage B steps live there. Force-added to the repo for road access.
- **Worked example:** the Great Sin bundle,
  `docs/reader/non-fiction/essays-and-criticism/the-great-sin/` — file naming,
  meta shape, overview voice. The engine is `docs/reader/assets/` +
  `docs/reader/index.html`; `docs/serve.py --build-only` renders the docs site.
- **Bundle destination:** mirror the work's live-site placement (per the
  corpus-dive placement rule): `docs/reader/non-fiction/personal-papers/a-confession/`.

## Only on the Mac

- **Audio** — Kokoro pipeline in `projects/audiobook/` (own repo, not on
  GitHub). Runs last anyway; hours of rendering.
- **`primary-sources/`** (gitignored): the Wiener source epub
  (`site-mirrors/tolstoyarchive.org/Non-fiction/files/My Confession.epub`),
  the Maude witness (`standard-ebooks/leo-tolstoy_a-confession_aylmer-maude.epub`),
  the TEI corpus for any re-extraction, and page scans for collating the XI repair.

## Held for Johan's nod even mid-build

The small settings file that marks the chosen translation as the site default —
first of its kind in the vault; show him before writing it (flagged in the
decision sheet).

## The Tolstoy↔Wiener record (found in this prep session; written nowhere else yet)

From the corpus's "Tolstoy and his contemporaries" encyclopedia entry
(`primary-sources/tolstoydigital-TEI/tolstoy_and_his_contemporaries/burnasheva_Viner_Lev_Solomonovich_3_918.xml`,
Mac-only path):

- 21 Nov 1904: Wiener wrote to Tolstoy asking for works he couldn't obtain in
  America («Часовщик», «Первый винокур», «Церковь и государство», the Ge
  picture text, and others).
- 19 Dec 1904: Tolstoy replied (PSS 75:193): «Очень приятно было узнать, что
  перевод моих сочинений доставил вам удовольствие и некоторую пользу.
  Постараюсь собрать недостающие вам вещи и на днях вышлю их вам» — warm and
  cooperative, but not a verdict on the translation itself. A further reply is
  registered ~March 1905.
- Makovitsky attests Wiener's English edition was **not** in the Yasnaya
  Polyana library (ЯПЗ 2, p. 293).
- Chertkov had no hand in the edition; *A Confession* was in the
  renounced-copyright set, so none was needed.

**Follow-up owned by Stage B:** fold a two-sentence version of this into the
dive's "Publication, censorship & translation" section
(`docs/research/works/non-fiction/personal-papers/1879-1882-a-confession/index.md`)
— it grounds the edition choice and belongs with the 1885/Dole/Maude history
already there.

## The standing intent — project versions "as Tolstoy wanted"

Johan's new standing direction (2026-07-17): beyond the published-translation
editions, the project will create **its own English versions, as close to what
Tolstoy intended, for all Prophet-period texts** — starting with A Confession.
Recorded in memory (`project_tolstoy_intended_versions`) and TODO §10. What it
means for this build: Wiener is the published witness and ships first; the
project translation comes later as a second English (the bundle format
supports versions side by side). The title question is part of the intent:
«Исповедь» was never Tolstoy's title — the manuscripts carry «Что я?» (What
Am I?) and «Как я потерял смысл жизни и в чём нашёл его» (How I Lost the
Meaning of Life and Where I Found It).

## Suggested skills

- `lean-execution` — this is a build with an existing plan.
- **Not** `corpus-dive` — the dive exists; only the small Wiener note (above)
  gets added to it.

## Reference

- Plan: `_generated/Fable-plan-a-confession-reader-edition.md`
- Decision sheet (local-only): `_generated/research/session-confession-prep-2026-07-11/decision-sheet.html`
- Reader-editions workflow memory: `project_reader_editions_workflow`
- Great Sin pilot: `docs/reader/non-fiction/essays-and-criticism/the-great-sin/`
