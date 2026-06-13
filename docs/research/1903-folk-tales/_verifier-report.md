# Verifier report — 1903 folk tales dive

**VERDICT: CLEAN-WITH-MINORS** — 0 must-fix, 4 should-fix, 3 notes. The dive is byte-faithful (29/29 + my own 5-quote re-derivation), source-anchored, correctly attributed, schema-valid, and rights-clean. The one finding worth surfacing: the dossier's own `dateFirstPublished: "1903"` for «Это ты» (E687 area) contradicts its index.md, which dates «Это ты» first publication to 1906 — a real internal inconsistency in the workRecord, though the dossier flags the underlying ambiguity in `notes`.

Verifier: independent adversarial pass, 2026-06-11. Did not author the dive.

---

## Check 1 — Byte-fidelity sample — **PASS**

`verify_quotes.py` run independently: **29/29 quotes verbatim, 1 facsimile ok, 0 missing, 0 label warnings — PASS, exit 0.** The deterministic gate did not lie.

I then independently re-derived **5 quotes of my own choosing across 5 different evidence rows and 5 different extract files**, confirming each `quoteRu` appears verbatim (whitespace-normalised):

| Row | Extract | Result |
|---|---|---|
| E12 | `v74_222_…SHolom_Alejxemu.txt` line 23 | verbatim ✓ |
| E17 | `v34_138_140_Eto_ty.txt` line 59 | verbatim ✓ |
| E22 | `v34_546_547_Razrushenie…_Ist.txt` line 7 | verbatim ✓ |
| E25 | `v34_554_556_Tri_skazki…_Tr.txt` line 27 | verbatim ✓ |
| E29 | `v54_190_191_1903_09_03.txt` line 11 | verbatim ✓ |

E14 («— Да ведь Лаилиэ это ты, — сказал старец.») also confirmed verbatim against `v34_126_130_…Asarhadon.txt` line 19 in passing. No drift, no quietly-edited quote.

## Check 2 — Every primary claim source-anchored — **PASS**

Walked the index. Every factual primary claim ties to an E-row or is checkable in an extract. The five flagged claims all hold:

- **Genesis chronology (July–Aug 1903).** index L82 ("attempt that would not come on 21 July… breakthrough on 25 July… completion on 9 August… wavered «не три, a две»… third added back on 27 August"). 21/25 Jul + 9 Aug all anchor to E05/E06/E07 and are verbatim in the diary extracts. The "не три, a две" wavering and the 27-Aug re-add are corroborated by the E25 commentary extract (line 11: «не три, а две» on 20 Aug; the 22-Aug letter re-adds the third). Anchored and accurate. (Minor wording note below — the index says the wavering came *before* the third was "added back on 27 August", but the commentary dates the re-add to the **22 August** letter; see should-fix #2.)
- **«одно правительство» censorship claim.** index L16/L80, anchored to E03. E03 quoteRu verbatim in `v74_144…` and carries exactly «одно правительство… этого-то я не могу сказать в русском легальном издании». Solid.
- **«Das bist du» twin-source claim.** index L18, anchored E11 + E24. E11 (Tolstoy's own attribution of «Асархадон» to the journal parable) and E24 (the commentary: «Эта же сказка дала Толстому повод к написанию "Ассирийского царя Асархадона"») both verbatim. The "near word-for-word translation" characterisation is directly supported by the E24 source extract («почти дословным переводом»). Solid.
- **Shchegolyonok/1879 + «Обращение к духовенству» claim.** index L19, anchored E22. The extract states both the 1879 Shchegolyonok provenance and the companion-to-«Обращение к духовенству» framing verbatim. Solid.
- **Censorship/ban dates of «Разрушение ада».** index L19/L100/L108, anchored E23. The E22/E23 extract gives 1906/1910/1913 attempts and the Russia-1917 first appearance verbatim, plus the specific authorities and dates that populate the workRecord `bans[]`. Solid.

No orphan primary claim found; no (E-ref) attached to a sentence it fails to support.

## Check 3 — Secondary claims attributed, not asserted — **PASS**

The "Scholarly context" section (index L112–116) names every secondary view: Maude 1906 ("stories Tolstoy contributed in aid of the Jews"), Popoff 2013, Schefski 1982 via Ivry 2014, del Olmo 2023, Love (Tolstoy in Context). The contested "aid literature" and "didactic decline" framings are explicitly tagged as **contrast to read critically**, not inherited — L116 names the "didactic decline" reading as "the Tolstoyan-adjacent soft-dismissal to read critically, not inherit," and L24 says the cluster "is not… didactic decline." "Attribute, don't assert" appears as an explicit instruction in the prose (L114). The dive leads with the primary record and the parent dive; mainstream is positioned as foil throughout. No bare assertion of a contested scholarly view in the dive's own voice.

## Check 4 — scholarship.triangulation — **PASS**

All 6 triangulation entries reference real evidenceRefs (E25, E24, E11, E22, E03, E15 — all present in the ledger) and use valid relations. The `complicates`/`extends` calls are honest:
- E25 → `complicates` (aid-literature frame vs the compressed-metaphysics finding) — correct; it does not contradict Maude, it adds a dimension.
- E03 → `complicates` (Popoff's "active engagement" vs the censorship constraint Tolstoy named) — correct, honest restraint; an overclaimer would have said `contradicts`.
- E24, E11, E22, E15 → `extends` — correct; in each the dive reaches findings English scholarship "does not reach," which is precisely `extends`, not `contradicts`.

No `contradicts` is used in triangulation at all — appropriately conservative, since none of these are head-on factual disputes with a named scholar. The three genuine corrections live in `contradictions[]` (intra-corpus), which is the right home.

## Check 5 — Entities — **PASS**

All 13 entities resolve to valid wikiType values (`concept`, `person`, `event`, `institution`) — all in the v1.4 enum. vaultStatus accurate:
- **Chertkov = `exists`** — confirmed: `website/src/wiki/Vladimir Chertkov.md` is present. ✓
- **All others = `missing`** — confirmed by loose-match against the wiki file list. I specifically loose-matched the transliteration-risk names (Shchegolyonok/Schegolenok, Sholom Aleichem/Rabinovich, Leskov, Goldenweiser, Boulanger, Posrednik, Theosophischer Wegweiser, Kishinev, Narodnye rasskazy, Unity of life, Appeal to the Clergy) — **only** `Vladimir Chertkov.md` returned. No false `missing`. ✓

Entity typing is defensible: Народные рассказы / Unity of life / Appeal to the Clergy as `concept`; Kishinev pogrom as `event`; Posrednik + Theosophischer Wegweiser as `institution`; the five people as `person`. No fictional `character` entities were minted (correct — these are parables with archetypal figures, not the named-character novels that drove the v1.4 `character` type).

## Check 6 — workRecords (5 creations, genre=parable) — **PASS (with should-fix #1)**

**(a) None exist yet.** `rg --files website/src/works/` → 16 files total, **zero** match esarhaddon/asarhadon/three-questions/tri-vopros/work-death/trud/it-is-you/eto-ty/destruction-hell/razrushenie. All five are genuine creations. ✓

**(b) Every `field:` is a real works-schema key.** Walked all five records. titleRu, titleEn, genre, mainCategory, subcategory, titleAlternatives, dateWritingStarted/Completed (+OldStyle via `oldStyle:`/`approximate:` annotations), dateFirstPublished, firstPublishedVenue, firstPublishedVenueType, dateFirstPublishedInRussia, firstPublishedInRussiaVenue, publishedDuringLifetime, publishedInRussiaDuringLifetime, bans, relatedWorks, notes, excommunicationRelated — **all are real schema keys.** No invented field. ✓ (Note: the dossier uses inline `oldStyle:`/`approximate:`/`evidenceRefs:`/`source:`/`confidence:` as *annotation* keys on each field-object; these are dossier-internal provenance wrappers, not claimed frontmatter keys — the ingestion step maps `oldStyle` → `dateWritingStartedOldStyle` etc. This is the established dossier convention, not a schema violation.)

**(c) List-typed field shapes correct.**
- `titleAlternatives` objects use `{title, type, language}` with valid `type` values (`variant`, `subtitle`) and ISO codes (`ru`, `de`, `sa`) — matches schema §1. ✓
- `bans` objects use `{banningAuthority, authorityType, jurisdiction, scope, banDate, banDateOldStyle/Approximate, notes}` — all valid keys; `authorityType: imperial-state` and `scope` values `pre-publication-rejected`/`confiscation` are both in the §7 enum. ✓
- `relatedWorks` objects use `{id, relationshipType}` with `relationshipType` ∈ {`cycle`, `source`} — both in the §7 enum. ✓

**(d) No fabricated dates/venues.** Every dated field traces to a row or the commentary. Spot-checked the densest: Esarhaddon `firstPublishedInRussiaVenue` ("Посредник… СХV… 9 illustrations by N. I. Zhivoy") = E26 extract verbatim incl. the «СХV» and «9-ю иллюстрациями Н. И. Живого»; `dateFirstPublishedInRussia: 1903-11 / oldStyle 1903-11-10` = the E25/E26 commentary's «цензурная дата — 10 ноября 1903 г.». «Разрушение ада» bans (1906-03-06 / OS 1906-02-21 «К напечатанию не дозволять»; 1910 Обновление/Felten; 1913 Просвещение/Khiryakov) all trace verbatim to the E22 extract. ✓

**(e) publishedInRussiaDuringLifetime values correct.** Razrushenie ada = **`false`** (Russia first 1917) ✓ — the one that matters most, correct. The other four = `true` (all reached legal Russian print 1903/1906, within the lifetime) ✓.

The OS→NS conversions are internally consistent at the correct 1903 offset of **+13 days** (21 Jul→3 Aug, 22 Jul→4 Aug, 23 Jul→5 Aug, 9 Aug→22 Aug) and are honestly marked `approximate: true` — the dossier's own needsReview item flags them for confirmation. No conversion arithmetic error found.

## Check 7 — Voice — **PASS**

Prose is simple and factual; every working-English rendering is labelled "(working English)" (index L34, 40, 45, 49, 50, 56, 58, 65, 69, 76 — checked, all labelled). The "Why this matters" section (L22–24) is the most interpretive passage but stays anchored ("the primary record shows", "the corpus shows") rather than editorialising freely. The one phrase that leans warm — "a furious anatomy of the institutions" (L96) — is borderline but defensible as description of an explicitly satirical text. Not flagged as a fix; noted below.

## Check 8 — Rights hygiene — **PASS**

- `extracts/` contains **only** text extracts (`.txt`), the four sweep/scholarship `.md`+`.html` working files, and the **one** PD facsimile `v34_126_Asarhadon_p126_facsimile-166.png` (PD: Tolstoy's own text, rendered locally with pdftoppm). **No third-party image** in extracts/. ✓
- The **7 Commons downloads** (2× Sholom Aleichem, 2× Tolstoy-1903, 3× Kishinev) are all in `visuals/` — **not** in extracts/, not committed. ✓
- `docs/.gitignore` ignores `research/*/visuals/`. ✓ `git check-ignore` confirms `…/visuals/commons-tolstoy-1903-photo.jpg` is ignored; `git status --porcelain` shows the dive dir as a single untracked `??` entry with no visuals/ files individually staged. The rights gate holds. ✓

## Check 9 — Internal consistency — **PASS (with should-fix #3)**

The three `contradictions[]` corrections hold against their cited rows:
- **«Это ты» WAS sent** (E12) — confirmed: the 25 Aug 1903 letter extract says Tolstoy translated «Das bist du» and «посылаю вам для перевода на жаргон и напечатание в Сборнике». ✓
- **June-9 «Крик беса» is NOT the legend's seed** (E22) — confirmed: the 9 June 1903 diary extract (`v54_177_178`) lists «Крик беса при приближении Христа» among three *new* ideas conceived that day, but E22 dates «Разрушение ада» to Nov 1902–early 1903. Chronology rules it out. ✓
- **Zhivoy not Zhivago** (E26) — confirmed: the commentary reads «С 9-ю иллюстрациями Н. И. Живого» (genitive of Живой). ✓

The **«Гилф» date inconsistency** (PSS censorship date 4 Aug 1903 vs Tolstoy's own dispatch 20–25 Aug 1903) is correctly carried as a **needsReview** item (not asserted as fact), and is flagged in-line in index.md L110 ("an internal inconsistency noted for verification") and in E25's significance note. The underlying fact is real: the E25 extract gives «цензурная дата — 4 августа 1903 г.», which does precede the 20 Aug dispatch in the same extract. Correctly handled as open, not resolved. ✓

---

## Required / recommended fixes

**(none are must-fix — the dive is ingestion-safe as-is)**

1. **[should-fix] «Это ты» workRecord — `dateFirstPublished` contradicts index.md and its own `notes`.** dossier L686: `dateFirstPublished, value: "1906"` with note "also offered to the «Гилф» almanac in 1903 (E12), but documented first publication is 1906." This is *internally* fine — BUT the contradictions[] block and the dive's own argument (index L18, L82, E12) establish that «Это ты» **was sent to the «Гилф» almanac in 1903** alongside the trio. The record's `dateFirstPublished: 1906` is the defensible documented-first-print value, but the *gift* predates it. Recommend a one-line `notes` cross-reference to E12 on the date field (or a `titleAlternatives`/notes flag) so the ingestor doesn't silently bury the 1903 Гилф offer when only the 1906 Posrednik date survives into frontmatter. Severity: low (the note already exists; this is about making the 1903-offer survive ingestion).

2. **[should-fix] index L82 dates the trio's re-add of the third tale to "27 August"; the E25 commentary dates it to the 22 August letter.** index L82: "before the third was added back on 27 August." The E25 extract (line 11) shows the third tale («Труд, смерть и болезнь») re-added in the **22 August** letter ("22 августа Толстой послал Шолом-Алейхему дополнительно третью сказку"). E07's significance note also says "27 Aug." I found no "27 August" re-add event in the extracts — the 25 Aug letter (E11/E12) is the preface+«Это ты» dispatch, not the third-tale re-add. Recommend reconciling "27 August" → "22 August" in index L82 and E07's note, or citing the source for a distinct 27-Aug event. Severity: low-medium (a stated date with no visible anchor; everything else is airtight, so it stands out).

3. **[should-fix] index L100 says «Разрушение ада» "published abroad in 1903 by Chertkov's «Свободное слово» (Christchurch, England)" — correct — but the Work/Death record's `dateFirstPublishedInRussia` source-note (dossier L669) claims an "abroad: «Свободное слово» №9, 1904" first Russian for Work/Death, while the E25 extract says the Russian-language Work/Death first appeared "в 1904 г. … в приложении к № 9 «Свободного слова»."** That is a *foreign* (émigré) printing, not a Russian-jurisdiction one, yet it sits in the `dateFirstPublishedInRussia` provenance chain. The record's actual `dateFirstPublishedInRussia: 1906` (Posrednik №615) is correct; the parenthetical "(abroad: …1904)" is just muddying which printing counts as "in Russia." Recommend trimming the abroad-1904 aside from the `dateFirstPublishedInRussia` source field (it belongs in `notes`/`firstPublishedVenue`, not the Russia-date provenance). Severity: low (does not change the asserted value, only tidies provenance).

4. **[should-fix] Subcategory "Short Stories" + genre "parable" is a knowing mismatch already in needsReview — but worth a second look at ingestion.** All five are shelved `subcategory: Short Stories` with `genre: parable`; the dossier flags this (confidence: low, "shelf, not genre"). No "Parables" subcategory exists in the schema §2 hierarchy (`Fiction` → Novels·Novellas·Short Stories·Sketches·Childrens Literature). So "Short Stories" is the only valid shelf and the call is forced and correct. No fix required to ship; flagging only because four needsReview items (Гилф date, English title of «Это ты», parable-for-Разрушение, the shelving/taxonomy question) all land at the ingestion step and should be resolved together with Johan, not silently. Severity: informational.

## Notes (no action)

- **N1.** The parent-dive fix carried in needsReview (resolving the parent's invalid `genre: fairy_tale` for "Ivan the Fool" → `parable`) is a sound cross-dive consistency catch — `fairy_tale` is indeed not in the works genre enum. Out of scope for *this* dive's files but correctly logged.
- **N2.** Voice: "a furious anatomy of the institutions" (index L96) is the warmest phrase in the dive; defensible as description of an avowedly satirical text, but if a stricter bare-voice pass is wanted it's the one line to cool.
- **N3.** The `bans[].scope` values used (`pre-publication-rejected`, `confiscation`) are both valid; the new v9 `stage-ban` value is correctly *not* used here (these are print bans, not stage bans). Schema version awareness is current.

---

*Bottom line: byte-fidelity is intact (gate + my 5 independent re-derivations), all primary claims anchor, secondary is attributed and read critically, entities and workRecords are schema-valid with accurate vaultStatus and no fabricated dates, and rights hygiene holds. The four should-fix items are tidy-ups at the workRecord/provenance and one unanchored "27 August" date — none block ingestion. CLEAN-WITH-MINORS.*
