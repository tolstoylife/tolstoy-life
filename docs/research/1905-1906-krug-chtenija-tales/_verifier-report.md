# Verifier report — 1905–1906 Круг чтения weekly-reading tales dive

**Verifier:** independent, fresh context. **Date:** 2026-06-12.
**Mechanical gate:** `verify_quotes.py` already PASSED (36/36, exit 0) — not re-run; judgement-level checks below.

**Verdict: CLEAN-WITH-MINORS — 0 blockers, 1 should-fix.**

The dive is in very good shape: every primary claim is source-anchored, the byte-faithful extracts hold up under spot-check, scholarship is scrupulously attributed (the section even self-labels "Attribute, don't assert"), the "first English" trap is explicitly avoided, entities and workRecord fields are schema-valid, and the publication boundaries (extracts/ PD-only, visuals/ git-ignored, draft note `draft: true`) are all correctly observed. One factual slip in a dossier ban-date, and three small polish items, are the whole of it.

---

## BLOCKER
(none)

---

## SHOULD-FIX

### S1. Молитва `bans[].banDate: "1908"` is the wrong year for the censorship cut
`dossier.yaml` (A Prayer workRecord, `bans[]`) sets `banDate: "1908"` (approximate) for the censor's excision of the Russo-Japanese-war-prayer passage, attributing it to "the 2nd edition of Круг чтения."

The commentary (`c_v42_557_583_Krug_chtenija_general.txt`) shows the second edition (Tolstoy's revised redaction) was **prepared** 1907–08 but **did not appear in his lifetime**. It was printed by Sytin/Biryukov: the first выпуск "в конце 1910 г.", the remaining выпуски "в 1911—1912 годах... под редакцией П. И. Бирюкова. ... Во всех выпусках были сделаны многочисленные цензурные изъятия." So the second edition that carried the Молитва cut appeared **1910–1912**, not 1908. 1908 is the year Tolstoy *revised the text*, not the year the censored edition was printed.

Fix: set `banDate` to ~`1910` (or `1911`), `banDateApproximate: true`, and adjust the note to say the cut appears in the 1910–1912 Sytin/Biryukov second edition. Confined to the dossier — index.md prose is safe because it only says "in the second edition of Круг чтения" without a year (and the commentary's "Во втором издании" is verbatim-correct).

---

## NICE-TO-HAVE

### N1. За что? "vol. II, the September reading" is stated more flatly in index.md than the dossier warrants
The За что? commentary (`c_v42_626_643_Za_chto.txt`) says only that the tale prints "по первопечатному тексту в **первом издании** «Круга чтения»" — first *edition* (vs the 1908 redaction), never the *volume* number. The dossier handles this correctly: it flags the vol. II / September placement in `needsReview` (phase 2: "the commentary states «первое издание», not the том number") and in `contradictions`. But index.md line 141 prints "За что? — vol. II, the September reading) appeared as weekly readings in the first edition" and the cluster table says "42 (с.84–106)" with no caveat. The inference itself is sound (vol. I = first half-year, vol. II = second half, so a September reading falls in vol. II), so this is presentation polish, not an error: consider a soft hedge in the index prose to match the dossier's own honesty.

### N2. Dangling `resurrection` relatedWorks reference
The Божеское workRecord proposes `relatedWorks: [{id: resurrection, relationshipType: source}]`, but there is **no `resurrection` record** in the works tree (15 records exist; Resurrection is not among them, despite an earlier Resurrection dive). This is a forward reference — like the six tale records themselves, none of which exist yet — so it is an ingestion-time concern the validator will catch, not a hard error. Flag at ingestion (or drop the ref until a Resurrection record is created).

### N3. Two light editorial touches in index.md
"the radiant realist sketch" (line 29) and "is the dive's quiet irony" (line 167). Both are mild and within the established dive register, and "quiet irony" is anchored to a documented fact (Tolstoy's own «совсем плохо. Бросил» against Mirsky's praise). Optional trim if a stricter factual voice is wanted.

---

## OK — checks that passed

- **Byte-fidelity spot-check (9 rows, all extract types).** Confirmed verbatim and in-context:
  - tale keystones E08 (Алёша, v36), E16 (Молитва cut span, v41), E22 (Nicholas I, v42), E12 (Корней, v41);
  - commentary E02 (marquee «нецензурное»), E07 (conviction), E17 (censor-cut location), E30 (reversed title, ×4);
  - diary E19 (Ягоды), E36 (22 executed);
  - letters E04 (Chertkov «не пройдет в России»), E34 (regret), E25 (А.Л. Толстая), E31 (ужаснулся), E32 (Gren/Новая жизнь).
  Working-English glosses are faithful (not mistranslations) and every one is labelled "(working English)".
- **Prompt-flagged sanity checks, all confirmed:**
  - **Gorbunov-Posadov conviction** — verbatim: "Суд состоялся на другой день после первой годовщины со дня смерти Толстого, 8 ноября 1911 г. ... признан виновным и присужден к заключению в крепости на один год"; 12 passages destroyed. Index.md accurate.
  - **Алёша `publishedDuringLifetime: false`** — E11 confirms "впервые... напечатан в I томе «Посмертных художественных произведений», 1911"; excluded from the anthology; index.md and dossier consistent.
  - **Молитва censor-cut span** — E16/E17 located exactly to «Вот сейчас» … «Японцы тоже молятся, чтобы им победить» (т.41 с.130); "Во втором издании" verbatim.
  - **Reversed title** — E30 confirms first form (30 Dec 1903, Tom 54) was «Человеческое и божеское» (human-first), inverted in reworking. Both `contradictions` and prose accurate.
- **"First English" non-overclaim.** index.md states outright "the dive does not claim its working glosses are «first English»"; the dossier carries the matching guard. Only Алёша had a pre-2000 English translation (Hagberg Wright 1912 / Maude c.1922 / Brown 1985); the other five appeared in English in 2000 (Sekirin/Zondervan + Spence/Northwestern). Accurately reflected in index, dossier `translationStatus`, and `coverage`.
- **Scholarship attributed, not asserted.** Every secondary claim names its source (Kirkus 2000, Publishers Weekly 2000, Spence 2000, Mirsky 1926, Pine 2020, Kuzminskaya). Quotes verified present in `extracts/_scholarship.md` (not invented). `triangulation` uses valid relations (3 `extends` + 1 `confirms`) against valid evidenceRefs. The "didactic decline" reading is explicitly framed as the mainstream view to read critically.
- **Entities resolve.** wikiTypes all valid (person ×9, concept ×3, character ×2, event ×1, institution ×1). Alyosha + Svetlogub correctly `character`; Nicholas I + Migurskis correctly `person` (historical figures as themselves). vaultStatus spot-checks: Chertkov = `exists` (✓ `Vladimir Chertkov.md` present); Gorbunov-Posadov, Lizogub, Maximov, Nicholas I, Migurski, Abrikosov, Shchegolenok, Stepnyak-Kravchinsky, Posrednik all genuinely absent from `website/src/wiki/` → `missing` correct (only 14 wiki pages exist).
- **workRecord proposals schema-valid.** All 18 field names are real works-schema keys; all genre values `short_story` (in enum), the two open calls (Молитва short_story/parable, Божеское short_story/novella) flagged in needsReview. `relatedWorks[].relationshipType` ∈ {cycle, source} (valid). `bans[].scope: passages-cut` valid. titleEn "Divine and Human" matches the 2000 editions. OS→NS conversions correct (+13 for 1905–06; e.g. Ягоды 11 Jun OS → 24 Jun NS, Алёша 24 Feb OS → 9 Mar NS). The shelving subcategory <TBD> is correctly flagged in needsReview, not invented.
- **coverage honesty.** "Reception & afterlife" honestly marked `partial` (contemporary press reception out of corpus); everything marked `covered` is supported by the evidence. No inflation.
- **Voice & boundaries.** Prose largely factual (two minor touches, N3). extracts/ holds only PD material (tale/commentary text + the one PD Алёша autograph facsimile rendered from the local jubilee PDF). visuals/ is git-ignored (`docs/.gitignore`: `research/*/visuals/`). No rights-reserved or unknown-licence image is committed; nothing image-like landed in `website/src/`. The draft note `website/src/posts/notes/2026-06-12-1905-1906-krug-chtenija-tales.md` has `draft: true`.
