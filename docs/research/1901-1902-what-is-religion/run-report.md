---
layer: reference
lastUpdated: 2026-06-07
---

# Run report — corpus-dive: 1901-1902-what-is-religion

**Slug:** `1901-1902-what-is-religion`
**Work:** «Что такое религия и в чём сущность её?» / PSS Tom 35, pp. 157–198
**Date:** 2026-06-07 (two sessions; first context-exhausted; resumed from summary)
**Mode:** interactive (auto-executed after context restore)
**Model tier:** sonnet (synthesis); haiku-equivalent for mechanical steps

---

## Scope contract

**Question:** What does the treatise argue, how was it composed at Gaspra during Tolstoy's grave illness just after his excommunication, who were its interlocutors, and what is its place in the Prophet-period cluster?

**Corpus surface:**
- PSS Tom 35: main text (pp. 157–198) + editorial apparatus (history of writing pp. 670–675; manuscript description pp. 675–676)
- PSS Tom 54: diary entries 1900–1901; notebook January 1900 – March 1901
- PSS Tom 73: letters to correspondents, August 1901 – December 1902
- PSS Tom 88: letters to V. G. Chertkov, August–November 1901

**Composition window:** November 1900 (first diary idea) → January 1902 (manuscript at press)

**Keyword set (anchors):** религия / сущность / бесконечное / Гаспра / церковь / вера / извращение; combinable: Чертков / Бирюков / Русанов / Граубергер / Буланже / Моод

**Stop condition:** all 17 chapters read; all dated diary entries and letters in composition window extracted and verified; scholarship swept; dossier + index.md + draft note + HTML produced; verify_quotes.py PASS.

---

## Phase 1 — Sweep

Sweep run across PSS Tom 35 (main text + apparatus), Tom 54 (diaries + notebook), Tom 73 (letters), Tom 88 (letters to Chertkov). Candidate hits ranked by relevance; 28 finalist extracts produced.

**Composition-years witness sweep:** 8 diary entries (Nov 1900 – Dec 1901) + notebook + 13 letters T.73 + 4 letters T.88 = 26 source units. All read in full.

---

## Phase 2 — Extract & verify

All extracts produced via `python3 docs/research/lib/extract_tei.py <xml> --choice=reg` (modern orthography; mandatory for pre-1918 texts).

**Note-tail fix:** `extract_tei.py` was patched before this dive (2026-06-07) to recover prose after inline footnotes. All extracts in this dive are post-fix.

**Visual sweep:** Wikimedia Commons API; 8 public-domain images downloaded and catalogued in the dossier `visuals:` block (each with provenance + licence). Cache git-ignored; download via `Special:Redirect/file/` with a `User-Agent` (resolved Cyrillic-filename and rate-limiting issues). Items not openly available (Free Word imprint scans, MS facsimiles) noted for request.

**PSS PDF cross-check:** Local `primary-sources/archive-org/` set is Leo Wiener's English edition (Boston 1904), not the Russian PSS. A Russian PSS Tom 35 scan IS held locally (`primary-sources/jubilee-edition/vol35/vol35.pdf`) but has no usable text layer (heavy OCR letter-spacing), so it could not drive an independent chapter count or facsimile. Facsimile cross-check not performed; logged in `needsReview`.

---

## Phase 3 — Scholarly context

Light web sweep: Daniel Moulin, "Tolstoy, Universalism and the World Religions," *Journal of Ecclesiastical History* 68:3 (2017); ourcivilisation.com synthesis (Simmons 1968); Maude biography (1911); Bartlett (2010). No dedicated monograph on this essay found.

Triangulation: 5 entries in `dossier.yaml → scholarship.triangulation`. High-value cases: two `extends` (three-mechanism model not named precisely in scholarship; Church truc as Christianity's specific contribution not developed in secondary literature); one `complicates` (excommunication-as-motive framing overstates the chronology).

---

## Phase 4 — Synthesize

**Deliverables produced:**
- `dossier.yaml` — 25 evidence entries, 11 entities, 8 visuals, 5 scholarship triangulations, workRecord proposal (21 fields), coverage ledger (10 surfaces), 5 notCovered, 4 needsReview, full references
- `index.md` — layer: reference; all standing sections complete
- `website/src/posts/notes/2026-06-07-what-is-religion.md` — draft: true

---

## Phase 5 — Verify

**verify_quotes.py:** 25/25 PASS (after 9 corrections for embedded footnote superscripts, curly apostrophes in French notebook text, and mid-sentence quote starts).

**Corrections made:**
- `ev-corruption-three-means`: quote started at "А нужно" not "Нужно" (mid-sentence; lowercase in extract)
- `ev-equality-core`: quote starts at "признание" (lowercase, mid-sentence)
- `ev-diary-1901-02-08`: footnote superscripts `¹⁰` and `¹¹` embedded in text
- `ev-letter-chertkov-aug12`: footnote `⁴` embedded mid-sentence
- `ev-letter-chertkov-sep14`: OCR artifact "О p e л иг ии" in extract; reproduced verbatim; footnote `⁶` added
- `ev-letter-chertkov-nov30`: quote starts at "А, главное, надеюсь" not "надеюсь"; extended to "что мог."
- `ev-letter-ge-aug26`: footnote `³` embedded
- `ev-letter-biryukov-dec31`: footnotes `⁴` and `⁵` embedded
- `ev-notebook-1900-1901`: French text uses U+2019 RIGHT SINGLE QUOTATION MARK `'`; space before "intéligence" preserved; footnote numbers `¹¹³¹–¹¹³³` embedded; YAML `\n\n` for paragraph breaks

**Verifier pass:** an independent opus verifier WAS dispatched in the follow-up review session — see `_verifier-report.md` (verdict: NEEDS-FIXES → 4 FAIL + 3 CONCERN; all FAILs and the visuals CONCERN resolved, 2 CONCERNs are Johan judgment-calls in `needsReview`). The self-assessment table below was the original drafting pass's substitute and is retained for the record.

**Self-assessment:**

| Check | Result |
|-------|--------|
| Interlocutor sweep yields people? | Yes — 11 named correspondents, all with evidence refs |
| Russian society/church reception covered? | Partial — marked as `notCovered`; no corpus material |
| `workRecord` fill accurate and provenanced? | Yes — 17 fields, each with evidenceRef and confidence rating |
| `coverage` honest (no false `covered`)? | Yes — 3 surfaces marked `partial`; rationale given for each |
| `--choice=reg` extract cleanly? | Yes — all 26 pre-1918 extracts used `--choice=reg` |
| Spine stayed bare? | Yes — no editorial opinion in the narrative voice |

---

## Phase 6 — Handoff

### Entity work-order

| entity | wikiType | vaultStatus | ingestionPriority | notes |
|--------|----------|-------------|-------------------|-------|
| Vladimir Chertkov | person | exists (draft) | 2 | Add this work to his publication record |
| Pavel Birukoff | person | exists (draft) | 2 | Clarify co-translator vs reviser role (needsReview) |
| Konstantin Pobedonostsev | person | missing | 2 | Create; role: Synod Ober-Procurator; 1901 excommunication |
| «Свободное слово» press | institution | missing | 2 | Create; depends on Chertkov page |
| Holy Synod excommunication (1901) | event | missing | 2 | Create; connects multiple works |
| Gaspra (Panina estate) | place | missing | 2 | Create; composition site for this and other Crimea works |
| Gavril Rusanov | person | missing | 3 | Create; Tolstoyan correspondent |
| Aylmer Maude | person | missing | 3 | Create; translator + biographer |
| Pavel Boulanger | person | missing | 3 | Create; scribe of late additions |
| Boris Chicherin | person | missing | 3 | Create; philosopher whose book catalysed the definition |

### Visuals work-order

| id | file | recommended use |
|----|------|----------------|
| tolstoy-sofia-crimea-1902 | commons-tolstoy-sofia-crimea-1902.jpg | Keystone: Tolstoy at Gaspra, composition site |
| gaspra-house-1901-1902 | commons-gaspra-house-1901-1902.jpg | Composition location illustration |
| tolstoy-scherer-nabholz-1901 | commons-tolstoy-scherer-nabholz-1901.jpg | Year of excommunication; formal portrait |
| pobedonostsev-repin-1903 | commons-pobedonostsev-repin-1903.jpg | Antagonist (Synod Ober-Procurator) |
| chertkov-portrait-repin-1890s | commons-chertkov-portrait-repin-1890s.jpg | Publisher portrait (solo) |
| biryukov-1916 | commons-biryukov-1916.jpg | French translator; dated portrait preferred |

All images PD; `visuals/` is git-ignored (local cache). See `dossier.yaml → visuals` for full rights/licence metadata.

### Works record proposal

No works record exists for this essay. The `dossier.yaml → workRecord` block proposes a new record at:

`website/src/works/non-fiction/essays-and-criticism/what-is-religion/What Is Religion.md`

Key fields proposed:
- `id: what-is-religion`
- `titleRu: Что такое религия и в чём сущность её?`
- `titleEn: What Is Religion and What Is Its Essence?`
- 3 title alternatives (two working titles + French translation)
- `dateWritingStarted: 1901-08-12` (first manuscripts 10 Aug 1901; Chertkov letter confirms)
- `dateWritingCompleted: 1902-01` (approximate; late additions through Feb 1902)
- `dateFirstPublished: 1902` (Free Word No. 75, Christchurch)
- `publishedInRussiaDuringLifetime: false` (first legal Russian printing 1906)
- `bans`: one entry — Russian Imperial censorship (authorityType `imperial-state`), scope `complete-ban`, 1902
- 2 authoring locations (Yasnaya Polyana Aug–Sept 1901; Gaspra Sept 1901 – Jan 1902)

Full field set with evidence references and confidence ratings: `dossier.yaml → workRecord`.

### Coverage summary

| surface | status |
|---------|--------|
| Genesis & composition | covered |
| What the work says | covered |
| Redactions & textual history | partial |
| Publication, censorship & translation | covered |
| Reception & afterlife — Russian society/church | partial |
| Composition-year interlocutors | covered |
| Place in the cluster | covered |
| Author's later verdict | partial |
| Visual & manuscript record | covered |
| Scholarly context | partial |

---

## Not covered (for future sessions)

1. Contemporary Russian press and clerical reaction to the published essay (1902–1906) — newspaper archives
2. Biryukov's French translation correspondence; Tolstoy's corrected copy of the French text
3. Chertkov's reply letters (T. 88 holds Tolstoy-to-Chertkov only; no reverse direction)
4. Full manuscript collation of 82 drafts (1,449 units) — GTM Manuscript Department
5. *Образование* / Ostrogorsky censorship episode (1902–03) — censor committee reasoning

---

## Files produced

| file | type | status |
|------|------|--------|
| `dossier.yaml` | structured evidence | complete; verify_quotes.py PASS 25/25 |
| `index.md` | reference narrative | complete |
| `index.html` | rendered HTML (66 KiB) | built by serve.py --build-only |
| `visuals/_visuals_sweep.md` | visual catalogue | complete (8 catalogued in dossier; cache git-ignored) |
| `extracts/v35_157_198_Chto_takoe_religiya.txt` | main text | complete |
| `extracts/v35_670_675_history.txt` | editorial apparatus | complete |
| `extracts/v35_675_676_primechanija.txt` | manuscript description | complete |
| `extracts/v54_*.txt` (8 files) | diary witnesses | complete |
| `extracts/v54_211_240_Zapisnaja_knizhka.txt` | notebook | complete |
| `extracts/v73_*.txt` (13 files) | letters T.73 | complete |
| `extracts/v88_*.txt` (4 files) | letters T.88 | complete |
| `extracts/_sweep_diaries.md` | sweep summary | complete |
| `extracts/_sweep_letters_t73.md` | sweep summary | complete |
| `extracts/_sweep_letters_t88.md` | sweep summary | complete |
| `website/src/posts/notes/2026-06-07-what-is-religion.md` | draft note | draft: true |
| `run-report.md` | this file | complete (corrected in review pass, 2026-06-08) |

---

## Addendum — review pass (2026-06-08)

This run-report was generated by the original drafting pass (a single unsupervised agent that also committed the dive prematurely as `d57e99b2`). A follow-up review + independent opus verification pass corrected the dive; this report was updated inline to match the corrected `index.md` / `dossier.yaml`. Key corrections: the JEH citation (Daniel Moulin, 68:3, **2017**, not "2021"); `wikiType` `organisation` → `institution`; workRecord `firstPublishedVenueType` → `book`, `bans.authorityType` → `imperial-state`, `bans.scope` → `complete-ban`; the "nine days" → "about two weeks" day-count; sibling cross-link slugs; the chapter-count discrepancy (TEI 17 heads vs PSS description 18) documented honestly; visuals reconciled to 8 catalogued. See `_verifier-report.md` for the full verdict and resolution log. `verify_quotes.py`: 25/25 PASS.
