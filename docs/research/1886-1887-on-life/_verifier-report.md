# Independent verifier report — On Life («О жизни») corpus-dive

Verifier: independent pass, fresh context. Date: 2026-06-06.
Scope: the judgment-level checks the byte-fidelity script cannot make. The mechanical
gate (`verify_quotes.py`) was re-run here and re-confirms **23/23 PASS**.

---

## 1. Byte-fidelity spot check (work / lecture / diary / letter)

Independently re-derived (Python `in` substring test, not via the dive's script) for a
sample spanning all four genres:

| Evidence id | Genre | Extract | Result |
|---|---|---|---|
| onlife-text-07 (Schopenhauer/Hartmann) | work | v26_313_442 | exact substring ✓ |
| onlife-text-04 (reason = law, ch. X) | work | v26_313_442 | exact substring ✓ |
| onlife-text-11 («нет смерти») | work | v26_313_442 | exact substring ✓ |
| onlife-ponjatie-01 / -02 (lecture) | lecture | v26_881_885 | exact substring ✓ |
| onlife-diary-02 (Разум — любовь — Бог — природа) | diary | v49_127_129 | exact substring ✓ |
| onlife-let-02 (title change) | letter | v64_148 | exact substring ✓ |
| onlife-let-03 (censorship) | letter | v64_181 | exact substring ✓ |

Footnote-marker / digit / elision scan on a further sample (text-03, -06, -09, -12):
no superscript markers, no stray digits, no quotes stitched across an unmarked elision.
Extracts carry only PD Tolstoy text with a byte-fidelity PSS bibl header; no editorial
commentary, copyright, or publisher markers found in any extract file.

**OK.** No must-fix.

## 2. Primary claims anchored

Spot-checked the load-bearing primary assertions in index.md ("What the work says",
"The shape of the question", "Genesis"): each is tied to a cited Tom-26 / Tom-49 /
Tom-64 quote or to the apparatus. The "instrument of life" claim is anchored — the
extract reads «животная личность для человека есть то орудие, которым он работает»
immediately before the cited spade passage. The genesis correction (June-1886 diary
precedes the Dieterichs letter) rests on onlife-diary-01/02, both byte-verified.

**OK.** No must-fix.

## 3. Secondary claims attributed, not asserted

- Medzhibovskaya & Denner, Gustafson, Soina, Simmons, Bartlett: attributed inline in
  "Scholarly context" and the dossier `scholarship` block.
- Genesis / censorship facts from the PSS commentary (Gusev) are attributed, not
  presented as byte-verified primary: "The PSS commentary names…", "The PSS commentary
  calls her the 'immediate instigator'", "recorded in the PSS commentary from
  N. Apostolov's reading of Synod file No. 2264." "PSS commentary" / "the commentary"
  appears 10×; Apostolov 2×. The dossier header and `needsReview` explicitly mark these
  as apparatus-sourced, not byte-checked.
- The «не слово Божие, а единственно… человеческий разум» Synod-report phrase is
  presented as a commentary-reported quotation, not as a byte-verified evidence row
  (it is not in the evidence ledger). Correct handling.

**OK.** No must-fix.

## 4. Voice

- Contested label **"mysticism"**: handled by attribution — the dive *rejects* the
  framing using Tolstoy's own words («страшное слово: мистицизм?» — which he denies),
  the primary text (reason as law), and the Synod's stated reason for the ban. Not
  adopted as the dive's own pejorative.
- "Pharisees, that is, our clergy" is a quoted phrase from Grot, attributed ("he wrote").
- No "reactionary", "heretic", "woolly", "crank", "obscurantist".
- **NIT:** "Soina reads it, **rightly**, as rational ethics… not mysticism." The adverb
  "rightly" endorses a secondary scholar's reading in the dive's own voice — the
  structural equivalent of the sibling dive's unattributed "reactionary" (an adopted
  stance rather than a pure attribution). The underlying point is independently
  grounded in the primary text, so this is a tone slip, not a factual error. Suggest
  dropping "rightly" (or recasting as "consistent with the primary text, Soina reads…").

**PASS-WITH-NIT** (1 nit).

## 5. Scholarship triangulation

- All 7 `triangulation[].evidenceRef` values resolve to real evidence ids
  (onlife-diary-01 ×2, text-04, text-07, text-08, ponjatie-01, let-03).
- All 6 `relation` values are in {confirms, complicates, contradicts, extends}.
- All `evidenceRefs[]` lists across entities and visuals resolve — zero dangling refs.
- **Headline claim verified against the extract.** onlife-text-07's surrounding context
  in v26_313_442 confirms Tolstoy NAMES Schopenhauer and Hartmann as "отрицательные
  философы нашего времени" who "отрицающие жизнь и все-таки остающиеся в ней," calls
  their resolution "недобросовестно" (in bad faith), and contrasts it with his own
  exit (love) — a genuine refutation, not an echo. The "complicates/contradicts"
  framing of the Schopenhauer-restatement reading is supported.

**OK.** No must-fix.

## 6. Entities

- Every entity has a valid `wikiType` (all 20 ∈ the allowed set).
- vaultStatus spot-checked against `website/src/wiki/` (16 files):
  - EXISTS claims all correct: Leo Tolstoy.md, Vladimir Chertkov.md, Sophia Tolstaya.md,
    Yasnaya Polyana.md — all present.
  - **MUST-FIX:** **P. I. Biryukov** is marked `vaultStatus: missing` with
    `wikilinkTarget: "Pavel Biryukov"`, but the vault already contains
    `Pavel Birukoff.md` (titleRu: Павел Иванович Бирюков, id: pavel-birukoff) — the same
    person under the project's "Birukoff" transliteration. The status should be `exists`
    and the wikilinkTarget should be `Pavel Birukoff` (the actual filename), or the
    ingestor will create a duplicate page. (Note: per project memory, the Biryukov vault
    page is a known fixture; the dive's spelling drift caused the miss.)
  - All other `missing` claims confirmed (no Grot, Strakhov, Anna Chertkova, Ozmidov,
    Alekseev, Obolensky, Hapgood, Elpidine, Moscow Psychological Society, or any of the
    four concepts/two events in the vault).

**FAIL on this check — 1 must-fix (Biryukov vaultStatus).**

## 7. Work-record

- **No existing On Life record** under `website/src/works/` — confirmed (searched
  on/life, zhizni, жизни). Confession exists at personal-papers/confession/;
  Kingdom of God at treatises/. The "no works/ record yet" claim is true.
- Field names mirror the works schema (titleAlternatives, firstPublishedVenue,
  publishedInRussiaDuringLifetime, samizdatCirculation, excommunicationRelated,
  censoredVersionExists, bans[], identifiers.jubileeEdition.volumes, relatedWorks[]).
- **Ban date internally consistent:** 5 April 1888 OS + 12-day 19th-c. Julian offset =
  17 April 1888 NS. Dossier `banDate: 1888-04-17` / `banDateOldStyle: 1888-04-05`
  matches exactly.
- `bans[].authorityType: holy-synod` — valid (∈ schema set).
- `relatedWorks[].relationshipType: sequel` — valid (∈ schema set; the note already
  flags "companion" as a possible better fit).
- **NIT:** `bans[].scope: banned-and-destroyed` is NOT in the schema's controlled
  vocabulary for `scope` (complete-ban · passages-cut · serialization-refused ·
  confiscation · pre-publication-rejected). Closest valid value: `complete-ban`
  (optionally + `confiscation`). The dive is honest about this — it routes the value to
  `needsReview` and the field note says "Verify the controlled value for `scope`…
  (proposed banned-and-destroyed)." The only blemish is the field note's lead word
  "Schema-clean:" immediately preceding a proposed non-schema value, which slightly
  overclaims. Downgrade to NIT because it is explicitly flagged for human review, not
  asserted as final.
- No fabricated dates/venues: the Mamontov 1888 venue, 600-copy run, «Неделя» 1889
  partial, De la vie 1889, Hapgood 1888, Geneva 1891, Christchurch 1903 are all
  apparatus/commentary-anchored.

**PASS-WITH-NIT** (1 nit; 0 must-fix on this check).

## 8. Coverage honesty

- "Visual & manuscript record" (covered): defensible. A medium sweep retrieved 7 PD
  portraits and honestly logged the two unobtainable title-pages ("not openly
  available", "only three copies survive", "to request"). The prose hedges its gaps.
- "Reception & afterlife" (covered): **NIT.** The rendered prose covers the *named*
  reception well (Synod + Nikanor; Grot / Astafyev / Bugaev; Strakhov-Fichte; Tsertelev;
  Kozlov), but the dossier's own coverage note admits "Wider lay/working-class reception
  … only sketched" — that hedge does not appear in the index.md prose, only in the
  dossier note and `notCovered`. The `covered` grade leans optimistic relative to the
  dive's own admission; `covered` is acceptable since the limit is disclosed in the
  dossier, but a reader of index.md alone would not see it. Optional: add a one-clause
  hedge to the prose, or downgrade to `partial`. Not a must-fix.
- "Redactions & textual history" and "The author's later verdict" are honestly graded
  `partial`. No `covered` surface materially overclaims.

**PASS-WITH-NITS** (no must-fix).

## 9. Rights

- `git add -n` on the dive root stages exactly: `dossier.yaml`, `index.md`, and the 12
  PD extract `.txt` files. No commentary file, no non-PD text committed.
- `visuals/` is git-ignored (`docs/.gitignore: research/*/visuals/`); confirmed via
  `git check-ignore`.
- `index.html` is git-ignored by design (`*.html` rule; serve.py regenerates from .md).
  It exists on disk for local viewing but is correctly never committed.
- No non-PD commentary file remains in the committed tree.

**OK.** No must-fix.

---

## Findings summary

| # | Check | Grade |
|---|---|---|
| 1 | Byte-fidelity spot check | OK |
| 2 | Primary claims anchored | OK |
| 3 | Secondary claims attributed | OK |
| 4 | Voice | NIT ("rightly" endorses Soina) |
| 5 | Scholarship triangulation | OK |
| 6 | Entities | **MUST-FIX** (Biryukov marked missing; vault has Pavel Birukoff.md) |
| 7 | Work-record | NIT (scope value off-vocab but flagged) |
| 8 | Coverage honesty | NIT (Reception "covered" hedge only in dossier, not prose) |
| 9 | Rights | OK |

Must-fix items: **1**
- Entity P. I. Biryukov: change `vaultStatus: missing` → `exists` and
  `wikilinkTarget: "Pavel Biryukov"` → `"Pavel Birukoff"` (the page exists in the vault
  under that transliteration; otherwise ingestion would duplicate it).

Nits: 3 (drop "rightly"; the `scope` controlled-value mismatch — already in needsReview;
the Reception-section hedge living only in the dossier).

The dive is substantively sound: byte-fidelity holds independently, the headline
Schopenhauer/Hartmann-refutation claim is genuinely supported by the extract, commentary
facts are properly attributed, the OS→NS ban date is correct, and rights are clean. The
single must-fix is a one-line transliteration/status correction.

---

## VERDICT: PASS-WITH-NITS — but 1 MUST-FIX (Biryukov vaultStatus); resolve, then PASS.

---

## Resolution (author, post-verification)

All items resolved before commit:
- **MUST-FIX (Biryukov):** entity now `vaultStatus: exists`, `wikilinkTarget: "Pavel Birukoff"`, note rewritten to point at the existing `Pavel Birukoff.md` and warn against a duplicate.
- **NIT (voice / "rightly"):** dropped; recast as "a reading the primary text supports."
- **NIT (bans scope):** `scope` changed to the schema value `complete-ban`; the note now flags the destroy order as an optional second `confiscation` entry; `needsReview` updated; the "Schema-clean:" overclaim removed.
- **NIT (Reception hedge):** a one-clause hedge on the un-swept wider lay reception added to the index.md prose (previously only in the dossier).

Re-checked after fixes: `verify_quotes.py` 23/23 PASS; dossier YAML parses; HTML re-rendered. Net verdict: **PASS.**
