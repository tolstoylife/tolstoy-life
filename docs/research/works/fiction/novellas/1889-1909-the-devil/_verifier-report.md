# Verifier report — *The Devil (Дьявол)* novella-dive

**Verifier:** independent (adversarial) pass. Did not author the dive.
**Date:** 2026-06-10
**Scope:** `index.md`, `dossier.yaml`, `website/src/posts/notes/2026-06-10-the-devil.md`, `extracts/`.
**Pre-condition:** `verify_quotes.py` re-run by the verifier — **26/26 quoteRu verbatim, 0 missing, 0 label warnings — PASS** (confirmed, not taken on trust).

Verdict legend: PASS (clean) · CONCERN (minor, non-blocking) · FAIL (must fix).

---

## 1. Byte-fidelity spot-check (belt-and-braces) — **PASS**

Picked rows across different extract files, including E9 (murder ending), a diary, and a letter; opened each named extract and confirmed the `quoteRu` verbatim and the `quoteEn` a fair, labelled "(working English)" rendering.

- **E9** (murder ending, `v27_516_517_Djavol_varianty_kontsa.txt` line 29): «…Да нет никакого Бога. Есть дьявол. И это она. Он овладел мной. А я не хочу, не хочу. Дьявол, да, дьявол» — verbatim. EN "No — there is no God. There is a devil, and it is she…" is accurate; «дьявол» = "devil" (note the work-title spelling «дьявол» here vs Evgeny's colloquial «чорт» in the suicide redaction E4 — the dive handles both correctly).
- **E10** (the three shots, same file line 31): «…раз, два, три раза выстрелил ей в спину» — verbatim; EN faithful.
- **E11** (diary 10 Nov 1889, `v50_177_177_1889_11_10_2.txt` line 7): «После обеда неожиданно стал писать историю Фредерикса» — verbatim; EN faithful ("Frederiks" transliteration is fine).
- **E21** (letter to Birukoff, `v65_005_P_I_Biryukovu.txt` line 11): «…другие художественные работы всё на тему половой любви (это секрет)» — verbatim; EN faithful.
- **E22** (Chertkov 1898, `v88_506_iyulya14.txt` line 35): «Иртенева нехорошо печатать, потому что мотив один и тот же, что в Отце Сергие» — verbatim; EN faithful.
- **E23** (Domna confession, `v85_022_a24.txt` line 11): «я назначил ей свиданье и пошел на него» — verbatim; EN faithful.
- **E14/E15/E17** (Aksinya diaries) and **E24/E25/E26** (commentary): all verbatim against their files.

No mistranslations. All EN fields carry the "(working English)" label. Minor observation (not a defect): E15's `quoteRu` normalises the diary's "...." to "…." — `verify_quotes` accepts it and the cited file (the diary, not the commentary) is the right source of record.

## 2. Primary claims are source-anchored — **PASS**

Walked index.md's own-voice factual claims about the primary record. Each ties to an evidence row or the PSS commentary (E24–E26):
- Composition window / interleaving with Kreutzer → E11, E13, E26.
- Double-ending conceived in the diary (18 Nov) → E12.
- Draft finished 19 Nov; revisions 20–24 Nov → commentary E26 (and the dated 19 Nov entry).
- Aksinya oscillation and «чувство оленя»→«мужа к жене» → E14–E17.
- 1908 / 1909 «Ермил» guilt → E18, E25.
- 1909 return / title / second ending → E19; the Sreznevsky handwriting-dating attributed to the commentary.
- Domna / interruption → E23.
- Fridrikhs external crime → attributed to the commentary "from the testimony of Fridrikhs's sister".
- Withdrawal from the Doukhobor sale → E22; the "three works" letter quoted (14 Jul 1898) is from the same Tom 88 letter as E22.

The Tveretinov→Irtenev name-change, the IRLI shelfmark 22.5.5, the Chertkov/Gorbunov copy, the 1911 *Posmertnye* vol. 1, the Maude 1925 translation date — all routed to the PSS apparatus or the edition, consistent with the corpus surface. No unanchored primary claim found.

## 3. Secondary claims are ATTRIBUTED, not asserted — **PASS**

Every scholarly/secondary claim is named to a source rather than stated as the dive's own fact:
- Femme-fatale frame → "popular editions and a strand of criticism," the "From the Ideal to *Femme Fatale*" line (flagged *unverified author* in the dossier triangulation — appropriately hedged).
- Misogyny-as-pathology → Rancour-Laferriere, *Tolstoy on the Couch* (1998), named.
- Autobiographical consensus → Wilson, Troyat, the Maude preface (named).
- Triptych pairing / withdrawal-quote gap → Møller, *Postlude to The Kreutzer Sonata* (1988), named.
- The "hidden in a chair" anecdote is explicitly *not* asserted (index.md line 129 + `needsReview`).
- Publication facts (1911 *Posmertnye*, Berlin 1912, Eikhenbaum–Khalabaev 1928, Maude) are bibliographic, attributed to the edition/apparatus.

No bare secondary assertion in the dive's own voice.

## 4. scholarship.triangulation — **PASS**

All 4 entries reference an `evidenceRef` that exists in `evidence[]` and use a valid `relation`:
- E9 → `contradicts` (E9 present ✓)
- E4 → `complicates` (E4 present ✓)
- E14 → `extends` (E14 present ✓)
- E22 → `complicates` (E22 present ✓)

All four relations ∈ {confirms, complicates, contradicts, extends}. Valid.

## 5. Entity routing (v1.4) — **CONCERN** (one wrong `vaultStatus`)

Types are correct against the v1.4 rules:
- `character` (fictional): Evgeny Irtenev, Stepanida, Liza Irteneva — correct.
- `person` (historical): Aksinya Bazykina, Domna, N. N. Fridrikhs, Sofia, Chertkov, Birukoff, Obolensky, Gorbunov, Maria — correct (Nicholas-I-style "real person appears as themselves" precedent not even needed here; none of these are fictional).
- `group`: Doukhobors — correct.
- `place`: Yasnaya Polyana — correct.

`vaultStatus` spot-check against `website/src/wiki/`:
- `exists` claims — Leo Tolstoy ✓, Vladimir Chertkov ✓, Pavel Birukoff ✓, Yasnaya Polyana ✓, Maria Tolstaya ✓ (page is the daughter M. L. Obolenskaya, 1871–1906 — matches the dossier's own disambig note).
- **CONCERN — Sofia is wrongly marked `missing`.** The dossier entry `name: "Sofia Andreevna Tolstaya"` carries `wikilinkTarget: sofia-tolstaya`, `vaultStatus: missing`. A page **exists**: `website/src/wiki/Sophia Tolstaya.md`, `id: sophia-tolstaya`, `titleRu: Софья Андреевна Толстая`. This is the exact transliteration gotcha (Sofia vs **Sophia**) the project memory warns about — a literal grep on "Sofia" misses "Sophia". A wrong `missing` would make the ingestor **duplicate** the page. **Fix: set the Sofia entry to `vaultStatus: exists` and align `wikilinkTarget`/title to `Sophia Tolstaya` / `sophia-tolstaya`.** (Confirmed genuinely absent: Aksinya Bazykina, Domna, Fridrikhs, Irtenev, Stepanida, Liza, Gorbunov, Obolensky — those `missing` flags are honest.)

`prototypes[]` certainty is **not** over-claimed:
- Stepanida ↔ Aksinya: `author-stated`/`documented` — justified; Tolstoy named the connection to Birukoff (E24, the commentary's «на это есть намек…»). OK.
- Irtenev ↔ Tolstoy: `autobiographical`/`probable`, explicitly "a hint of himself, not a portrait" (index.md line 207) — correctly **not** author-stated-as-portrait. OK.
- Irtenev ↔ Fridrikhs: `contemporary`/`editorial` + `documented` *for the borrowing* — appropriately scoped.

## 6. workRecord — **PASS**

Field names mirror real `tolstoy-works-schema.md` keys, and object shapes match:
- `titleAlternatives[]` = `{title, type, language}` with `type: working` — matches §1 (working ∈ {working, translation, subtitle, variant}). ✓
- `manuscripts[]` = `{draftLabel, dateCreated, numberOfFolios, currentRepository, repositoryCity, repositoryCountry, repositoryCallNumber}` — all valid §5 keys; `draftLabel` values `first-draft`/`fair-copy` ∈ enum. ✓
- `bans: []` — correct shape; honest (no living-author censorship; self-suppressed → posthumous). ✓
- `relatedWorks[]` = `{id, relationshipType}` with `companion` ∈ §7 enum. ✓
- `epigraph` (string) + `epigraphSource` + `epigraphLanguage` — match §7 shape (string, not object). ✓
- Field names cross-checked against the real Master and Man record (`website/src/works/fiction/novellas/master-and-man/Master and Man.md`): all the keys used (titleAlternatives, manuscripts, bans, relatedWorks, epigraph*) are present there. ✓

Dates / OS→NS:
- `dateWritingStarted: 1889-11-22`, `oldStyle: 1889-11-10` — verified: 10 Nov OS + 12 days = **22 Nov NS**. ✓ `approximate: false` correct (diary-dated to the day).
- `dateWritingCompleted: 1889-12-01`, `oldStyle: 1889-11-19`, `approximate: true` — verified: 19 Nov OS + 12 = **1 Dec NS**. ✓ `approximate: true` correctly used because "completion" is split (variant ending + title c. 1909), as the note explains.
- `dateFirstPublished: 1911` — consistent with the posthumous edition; no fabricated venue. `firstPublishedVenue` matches the apparatus (one bookseller catalogue's "vol. II" honestly routed to `needsReview`, dive follows PSS vol. 1).

No fabricated dates or venues.

## 7. Coverage honesty — **PASS**

No surface marked `covered` that the evidence shows is really partial. Both "Reception & afterlife" and "Visual & manuscript record" are marked **`partial`** with honest notes (posthumous → no contemporary reception surveyed; period PD photos held but Aksinya photo / 1911 title page / manuscript facsimiles are request-targets). The `covered` surfaces (marquee, genesis, close-read, redactions, publication, characters, themes, scholarly context, later verdict) each have a substantiating note and matching evidence. Honest.

## 8. Voice — **PASS**

Bare project voice; contested interpretations are framed as the dive's tested hypothesis, not asserted:
- The marquee is explicitly "**Hypothesis.**" (index.md line 29) and "an interpretive marquee… contested" (line 31); the outcome is "reported," not assumed.
- "femme fatale" and "misogynist" labels are consistently attributed to "the mainstream," "popular editions," "a strand of criticism," Rancour-Laferriere — never adopted (e.g. lines 31, 229, 235, 237).
- All translations labelled "(working English)."
- The one place the dive states the reading flatly ("The 'devil' is Evgeny's projection," line 16) sits inside the **Key findings** block whose framing sentence is "the title names a delusion the work diagnoses" — i.e. presented as the dive's argued conclusion from the two endings + epigraph, with the evidence adjacent. Acceptable as a tested claim, not a bare assertion.

No editorialising drift found.

## 9. Rights / PD — **PASS**

- `docs/.gitignore` contains `research/*/visuals/` — confirmed (`cat`). The visuals cache is git-ignored.
- `git ls-files docs/research/1889-1909-the-devil/visuals/` → **0 tracked files**. The 5 cached jpgs (incl. the FAL/CC-BY-SA Yasnaya aerial, V5) sit on disk but are **not committed**. ✓
- `extracts/` holds only PD text (TEI extracts of Tolstoy's own words + PSS commentary). No rights-reserved image committed. ✓
- index.md embeds exactly **2** figures: `commons-tolstoy-1891-repin-yasnaya.jpg` (Repin 1891, PD — Repin d. 1930) and `commons-sofia-tolstaya-1908.jpg` (Sofia 1908, PD — pre-1928). Both genuinely PD; both captioned "Public domain (Wikimedia Commons)." The FAL-encumbered aerial (V5) and all rights-reserved request-targets (V6 Aksinya, V7 title page, V8 facsimile) are **not** embedded. ✓

(Note, non-blocking: the whole dive directory is currently untracked — `?? docs/research/1889-1909-the-devil/`. Expected for a fresh, not-yet-committed dive; the rights gate is what matters and it holds.)

## 10. Marquee integrity — **PASS**

The marquee reads as a tested claim, not a foregone conclusion. It is stated as **Hypothesis** (line 29), flagged contested (line 31), and the `contradicts`+`extends` outcome is argued from primary evidence:
- the epigraph (Matthew V — pluck out *your own* eye, E1),
- the suicide ending turning the gun inward (E2, E7),
- the involuntary-will language (E3, E4),
- and crucially the murder-ending God-denial (E9) where naming-her-devil *is* the murderous act.
The dive grants the counter-reading air ("does not deny the novella's harshness toward sexuality") and distinguishes its move from Rancour-Laferriere's (projection located in the *character*, not the author). The conclusion follows from the staged evidence rather than preceding it.

---

## Overall verdict: **CLEAN-WITH-MINORS**

- **FAIL items:** 0
- **CONCERN items:** 1

### Required fixes (numbered)

1. **`dossier.yaml`, Sofia entity (check 5):** change `vaultStatus: missing` → `vaultStatus: exists` and set `wikilinkTarget: sophia-tolstaya` (the page is `website/src/wiki/Sophia Tolstaya.md`, `id: sophia-tolstaya`). The "Sofia" vs "Sophia" transliteration mismatch makes the current `missing` flag wrong and would cause the ingestor to duplicate the existing page. Optionally add a one-line `needsReview` noting the Sofia/Sophia spelling so the ingestor uses the canonical title.

Everything else — 26/26 byte-fidelity, source-anchoring, attribution discipline, triangulation refs/relations, workRecord shapes and OS→NS dates, coverage honesty, voice, rights/PD, and marquee integrity — passes.
