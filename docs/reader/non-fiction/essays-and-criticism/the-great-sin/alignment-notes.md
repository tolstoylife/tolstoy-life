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

**Consequence — deferred:** rejoining shifts 3 sentence boundaries in Part II
and Part IX, so the English **audio + EPUB for those two chapters is now stale**
and must be regenerated at the next audio pass (separate `projects/audiobook`
repo). The current English build keeps working until then; `build/` is
regenerable and gitignored.

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
  in Part II — apparatus, not Tolstoy's text; the English carries no notes.
- Fixed 5 OCR homoglyphs (Latin letters sitting inside Cyrillic words): 3×
  «зa»→«за», «тело to человека»→«тело человека», «Ha-днях»→«На-днях». The two
  remaining Latin runs (Мф. **XXIII**, Александр **II**) are Roman numerals — kept.
- Added the closing dateline **«Ясная Поляна, июль 1905 г.»** to parallel the
  English "Yasnaya Poliana, July, 1905." — editorial: the PSS reading text omits
  it; the manuscript was signed «Июль 1905» (A. L. Tolstaya's hand, per the
  PSS commentary), and the place is Yasnaya Polyana.

## Caveat

The Russian is machine-extracted from the TEI/PSS and **not fully proofread**
against the printed scan. The alignment and the fixes above are verified;
subtler in-word errors may remain and want a separate reading pass.
