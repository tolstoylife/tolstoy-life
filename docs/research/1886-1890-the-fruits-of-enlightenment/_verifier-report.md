# Phase-5 Verifier Report — The Fruits of Enlightenment (Плоды просвещения, 1886–1890)

**Verifier:** fresh, independent adversarial pass (author did not self-approve).
**Date:** 2026-06-11
**Artifacts:** `index.md`, `dossier.yaml`, `extracts/`, works-schema v9 edit (`website/schema/tolstoy-works-schema.md`).
**Mechanical gate re-run:** `python3 docs/research/lib/verify_quotes.py …/dossier.yaml` → **32/32 verbatim, 0 facsimile missing, 0 label warnings — PASS** (re-confirmed by me).

---

## Check 1 — Byte-fidelity spot-check (belt-and-braces) — PASS

Independently `grep -F`'d these `quoteRu` against their named extracts; all verbatim:

| evidence id | extract | result |
|---|---|---|
| `fe-prof-mediumism` | v27_095_250_Plody_prosveschenija.txt | FOUND |
| `fe-ishitrilas-title` | v27_438_475_Ishitrilas.txt | FOUND |
| `fe-com-stageban` | v27_commentary_fruits.txt | FOUND |
| `fe-biryukov-mocks` | witness_1886_1890_diaries_letters.txt | FOUND |
| `fe-plan-lvov` | v27_433_435_Pervyj_plan.txt | FOUND |
| `fe-com-uncensored` | v27_commentary_fruits.txt | FOUND |

**TEI traceback (2 quotes → original TEI, not just the extract).** Extracted the play from `primary-sources/tolstoydigital-TEI/texts/works/v27_095_250_Plody_prosveschenija.xml` via `extract_tei.py --choice=reg --notes=auto` (6,490 lines). Both quotes appear verbatim in the freshly-extracted TEI:
- `fe-prof-mediumism` ("…Я говорю об энергии медиумизма.") → TEI-FOUND.
- `fe-land-need` ("…не то что скотину, — курицу, скажем, и ту выпустить некуда") → TEI-FOUND (and the same refrain recurs at the close, confirming `fe-made-people`).

The extract is faithful to source, not merely internally consistent.

## Check 2 — Every primary claim in index.md is source-anchored — PASS

Walked the narrative. Each load-bearing factual assertion traces to an evidence row or an attributed secondary source:
- 1886 twin-birth with *The Power of Darkness* → `fe-com-simultaneous` (verbatim "одновременно или почти одновременно с работой над «Властью тьмы»").
- Séance source / Lvov / "on his own initiative" → `fe-com-seance`; cane-and-milk → `fe-com-milk`; Lvov in 1884 diary → `fe-diary-lvov-1884`.
- 30 Dec 1889 staging + cast → `fe-com-staging` + `fe-com-staging-cast` (full cast list verbatim).
- 1891 uncensored publication → `fe-com-uncensored`.
- Stage-ban chronology (Alexander III ruling; Feoktistov 28 Apr 1890; reaffirmed 11 Mar 1891; Alexandrinsky 26 Sept 1891; provincial from Nov 1893; general 1894) → all present in the `fe-com-stageban` extract paragraph (independently confirmed; the apparatus carries every date the index cites).
- Prototypes (Lvov→Zvezdintsev, Samarin→Sakhatov, Butlerov name-source, Feldman→Grossman) → `fe-com-prototypes` + `fe-let-wagner`.
- Secondary-only items are explicitly marked secondary: Maly transfer Dec 1891 ("this date is secondary-sourced, not in the apparatus — see `needsReview`"); Stanislavski via Britannica/My Life in Art.

## Check 3 — Secondary claims ATTRIBUTED, not asserted — PASS

- Simmons, Britannica, Wikipedia, Stanislavski (*My Life in Art*), Raskolnikov (1928), Maude all named in-text and in References → Background.
- **CRITICAL item PASS:** Mendeleev's 1875–76 commission and the medium D. D. Home are presented as general history-of-science background and **explicitly excluded** from the PSS apparatus. index.md line 258 states it outright: "Mendeleev's commission and the medium D. D. Home … are **not** in the PSS Tom 27 apparatus … the wider science-history frame is attributed strictly to general scholarship, never to the PSS." References → Background repeats it ("Background — NOT in PSS"); `needsReview` item reinforces it. The play's own naming of «Юм» (Home) is correctly distinguished from the external science-history frame.
- No contested movement-labels adopted in the dive's own voice; "Tolstoyan" framing routed to the Tolstoyanism cross-link.

## Check 4 — Marquee discipline — PASS

- Marquee stated as a hypothesis ("The claim this dive set out to test:"), outcome **`confirms` + `extends`**, not a foregone "confirms." Explicitly: "`confirms` on the play's targets and its external facts; `extends` on the interpretive spine."
- The three `extends` claims (audience-inversion vs *Power of Darkness*; *What Is Art?* continuity; stage-ban irony) are framed as the dive's corpus-grounded synthesis ("a turn no mainstream source draws," "the dive's synthesis," "the mainstream simply omits").
- **What-Is-Art NOT over-claimed:** index.md line 76 explicitly fences it — "*Fruits* is not a demonstration of accessible 'good art' — it is a satire for the educated … The continuity is one of target (false enlightenment, false art), not of method." This is exactly the discipline the brief required.
- `scholarship.triangulation`: all 6 entries reference valid `evidenceRef`s (`fe-biryukov-mocks`, `fe-com-prototypes`, `fe-land-need`, `fe-ge-three-works`, `fe-com-stageban`, `fe-diary-trash`) and use valid relations (`extends` ×3, `confirms` ×3). Relations match the marquee outcome.

## Check 5 — Entity routing (wiki-schema v1.4) — PASS

- Fictional figures → `character` with `prototypes[]`: Tanya, Zvezdintsev, Krugosvetlov, Grossman, Sakhatov, Semyon. ✓
- Real people → `person`: Lvov, Samarin, Davydov, Butlerov, Wagner, Feldman, Stakhovich, Lopatin, Stanislavski, the Tolstoy daughters, Chertkov, Tolstoy. ✓
- Spiritualism → `concept`; theatres + press-office → `institution`; séance + première → `event`. ✓
- **Krugosvetlov←Butlerov NOT over-claimed:** `certainty: probable`, with a note stating it is a "name-source/composite, NOT a documented portrait," that "Tolstoy explicitly DENIED portraying Butlerov or his friend N. P. Wagner," and "Do not overclaim." Exactly as the brief demanded. (By contrast Zvezdintsev←Lvov and Sakhatov←Samarin are `documented` — justified, since the characters bear the real surnames in the plans, confirmed verbatim in `fe-plan-lvov`.)
- **vaultStatus vs `website/src/wiki/`:** all 14 pages confirmed present (Leo Tolstoy, Sophia Tolstaya, Tatyana/Maria/Sergei/Lev Lvovich/Andrei Tolstoy(a), Alexandra Tolstaya, Vladimir Chertkov, Pavel Birukoff, Yasnaya Polyana, Astapovo, Tolstoyanism, Christian Anarchism). Dossier marks `T. L. Tolstaya`, `M. L. Tolstaya`, `V. G. Chertkov`, `Leo Tolstoy` as `exists` — all four pages exist. ✓ Every other entity marked `missing` has no page — verified by absence. No wrong `exists`/`missing` found.

## Check 6 — workRecord — CONCERN (minor, already self-flagged)

- Current works-record stub confirmed: `publishedDuringLifetime: false`, `publishedInRussiaDuringLifetime: false`, `genre: play`, `mainCategory: Plays`, `subcategory: Comedy`. The dive's corrections to **both** booleans → `true` are evidence-anchored to `fe-com-uncensored` (1891, Russia, uncensored; Tolstoy died 1910). Correct.
- `bans[].scope: stage-ban` matches the new v9 schema value (see Check below). Dates plausible: OS 28 Apr 1890 → NS 10 May 1890 (+12 days, correct for C19); banLifted 1894 approximate. ✓
- Field names checked against the schema. **Two out-of-enum values, both hedged in `note`/`needsReview` but worth surfacing:**
  - `titleAlternatives[].type: working-title` — schema enum is `working` (§1). The dossier note flags "verify … if absent, use the nearest permitted value." Should be `working`.
  - `relatedWorks[].relationshipType: related` — schema enum (§7) is `cycle · sequel · prequel · revision · source · companion · adaptation`; **`related` is not in it.** `companion` (used for *Power of Darkness*) is valid. The dossier flags relationshipType for ingestion review but its note only asserts "companion is attested" and does not call out that `related` itself is invalid. Recommend `companion` or `cycle` for the Kreutzer link, resolved at ingestion.
- These are *proposals* hedged for ingestion, not committed frontmatter (the live record is still the untouched draft stub, validator-clean). Hence CONCERN, not FAIL.

## Check 7 — Coverage honesty — PASS

- `Visual & manuscript record` correctly marked `partial` (8 PD images; no 1891-première photo / Korovin designs / 1889 production photo / Posrednik first-edition title page — the VIS-GAP-premiere work-order is honest).
- `The Gogol/Ostrovsky/Molière comedic lineage` marked `partial` ("context, not a sourced thesis") — honest.
- The five `covered` surfaces are genuinely covered; none overstated. Redactions surface correctly notes "Full manuscript collation not done (sampled, per novel-mode)" while marked covered — acceptable under novel-mode's sampling rule and disclosed in notCovered.

## Check 8 — Voice & hygiene — PASS (1 trivial note)

- Voice factual, not purple; no editorializing beyond the disclosed interpretive synthesis. The closing "and was, all the same, very good" (line 293) is a light evaluative flourish — acceptable as a section-closing judgment, the one place worth a glance, but within house tolerance.
- All Russian quotes labelled "(working English)". ✓
- `extracts/` holds **only PD text** — no image files committed (scanned: 0 jpg/png/etc.). ✓
- `visuals/` images are **git-ignored** (`git check-ignore` confirms) — matches the index.md claim that "the cache is git-ignored." ✓
- Dive visuals are **not referenced from `website/src/`** (grep clean). ✓
- **nl2br rule:** every blockquote is a single source line (16 `^>` lines, none multi-line-wrapped); paragraphs each on one source line (longest lines 953/946/906 chars = whole paragraphs, confirming no hard-wrapping into ragged `<br>` columns); list items each on one line with a blank line before each list. PASS.

---

## Additional finding (raised, then cleared) — Wagner quoteEn ≠ quoteRu mapping — CONCERN (resolved, source-faithful)

`fe-let-wagner` byte-verifies its `quoteRu` ("И главное мое с годами всё усиливающееся отвращение … спиритизм.") — the §3 sentence. But its `quoteEn` prepends "Of you and of Butlerov I never thought while writing the comedy." That clause is **not** in the verified `quoteRu`, so the mechanical verifier never checked it. I traced it to the extract: it **is** present verbatim — "О вас и о Бутлерове я никогда не думал, пиша комедию" (§2 of the same letter). So the English gloss is source-faithful; it simply conflates §2 (the denial) and §3 (the hatred-of-superstition) into one "(working English)" gloss and elides §3's opening clause. No fabrication; the index.md blockquote uses only the verified §3 sentence, so the reader is not misled. Flagging only because the dossier's En→Ru mapping is not 1:1 — a tidy-up, not a defect.

---

## VERDICT: CLEAN-WITH-CONCERNS

The dive is byte-faithful (32/32 + independent spot-checks + TEI traceback), source-anchored, correctly attributed (Mendeleev/Home discipline observed), marquee-disciplined (confirms+extends, What-Is-Art fenced), correctly routed (Butlerov prototype not over-claimed; all 14 vault pages verified), coverage-honest, and hygiene-clean (no images in extracts, visuals git-ignored and unreferenced, nl2br correct). The works-record corrections are evidence-anchored and the live record is validator-clean.

### Prioritized fix list (all minor, all resolvable at ingestion — none block shipping)

1. **`relatedWorks[].relationshipType: related` is out-of-enum** (schema §7 has no `related`; use `companion`/`cycle`). Dossier flags relationshipType for review but doesn't name `related` as invalid — tighten the `needsReview` note. (Highest priority of the three: it's a hard enum miss, not just a naming variant.)
2. **`titleAlternatives[].type: working-title`** → schema enum is `working`. Already flagged for ingestion; normalize to `working`.
3. **Cosmetic:** `fe-let-wagner` `quoteEn` conflates two non-adjacent sentences; consider splitting the gloss or trimming to match the verified `quoteRu` so the dossier En↔Ru mapping is 1:1. (Source-faithful as-is; optional.)
