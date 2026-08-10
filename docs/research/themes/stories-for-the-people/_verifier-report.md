# Verifier report — Stories for the People (народные рассказы)

Adversarial verification pass, fresh context, 2026-06-11. Subject:
`docs/research/stories-for-the-people/`. Mechanical gate (`verify_quotes.py`)
re-run independently below.

---

## Check 1 — Byte-fidelity sample (8–10 quotes)

**PASS.** Re-derived 10 evidence quotes directly from their extract files with
`grep -c` (exact-substring match = 1 in every case), and cross-checked the
date/addressee/Tom attribution against each extract's `# bibl:` header.

| id | quote spot-check | attribution check |
|---|---|---|
| E05 (1883 diary) | verbatim ✓ | entry header «Дневник, 11 июня 1883 г.» + opener «11/23 июня» → 1883 confirmed (see note) |
| E18 (Sytin transfer) | verbatim ✓ | header: В. Г. Черткову, 10–11 мая 1885, Т. 85 С.193–196 ✓ |
| E19 (глубже в народ) | verbatim ✓ | header: Черткову, 10–11 мая 1885, Т. 85 С.196–199 ✓ |
| E20 (как можно дешевле) | verbatim ✓ | v85_077, 29–30 Aug 1885 ✓ |
| E31 (Tikhon verdict) | verbatim ✓ | v25_715–719 apparatus ✓ |
| E40 (1910 letter) | verbatim ✓ | header: И. И. Горбунову-Посадову, 24 окт 1910, Т. 82 С.206–210 — matches dossier `pages: 206–210` ✓ |
| E42 (ChLZ keystone) | verbatim ✓ | v25_007–025 ✓ |
| E48 (Ivan callus) | verbatim ✓ | v25_115–138 ✓ |
| E07 / E08 (Речь) | verbatim ✓ | v25_523–529 ✓ |
| E09 (Цветник) / E34 (French) | verbatim ✓ | v26_307–309 / v64_268 ✓ |

Independent `verify_quotes.py docs/research/stories-for-the-people/dossier.yaml`:
**SUMMARY: 50/50 quotes verbatim, 1 facsimile ok, 0 missing, 0 skipped, 0 label
warnings — PASS.**

Note (not a defect — the dive got it right): the E05 extract's `# bibl:` line
mislabels the source as «Дневник 1884 г.» while the entry itself is 11 June
**1883** (header + «11/23 июня» opener). This is the documented TEI
diary filename-year gotcha. The dive correctly dated E05 to 1883-06-11
everywhere (dossier, index §2, diary table). Trap avoided.

## Check 2 — Source-anchoring

**PASS.** Every primary claim in `index.md`'s own voice carries an `(Enn)`
ref or names its source inline. All six "Key findings" bullets cite E-refs
(E11, E05/E06, E08/E09/E10, E19/E20/E25, E29–E33, E21/E40). Numeric/factual
claims audited: "900 rubles, at 1½ kopecks per copy" → anchored to E18 (line
94); "circulation in the millions by the late 1880s" → attributed to Brooks
1985, not asserted as primary. No bare unanchored factual assertion found.

Good discipline note: the dossier `needsReview` flags a 60,000-vs-600,000
print-run arithmetic discrepancy on the E18 transfer; the index voice avoids
that contested number entirely and uses only the attributed aggregate.

## Check 3 — Attribution discipline

**PASS.** Scholarly claims are attributed throughout: "Jahn (2002)…",
"Brooks (1985)…", "Christian (1969)", "McLean (2005/2008)", "Wilson 1988",
"Bartlett 2010". Every secondary name has a References entry (verified against
§References primary/background lists). Gap claims ("no accessible scholarship
cites the 1910 grading letter") are framed as absence-of-coverage, not as
contested assertions in the dive's voice. The "didactic decline" frame is
explicitly attributed to popular biography rather than asserted or rebutted in
project voice. No contested label asserted as fact.

## Check 4 — Translations

**PASS.** 17 blockquotes in `index.md`, 17 `(working English)` renderings — a
clean 1:1. Both French quotes (E34, E35) carry "(working English)" with a
"[from the French original]" tag. No untranslated Russian/French quote.

## Check 5 — Voice

**PASS.** Simple, factual, minimal editorial. The marquee finding ("the
tension is the finding") is stated as an observed contradiction between two
primary records, not as editorial flourish. "demonstrably reached its
audience" is backed by the attributed Brooks circulation figure. No purple
prose; no unattributed superlatives detected. One mild rhetorical cadence
("the gesture is unmistakable", §8) but it is anchored to E40 and stays
factual.

## Check 6 — Dossier integrity

**PASS.** 
- `scholarship.triangulation`: 8 entries, all `evidenceRef`s valid (E01, E05,
  E11, E18, E30, E31, E34, E40); relations all in enum (5 extends, 2
  complicates, 1 confirms — no invalid values).
- entities: 23 total, wikiTypes all valid (19 person, 2 concept, 2
  institution).
- vaultStatus honesty: `Vladimir Chertkov` = exists → file present ✓;
  `Pavel Biryukov` (entity name) = exists with `wikilinkTarget: Pavel Birukoff`
  → `Pavel Birukoff.md` present ✓ (transliteration gotcha correctly handled).
  All others marked `missing` confirmed absent — broad transliteration scan
  (repin/ge/leskov/sytin/gorbunov/shchegol/afanasyev/tikhon/… ) found no
  shadow pages in the 14-page vault. No false `missing`, no false `exists`.
- coverage statuses honest: items marked `partial` (redactions, thick-journal
  reception, peasant-reader reception, translation reach, visual record) each
  carry an accurate note explaining the gap; nothing marked `covered` that is
  really partial.

## Check 7 — workRecords

**PASS (with one enum caveat correctly self-flagged).** Six proposals; field
names match `tolstoy-works-schema.md` v9:
- flat keys (titleRu/titleEn/mainCategory/subcategory/genre/dateWriting*/
  firstPublishedVenue/publishedDuringLifetime/epigraph*/identifiers.jubilee…) ✓
- `bans[]` object shape correct: banningAuthority / authorityType /
  jurisdiction / scope / banDate / banDateOldStyle / banDateApproximate /
  banLiftedDate… ✓ — `scope` values used (`confiscation`, `complete-ban`) are
  in the v9 enum.
- `relatedWorks` = `{id, relationshipType}` with `cycle` (valid enum) ✓
- date sub-flags `oldStyle` / `approximate` present where used ✓

OS→NS conversions correct (19th c. = +12 days): WMLB ban 1887-02-04 OS →
1887-02-16 NS ✓; ban 1887-10-10 OS → 1887-10-22 NS ✓; Where Love writing-start
1885-03-17 OS → 1885-03-29 NS ✓.

create/fill targets verified against the live `works/` tree: all 5 `create`
targets (what-men-live-by, where-love-is-god-is, two-old-men,
tale-of-ivan-the-fool, the-three-hermits) are absent (correct for `create`);
`how-much-land-does-a-man-need` exists (correct for `fill`).

The two CORRECTION fills are justified: the existing
`How Much Land Does a Man Need?.md` record currently carries
`publishedDuringLifetime: false` and `publishedInRussiaDuringLifetime: false`,
which is wrong — the tale was published in «Русское богатство» 1886 (in Russia,
during Tolstoy's lifetime). The dossier's flip to `true`/`true` is correct.

Enum caveat (already flagged, not an error): `genre: fairy_tale` proposed for
Ivan the Fool is NOT in the schema v9 genre enum. The workRecord note itself
says "fall back to short_story if fairy_tale is not in the enum" and the
`needsReview` block flags it. Honest; ingestion must apply the fallback.
Confidence levels are sane (high for titles/publication facts, medium for
approximate dates and the disputed Ivan-the-Fool venue).

## Check 8 — Rights

**PASS.** `extracts/` holds exactly one committed image: the PD facsimile
`facsimile-v25-p007-chem-ljudi-zhivy-018.png` (rendered from the local Jubilee
PDF). `visuals/` is git-ignored — `docs/.gitignore` line 18 (`research/*/visuals/`)
covers it, and `git ls-files` confirms zero tracked files under
`visuals/`. All 12 dossier visuals carry `licence: PD` + `rights: PD` (12/12).
The two undigitised targets (Posrednik covers; Ge album) are `localPath: null`,
`usable: with-clearance`, not committed. Nothing placed in `website/src/`
except the draft note. No rights-reserved image committed.

## Check 9 — Note

**PASS.** `website/src/posts/notes/2026-06-11-stories-for-the-people.md` has
`draft: true`. Claims consistent with the dive: parable-form genesis from the
1883 diary, the «как можно дешевле» pricing, the Feb-1887 arrests, and the
1898-vs-1910 self-verdict contradiction ("nine of the tales in the top grade")
all match index.md. The "six work-record proposals" and "23-entity routing
map" counts match the dossier.

## Check 10 — nl2br discipline

**PASS.** All 17 blockquotes are single physical source lines (verified by
line-by-line inspection — no `>`-line breaks mid-sentence). Prose paragraphs
(incl. the longest at 1156 and 1143 chars: the scholarship and Method
paragraphs) are each a single line, which is the correct shape for the site's
nl2br rendering. No hard-wrapped paragraph that would emit ragged `<br>`s.

---

## Issues found

1. **[MINOR — provenance pointer]** `dossier.yaml:958` —
   `visuals[].localPath: extracts/facsimile-v25-p007-chem-ljudi-zhivy-18.png`
   is missing a zero. The actual committed file, the `index.md` `<img src>`
   (line 238), and the `E41.facsimile` key (dossier:577) all correctly say
   `…-018.png`. `verify_quotes.py` still passes because its facsimile check
   reads the E41 `facsimile:` key, not the `visuals[]` `localPath`. But
   `fetch_visuals.py` / any provenance consumer that trusts the `visuals[]`
   block will point at a non-existent file. One-character fix: `-18` → `-018`.

2. **[MINOR — directory hygiene]** `extracts/.omc/state/` contains three agent
   telemetry files (`mission-state.json`, `subagent-tracking.json`,
   `agent-replay-*.jsonl`). These are not PD source material and not
   `_`-prefixed deliverables — they are stray run artifacts inside the
   committed `extracts/` dir. Content is harmless (no rights issue), but they
   should be removed or git-ignored before the dive is committed, so the
   extracts/ channel stays "PD text + the one facsimile" only.

Neither issue touches quote fidelity, rights, schema correctness, or any
published-surface (`website/src/`) content. Both are pre-commit cleanups.

---

## Overall verdict

**2 issues (both MINOR, non-blocking): (1) `dossier.yaml:958` facsimile
`localPath` missing a zero (`-18.png` → `-018.png`); (2) stray `extracts/.omc/`
agent-telemetry files should be removed or git-ignored before commit.**
Every load-bearing check — 50/50 byte-fidelity, source-anchoring, attribution,
translations, voice, dossier integrity, workRecord schema + OS→NS conversions +
the two justified CORRECTION fills, rights/PD discipline, the draft note, and
nl2br — PASSES.
