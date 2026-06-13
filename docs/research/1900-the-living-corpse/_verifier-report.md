# Separate-pass verifier report — The Living Corpse (Живой труп) dive

**VERDICT: CLEAN-WITH-MINORS**

Independent adversarial review (I did not author any of this). The mechanical gate re-ran here: `verify_quotes.py` → **40/40 verbatim, 0 facsimile missing, 0 label warnings, exit 0**. Belt-and-braces checks below confirm the dive is sound; findings are 0 BLOCKER, 5 MINOR, 6 NOTE.

---

## 1. Byte-fidelity spot-check (9 quotes across all genres) — PASS

Each `quoteRu` re-grepped with `grep -F` in its named extract:

| id | extract | genre | result |
|---|---|---|---|
| lc-suicide-note | v34_007_099_play.txt | play | ✓ verbatim |
| lc-tri-vybora | v34_007_099_play.txt | play | ✓ verbatim |
| lc-chernyshevsky | v34_007_099_play.txt | play | ✓ verbatim |
| lc-uncle-vanya | v54_010_010_1900_01_27.txt | diary | ✓ verbatim |
| lc-brosit | v54_065_066_1900_11_28.txt | diary | ✓ verbatim |
| lc-chertkov-baluyas | v88_607_chertkov_dec12.txt | letter | ✓ verbatim |
| lc-comm-protasovy | v34_533_543_history.txt | commentary | ✓ verbatim |
| lc-var-kryukova | v34_411_483_variants.txt | variants | ✓ verbatim |
| lc-plan-predsmertnye | v34_407_410_plans.txt | plans | ✓ verbatim |

All `quoteEn` carry the `(working English)` label (verify_quotes reports 0 label warnings across all 40). Translations are fair and unembellished. Two worth noting as accurate-but-loose (not errors — flagged for transparency only):

- **[NOTE] lc-brosit** — «ту драму» is rendered "that [other] drama" with an editorial gloss; defensible given the 7 Sept "большая/малая драма" distinction (which the dossier itself records under `notCovered`). Acceptable.
- **[NOTE] lc-kreutzer-lineage** — the `quoteEn` is a *composite* gloss: the bracketed work-names and the «Не то ли и с Трупом?» tail are paraphrased into the English, but the `quoteRu` field itself is only the verbatim fragment «я писал без всякой думы о проповеди людям, о пользе». The fuller Russian («Не то ли и с Трупом») was independently confirmed present in the extract (grep ✓), so nothing is invented — but a reader comparing the English to the single quoted Russian line will find the English says more than the Russian shown. Working-translation latitude; within bounds for a dive (not wiki-grade), no fix required.

## 2. Claim-anchoring (index.md primary claims) — PASS

Every primary claim traces to an evidence id / extract. Specifically re-verified:

- **«возмутился» / provoked-by-Uncle-Vanya correction** (index L17, L63) — anchored to lc-uncle-vanya (diary, grep ✓) + lc-comm-uncle-vanya (PSS confirms Jan-1900 start "после просмотра… Дядя Ваня"). Solid; this is the dive's headline correction and it is fully sourced.
- **Marriage/divorce-law trap** (perjured adultery) — lc-razvod-lozh, lc-suicide-note, lc-ne-lgat, all play-text verbatim. The *statistic* (0.0038% / 1913) is correctly quarantined to the secondary layer (see §3).
- **Prototype mappings** — Protasovs←Gimers (lc-comm-protasovy ✓), Anna Pavlovna←Simon (lc-comm-simon ✓), Aleksandrov←Ivanov (lc-comm-ivanov ✓), Afremov←Ofrosimov (lc-comm-ofrosimov ✓). All four PSS-named edges grep-confirmed in the commentary extract.
- **Abandonment chronology** — Aug dissatisfaction (lc-ne-delo-bozhie, 21 Aug ✓) → 28 Nov drop (lc-brosit + lc-narod-vina, both ✓, with the Novikov/people's-need driver in-extract) → 12 Dec Chertkov (lc-chertkov-baluyas, lc-chertkov-legkomysl ✓). Chronology is airtight and the "conscience-turn dominant in his own hand" reading is genuinely supported.
- **Title evolution Труп→Живой труп** — confirmed independently against v34_543_545_manuscripts.txt: ms. № 12 carries «Заглавие рукой Толстого: „Живой труп"», and base ms. № 14 opens «Живой труп». The index's "appearing on the copy that is manuscript № 12" (L95) is exactly right. *(NOTE: this manuscripts extract is not itself an evidence row — see §10/MINOR-1.)*
- **Keystone Kryukova redaction** — lc-var-kryukova (✓), correctly tagged KEYSTONE; the "restored in Act V picture 2" detail matches the variants apparatus.

## 3. Secondary-claim attribution — PASS (one minor gap)

Reception/scholarly claims are attributed, not asserted, and appear in References:

- 1911 MAT cast & directors → "cast per Russian Wikipedia" (index L136) + Alexandrinsky collection for the Meyerhold rivalry. Attributed.
- Wachtel (PMLA 1992), Simmons (1968) → named inline and in References. ✓
- Divorce statistics → "popular and scholarly sources agree… ~0.0038%" with Russia Beyond / UNI ScholarWorks in References. ✓
- "about-face" reading → attributed to Kommersant (2024). ✓
- Redemption / Barrymore / 1929 Otsep film → afterlife para (L138–140), with EN/RU Wikipedia in References.

- **[MINOR-2] "204 performances"** (index L138) and **"seventeen / seventeen screen versions across nine countries"** (L21, L140) are stated as bare figures. The film count is loosely sourced ("The Russian Wikipedia lists seventeen"), but the **204-performance Broadway run** has no inline attribution. It belongs to the same EN-Wikipedia/IBDB reception sweep already in References, so this is a thin-attribution nit, not an unsupported claim. Fix: append "(per …)" or fold into the existing Wikipedia citation.

No secondary claim is smuggled in as primary fact. No byte-fidelity is demanded of secondary sources — correct per the prototype-rigor rule.

## 4. Scholarship triangulation — PASS

All 7 `triangulation[].evidenceRef` resolve to real evidence ids (lc-chernyshevsky ×2, lc-comm-davydov, lc-suicide-note, lc-kreutzer-lineage, lc-brosit ×2). All `relation` values ∈ {confirms, complicates, extends} — valid. The marquee outcome **confirms + complicates + extends** is genuinely staged by the evidence:

- `confirms`: Wachtel/Chernyshevsky (lc-chernyshevsky) + Simmons/legal-circle (lc-comm-davydov) + divorce-trap (lc-suicide-note).
- `complicates`: the "about-face" (lc-kreutzer-lineage) and "spared the Gimers" (lc-brosit) readings.
- `extends`: the in-play Chernyshevsky citation + the diary-grounded conscience-turn.

Not overstated — each leg is carried by a verbatim quote. This matches the index's stated verdict (L50) and the Key-findings framing.

## 5. Entities — PASS

- **wikiType validity**: every `entities[].wikiType` used (character, person, group, event, institution, adaptation) is in the wiki-schema v1.4 enum (all 12 types confirmed present in `website/schema/wiki-schema.md`).
- **vaultStatus**: grep of `website/src/wiki/` returns 14 content pages; only **Vladimir Chertkov.md** and **Pavel Birukoff.md** match dive entities. Dossier marks exactly those two `exists` and every other entity `missing`. Accurate.
- **character vs person routing**: fictional figures (Fedya, Liza, Karenin, Masha, Anna Pavlovna, Aleksandrov, Afremov) all routed `character` with `prototypes[]`; real people (the Gimers, Simon, Davydov, Koni, Ivanov, Nemirovich-Danchenko, Stanislavski, Moskvin, Chekhov, Posse, Biryukov) all `person`; gypsy choirs `group`. No mis-route.
- **prototype certainty**: the four PSS-named edges are `documented`/`basis: editorial` (correct); Karenin←Chistov is `conjectured` with an explicit "NOT named in the PSS" note (correct); Masha is `conjectured`/milieu-only (correct). Certainty is **not** over-claimed.

## 6. WorkRecord — PASS (one minor field-name flag)

- **Record-creating**: confirmed no `works/` record exists — `rg --files website/src/works/` returns nothing matching *living*/*trup*. The proposal at `plays/drama/the-living-corpse/` mirrors the existing `plays/drama/the-power-of-darkness/` precedent. Correct.
- **completionStatus=incomplete** — right (Tolstoy revised only Acts I–II of the base copy; "оно не кончено… совсем бросил", lc-comm-koni-1904).
- **publishedDuringLifetime=false / publishedInRussiaDuringLifetime=false** — right (withheld; first published Sept 1911, posthumous).
- **bans=[]** with the "author-withheld, not censored" rationale — defensible and well-argued (distinct from the PoD/Fruits stage-bans; the play ran freely at MAT *and* the imperial Alexandrinsky in 1911). The one residual ("verify no incidental 1911 stage-censorship") is correctly parked in needsReview.
- **OS/NS dates** — all three pairs are arithmetically correct, *including the leap-century subtlety*: Jan 1900 (pre-1-Mar-1900) → +12 (1900-01-27 OS = 1900-02-08 NS ✓); Aug 1900 (post-boundary) → +13 (1900-08-15 OS = 1900-08-28 NS ✓); 1911 → +13 (1911-09-23 OS = 1911-10-06 NS ✓). This is a frequent error elsewhere and is done right here.

- **[MINOR-1] OS/approximate sub-field naming.** The workRecord proposal uses bare keys `oldStyle:` and `approximate:` nested under each date field, but the live works schema names them per-field: `dateWritingStartedOldStyle` / `dateWritingStartedApproximate`, `dateFirstPublishedOldStyle`, etc. As a *dossier proposal* this is a shorthand, not live frontmatter, so it is not a data error — but the ingestor must expand these to the schema's flat per-field names (and `dateWritingStartedApproximate` is implicitly false where omitted). Fix: at ingestion, map `oldStyle`→`<field>OldStyle`, `approximate`→`<field>Approximate`.
- **[NOTE] `identifiers.jubileeEdition.volumes`** is used as a workRecord field, but the schema's `identifiers.*` table lists only wikidata/openLibrary/gutenberg/internetArchive/etc. — there is no documented `identifiers.jubileeEdition`. This key is, however, used by the same convention in prior dives; treat as an established-but-undocumented extension, not an error. Flag for schema-doc catch-up.
- **[NOTE] relatedWorks=[]** — correctly left empty with a clear rationale (the schema `relationshipType` enum has no "thematic sibling" value for the Kreutzer/PoD/Resurrection grouping). Honest; deferred to a human call. Confirmed the enum is {cycle, sequel, prequel, revision, source, companion, adaptation} — no fit.

## 7. Coverage honesty — PASS

- "Russian society & church reaction (contemporary, pre-1911)" → `partial`, with the correct rationale (play unpublished until 1911 → no contemporary public/church reception; only the Gimer plea + press leak). Honest — not dressed up as `covered`.
- "Manuscript facsimile" → `not-covered`, correctly noting Commons has none and the local archive-org PDFs are Wiener's *English* edition, not the Russian PSS.
- "Variant collation" → `partial` (sampled for the keystone only). Honest.
- No `covered` status overstates what the evidence shows.

## 8. Voice & rights — PASS

- **Voice**: index.md is factual and attribute-don't-assert throughout; scholarly section is explicitly framed as "a divergence map, not corroboration." No editorialising beyond the sourced marquee reading. Consistent with the site voice target.
- **Rights / images**: `git ls-files` on the dive dir returns **no tracked image files**. `visuals/` is git-ignored (`docs/.gitignore:18` → `research/*/visuals/`; `git check-ignore` confirms a sample jpg is ignored). The 12 PD images sit locally only. `extracts/` holds text only. ✓
- **No vault pages created**: the only website file is `website/src/posts/notes/2026-06-12-the-living-corpse.md`, and it carries **`draft: true`** (line 8). No `works/` or `wiki/` files written. ✓

## 9. Other observations

- **[NOTE] verify_quotes header drift.** dossier.yaml L15 comment says "verify_quotes.py 43/43 candidates PASS" and topic block (implicitly) references 43; the tool actually reports **40/40**. The "43 candidates" likely counts three rows later trimmed. Harmless stale comment — fix the number to 40 for cleanliness.
- **[NOTE] References list "Letters to V. A. Posse (6 & 14 Oct 1900), PSS Tom 72"** but only the 6 Oct letter (lc-posse) is an evidence row; the 14 Oct second refusal is mentioned in prose (index L65) and an extract exists (v72_399) but is not staged as evidence. Not a defect — prose-level, and the extract is present — just noting the asymmetry.
- **[NOTE] needsReview is appropriately populated** (6 items): the Chistov/Masha conjectural prototypes, the unverified Koni "14 Jan 1900 self-sacrifice letter" web claim (correctly flagged phase-3, not asserted in the index as fact — index L191 lists it as an open call), incidental 1911 stage-censorship, the Kryukova node question, and wordCount=0. The Koni-letter handling is exemplary: a web-sweep claim that could not be PSS-verified is held out of the primary narrative.

## 10. Summary of actionable items

| # | tag | location | fix |
|---|---|---|---|
| 1 | MINOR | dossier workRecord date fields | expand `oldStyle:`/`approximate:` → per-field `<field>OldStyle`/`<field>Approximate` at ingestion |
| 2 | MINOR | index.md L138 ("204 performances"), L21/L140 (17 films) | add inline "(per EN/RU Wikipedia)" attribution |
| 3 | NOTE | dossier L15 comment | change "43/43" → "40/40" |
| 4 | NOTE | dossier workRecord | `identifiers.jubileeEdition.volumes` is undocumented in the works schema — schema-doc catch-up (not a dive defect) |
| 5 | NOTE | lc-kreutzer-lineage quoteEn | composite gloss says more than the single quoted Russian line; working-translation latitude, optional tightening |

No blockers. The dive's headline claims (the «возмутился» correction, the over-determined-abandonment reading, the four documented prototype edges, the keystone Kryukova redaction, the bans=[] author-withheld rationale, the OS/NS dating) are all correctly anchored and, where checked independently, correct — including the leap-century OS/NS gap, which is easy to get wrong and is right here. Ship after the two MINOR fixes (or note them for the ingestion pass).
