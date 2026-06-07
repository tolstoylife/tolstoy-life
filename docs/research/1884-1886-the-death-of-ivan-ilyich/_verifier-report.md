# Independent verifier report — «Смерть Ивана Ильича» work-dive

**VERDICT: CLEAN-WITH-NOTES** — substantively sound; 0 must-fix, 4 nice-to-fix (internal-consistency / vocab-precision items only). The published artifact (`index.md`) and the machine-readable `dossier.yaml` are accurate, well-anchored, and rights-clean. The nice-to-fix items are confined to one stale internal note file and two controlled-vocab values that the dossier itself already flags for review.

Reviewer: independent opus pass (did not author the dive). Mechanical gate (verify_quotes.py 22/22) was already green; this is the judgement-level review.

---

## Check 1 — Byte-fidelity spot-check (PASS)

Re-derived 15 `evidence[].quoteRu` strings (well over the requested 4–5) by `grep -F` against the named `extract:` files. **All 15 are present byte-exact** (substring count = 1 each). Mix covered work-text, genesis diary, genesis letter (incl. pre-reform), and commentary:

- **Work (W*):** W1 «что умер он, а не я», W2 «Прошедшая история жизни… самая ужасная.», W5 «люди смертны, потому Кай смертен», W10 «Вместо смерти был свет» — all in `v26_061_113_Smert_Ivana_Ilicha.txt`. ✓
- **Genesis diary (G*):** G1 «Хочу начать и кончить новое» (`v49_087…`), G2 «Смерть Ивана Ильича достал — хорошо и скорее могу» (`v49_088…`), G3 «мне нужен отдых от той работы, и эта, художественная, такая» (`v49_089…`). ✓
- **Genesis letter (G*):** G4 «по содержанию ко всем» (`v85_067…`), G5 pre-reform «описаніе простой смерти простого человѣка» (`v63_408…`), G6 «весь поглощен теперь этой работой, уже тянущейся несколько лет» (`v83_336…`), G7 «скоро сталь путаться» (`v85_095…`, the verbatim `сталь`-for-`стал` typo is correctly preserved and disclosed). ✓
- **Commentary (C*):** C1 «Иван Ильич Мечников умер 2 июля 1881 года», C2 «Повесть (1884—1886)», C3 «Нельзя, нельзя и нельзя так жить» — all in `v26_679_691…commentary.txt`. ✓
- **Variant (R1):** «Я узнал о смерти Ивана Ильича в суде» in `v26_505_528…Varianty.txt`. ✓

No mismatches. The em-dash, «» guillemets, and pre-reform characters (ѣ, і, ъ) all match.

## Check 2 — Claim-anchoring, primary (PASS)

Sampled ~10 factual claims; each is anchored:

1. **Composition 1884–1886 (not 1885–86)** → C2 (Strakhov's «(1884—1886)») + G1–G3 diaries + commentary's rejection of Sreznevsky. Anchored.
2. **Prototype = Ivan Ilyich Mechnikov, Tula prosecutor, d. 2 July 1881, aged 45, b. 13 June 1836, brother of Élie** → C1 + commentary (confirmed: «родился 13 июня», «45 лет», «2 июля 1881», «прокурор тульского суда», and Tolstoy's conversational confirmation quote all present in the extract). Anchored.
3. **Conception 1881, working title «Смерть судьи»** → commentary + G1. Anchored.
4. **Diary 1 May 1884 "artistic rest" framing** → G3. Anchored.
5. **Wife's deadline / "surprise" motive** → G5 (`v63_408`) + witness sweep. Anchored.
6. **Three redactions (Творогов frame → authorial → galley de-localisation)** → R1 + commentary + `_witness_sweep.md` naming note. Anchored.
7. **Galley stamps (15 Feb; verstka 17/18/21 Mar; closed 25 Mar 1886)** → commentary. Anchored (dates are editorial, attributed to the apparatus).
8. **First publication: Сочинения ч. 12, 1886, pp. 394–469** → C2/commentary. Anchored.
9. **Keystones (ordinariness-as-horror, Caius, Gerasim, "не то", light)** → W2, W5, W6, W8, W10. Anchored.
10. **Uncensored vs. suppressed treatises** → commentary apparatus (attributed, confidence `medium`). Anchored.

No free-floating assertions found. Where a claim is editorial rather than from Tolstoy's own words (e.g. the galley stamp dates, the "no censor intervention" reading), the prose attributes it to the PSS Tom 26 editorial history explicitly.

## Check 3 — Secondary claims attributed, not asserted (PASS)

Every scholarly claim in "Reception & afterlife" and "Scholarly context" is attributed to a named source: Jahn (UMN Electronic Study Edition), Mikhailovsky, Lisovsky, Stasov, Nabokov, Thomas Mann, Heidegger, Irwin, Papadimos & Stawicki, the 2009 *Lancet* editorial. No scholarly claim is stated in the dive's own voice.

- **Heidegger §51 is correctly precision-graded.** index.md line 268 states the novella is invoked "for the collapse of that evasion… **not** as a reading of the closing light," and adds that "later scholarship (e.g. William Irwin…) has often expanded the single reference into a fuller alignment than *Being and Time* itself states." This is exactly the required precision — it does NOT claim Heidegger reads the ending. The "only prose fiction in *Being and Time*" claim is appropriately logged in `needsReview` (phase 3) as not verified against the full German text.
- **Stasov is flagged**: "reported (in secondary sources, not the corpus)… could not be traced to a dated letter in this corpus and is flagged for verification." No overstatement.

## Check 4 — Triangulation integrity (PASS)

All 8 `triangulation[].evidenceRef` values (G3, G4, C1, C2, W5, W7, W10, W6) resolve to real evidence ids in the dossier ledger. All `relation` values are from the valid set: complicates ×4, confirms ×2, extends ×2. No invalid relations, no dangling refs.

## Check 5 — Entities (PASS, one minor wikiType note)

Listed `website/src/wiki/` (14 content pages). **vaultStatus values are accurate:**

- Only **Leo Tolstoy**, **Sophia Tolstaya**, **Vladimir Chertkov** are marked `exists` — and all three exist (`Leo Tolstoy.md`, `Sophia Tolstaya.md`, `Vladimir Chertkov.md`), with `wikilinkTarget` matching the filenames exactly.
- All 8 entities marked `missing` (Ivan Ilyich Mechnikov, T. A. Kuzminskaya, L. D. Urusov, Ilya/Élie Mechnikov, N. N. Ge, N. N. Strakhov, A. P. Ivanov, G. A. Zakharyin) were loose-matched against the wiki listing under every plausible transliteration — **none exists under any variant name**. The `missing` flags are correct; no false-missing that would cause the ingestor to duplicate a page.

**wikiType values:** person ×11 and concept ×2 are all valid wiki types. The one anomaly: the entity "The Death of Ivan Ilyich (work)" uses `wikiType: work`, which is NOT among the ten valid wiki article types (person, place, event, concept, translator, institution, adaptation, criticalWork, archivalFond, edition). This is a soft issue, not a hard error: the entity's `role` explicitly says "see workRecord… (no record exists yet)", i.e. it denotes a works/ record, not a wiki page. `work` is being used as an honest pointer to the works/ system rather than the wiki vocabulary. Worth a one-word note. (nice-to-fix #1)

## Check 6 — workRecord (PASS, one vocab note)

- **Field names match the schema.** Spot-checked titleEn, titleRu, titleAlternatives, mainCategory, subcategory, genre, language, completionStatus, publishedDuringLifetime, publishedInRussiaDuringLifetime, dateWritingStarted/Completed, dateFirstPublished, firstPublishedVenue(Type), dateFirstPublishedInRussia, firstPublishedInRussiaVenue(Type), censoredVersionExists, censorshipNotes, excommunicationRelated, themes, relatedWorks, identifiers.jubileeEdition.volumes — all present in `website/schema/tolstoy-works-schema.md` and in the live `Master and Man.md` record the proposal is modelled on.
- **No invented dates/venues.** Every value is evidence-anchored or marked as convention/genre with explicit confidence. The OS/NS arithmetic is correct: dateWritingStarted 1884-04-27 OS → 1884-05-09 NS (+12d), dateWritingCompleted 1886-03-25 OS → 1886-04-06 NS (+12d). Both verified by hand.
- **relatedWorks ids resolve**: `what-is-art` (id confirmed in `What Is Art?.md`) and `master-and-man` (id confirmed in `Master and Man.md`) both exist.
- **1884–1886 dating is defensible** from the commentary: Strakhov's title-page «(1884—1886)», the three April–May 1884 diary entries, and the editor's explicit rejection of Sreznevsky's Aug-1885 and Balukhatyi's Oct-1885 datings. Stronger than the 1885-86 mainstream; correctly framed as "complicates" rather than "contradicts."
- **`publishedInRussiaDuringLifetime: true` is correct** — first published in Russia in 1886 (Сочинения ч. 12), Tolstoy d. 1910, uncensored.
- **Vocab nit:** `titleAlternatives[].type: "working-title"` does not match the schema vocab, which is `working` (schema lists `working · translation · subtitle · variant`). The dossier's own `note` already says "Verify titleAlternatives.type vocab against the works schema," so it is self-flagged, but the value as written would fail validation. (nice-to-fix #2)

## Check 7 — Coverage honesty (PASS)

The `coverage[]` ledger is honest. `partial` is correctly used where the work is genuinely incomplete:

- Translation history → `partial` ("outlined only; no edition-by-edition Maude lineage") — honest; the index also routes the full lineage to `notCovered`.
- Reception (Russian society & critics) → `partial` ("Mikhailovsky, Lisovsky, Stasov recovered (thin); full 1886 periodical survey out of web scope") — honest.
- Visual record → `partial` (facsimile + 3 portraits; 1886 title page a gap) — honest.
- "The author's later verdict" → `not-covered` — honest; the index says plainly no firmly-sourced later judgement surfaced.

Nothing is marked `covered` that is really `partial`. The `needsReview` and `notCovered` blocks are candid (diary-year mismatch, Stasov, Heidegger German wording, What Is Art? footnote, the absent Ge letter).

## Check 8 — Voice & rights (PASS)

- **Voice is bare and non-editorialising.** Mainstream "didactic / moralising Tolstoy" and "Tolstoyan" framing is explicitly attributed to the outside (line 278: "the dominant frame… the mainstream's word for the period, not the novella's own posture"), consistent with the project's framing-watch rule. The dive resists the slide rather than asserting it.
- **Translations labelled "(working English)"** throughout index.md, dossier.yaml, and all extract deliverables. ✓
- **Rights are clean.** `extracts/` holds exactly one committable image — the PD facsimile `pss-tom26-p61-ivan-ilyich-opening.png` rendered from the local PSS PDF. `git check-ignore` confirms `visuals/` (the 4 Commons portraits) is git-ignored, so no rights-reserved / Commons image is staged for commit. No `.jpg/.png/.ppm` is currently tracked under the dive folder. The PD claim on the facsimile (Tolstoy's text; pre-1928 scholarly edition) is sound.

---

## Must-fix

*(none)*

## Nice-to-fix

1. **`extracts/_visuals.md` is stale vs. the shipped facsimile.** The V05 row + Notes still call the file `extracts/pss-tom26-p72-ivan-ilyich-opening-072.ppm`, "PDF page 72", and "PPM format; convert to PNG before publishing." The actual committed/rendered file is `extracts/pss-tom26-p61-ivan-ilyich-opening.png` (printed p. 61), and `dossier.yaml` (lines 164, 483) and `index.md` (line 316) already reference the correct `.png`. Update `_visuals.md` V05 to the final `.png` filename, printed p. 61, and drop the "convert before publishing" instruction. (Location: `extracts/_visuals.md` line 17 + the "Local PSS facsimile" note.) Internal-consistency only; the published artifact is correct.

2. **`workRecord.fields[] titleAlternatives.type: "working-title"` → should be `working`.** Schema vocab (`website/schema/tolstoy-works-schema.md`) is `working · translation · subtitle · variant`. As written the value would fail `validate-frontmatter.mjs` at ingestion. (Location: `dossier.yaml` line 563.) Already self-flagged in the adjacent `note`.

3. **`entities[] "The Death of Ivan Ilyich (work)" wikiType: work` is not a valid wiki article type.** Valid set is person/place/event/concept/translator/institution/adaptation/criticalWork/archivalFond/edition. The entity legitimately denotes the *works/* record (not a wiki page), so consider either a clarifying note that `work` here means "see workRecord, not a wiki type," or moving the work-as-entity out of the wiki-type-keyed `entities` list. (Location: `dossier.yaml` line ~404.) Low impact — the entity already points unambiguously at the workRecord.

4. **Minor page-range cross-reference drift for G5.** `dossier.yaml` gives Tom 63 pp. 282–283 for `v63_408_Kn_L_D_Urusovu` and the index renders the date "~20 Aug 1885"; the witness sweep agrees (pp. 282–283, ~20 Aug 1885). Consistent across files — listed only as a spot for a one-line PDF page-number confirmation at ingestion, not a discrepancy. (No action strictly required.)
