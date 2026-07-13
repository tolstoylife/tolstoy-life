# Verifier report — *Christianity and Patriotism* (Христианство и патриотизм) work-dive

**VERDICT: CLEAN-WITH-MINOR-NOTES** — one stale number in `index.md` (the only required fix); everything substantive is source-anchored, attributed, and byte-faithful.

Independent verification pass, fresh eyes. Mechanical gate re-run and confirmed:
`verify_quotes.py … dossier.yaml` → **27/27 quotes verbatim, 0 missing, 0 label warnings — PASS**.

---

## Per-check findings

### 1 · Byte-fidelity spot-check — ✓ PASS
Re-derived 6 quotes by eye against their named extracts; all verbatim, none paraphrased, no footnote-superscripts inside any quote span:
- **W12** «Патриотизм есть рабство.» — verbatim, `v39_027_080…txt` line 349. ✓
- **W8** «Я прожил полвека среди русского народа…патриотизма» — verbatim, line 249. ✓
- **W16** «Народы же, подчиняющиеся правительствам, не могут быть разумны…неразумия.» — verbatim, line 351. ✓
- **W13** «нужно только не лгать» — verbatim, line 433 (sits inside the longer sentence, span boundary clean). ✓
- **D3** «За всё это время писал Тулон и дней 5 тому назад кончил и решил не переводить и не печатать. И это облегчило меня.» — verbatim, `v52_112_114…txt` line 7. ✓
- **L3** «Но с Тулоном сделалось то, что он мне опротивел» — verbatim, `v87_352_noyabrya3.txt` line 11. ✓
- **D1** «Написал Тулон и не посылаю.» — verbatim, `v52_103_104…txt` line 7. ✓

`quoteEn` renderings are faithful working translations of their `quoteRu`.

### 2 · Primary claims source-anchored — ✓ PASS
Every genesis/redaction/publication claim in `index.md` traces to the editorial history extract `v39_229_234_history.txt` (read in full) or to an evidence row:
- Toulon occasion, 8 Oct 1893 start, рук. №1 «Я.П.», Sikorsky/malevanshchina opening — history lines 5–7. ✓
- Leskov "Why German and not English?" → 20 Oct agreement; Suttner via S.A.→Tatyana; Gorbunov clipping "пригодилась" into ch. II — history lines 13–19. ✓
- 3 Nov repudiation / 5 Nov retraction / 1 Dec signature / Feb grind / 22 Feb рук.№38 / 17 Mar рук.№37 «Совсем, совсем, совсем кончено» — history lines 21–29. ✓
- 39 redactions, 1,384 leaves, copyist list, title evolution, name-encryption table, "PSS follows Elpidin 1895, errors corrected against MSS" — history lines 53–117. ✓
- Publication/censorship chain (FR May 1894 → EN Daily Chronicle June 1894 / Turner→Chertkov/Battersby → DE Henkel Aug 1894 → Elpidin Geneva 1895 → 1901 import-ban file 78 pt IV → 1906 Обновление / Felten prosecuted → 1911 & 1913 censored printings) — history lines 37–49. ✓
No free-floating factual assertion found.

### 3 · Secondary claims attributed, not asserted — ✓ PASS
Every scholarly/reception claim carries a named source: Maude (1910) "~six lines," Simmons/Bartlett/Wilson "biographically," Christoyannopoulos (2013), McKeogh (2009), Alston (2014), Kijewska-Trembecka (2024), *The Spectator* (14 July 1894), Wikisource excommunication decree, British Library (2024). Contested labels are kept as the mainstream's words and never adopted in the dive's voice:
- "Christian anarchism" — flagged "the *mainstream's* word" (l.29, l.176); attributed to Christoyannopoulos (l.188).
- "extremist" — attributed to *The Spectator*'s reading (l.162).
- "utopian or naïve," "simplistic" — attributed to Christoyannopoulos (a charge he contests) and McKeogh, closed with "These are the outside's words; the dive keeps them visible as such rather than adopting them" (l.196).
- "pacifist" appears only in the hedged `complicates` discussion (l.193).
Conforms to the project rule (ground in primary, attribute the mainstream, no label sticks as fact). ✓

### 4 · Triangulation integrity — ✓ PASS
All 5 `evidenceRef`s resolve to real evidence rows (W3, W8, W9, W13, W16 each present exactly once). Relations all valid: 3×`extends`, 1×`confirms` (W9), 1×`complicates` (W16). The "not-arbitration-pacifist" claim (W16, `complicates`) is genuinely supported: the W16 quote sits inside the «Проповедники мира посредством арбитрации» passage (extract line 351) and the argument continues to «не может быть достигнут мир народов…конвенциями, арбитрацией» (line 355) — Tolstoy is explicitly rejecting arbitration/congress pacifism, exactly as the triangulation claims. ✓

### 5 · Translations labelled — ✓ PASS
All 27 `quoteEn` values begin with "(working English)". Every English rendering of Russian in `index.md` is paired with the Cyrillic original and marked "(working English)" or set as a translation. No Russian-origin line is passed off as an English original. ✓

### 6 · Entities — ✓ PASS
All `wikiType` values valid (16×person, 1×concept, 1×work, 1×event). `vaultStatus`: 4 `exists` + 13 `missing`, all valid enums. Spot-checked against `website/src/wiki/` (16 files total):
- `exists`: Leo Tolstoy, Vladimir Chertkov, Tatyana Tolstaya, Sophia Tolstaya — all 4 present. ✓
- `missing`: Leskov, Suttner, Sikorsky, Déroulède, Schmidt, Khilkov, Rusanov, Gorbunov-Posadov, Legras, Avelan, Patriotism, Christianity-and-Patriotism (work), Toulon-festivities — confirmed absent, including transliteration-variant grep (hilkov/deroulede/shmidt/avellan/legra/sikorsk etc.). No wrong status. ✓

### 7 · workRecord (work-dive specific) — ✓ PASS
- Field NAMES match the works schema: `titleEn/titleRu/titleAlternatives/mainCategory/subcategory/genre/language/completionStatus/publishedDuringLifetime/publishedInRussiaDuringLifetime/dateWritingStarted/dateWritingCompleted/dateFirstPublished/firstPublishedVenue(+Type)/dateFirstPublishedInRussia/firstPublishedInRussiaVenue/authoringLocations/samizdatCirculation/censoredVersionExists/censorshipNotes/bans/excommunicationRelated/relatedWorks/themes/identifiers.jubileeEdition` — all present in `website/schema/tolstoy-works-schema.md`. Cross-checked the model record `website/src/works/non-fiction/essays-and-criticism/bethink-yourselves/Bethink Yourselves!.md` (uses `mainCategory: Non-Fiction`, `subcategory: Essays and Criticism`, `id: bethink-yourselves`). ✓
- The `oldStyle:`/`approximate:` sub-keys (vs the schema's suffix-style `…OldStyle`/`…Approximate`) are the **established dive-proposal convention** — identical encoding in the Ivan Ilyich model work-dive and 6 other dossiers. This is a proposal layer mapped to schema keys at ingestion, not a defect.
- OS→NS conversions verified arithmetically: `dateWritingStarted` NS 1893-10-20 = OS 1893-10-08 +12 ✓; `dateWritingCompleted` NS 1894-03-29 = OS 1894-03-17 +12 ✓ (19th-c. +12 days, both correct).
- No fabricated dates/venues: every date/venue traces to the editorial history. `bans` banDate and `excommunicationRelated` correctly flagged medium/resolved-confidence. ✓
- Minor: the proposal uses `workId:` (the universal dive field name) where the literal schema frontmatter key is `id`; harmless at the proposal layer (Ivan Ilyich + siblings do the same).

### 8 · Coverage honesty — ✓ PASS
Ledger is honest. "The author's later verdict" is correctly marked **partial** (not covered) in both the coverage block (l.828) and `index.md`'s dedicated section (l.182, `needsReview`). Reception and Scholarly context are legitimately `covered` (contemporary review + correspondence + church clarification; 5 triangulation entries). The "Material not covered" list in `index.md` matches the `notCovered`/`needsReview` blocks. ✓

### 9 · Rights/voice hygiene — ✓ PASS
- `visuals/` is **git-ignored** (`git check-ignore` → match; `git ls-files` → empty). No images tracked. `extracts/` holds only PD text + working-report `.md/.html`. ✓
- Only PD/CC0 images embedded in `index.md` (Tolstoy 1897 LoC PD; Cronstadt-Toulon lithograph CC0; Suttner 1903 PD). The `usable: unknown` Elpidin title page and the un-downloaded Avelan arch are never embedded. No "All rights reserved" reference anywhere. ✓
- `index.md` voice is bare/factual, minimal editorial — matches the project voice target. ✓

### 10 · Internal consistency — ✓ PASS
- Diary filename-date artifacts confirmed and handled correctly: D1 file `…1893_10_06` opens "Нынче 3 Ноября 1893" (true date 3 Nov OS) — dossier D1 dated 1893-11-03 with the artifact note. D3 file `…1894_03_09` opens "Февраля 94 … 23 Марта. Москва" (true date 23 Mar OS) — dossier D3 dated 1894-03-23 with the note. `index.md` (l.20, Method l.232) and the `contradictions` block agree. ✓
- Slug window `1893-1894` is consistent across frontmatter tags, title, intro, and Key-findings rationale (composition crosses the year boundary). ✓

---

## Required fixes (prioritized)

1. **[MUST — stale number] `index.md` line 232 (Method, Phase 5):** reads
   `` `verify_quotes.py` PASS (26/26 quotes byte-faithful) `` but the dossier carries **27** evidence quotes (W1–W16 + D1–D4 + L1–L7) and the script reports **27/27**.
   → Change `26/26` to `27/27`.

## Optional / non-blocking notes

- **(cosmetic) workRecord `workId:`** is the dive-proposal field name; the literal works-schema frontmatter key is `id`. Consistent with all sibling dives — leave as-is unless the ingestion convention is being tightened project-wide.
- No other discrepancies found. The `oldStyle`/`approximate` sub-keys, page-range citations (L1 «414–415» confirmed against the extract bibl line), and all entity statuses are correct.
