# Verifier report — *Bethink Yourselves!* (Одумайтесь!, 1904) corpus work-dive

- **Dive:** `docs/research/1904-bethink-yourselves/`
- **Verifier pass:** 2026-06-08, independent (did not author the dive)
- **Mechanical gate:** `verify_quotes.py` re-run by verifier → **29/29 verbatim, 0 facsimile missing, exit 0** (confirmed).

---

## 1. Byte-fidelity spot-check — **PASS**

Re-ran `verify_quotes.py docs/research/1904-bethink-yourselves/dossier.yaml`: `SUMMARY: 29/29 quotes verbatim … PASS`, exit 0.

Independently re-derived 4 rows across 4 different extracts (essay / diary / letter / commentary), each a fresh `grep -F` of the dossier `quoteRu` against the named `extract` file:

- **essay** `odum-children-gunpowder` → `extracts/v36_100_148_Odumajtes.txt` — verbatim (quote is the head of a longer sentence; bytes match).
- **diary** `odum-diary-oscillation` → `extracts/v55_045_047_1904_06_06.txt` — verbatim (quote is the tail of the `и иногда думаю…` sentence; bytes match).
- **letter** `odum-verdict-tol` → `extracts/v75_179_S_D_Tol.txt` — verbatim (`Я виноват, что тон…на смертном одре.` matches inside the paragraph).
- **commentary** `odum-pub-russia-banned` → `extracts/v36_604_621_Odumajtes_comments.txt` — verbatim (`В России «Одумайтесь!» вышло впервые в 1906 г. … (конфискована).`).

All four match. Gate independently confirmed.

## 2. Source-anchoring of primary claims — **PASS**

Every primary quote in `index.md` carries a TEI id and a PSS Tom + page anchor (e.g. *Chapter VI · PSS Tom 36 · TEI `v36_100_148`*; *Diary, 6 June 1904 (OS) · TEI `v55_045_047_1904_06_06` · PSS Tom 55, pp. 45–47*). 28 source blockquotes, 36 citation-anchored lines. The composition narrative carries a standing attribution header (line 35) routing reconstructed facts to Gorbachev's editorial history. No primary assertion of fact was found floating without a citation.

## 3. Attribution of secondary claims — **CONCERN**

Reception / publication-history / translation / scholarship statements are, with one exception, attributed and References-backed: editorial commentary (TEI `comments/v36_604_621`), Project Gutenberg #27189, Projekt Runeberg, Scotland-Russia project, Kōtoku (*Heimin Shimbun* no. 40, 1904), Wikipedia (Petropavlovsk ~679 dead), and the German/French translators all carry inline attribution and a References entry. The "all reception claims here are attributed" disclaimer (line 295) is honest.

**One bare-asserted secondary claim:** the Navalny line — *"Alexei Navalny cited its opening sentence at his 2022 trial"* (`index.md` line 293) — is stated in the dive's own voice with **no source pointer and no References entry**. It traces only to the dive's own scholarship-sweep extract (`extracts/_scholarship.md` lines 90, 100), which likewise gives no external citation. Under prototype rigor no byte-fidelity is demanded of a secondary source, but this claim should carry an attribution tag or a References entry (or be softened) before ingestion. This is the only attribution gap found.

## 4. scholarship.triangulation — **PASS**

All 7 triangulation entries validated programmatically: every `evidenceRef` (`odum-pub-abroad`, `odum-pub-russia-banned`, `odum-individual-not-external`, `odum-bethink-definition`, `odum-genesis-letter`, `odum-metanoeite`, `odum-fire-rising`) exists in the 29-row evidence ledger, and every `relation` ∈ {confirms, complicates, contradicts, extends}. No dangling refs. (All entity and workRecord `evidenceRefs` also resolve.)

## 5. entities — **CONCERN**

`vaultStatus` accuracy: all 4 `exists` claims confirmed present (`Leo Tolstoy.md`, `Vladimir Chertkov.md`, `Alexandra Tolstaya.md`, `Christian Anarchism.md`); 14 `missing` claims confirmed absent with transliteration-aware loose matching (Verigin, Novikov, Makarov, Vereshchagin, Mayo, Kotoku, Nicholas/Nikolai, Metanoia, Free Age, Igumnova, Ivus, Crosby, Russo-Japanese War — none present). **No wrong `missing`**, so no ingestion-duplication risk. Good.

`vaultStatus` enum: all ∈ {exists, stub, missing}. OK.

**wikiType enum violation:** `Free Age Press` carries `wikiType: organization`. The wiki-schema (v1.3) has **no `organization` type** — the 10 valid types are `person, place, event, concept, translator, institution, adaptation, criticalWork, archivalFond, edition`. Publishers/presses map to **`institution`** (schema example: "Intermediary (Posrednik), Russkiy Vestnik, Tolstoy Museum"). Prior committed dives use `institution` 22× and `organization` only 1× (a stray). The validator (`validate-frontmatter.mjs` `WIKI_TYPES`) does not gate the dossier `wikiType` field, so this is non-blocking, but it should be `institution` before this entity becomes a page. Concern, not fail (planning-layer, never written).

*(Note: the prompt's "9 wiki types" is now 10 — `edition` was added in schema v1.3, 2026-05-31. Does not affect this dive.)*

## 6. workRecord — **PASS**

All field names resolve against `tolstoy-works-schema.md` / the live record: `dateFirstPublished`, `firstPublishedVenue`, `bans`, `titleAlternatives`, `relatedWorks`, `dateWritingCompleted`, `censorshipNotes` — all real keys. Spot-checks:

- **`bans`** — proposed two-entry array (1906 Обновление confiscation; 1911 vol.19 confiscation), `evidenceRef: odum-pub-russia-banned`, which is byte-verified against the commentary (`…в 1906 г. в издании «Обновление» … (конфискована). В 1911 г. … (том конфискован).`). Sub-fields (`banningAuthority`, `authorityType`, `jurisdiction`, `scope`, `banDate`) match the schema's `bans` object shape. Evidence-anchored.
- **`titleAlternatives`** — Betänken Eder! / Besinnet Euch! / Ressaisissez-vous! / the RU subtitle, each shaped to `{title, type, language}`; sourced to Runeberg / Diederichs / fr.Wikisource / PSS commentary. Anchored.
- **`dateFirstPublished`** = "1904" — matches live record; anchored to `odum-pub-abroad`.
- **`dateWritingCompleted`** = "1904-05-13" — matches live record (NS; OS 1904-04-30), anchored to the fire-coda dateline + seaman postscript; the note honestly flags the essay kept growing to 20 May OS (→ `needsReview`).

No fabricated dates/venues; the `relatedWorks` proposal for *Единое на потребу* honestly carries `confidence: medium` and "Verify the slug/id … before adding (may not yet have a record)" — and indeed no such works record exists yet (verified). Clean.

## 7. coverage honesty — **PASS**

"Reception & afterlife (Russian/Church first)" is marked **`partial`** in the dossier (line 983) and the index prose openly states a Synod statement specific to this essay was not found and biography page-level treatment "could not be confirmed in this pass" (lines 289, 295). "Visual & manuscript record" is marked **`partial`** (line 992) with the three not-openly-available items (dated 1904 Tolstoy photo, period Chertkov photo, Free Age Press / *Times* title pages) named with where-to-request. Both honest; no surface overclaims `covered`.

## 8. Voice & translations — **PASS**

28 source blockquotes (Russian + the one Swedish coda) each followed by exactly one "(working English)" label — clean 1:1, no unlabelled renderings. Contested labels handled correctly: "Christian anarchism" and "Tolstoyanism" are framed as "the contested mainstream labels … labels the dive points at rather than asserts" (line 321) and cross-linked, never asserted in the dive's own voice. "Tolstoyan" appears only as descriptors of others (Crosby; "the socialist critique of Tolstoyan non-resistance"), not as a self-asserted frame for Tolstoy. No editorial drift found.

## 9. Boundaries — **PASS**

- `extracts/` holds only PD text: 11 `.txt` (PSS extractions) + 2 `.md` + 2 `.html` (the sweep/scholarship working notes). No images. Confirmed PD facsimile zone.
- `visuals/` is git-ignored: `docs/.gitignore` carries `research/*/visuals/`; `git check-ignore` confirms all 5 cached images are ignored; `git ls-files` on the dir is empty. None committed.
- No image leaked into `website/src/` (searched assets/images and src tree for betanken/petropavlovsk/makarov/chertkov — none).
- No `website/src/wiki/**` or `website/src/works/**` page was created by the dive (`git status` / `git ls-files --others` on both dirs empty). The dive plans pages; it does not write them.
- The only `website/` write is the draft note `website/src/posts/notes/2026-06-08-bethink-yourselves.md`, which carries `draft: true` (line 9). Correct.

*(Whole dive is currently untracked/uncommitted — expected for a fresh dive pending this verification.)*

## 10. Internal consistency — **PASS**

- The index states "29/29 PASS" (line 352) and the gate confirms it.
- The coda RU↔SV variance is consistently presented as a **free-translation variant, not a different source**, in index (lines 22, 277), dossier `contradictions` (line 999), and the evidence note for `odum-fire-rising` — every instance says the Swedish was made from the Russian (epigraphs dropped) and the divergence is a rendering, not a separate witness.
- The **Petropavlovsk** (ch XI, Russian loss, ~679 / "six hundred" dead, Makarov + Vereshchagin) is kept **distinct** from the ch XII "multitude of Japanese" drowned (Iessen / Genzan transports, Chertkov's «несколько тысяч» → «множество» softening), flagged explicitly in `needsReview` (line 1028: "Keep the two events distinct in any wiki page"). Death-toll figure (~679) is consistent across all index occurrences. No internal contradiction found.

---

## VERDICT: NEEDS-FIXES

Two non-blocking items; both should be cleared before this dossier feeds wiki ingestion / the work record. The mechanical gate, source-anchoring, triangulation, vaultStatus accuracy, coverage honesty, voice, and boundaries are all clean.

1. **(Check 3) Navalny 2022 claim is bare-asserted.** `index.md` line 293 ("Alexei Navalny cited its opening sentence at his 2022 trial") has no inline attribution and no References entry; it traces only to the dive's own `extracts/_scholarship.md`, which also gives no external source. Add an attribution + a References entry, or soften / drop the claim.
2. **(Check 5) `Free Age Press` has an invalid `wikiType: organization`.** The wiki-schema has no `organization` type; change to `wikiType: institution` (the schema's category for publishers/presses) in `dossier.yaml` entities, so the planned page is created with a valid type.
