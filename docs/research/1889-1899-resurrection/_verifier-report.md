# Verifier report — Resurrection (Воскресение) novel-dive

**Verifier:** independent pass (fresh eyes), 2026-06-08
**Scope:** the judgement-level checks the byte-fidelity script cannot make. The
`verify_quotes.py` gate was re-run during this pass and independently confirmed:
**31/31 quotes verbatim, 0 facsimile missing, 0 label warnings — PASS.**

**VERDICT: CLEAN-WITH-NITS** — no blockers. 2 should-fix (one of them a stale
committed-file housekeeping issue, one a wikiType schema-gap to acknowledge), 4 nits.

---

## Check-by-check

### 1. Byte-fidelity spot-check (belt-and-braces) — PASS
Re-confirmed distinctive substrings of evidence `quoteRu` rows across multiple
extract files (each appears exactly once in the named extract):
- `communion-service-physical` → `v32_003_445_Voskresenie.txt` ✓
- `communion-cross-gallows` (ch XL) → same ✓
- `communion-bells-same-service` (ch XLI) → same ✓
- `diary-1898-11-02-12000` → `v53_210_211_1898_11_02.txt` ✓
- `letter-marks-contract` (12,000 advance) → `v71_279_A_F_Marksu.txt` ✓
- `commentary-tolchok-publish` → `v34_575_577_Otvet_commentary.txt` ✓
- `diary-1899-12-18-completion` → `v53_232_234_1899_12_18.txt` ✓

The four **index.md** hand-copied block-quotes named in the brief were each tested
verbatim (`grep -F`) against their source extract and **all matched**:
- communion «Богослужение состояло…» → Voskresenie.txt ✓
- 17 Jul 1898 «…Возбуди воскресение во мне.» → v53_203_204 ✓
- censorship «…сохранилась только первая фраза: Началось богослужение.…» → v32_471_505 ✓
- Reply «…как последняя и высшая степень моей виновности» → v34_245_253 ✓

All 8 RU block-quotes in index.md carry a 1:1 `(working English)` label (8/8).

### 2. Every primary claim source-anchored — PASS
Spot-traced the non-quote factual assertions most at risk of being unsourced:
- "first sustained work 26 December 1889" + the «Неожиданно стал писать Коневскую
  повесть» diary line → present in `v33_329_422_Istorija_pisanija.txt` ✓
- "title «Воскресение» fixed 15 December 1890" → present in the same commentary ✓
- Bonch-Bruevich "**497** distortions … **10,240** words" → commentary reads
  «…497, причём всем этим искажениям подверглось 10240 слов» — index.md figure
  is exact (digit-grouping only) and attributed to "V. D. Bonch-Bruevich counted" ✓
No orphan factual assertions found.

### 3. Secondary/scholarly claims attributed, not asserted — PASS (with one nit)
- **Excommunication causation** ("complicates"): index.md presents the verdict as
  a *tested hypothesis*, attributes the PSS editor (Opulsky) by name, quotes the
  decree only via Tolstoy's own verbatim Reply, and labels Bartlett's strong
  formulation as the popular line the dive *contradicts*. Disciplined. ✓
- **Pobedonostsev-role contest**: index.md reports the split (Soviet-PSS author /
  prime-mover vs revisionist reluctant) and explicitly "does not adjudicate … and
  does not let either label harden." ✓
- **Doukhobor money figures (CRITICAL)**: PASS. index.md anchors the **12,000 r.
  advance** + 1,000 r./sheet as the corpus datum (twice: key-findings line 20 and
  accuracy-note line 170), and labels the lump-sum totals (Wikipedia 34,200 r.;
  others ≈30,000 r.; the 22,000 r. Marks figure) as "secondary and not mutually
  consistent — treated here as approximate, not asserted." Exactly the required
  discipline. The **draft note** carries the same discipline: it cites only the
  corpus 12,000 figure and asserts no total. ✓
- NIT (see nit-1): the Chekhov reception detail is stated in the dive's voice
  without attribution at the point of assertion.

### 4. scholarship.triangulation — PASS
All 7 `evidenceRef`s resolve to real rows in `evidence[]`
(diary-1898-07-17-decision, letter-marks-contract, communion-service-physical,
reply-eucharist-climax, commentary-tolchok-publish, censorship-communion-cut,
diary-1899-12-18-completion). All `relation` values are in the valid enum:
confirms ×3, complicates ×2, contradicts ×1, extends ×1.

### 5. entities — PASS on vaultStatus; SHOULD-FIX(b) acknowledged on wikiType
- `wikiType` values used: work ×1, event ×1, person ×6, concept ×5. All are valid
  wiki-schema v1.3 types. (Dossier header says "wiki-schema 10 types" — correct;
  schema v1.3 has 10.)
- **vaultStatus accuracy — independently re-checked:**
  - `present` → Chertkov: `website/src/wiki/Vladimir Chertkov.md` exists ✓
  - `present` → Pavel Birukoff: `website/src/wiki/Pavel Birukoff.md` exists ✓
    (loose-grep used per the transliteration gotcha — both confirmed real)
  - `missing` spot-checks (confirmed truly absent from src/wiki/): Koni,
    Pobedonostsev, Marks, Pasternak — all absent ✓; Doukhobors has no dedicated
    page (matches the dossier note) ✓
- **SHOULD-FIX(b) — `concept` for fictional characters Maslova & Nekhlyudov:**
  there is no `character` wikiType, so `concept` is the best-available mapping and
  the dossier self-documents the choice ("a character, not a historical person —
  routed as concept"). This is acceptable *as a routing stopgap*, but it is a
  genuine schema gap: a fictional character is neither a concept nor a person, and
  routing both protagonists as `concept` will mis-shape their eventual wiki pages.
  Flag for a schema decision (add a `character` type, or fold both into the
  Resurrection work page) before ingestion — do not let the `concept` label
  silently harden into the vault. `Doukhobors` as `concept` (a sect/people-group,
  not an idea) is the same best-available-type situation; lower stakes, accept.

### 6. workRecord (record-creating) — PASS
- No `resurrection` record exists under `website/src/works/` → record-creating
  premise correct.
- `recordPath: website/src/works/fiction/novels/resurrection/Resurrection.md` is
  plausible: the real layout is `fiction/novels/<slug>/<Title>.md`
  (anna-karenina, war-and-peace present).
- **Every field NAME checked against the real Anna Karenina record** (not just the
  schema doc): titleRu, titleEn, genre, **mainCategory** (`Fiction`), **subcategory**
  (`Novels`), completionStatus, dateWritingStarted/Completed, dateFirstPublished,
  publishedInRussiaDuringLifetime, censorshipNotes, censoredVersionExists, bans,
  excommunicationRelated, relatedWorks, identifiers.jubileeEdition.volumes, themes,
  synopsis — all are real fields in the live record. (Note: `mainCategory`/
  `subcategory` are NOT in `tolstoy-works-schema.md` but ARE in the real record;
  per the "works records ARE source of truth" convention this is correct, not an
  error.)
- List-typed fields shaped as object arrays per schema: `bans[]` → object array
  ({banningAuthority, authorityType, jurisdiction, scope, …}); `relatedWorks[]` →
  {id, relationshipType} (matches AK); `titleAlternatives[]` → object array. ✓
- Values evidence-anchored; no fabricated dates/venues. The OS↔NS completion date
  reasoning (diary OS 1899-12-18 → NS 1899-12-30) and the «Нива» No. 11 publication
  date are tied to evidence rows. `relatedWorks` target IDs (father-sergius,
  a-confession, the-kingdom-…) are explicitly flagged in `needsReview` as
  "confirm slugs before writing" — honest, no dangling claim asserted.

### 7. Translations labelled / no editorialising / contested labels attributed — PASS
- "(working English)" on every RU block-quote (8/8).
- "Tolstoyan" appears once, explicitly as "the contested label," cross-linked to
  the dedicated tolstoyanism dive — attributed, not asserted. ✓
- The dive's own voice stays factual; interpretive readings ("church and prison
  are one institution") are presented as readings of the text, grounded in the
  quoted passages. No unattributed aesthetic verdicts in the dive's voice (Tolstoy's
  own «Нехорошо…» verdict is his, quoted).

### 8. Rights hygiene — PASS
- `git ls-files` over the dive shows **no image files committed** anywhere under
  the dive (0 jpg/png/etc.); `extracts/` holds only `.txt` PD text extracts + the
  `_*.md/.html` deliverables.
- `visuals/` is git-ignored: `docs/.gitignore` line `research/*/visuals/` covers
  it; `git ls-files .../visuals/` returns nothing. ✓
- No rights-reserved (or any) Resurrection/Pasternak/Repin image found under
  `website/src/`. ✓
- CC-BY spot-check: `chekhov-gorky-tolstoy` carries `licence: CC BY 4.0`,
  `rights: CC BY 4.0`, and `note: "NOTE: CC BY 4.0 — attribution to Glavarkhiv
  Moskvy required. Not PD."` — correctly flagged usable-with-attribution, NOT PD. ✓

### 9. coverage ledger honest — PASS
- Reception = `partial`, and index.md states the gap twice (inline line 158 "Named
  1899–1900 Russian press reviews remain a gap" and "Material not covered" line
  182). ✓
- Redactions = `partial`, matching the "light sampling" / third-redaction-only
  language in index.md and the dossier note. ✓
- The remaining `covered` surfaces (genesis, communion, publication/censorship,
  excommunication, visuals, scholarship) are each backed by multiple byte-verified
  evidence rows. No over-claimed `covered`. ✓

### 10. nl2br rendering — PASS
All 8 RU block-quotes and the prose paragraphs are single source lines (the
shortest `>` line is 218 chars; zero `>` lines under 60 chars; no mid-paragraph
hard wraps). No ragged-`<br>` risk.

---

## Findings by severity

### Blockers — NONE

### Should-fix
- **SF-1 (housekeeping): stale committed duplicate `resurrection-dive.md` /
  `.html`.** The dive's canonical narrative is `index.md` (untracked/new,
  `layer: reference`, title "… — a novel-dive"), and `INDEX.html` line 862 links
  the dive's main page to `index.html`. But an **older** `resurrection-dive.md`
  (committed in `8fe5e056`, `layer: research`, title "… — Corpus Dive", 357 lines
  vs index.md's 226) and its `resurrection-dive.html` sibling still sit in the
  folder, diverging in content. Nothing live points to them (only an indirect
  session-log mention). Recommend deleting `resurrection-dive.md` +
  `resurrection-dive.html` so the committed tree has one canonical narrative.
  (Not a content defect — a leftover-file issue.)
- **SF-2 (schema): fictional characters routed as `wikiType: concept`.** Maslova
  and Nekhlyudov (and, lower-stakes, the Doukhobor sect) use `concept` because no
  `character`/`group` type exists. Acceptable as an interim routing label, but get
  a schema decision (add `character`, or fold the protagonists into the
  Resurrection work page) before these entities are ingested, so the stopgap label
  doesn't harden in the vault. Per the project's "explain schema before editing"
  rule, this is a discuss-with-Johan item, not a silent fix.

### Nits
- **N-1:** Chekhov's reception verdict ("found the Gospel-resolution 'too
  theological'", heard a draft read aloud in 1895) is stated in index.md's voice
  (line 158) without an at-the-point attribution; the backing `_reception.md`
  notes it is "summarised in the Russian Wikipedia article … quoting Chekhov
  directly" (secondary). Consider a light "(per …)" tag, matching the attribution
  discipline applied elsewhere.
- **N-2:** index.md line 23 says "the **1899 imperial censor** cut chs XXXIX–XL";
  the underlying datum (`censorship-communion-cut`) is the «Нива» serialisation
  cut. "Imperial censor" vs the Marks "domestic pre-censorship via Sementkovsky"
  are slightly conflated in the one-line key-finding (the fuller line 130 + the
  workRecord censorshipNotes get the mechanism right). Minor precision nit.
- **N-3:** The dossier `evidence` header comment says "wikiType ∈ wiki-schema 10
  types" in one place and the brief references "9 types"; the schema (v1.3) is 10.
  The dossier is correct; flagging only because the brief's "9 types" wording could
  cause confusion — no change needed in the dive.
- **N-4:** `relatedWorks` proposed IDs in the workRecord (father-sergius,
  a-confession, the-kingdom-of-god-is-within-you) are unverified slugs. Already
  honestly flagged in `needsReview`; left as a nit only because the record-writing
  step must resolve them before they go live (a-confession / kingdom records were
  observed; father-sergius was not confirmed this session).

---

## Could not fully resolve
- The full Synod decree wording beyond Tolstoy's verbatim quotations is web-sourced
  (Skvortsov 1901) and outside the corpus; the dossier already isolates this in
  `needsReview` and the index.md only ever quotes the decree *via the Reply*. I
  confirmed the discipline holds (no web-sourced decree wording leaks into the
  evidence ledger), but I cannot independently verify the Skvortsov text itself —
  correctly out of scope, and the dive does not rely on it.

---

**FINAL VERDICT: CLEAN-WITH-NITS** (0 blockers / 2 should-fix / 4 nits).
The dive's primary-source spine, money discipline, attribution discipline,
workRecord field-name fidelity, vaultStatus accuracy, and rights hygiene are all
sound. The two should-fix items are a leftover committed duplicate file and a
schema-routing decision for fictional characters — neither impugns the dive's
content or its citations.
