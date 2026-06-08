---
layer: reference
lastUpdated: 2026-06-08
tags: [research, corpus-dive, verifier-report, kreutzer-sonata]
---

# Verifier report — The Kreutzer Sonata novel-dive

Independent, adversarial verification pass. Verifier did **not** author the dive.
Scope: the nine judgement-level checks the mechanical gate (`verify_quotes.py`, already PASS 37/37) cannot make.

**Verdict: 2 concerns (0 blocking).** Both concerns are non-blocking ingestion-time polish on the `workRecord` controlled-vocab; the dive is sound, source-anchored, and schema-faithful everywhere that matters. No fabrication, no unanchored primary claim, no invalid wiki type, no byte-fidelity failure.

---

## Check 1 — Byte-fidelity belt-and-braces — PASS

Re-ran `python3 docs/research/lib/verify_quotes.py …/dossier.yaml` independently: **37/37 verbatim, exit 0**. The script's PASS is real, not gamed.

Independent `grep -c` re-confirmation of a random sample (each found exactly once in the *named* extract):

| evidence id | extract | result |
|---|---|---|
| `ks-doctrine-passion-evil` | `v27_007_078_Krejtserova_sonata.txt` | 1 ✓ |
| `pos-chastity-ideal-not-rule` | `v27_079_092_Posleslovie…txt` | 1 ✓ |
| `comm-sofia-audience` | `v27_563_624_Krejtserova_sonata.txt` | 1 ✓ |
| `letter-1890-08-25-andersen` («Отвечаю: да») | `v65_131_…Andersen.txt` | 1 ✓ |
| `litho-stud-horses` | `v27_291_338_…litografirovannoj_redaktsii.txt` | 1 ✓ |
| `diary-1889-07-04-conception` | `v50_103_104_1889_07_04.txt` | 1 ✓ |
| `comm-8th-lithographed` | `v27_563_624_Krejtserova_sonata.txt` | 1 ✓ |

Also confirmed the two `contradictions[].correction` quotes are verbatim in the litho extract («я душил ее, и я ударил ее кинжалом»; «обман и насилие»). The PASS is genuine.

## Check 2 — Every primary claim in index.md is source-anchored — PASS

Sampled ~10 factual/interpretive claims; every one traces to an `evidence` row or a clearly attributed source. Spot re-greps against extracts:

- Marquee conclusion "owns the doctrine, but not its modality" → `pos-horrified-own-conclusions`, `pos-chastity-ideal-not-rule`, `letter-1890-08-25-andersen` (all verbatim).
- "epigraph — Matthew V:28 — was chosen 23 August 1889" → diary `v50_126_127_1889_08_23.txt` line 7 directly states «Эпиграф к Крейцеровой Сонате Мф. V, с 28 по 30». Anchored. (The workRecord `epigraph` value "Matthew V:28–30" matches the diary exactly.)
- Censorship/publication chain (ban Dec 1889 → vol. 13 June 1891 → Sofia's 13 Apr 1891 audience → separate-edition ban to 1900) → `comm-ban-categorical`, `comm-vol13-1891`, `comm-sofia-audience`, `letter-1891-05-22-tsar-permission`; "until 1900" and "~300 lithographed copies" both confirmed present in the commentary extract («300 литографированных списков»).
- In-text quotes cited in index but not in the ledger («страшное средство в руках кого попало», «погружение ножа в мягкое», «надоела», «ниже всякой критики», «своим выводам») all re-grep to 1 hit in their source extracts — the prose draws only verbatim from extracted text.

No primary claim found asserted without an anchor.

## Check 3 — Secondary/scholarly claims ATTRIBUTED, not asserted — PASS

`extracts/_scholarship.md` is exemplary: every claim carries an inline source (Simmons, Bartlett 2010, Maude, Yacobi 2005, Gershkovich 2019 PMLA, Knapp 1988, Edwards 1993, Chesterton, Basinsky, Stockham, Blavatsky…), and genuine uncertainty is flagged ("specific page references could not be verified"; "needs verification").

The three load-bearing loaded terms appear in index.md **only** as explicitly-attributed mainstream framing, never in the dive's own voice:
- "misogynist's confession" (line 23) — introduced as "The standard frame —", i.e. the view being tested.
- "mouthpiece reading" (line 127) — attributed "(Maude; popular reception)".
- "autobiographical frame" (lines 17, 23) — "the Sofia-centred reading as the mainstream's frame, attributed and read critically".

This is exactly the required handling (memory `corpus-dive-ground-in-primary-not-mainstream`). No mouthpiece/misogynist/autobiographical assertion in propria voce.

## Check 4 — scholarship.triangulation integrity — PASS

All 5 entries machine-validated:

| evidenceRef | exists in `evidence`? | relation | valid? |
|---|---|---|---|
| `pos-horrified-own-conclusions` | yes | extends | yes |
| `pos-chastity-ideal-not-rule` | yes | complicates | yes |
| `ks-music-irritating` | yes | confirms | yes |
| `comm-andreev-burlak` | yes | complicates | yes |
| `pos-abstinence-in-marriage` | yes | complicates | yes |

Every `evidenceRef` resolves; every `relation` is in {confirms, complicates, contradicts, extends}. (Also machine-checked: all entity, workRecord, and visual `evidenceRefs` resolve to real evidence ids — zero dangling refs.)

## Check 5 — Entities resolve to valid wiki types, accurate vaultStatus — PASS

All 18 entities use types within the allowed 10: person ×11, concept ×5, translator ×1, event ×1. **No invented `character` type.** The three fictional figures are routed correctly:

- `Pozdnyshev` → concept / missing
- `Pozdnyshev's wife` → concept / missing
- `Trukhachevsky` → concept / missing

…each carrying a "STOPGAP ROUTING" note, and the schema gap is logged in `needsReview` ("Do NOT invent a type"). Correct.

`vaultStatus` spot-checks against `website/src/wiki/` (14 files total):
- **exists** (all confirmed present): `Leo Tolstoy.md`, `Sophia Tolstaya.md`, `Vladimir Chertkov.md`, `Pavel Birukoff.md`, `Maria Tolstaya.md`, `Tatyana Tolstaya.md`. The Biryukov transliteration gotcha (`Pavel Birukoff.md`) was handled — `wikilinkTarget: "Pavel Birukoff"` matches the real filename.
- **missing** (confirmed absent, no loose/Cyrillic/alias match anywhere in the vault): Andreyev-Burlak, Repin, Hansen/Ganzen, Pobedonostsev, Feoktistov, Alexander III. A `grep -ilE` over all wiki files for Cyrillic surnames (бурлак, репин, победоносцев, ганзен, феоктистов, александр) returned zero — the `missing` flags are not transliteration false-negatives.

## Check 6 — Translations labelled; no editorializing voice — PASS

- "(working English)" label present on **37/37** `quoteEn` in the dossier and on every rendered translation in index.md. Consistent.
- The chastity doctrine is rendered exactly as Tolstoy argued it: the maximal claim is stated as made (`pos-abstinence-in-marriage`, `pos-marriage-is-sin`, `pos-sister-brother` — "still more obligatory in marriage", "a fall, a sin", "sister and brother") AND the modal qualifier is preserved (`pos-chastity-ideal-not-rule` — "ideal, not a rule"). Neither softened nor hardened into caricature. The "Accuracy in both directions" note (index line 55) explicitly guards both flattenings — aligned with memory `feedback_ingestion_accuracy_both_directions`.
- Project voice is bare and factual; mainstream framings attributed (Check 3).

## Check 7 — workRecord (two records) — PASS, with 2 non-blocking concerns

Two record-creating proposals (novella + Afterword), as the PSS catalogues them. Field names checked against the live `Master and Man.md` record and `tolstoy-works-schema.md`:

- `mainCategory` / `subcategory` — used by the dossier and by **all 15 live works records** (incl. Master and Man, lines 12–13). NOTE: these two names get 0 hits in `tolstoy-works-schema.md` (the schema doc table doesn't define them), but the live records are also source-of-truth (memory `reference_works_wiki_records_source_of_truth`), and the dossier matches the live records. Not a dive fault — a schema-doc gap, out of scope here.
- `genre` values `novella` and `essay` are both in the schema's enum (line 44). Good.
- All other field names (`titleAlternatives`, `publishedInRussiaDuringLifetime`, `dateWriting*`, `dateFirstPublished*`, `epigraph`, `bans`, `samizdatCirculation`, `censoredVersionExists`, `excommunicationRelated`, `relatedWorks`, `jubileeEdition.volumes`) exist in the schema. `relatedWorks[].id` cross-links (`afterword-to-the-kreutzer-sonata` ↔ `the-kreutzer-sonata`, `what-is-art`) are internally consistent.
- Dates evidence-anchored, no fabrication: `dateWritingCompleted: 1889-12-08` carries `oldStyle` + an explicit "NS conversion to be applied at ingestion" note; `dateFirstPublished: 1890` (foreign) vs `dateFirstPublishedInRussia: 1891-06` correctly separated; the OS/Approximate handling is sane and the conversion is correctly *deferred* (logged in `needsReview`), not faked.
- `excommunicationRelated: false` justified: note correctly states the 1901 trigger was *Resurrection*, with the doctrinal contribution acknowledged. Matches the project's Resurrection-dive framing.

**CONCERN 7a (non-blocking):** `bans[].authorityType: "state censorship"` is not in the schema's controlled vocab (`imperial-state · holy-synod · foreign-government · periodical-editor · other`). Suggested fix at ingestion: map to `imperial-state`.

**CONCERN 7b (non-blocking):** `bans[].scope: "independent/separate publication"` is not in the schema's `scope` enum (`complete-ban · passages-cut · serialization-refused · confiscation · pre-publication-rejected`). The factual situation (separate-edition publication refused, work allowed only inside Collected Works) maps best to `pre-publication-rejected` or `serialization-refused`; suggested fix at ingestion. Both are PROPOSALS the dive explicitly hands to human ingestion, so neither blocks.

## Check 8 — coverage honesty — PASS

Spot-checked the two surfaces most at risk of over-claiming:
- **Characters & prototypes** → `partial` (honest: the stopgap routing means the surface genuinely isn't fully covered).
- **Visual & manuscript record** → `partial` (honest: Andreyev-Burlak portrait, vol. 13 title page, and litho artefacts flagged as not openly available in `visuals` with `usable: false`).

No `covered` surface found that the evidence shows is really partial. The `notCovered` list and `needsReview` (incl. the honestly-disclosed 15 Jan 1890 diary that "did not yield a byte-verifiable form" and was left out of the ledger — index line 142) are candid about gaps. Coverage is not inflated.

## Check 9 — Rights hygiene — PASS

- `extracts/` holds only PD text/`.txt` (Tolstoy's own PSS text + self-rendered material) and `.md`/`.html` — no rights-reserved image committed there.
- `visuals/` cache is git-ignored: `docs/.gitignore` rule `research/*/visuals/` and `git check-ignore` on `…/visuals/commons-repin-tolstoy-portrait-1887.jpg` → **IGNORED**. Confirmed.
- No rights-reserved/unknown image is referenced as committed-to-`website/src/`. The two `usable: false` items (VIS-19 Andreyev-Burlak, VIS-20 vol. 13 title page) carry `rights: unknown` and empty `localPath` — correctly *not* embedded. `local-tolstoyru-kreutzer-sonata-cover.jpg` (rights unknown) lives only in the ignored cache, not referenced in index.md. Clean.

---

### Blocking vs non-blocking summary

- **Blocking issues: 0.** No fabrication, no unanchored primary claim, no invalid wiki/schema type, no byte-fidelity failure, no rights leak.
- **Non-blocking concerns: 2**, both Check 7 controlled-vocab mismatches on `bans[]` (`authorityType`, `scope`) — resolvable in one line each at human ingestion; the dive correctly frames the workRecord as a proposal.

The dive is verification-clean and ingestion-ready, subject to the two trivial vocab maps at ingestion.
