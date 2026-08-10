# Phase-5 verifier report — The Kingdom of God Is Within You (work dive)

- **Dive:** `docs/research/1890-1893-the-kingdom-of-god-is-within-you/`
- **Verifier:** independent Phase-5 (fresh context)
- **Date:** 2026-06-07
- **Verdict:** **PASS-WITH-NITS**

The dive is sound across all ten judgment-level checks. Byte-fidelity holds belt-and-braces (re-derived from the original TEI, not just the committed extract); every primary claim is anchored; secondary facts are attributed to the PSS Tom 28 commentary and to Gandhi/scholarship, never byte-claimed; the commentary is correctly kept out of `extracts/` and the evidence ledger; triangulation is valid; entities resolve with accurate `vaultStatus`; and the workRecord corrections are all supported by the dive's evidence and by the live record's actual field values. The nits are documentation precision, not correctness.

---

## Per-check findings

### 1. Byte-fidelity belt-and-braces — PASS
Re-extracted the original TEI with `extract_tei.py --choice=reg --notes=auto` and confirmed a sample of quotes verbatim, independent of the committed extracts:

- **Work** (`v28_001_293_…xml`): fresh extract is byte-identical in size (1,142,210 bytes) to the committed `extracts/v28_001_293_Tsarstvo_bozhie_vnutri_vas.txt`. Sampled `kgd-text-01, -02, -05, -06, -09, -12` — all verbatim. The seven additional headline blockquotes in index.md §3 (full four-means sentence, full army sentence, "realm of causes", "kingdom by effort", hypocrisy, divine-life-in-God, new-жизнепонимание) — all verbatim.
- **Diaries**: `kgd-diary-01` (`v51_060`), `kgd-diary-03` (`v52_069`), `kgd-diary-04` + "Я свободен" (`v52_078`), `kgd-diary-02` (`v51_068`, §4.1 headline) — all verbatim. The 1893-05-14 diary independently confirms index.md §9's "так плохо" verdict and the "I am free / illness pushed me to stop" framing.
- **Letter**: `kgd-let-01` (`v87_304_dekabrya14.xml`) verbatim; the extract header independently confirms addressee (Chertkov), date (14 Dec 1891), place (Begichevka), Tom 87 p.117 — matching dossier `pages: "117"` and the §6 attribution.
- **Independent gate run**: `verify_quotes.py` → **17/17 verbatim, 0 missing, 0 label warnings — PASS**.
- §10 line-number table cross-checked against the fresh extract: l.7 (epigraph), l.17 (premise), l.1477 (army inward), l.2811 (hypocrisy), l.2845 (Luke 17:20–21 closing) all land on the cited passages.

### 2. Primary claims source-anchored — PASS
Every primary factual claim about what the book argues (§3, §5) ties to a byte-checked evidence row or the extract. The keystone quotes (epigraph, "chief departure", army-inward, four means, freedom/causes, one free act, hypocrisy, last line) each map to `kgd-text-NN`. The genesis-by-diary claims (§4) map to `kgd-diary-NN` and the Chertkov refusal to `kgd-let-01`. No unanchored primary claim found.

### 3. Secondary claims attributed, not asserted — PASS
- Genesis/publication/censorship facts are explicitly attributed to "the PSS Tom 28 commentary (N. K. Gudzy)" in §4, §6, §7, §11, §14, and in the dossier header comment + every relevant `workRecord` note (`source: jubilee-edition`, `confidence` set, byte-claim disclaimed).
- Gandhi reception attributed to Gandhi's *Autobiography* + scholarship (§8.2, §11, §12; entity `M. K. Gandhi` carries `sources: []`, `evidenceRefs: []`, and a note that it is "not in the corpus").
- `extracts/` contains ONLY PD Tolstoy text: the work + four diaries + one Chertkov letter. No `_apparatus`/commentary/Gudzy file present (grep for apparatus|comment|gudz|izdani|istori → none).
- No commentary quote sits in the evidence ledger (all 17 rows are `genre: work|diary|letter`).

### 4. Scholarship triangulation valid — PASS
All five `triangulation[].evidenceRef` values resolve to real evidence ids; all five `relation` values are in {confirms, complicates, contradicts, extends}. The two headline triangulations are sound: publication (`kgd-text-12`, `complicates` — French-first 1893 vs "first published in Germany 1894"/Leipzig) and mysticism (`kgd-text-03`, `contradicts` — subtitle rejects it). The subtitle text «не как мистическое учение» is present in the work extract, grounding the latter.

### 5. Translations labelled — PASS
Every English rendering of Russian carries "(working English)" — in index.md §3, §4, §6, §7 blockquotes and in every dossier `quoteEn`.

### 6. Voice / contested labels — PASS
No endorsing adverbs ("rightly"/"correctly"/etc.) before a source (grep → none). The contested labels ("Christian anarchism", "anarchist", "mystical") are consistently attributed to the outside and cross-linked to `../christian-anarchism/index.html` rather than re-argued (lines 13, 37, 242, 291–293). "Christian anarcho-pacifism" appears only inside an explicitly attributed scholarship sentence ("what is usually called", §11). The dive does not adopt any contested badge as fact.

### 7. Entities resolve — PASS (with one note)
Wiki listed (`website/src/wiki/`, 15 pages). Critical resolutions confirmed:
- `Lev Tolstoy → Leo Tolstoy` exists; `Chertkov → Vladimir Chertkov` exists; `S. A. Tolstaya → Sophia Tolstaya` exists; `T. L. Tolstaya → Tatyana Tolstaya` exists; `Yasnaya Polyana` exists.
- **P. I. Biryukov → `Pavel Birukoff`** correctly resolved to the existing page (NOT a new "Biryukov" page); dossier note explicitly warns against the duplicate. Correct.
- Gandhi, Ballou, Garrison, Strakhov, Popov, Deubner, Halpérine-Kaminsky, Garnett, Chelčický — all correctly `missing`.
- All `wikiType` values are within the controlled set (person/concept/event/place used here).
- **Maria Tolstaya provisional caution**: the dossier flags `Maria Tolstaya.md` `vaultStatus: exists` as PROVISIONAL (could be sister Maria Nikolaevna). On inspection the page IS the daughter Maria Lvovna (1871–1906, later Obolenskaya; `relationToTolstoy: daughter`) — i.e. the correct copyist. So the `exists` status is correct, and the hedge, while a reasonable ex-ante caution, is in fact resolvable: the page is unambiguously the daughter. See Nit 1.

### 8. Work-record proposals — PASS
All `workRecord.fields[]` names exist in `website/schema/tolstoy-works-schema.md`. The corrections are evidence-anchored and match the live record's actual values:
- **(a) firstPublishedVenue** — live record reads `"Wilhelm Friedrich Verlag, Leipzig"` (line 38) and `dateFirstPublished: "1894"` (line 35). The dive's correction (French *Le salut est en vous*, Perrin 1893, first anywhere; Berlin/Deubner first-printed Russian Jan 1894; Stuttgart German Jan 1894) is drawn from the commentary, flagged `confidence: medium`, and routed to `needsReview` for the human to choose field semantics. Sound.
- **(b) dateWritingCompletedOldStyle** — live record reads `"1893-04"` (line 32) while `dateWritingCompleted: "1893-05"` (line 31); the OS/NS mismatch is real. The diary (`v52_078`, 14 May 1893 OS) confirms completion is May, so OS should be `1893-05`. The dive flags this correctly (`needsReview`, phase 4). Sound.
- The Holy Synod `complete-ban` IS present in the live record (lines 117–121); the dive honestly flags it as not corroborated by the Tom 28 commentary and routes to `needsReview` rather than asserting it. Appropriate.
No fabricated dates/venues found.

### 9. Coverage honest — PASS
9 surfaces: 6 `covered`, 3 `partial`. The three downgrades are warranted: textual history (Varianty/Afterword summarized, not collated), Church/Synod tie (climate not documented ban), author's-later-verdict (no retrospective beyond completion in-window). No `covered` overstates the evidence.

### 10. Rights / visuals — PASS
`visuals/` is git-ignored (`check-ignore` confirms) and nothing under it is tracked (`git ls-files` → none). No `commons-*.jpg` exists anywhere under `website/src/` (find → empty). index.html references only local-cache `visuals/…` paths. Every `visuals[]` entry that was retrieved carries `licence: PD` / `rights: PD`; the two unretrieved items (French title page; manuscript facsimile) are honestly `usable: no` with `rights: unknown`/`PD` and `localPath: ""` — not committed.

---

## Must-fix
*(none — no correctness defects found)*

## Nits
1. **Maria Tolstaya caution can be tightened** — dossier `entities[]` (the `M. L. Tolstaya` note, ~line 366) and `needsReview` item (~line 748) hedge that `Maria Tolstaya.md` "could be the sister Maria Nikolaevna." The page is unambiguously the daughter Maria Lvovna (1871–1906, `relationToTolstoy: daughter`). The hedge is harmless but now resolvable; on ingestion the human can simply confirm-and-close rather than re-investigate.
2. **index.md §3.1 wording — "Lewis Wilson sent him the works of Adin Ballou"** (line 61) vs §4.1 "Adin Ballou's *Christian Non-Resistance*, sent by Ballou's helper Lewis Wilson" (line 135). Both are attributed-to-commentary genesis detail (not byte-claimed), but the two sentences describe the same fact at slightly different granularity; harmless, no contradiction.
3. **Dev-blog note `draft: true`** is correctly set; its date (`2026-06-06`) is one day behind the report date — expected for an end-of-session artifact, no action needed.
4. **`pages` fields in evidence rows** (e.g. `kgd-text-03 "~67 (гл. V)"`) are tilde-approximate PSS page guesses, clearly marked with `~`; not byte-checkable and not claimed to be. Fine for prototype rigor.

---

## Resolution (applied 2026-06-07, main context)

- **Nit 1 (applied).** The `M. L. Tolstaya` entity note and the matching `needsReview` item were updated to record the verifier's finding — `Maria Tolstaya.md` is confirmed the daughter Maria Lvovna (1871–1906, `relationToTolstoy: daughter`); the provisional "could be the sister" hedge is resolved, `vaultStatus: exists` confirmed.
- **Nits 2–4 (no action, as noted by the verifier).** §3.1 / §4.1 describe the same Ballou/Wilson genesis fact at different granularity with no contradiction; the note's `2026-06-06` date is the correct session-start stamp; the `~`-marked approximate page fields are honest prototype rigor.
- `verify_quotes.py` re-run after the edits → **17/17 PASS** (the edits touched only entity/needsReview prose, no quotes).

Verdict stands: **PASS-WITH-NITS**, 0 must-fix, all actionable nits resolved.
