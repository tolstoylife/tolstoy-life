# The Great Sin — Russian spine alignment notes

How `the-great-sin.ru.md` (PSS «Великий грех», t. 36, pp. 206–230) was made
paragraph-parallel to `the-great-sin.en-1905.md` (the 1905 Mayo/Tchertkoff
translation), so the two share one **paragraph coordinate** (paragraph N in
either version points to the same place in the work).

Both versions now segment to **10 sections / 135 paragraphs** and pass
`reader.segment --spine-json` (the per-section paragraph-count check).

## Which version defines the coordinate

The English is the incumbent: its read-along audio is already aligned to its
paragraph/sentence structure. So the Russian was fitted to the English shape,
not the other way round. The Russian wording is untouched — only paragraph
**breaks** were moved (split or merged) to match where the English breaks.

## English repairs (3)

The pilot English edition had three places where a single sentence was split
across a paragraph break (transcription defects — they read and speak wrong).
These were rejoined:

- Part II: *"…those called the working people" + "were the people who lived in the poorest houses."*
- Part II: *"We naturally" + "despise poverty, and it is reasonable…"*
- Part IX: *"…with whom he comes in" + "contact."*

**Consequence — resolved 2026-07-02:** rejoining shifted 3 sentence boundaries
in Part II and Part IX, which left the English audio + timing for those two
chapters (`sec-3`, `sec-10`) out of sync with the renumbered text — the voice
skipped and jumped while the highlight moved normally down the page. Both
chapters were regenerated (re-synth in the `projects/audiobook` repo, then a
`reader.build_epub` restitch). `build/` is regenerable and gitignored, so the
fix left no tracked change beyond this note.

**Watch out — the wav cache is keyed by sentence ID, not by the text.** A plain
rebuild does *not* fix this: `build_audiobook.py` reuses any
`wav_full_bm_daniel/<id>.wav` that already exists without checking whether the
text still matches, so once a rejoin renumbers the sentences, the old (wrong)
recording sits under a reused ID and gets served again. The fix was to delete
*all* of `sec-3` and `sec-10`'s cached wavs — every renumbered clip, not just
the audibly-broken ones, because a shifted sentence that happens to be the same
length would slip past a words-per-second check while still being the wrong
recording — then let the build re-synthesize them from the corrected text. Only
those two chapters were renumbered, so the other eight kept their cache and came
out timing-identical. (Same trap applies to any future pronunciation respell: it
won't take until you also delete that sentence's cached wav.)

Verified: the words-per-second check went from 13 impossible-rate sentences
(7 in `sec-3`, 6 in `sec-10`) to 0 across all ten chapters; the eight untouched
chapters' timing is byte-identical to before; every read-along slot fits inside
its chapter's audio; EPUBCheck clean. Final ear-check in Thorium is still worth
doing. Still open (deferred, not blocking): the "Kvas" pronunciation respell
(Part I) and the high-pitched "I asked" dialogue tags — voice-quality notes,
separate from this alignment fix.

## Russian break adjustments (per section)

Native PSS paragraphing → English coordinate. Every split/merge is at a real
sentence boundary; no wording changed. The starting text is the native extract
`docs/research/1905-the-great-sin/extracts/v36_206_230_Velikij_greh.txt`; the
committed `the-great-sin.ru.md` is the curated result (source of truth, not
regenerated).

| Section | Native | Target | Adjustment |
|---|---|---|---|
| Introduction | 5 | 5 | — |
| Part I | 46 | 45 | split the "knacker's beast / in whose mine" turn (two speakers PSS ran together); merge the blind-man narration+question; merge "Я спросил:" + "— О чем?" |
| Part II | 15 | 14 | split the Henry George opening (attribution / quote); merge "Отчего это?" + "Оттого, что…"; merge the closing George question back onto its paragraph |
| Part III | 8 | 9 | split the Oxford passage before "Главными же орудиями…" |
| Part IV | 10 | 9 | merge the question "…хорошую жизнь народа?" + its answer |
| Part V | 12 | 11 | merge "…кормили нас." + "Наши грехи всегда перед нами." |
| Part VI | 9 | 8 | merge the two halves of the Matthew epigraph |
| Part VII | 10 | 10 | — |
| Part VIII | 5 | 8 | split R4 three ways and R5 two ways (English breaks each declarative sentence into its own paragraph) |
| Part IX | 14 | 16 | split the closing George quote before "Земля вспахана…"; add the dateline |

## Other spine cleanups

- Stripped one PSS editorial footnote marker (³⁷) at the Henry George citation
  in Part II — apparatus, not Tolstoy's text; the English carries no notes. (The
  printed scan also carries a *second* editorial footnote in Part II — marker ¹
  on «своих статей», citing «Речи и статьи Генри Джорджа». Изд. «Посредника»,
  стр. 143 и 144. — but that marker and its citation never entered the extract,
  so there was nothing to strip. Same apparatus category; noted for provenance.)
- Fixed 5 OCR homoglyphs (Latin letters sitting inside Cyrillic words): 3×
  «зa»→«за», «тело to человека»→«тело человека», «Ha-днях»→«На-днях». The two
  remaining Latin runs (Мф. **XXIII**, Александр **II**) are Roman numerals — kept.
- Added a closing dateline to parallel the English "Yasnaya Poliana, July,
  1905." — the PSS reading text has none. First pass added the full
  **«Ясная Поляна, июль 1905 г.»** to visually match the English; on review
  (2026-07-01) that was reverted in favour of the **manuscript form,
  «Июль 1905»** (no place) — what A. L. Tolstaya actually signed, per the
  PSS commentary. Keeping strictly to the attested wording matches how every
  other spine fix was handled (breaks moved, wording untouched; OCR fixes
  correct transcription, they don't add content) — inventing "Ясная Поляна"
  would have been the one exception.

## Proofread against the scan (2026-07-01)

The Russian was machine-extracted from the TEI/PSS. It has now been checked
paragraph-by-paragraph against the printed scan (PSS Tom 36 =
`primary-sources/jubilee-edition/vol05/vol05.pdf`, pp. 206–230) — a full read
plus a word-level automated diff against the scan's own independent OCR, with
every disagreement adjudicated by rendering the actual page image and reading
it. **Result: clean.** No wording errors beyond the fixes already listed above;
every one of the ~35 raw diffs was either an already-recorded fix or noise in
the scan's OCR layer (dropped letters, stray mid-word spaces, letter-spaced
emphasis the OCR mangled) where the extract's wording was the correct one. All
proper names and numbers (Александр II, Новиков, Радищев, Parnell, Toynbee,
Gladstone, Spencer, Labouchère, Mazzini, the rent/wage/year figures) verified;
the «Мф. XXIII» citation confirmed against the page image (OCR garbles it as
«X X III»). The «Марфа, Марфа» epigraph on the same scan page belongs to the
*preceding* essay («Конец века») and is correctly excluded here.

Caveat on the caveat: this is a verification pass (extract vs. scan-OCR +
visual spot-check of every conflict), not a word-perfect human transcription
against the physical book. It's strong evidence the text is right, not a proof.
