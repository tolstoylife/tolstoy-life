# Verifier report — Father Sergius (Отец Сергий) novel-dive

**Overall verdict: PASS-WITH-NITS**

Independent, adversarial verification pass on `docs/research/1890-1898-father-sergius/`.
The mechanical quote gate already passed 15/15; this report covers the judgement-level
checks. The dive is sound: every Russian quote I re-derived directly from the TEI is
verbatim, every primary claim ties to the record, scholarship is attributed throughout
(the hagiographic prototype claims are correctly flagged unverified, never asserted),
entity routing is correct, and the workRecord enums are valid. Findings below are one
real (minor) date error and a handful of nits.

**Issue count:** 0 BLOCKER · 0 MAJOR · 2 MINOR · 4 NIT

---

## 1. Byte-fidelity (belt-and-braces) — PASS

I re-extracted each sampled quote **directly from the TEI** with
`extract_tei.py --choice=reg --notes=auto` (not from the committed extract files) and
string-matched against the dossier `quoteRu`. All match byte-for-byte across all genres:

| Ev | Genre | TEI source | dossier quoteRu (head) | TEI re-derive |
|---|---|---|---|---|
| E1 | main text ch.VII | `works/v31_005_046_Otets_Sergij.xml` | `Очисти от скверны славы людской, обуревающей меня` | identical |
| E2 | main text ch.VII | same | `дьявол подменил всю его деятельность для бога деятельностью для людей.` | identical |
| E3 | main text ch.V | same | `положил указательный палец левой руки на чурбан, взмахнул топором и ударил по нем ниже второго сустава.` | identical |
| E4 | main text ch.VIII | same | `Я жил для людей под предлогом бога, она живет для бога, воображая, что она живет для людей.` | identical |
| E5 | main text ch.VIII | same | `Чем меньше имело значения мнение людей, тем сильнее чувствовался бог.` | identical |
| E6 | main text ch.II | same | `была за год тому назад любовницей Николая Павловича` | identical |
| E7 | variant № 7 | `works/v31_203_210_..._Plany_i_varianty.xml` | `взмахнув топором, ударил ее вдоль головы ниже темени` | identical |
| E10 | diary 31 Oct 1890 | `diaries/v51_098_101_1890_10_31.xml` | `Большое самолюбие ( Кузмннский и Урусов ), честолюбие и потребность безукоризненности.` | identical |
| E11 | letter Chertkov | `letters/v87_280_a16.xml` | `Борьба с похотью тут эпизод, или скорее одна ступень, главная борьба с другим — с славой людской.` | identical |
| E13 | diary 17 Jul 1898 | `diaries/v53_203_204_1898_07_17.xml` | `Решил отдать свои повести: Воскресение и Отец Сергий в печать для духоборов.` | identical |
| E14 | diary 17 Jul 1898 | same | `Успокоение только тогда, когда человек живет для служения Богу среди людей.` | identical |
| E15 | main text ch.I | `works/v31_005_046_Otets_Sergij.xml` | `погрозил пальцем и потом, уезжая, сказал:` | identical |

No drift. The TEI source-slip "Кузмннский" (for *Кузминский*) is genuinely in the
primary file, not an extract mistranscription — and the dive correctly flags it as a
source slip and quotes it as-is (index.md L72; dossier E10 note). **No issues.**

## 2. Every primary claim source-anchored — PASS (1 MINOR date error)

Key findings, marquee, genesis, and redaction claims all tie to an evidence row or
extract. Spot-checks beyond the dossier evidence ids: the index.md "where material
clusters" table cites `v52_048_050_1891_08_12` for "не нужно искать добрых дел,
подвигов" — present in the TEI. Verified.

- **MINOR — the "6 June 1890" conception-note date is wrong; it is 8 June.** index.md
  L60 ("The conception note (6 June 1890)") and the diaries table L195 (`6 Jun 1890`),
  plus dossier E8 `date: "1890-06-06"`, all date the «Начал Отца Сергия…» entry to
  6 June. The TEI file is `v51_047_048_1890_06_08`; its opener header reads `8 июня`
  and the bibl is PSS T.51 pp.47–48. The dive's own E8 significance note already
  concedes "(In the 8 June bundle file; no standalone 06_06 entry exists.)" — so the
  evidence is internally contradicted by the claimed date.
  **Fix:** change "6 June" → "8 June" at index.md L60 and L195, and `date: "1890-06-06"`
  → `"1890-06-08"` at dossier E8. (The conception note as an event may indeed sit a day
  or two earlier in Tolstoy's own reckoning, but the dated diary entry that carries the
  quote is 8 June; either re-date to 8 June or add `dateApproximate`/a note explaining
  the 6-vs-8 gap.)

## 3. Scholarship attributed, not asserted — PASS

Every mainstream claim is attributed in-voice. Britannica ("sainthood cannot be
consciously sought") and Wilson (NYRB, "spiritual pride") are named at each use
(index.md L185; scholarship extract L10). **CRITICAL CHECK — the hagiographic prototype
claims are correctly handled:** Jacob the Monk and Serafim of Sarov appear at index.md
L154, L186, L226 and are *every time* attributed to "the mainstream" / "Wikipedia;
Grokipedia" and explicitly flagged "**not** verified against the PSS Tom 31 commentary
in this dive." In the dossier they carry `basis: scholarly`, `certainty: conjectured`
(prototypes[] under Father Sergius), and are listed in both `needsReview` (phase 3) and
`notCovered`. They are never stated as fact. **No issues.**

## 4. scholarship.triangulation — PASS

All 6 triangulation entries reference defined evidenceRefs (E11, E13, E10, E7, E6, E12 —
all exist). Relations used: 1×complicates, 2×confirms, 3×extends — all valid enum
values. The marquee verdict (`confirms` + `extends`) is defensible: the pride/vainglory
reading IS the received English-language reading (Britannica, Wilson) so `confirms` is
honest, and the `extends` is real and precisely stated — Tolstoy states the thesis in
the 16 Feb 1891 Chertkov letter (E11) and 14 Mar 1891 Zolotarev letter (E12) *while
composing*, which the thematic criticism does not cite. The axe-murder variant (E7,
`extends`) is genuinely absent from the English literature. Well-judged.

## 5. Entity routing (novel-mode) — PASS

- **Routing correct.** Nicholas I → `person` (real figure appearing as himself; E6/E15
  show him speaking and acting; matches the Hadji Murat precedent). Genesis figures
  (Chertkov, Birukoff, Maria Lvovna, Urusov, Kuzminsky, Zolotarev, Leontyev, Amvrosy,
  Gorky) → `person`. Fictional cast (Kasatsky/Sergius, Pashenka, Makovkina, Marya,
  Korotkova) → `character`. Doukhobors → `group` (`groupType: religious-sect`).
- **Prototype certainty not over-claimed.** Kuzminsky and Urusov → `basis: author-stated`,
  `certainty: documented` — correct; it is the 31 Oct 1890 diary (E10), byte-verified.
  Jacob/Serafim motif source → `basis: scholarly`, `certainty: conjectured` — correctly
  NOT flattened to documented.
- **vaultStatus verified by loose surname match against `website/src/wiki/`.** Confirmed
  present: `Leo Tolstoy.md`, `Vladimir Chertkov.md`, `Pavel Birukoff.md` (the dossier's
  `vaultStatus: exists` for Chertkov/Birukoff is right; the non-obvious "Birukoff"
  transliteration is the page that exists). Confirmed genuinely **absent** (so
  `vaultStatus: missing` is correct): all characters, Nicholas I, Urusov, Kuzminsky,
  Zolotarev, Leontyev, Gorky, Amvrosy, Optina Pustyn, Doukhobors. No false `missing`.
- **NIT — `Maria Tolstaya.md` exists; dossier marks Maria Lvovna `vaultStatus: stub`.**
  The dossier already flags this as a disambiguation risk (daughter Maria Lvovna vs
  sister Maria Nikolaevna) in both the entity note and `needsReview` phase 4. This is
  correctly surfaced, not an error — recording it only so the ingestor does not blindly
  link `[[Maria Tolstaya]]` to the wrong Maria.

## 6. workRecord — PASS (1 NIT, schema-doc stale not dive-wrong)

No `works/` record exists for father-sergius (confirmed by walk of `website/src/works/`);
the record-CREATING proposal is honest. Enum values all valid against the schema:
`completionStatus: incomplete` ✓, `firstPublishedVenueType: book` ✓,
`bans[].scope: passages-cut` ✓, `bans[].authorityType: imperial-state` ✓.
`excommunicationRelated: false` is correct and honest — the work was unpublished in
Tolstoy's lifetime and played no part in the Feb 1901 action (proximate trigger was
*Resurrection*); the dive states this non-causal relation as thematic context only
(index.md L175).

- **NIT — `mainCategory` / `subcategory` are not in `tolstoy-works-schema.md`, but they
  ARE live fields.** A literal schema-doc check flags these two field names as absent.
  However, 16 existing work records use them, and the claimed mirror
  (`Master and Man.md`) carries exactly `mainCategory: Fiction` / `subcategory: Novellas`
  — identical to the dive's proposal. So the dive is **correct against the real data**;
  the schema markdown is simply stale (does not document these two fields). No fix to the
  dive needed. (Optional out-of-scope: update the works-schema doc to add
  `mainCategory`/`subcategory`.)

## 7. coverage ledger honesty — PASS

- "Scholarly context" → `status: partial`, note "the academic layer
  (Greenwood/Gustafson/Orwin/Bartlett) not read in full." Honest — confirmed by the
  scholarship extract, which leans on reference works and review-essays and marks
  Greenwood "full text behind subscription … not fully verifiable in this pass."
- "The censored Nicholas-I text (verbatim)" → `status: not-covered`, "Described, not
  quoted; needs the printed Berlin 1912 text." Honest — the local TEI has the canonical
  PSS text, not the bracketed Berlin restoration. Matched in `notCovered` and the
  "Material not covered" section.
- No `covered` surface looks inflated. **No issues.**

## 8. Voice / accuracy — PASS

Bare and factual; every working translation is labelled "(working English)". The
contested labels are kept as the mainstream's word and cross-linked, not asserted:
"Tolstoyan" → `[[tolstoyanism]]` (index.md L175, L243, flagged "the contested label,
attributed to the mainstream"); the anti-Church reading is explicitly `complicates`,
kept "subordinate to the pride-diagnosis, as the primary record does, rather than
reading it as free-standing anti-clerical polemic" (index.md L168). No anachronistic
hardening/softening of Tolstoy's views observed. **No issues.**

## 9. File hygiene — PASS

- `extracts/` holds only TEI-derived text (PD: Tolstoy's own text + PSS apparatus) — no
  third-party rights-reserved material.
- `visuals/` is git-ignored: `git check-ignore` confirms
  `visuals/tolstoy_1897_taylor.jpg` is ignored via the `research/*/visuals/` rule in
  `docs/.gitignore`; `git ls-files visuals/` returns nothing tracked.
- All 9 dossier `visuals` carry `licence: PD`; none rights-reserved.
- No Sergius image committed under `website/src/` (walk returned none). All index.html
  `<img>` srcs are local `visuals/...` paths.
- **NIT — `tolstoy_1897_taylor.jpg` is 2.4 MB and `father_sergius_1918_poster.jpg` is
  1.36 MB.** Both are cached locally and git-ignored, so this is not a repo-weight issue;
  noting only in case a future publish step pulls them into `website/src/` (they would
  want downsizing then).
- **NIT — dossier uses both "Birukoff" (entity `wikilinkTarget: Pavel Birukoff`, matches
  the existing vault page) and "Biryukov" (visuals vis-09 `relatedEntity`, references
  block).** Cosmetic transliteration inconsistency within the dossier; the
  vault-resolving target ("Pavel Birukoff") is the correct one and is used where it
  matters (entity routing).

---

## Must-fix before commit (BLOCKERs + MAJORs only)

**None.**

The single substantive correction is the **MINOR** 6-vs-8 June date error (check 2): the
conception-note diary entry that carries the «Начал Отца Сергия…» quote is dated 8 June
1890, not 6 June. Fix at index.md L60 + L195 and dossier E8 `date`. Everything else is a
NIT. The dive is accurate, well-anchored, and ingestion-ready once the date is corrected.
