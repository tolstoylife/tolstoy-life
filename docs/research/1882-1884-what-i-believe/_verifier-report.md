# Phase-5 Verifier Report — *What I Believe* (В чём моя вера?) corpus-dive

**Verdict: PASS-WITH-NITS (2 nits)**
**Date:** 2026-06-06 · adversarial fresh pass · mechanical gate re-run: 24/24 verbatim PASS.

Scope: judgement-level checks the mechanical gate cannot make. Files reviewed:
`index.md`, `dossier.yaml`, `extracts/`, `website/src/posts/notes/2026-06-06-what-i-believe.md`.

---

## 1. BYTE-FIDELITY (belt-and-braces) — PASS

Re-derived 5 quoteRu independently from the named extract files, character-for-character; index.md and dossier match the extract exactly, pre-reform-mixed forms intact:

| evidence | extract | spot-checked feature | result |
|---|---|---|---|
| believe-text-04 (work, центр тяжести) | `v23_304_465_…txt` | full keystone sentence | PASS |
| believe-text-08 (work, first commandment) | `v23_304_465_…txt` | «с стиха 21—28 … справедливым» | PASS |
| believe-let-01 (Engelhardt) | `v63_140.txt` | «Воть в чем…» (pre-reform Воть, блядуй) | PASS |
| believe-let-07 (A.A.Tolstaya) | `v63_291.txt` | «естетики … сумашедшим … диаволом» | PASS |
| believe-let-05 (Ge) | `v63_202.txt` | Latin 'a' (U+0061) in «воскресения, a период» | PASS — extract, dossier AND index all carry the **Latin** a (U+0061), not Cyrillic а |
| believe-diary-01 (Chertkov) | `v49_1883_03_09.txt` | «Письмо Черткова — вызывает…» | PASS |
| believe-let-04 (Buturlin ban) | `v63_199.txt` | «не сожжена, а увезена в Петербург…» | PASS |

No mismatch found. The pre-reform/odd forms flagged in the brief (Воть, естетики, диаволом, чтò, Latin a) are all CORRECT — they match the extract.

## 2. PRIMARY CLAIMS SOURCE-ANCHORED — PASS

Every spot-checked load-bearing claim traces to the work extract or the PSS Tom 23 commentary (`extracts/v23_548_560_commentary.txt`). Confirmed present in commentary (grep count = 1 each unless noted):

- completion 10 Jan 1884 last sheets to printer (Pypin letter) — present (×2); colophon 22 Jan 1884 is the text's own date (believe-text-11) — both correctly distinguished in index & dossier.
- ban 14 Feb 1884 "unconditional prohibition" (Feoktistov, № 785) — present.
- 39 copies seized 18 Feb by the printing inspector at Kushnerev — present.
- ~50 copies / 25 roubles, printed to slip past the censor — present.
- title-evolution chain «Как мне открылось учение Христа» → … → «В чём моя вера?» — present (ms no. 10).
- manuscript no. 7 (622 leaves) to the Imperial Public Library via Strakhov, 1884 — present.
- jury-summons draft: Tula District Court summons of 1 Sept 1883, draft written on its back — present (ms no. 14).
- keystone «не противься злу» = «центр тяжести всей мысли» and five-commandments «мира между людьми» — verbatim in the work extract.
- Elpidine undated first Geneva ed. + 1888 2nd; first legal Russia 1906; French *Ma religion* 1885 (Urusov) — all present.

No primary claim found without an anchor.

## 3. SECONDARY CLAIMS ATTRIBUTED, NOT ASSERTED — PASS

Reception & Scholarly-context sections attribute every scholarly claim to a named source: Gusev, Orfano, Karyshev, Kolstø, Bakhmetyev, Bogolyubsky, Fyodorov, Feoktistov, John of Kronstadt, Pobedonostsev (via S. A. Tolstaya), Maude, Simmons, Wilson, Medzhibovskaya, Gustafson, Christoyannopoulos.
- The **"counsel of craziness"** framing is explicitly attributed to Wilson and argued *against* (index L152) — not adopted.
- **"Christian anarchism"** is named the scholars' taxonomy (Christoyannopoulos), "not Tolstoy's word; this dive attributes it rather than adopting it" (index L16, L148, L152). Not adopted as the dive's voice.

No unattributed secondary assertion found.

## 4. TRIANGULATION VALIDITY — PASS

All 5 `scholarship.triangulation` entries: every `evidenceRef` exists in the evidence ledger; every `relation` ∈ {confirms, complicates, contradicts, extends}.
believe-text-03=confirms · believe-text-04=extends · believe-text-08=extends · believe-let-01=extends · believe-let-04=complicates. All valid.

## 5. ENTITIES — PASS

- All 24 `wikiType` values ∈ the 10 wiki types (person / place / concept / institution only used; all valid).
- All `vaultStatus` values ∈ {exists, stub, missing} and **accurate**: every `exists` claim (Leo Tolstoy, Christian Anarchism, Vladimir Chertkov, Sophia Tolstaya, Yasnaya Polyana) resolves to a real `website/src/wiki/*.md` file by its `wikilinkTarget`; no `missing` entity has a file that actually exists. Engelhardt, Minor, Ge, Buturlin, Pypin, the cousin A. A. Tolstaya, Strakhov, Pobedonostsev, Elpidine etc. correctly = missing.
- **Two-A.A.-Tolstaya note present and correct.** The dossier entity carries `note: DISTINCT from the existing wiki page 'Alexandra Tolstaya' (= the daughter Alexandra Lvovna, 1884–1979)`. Confirmed against the wiki file: `Alexandra Tolstaya.md` is the daughter (birthDate 1884-06-30, death 1979, relationToTolstoy: daughter). Index L180 carries the prose flag "the cousin Countess A. A. Tolstaya (distinct from the daughter Alexandra Lvovna)." Correct.

## 6. WORK-DIVE CHECKS

(a) `workRecord` field names — **PASS with 1 NIT.**
- All 16 proposed field names are real works-schema keys (titleRu/En, titleAlternatives, genre, dateWriting*, dateFirstPublished*, firstPublishedVenue, bans, censoredVersionExists, samizdatCirculation, excommunicationRelated, identifiers.jubileeEdition.volumes). `genre: essay` matches the controlled enum AND the existing Confession record (genre: essay). Dates/venues are evidence-anchored, not fabricated.
- **NIT-1 (controlled-vocab):** the proposed `bans[]` value uses `authorityType: state-censorship`, which is NOT in the works-schema enum (`imperial-state` · `holy-synod` · `foreign-government` · `periodical-editor` · `other`). Should be **`imperial-state`**. Likewise `scope: 'unconditional prohibition; 39 copies seized at Kushnerev'` is free text rather than the controlled `scope` enum (`complete-ban` · `confiscation` · …) — the controlled value should be `complete-ban` (or `confiscation`), with the seizure detail moved to `bans[].notes`. This is a *proposal* routed to human ingestion, so it is low-impact, but it would fail `validate-frontmatter.mjs` if applied verbatim. Recommend fixing in the proposal so the human paste is clean.

(b) `coverage` ledger honesty — **PASS.** No dishonest `covered`. The Reception surface is `covered` but self-flags its limit ("Refutation texts named, not read in original"); "The author's later verdict" is honestly `not-covered`. Matches what the evidence supports.

(c) Standing spine sections obey bare-voice / attribute-don't-assert — **PASS.** Genesis, What the work says, Redactions, Publication/censorship, Reception, Place in the cluster lead with Tolstoy's/Savodnik's words and attribute all secondary framing.

## 7. VOICE & TRANSLATIONS — PASS

All Russian renderings carry "(working English …)" labels in both index and dossier. Cited foreign titles kept verbatim (*Ma religion*, *Worin besteht mein Glaube?*, *Christ's Christianity*, *Так что же нам делать?*). No editorializing in the dive's own voice; interpretive claims are routed to attribution or to `needsReview`.

## 8. RIGHTS HYGIENE — PASS

- `git check-ignore docs/research/1882-1884-what-i-believe/visuals/` → reports it ignored. Confirmed.
- No dive image placed under `website/src/` (find for ma-religion / what-i-believe / ge-tolstoy image files = none).
- `extracts/` holds only PD material: TEI extracts from Tolstoy (v23/v49/v63) + the PSS Savodnik commentary (PD), plus the dive's own working-note `.md`/`.html` files (sweep summaries and the attributed scholarship synthesis — the dive's own prose, no pasted third-party copyrighted text).
- Every `visuals` entry carries a `licence` field (PD, or `unknown` for the not-located physical-only items). Confirmed.

## 9. nl2br HYGIENE — PASS

No hard-wrapped paragraphs or blockquotes. The only consecutive-non-empty-line pairs are adjacent list items (lines beginning `- `), which render as separate `<li>` under nl2br — correct, not ragged `<br>`. Every paragraph, blockquote and list item is a single source line.

---

## NITS (2) — iterate-worthy but non-blocking

1. **[workRecord proposal, dossier.yaml `bans[]`]** `authorityType: state-censorship` is not a schema-controlled value → use `imperial-state`; `scope` free text → use the controlled `complete-ban` (or `confiscation`) and move "39 copies seized at Kushnerev" to `bans[].notes`. Would fail the frontmatter validator if applied verbatim. (Proposal only; human ingestion can fix at paste-time, but cleaner to fix in the dossier.)

2. **[index.md L18/L52, minor imprecision]** The Engelhardt letter is dated "December 1882" in prose, while the PSS commentary and the dossier (`believe-let-01` date `1882-12-20 – 1883-01-20 OS`) give the wider "second half Dec 1882 or first half Jan 1883." Not a fabrication — the dossier is honest and the prose simplification is defensible — but the prose could read "late 1882 / early 1883" to match the apparatus exactly.

No FAILs. Both nits are in the work-record *proposal* / a prose simplification, neither touches a byte-fidelity quote, a primary anchor, an entity status, or rights hygiene.
