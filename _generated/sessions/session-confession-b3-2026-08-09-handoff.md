# Handoff — A Confession, Task B3: the machine-translation leg

Continues `_generated/sessions/session-confession-stageb-2026-07-17-handoff.md`. That note said B1 and B2 were done; this session found B2 was **not** finished, fixed it, and stopped before writing any translation. **No English has been written yet** — B3 starts from zero tomorrow.

**Branch:** `great-sin-redive-pass2` (2 commits unpushed). **Plan:** `_generated/Fable-plan-a-confession-reader-edition.md` Task B3, which defers the method to `_generated/Fable-plan-great-sin-machine-translation.md` Tasks 2–5. **Bundle:** `docs/reader/non-fiction/personal-papers/confession/`.

## Done this session (`6d9c231b`)

The July handoff's claim that all 16 chapters aligned was true of the prose but false of the file. Four capture notes sat inline as standalone HTML comments; `reader.segment` splits paragraphs on blank lines, so each counted as a paragraph and the spine check failed in chapters IV, V, VII and XI. Moved all four into a new `alignment-notes.md` — where two of them already pointed by name, and which B2 owed anyway. Attaching them to a neighbouring paragraph instead was not an option: `resolve_reading_text()` strips CriticMarkup and wikilinks but **not** HTML comments, so the note text would have reached the reading display and the spoken audio.

Also added `meta.ru.json` and `meta.en-wiener.json` (B2's other debt). Both editions now segment to **16 sections / 212 paragraphs**; `reader/tests` 45 passed.

## The thing that matters most: this is the project's FIRST machine leg

`the-great-sin.en-machine.md` **does not exist** — the Great Sin's machine leg was never built and is still open on the TODO. So there is no precedent file to copy conventions from, and whatever register B3 sets becomes the pattern for every work after it. Do not assume a house style exists; the decisions below were derived from scratch this session and are the only record of them.

## Size, and why it must be batched

The Russian spine is **21,400 words / 128,000 characters — 2.5× The Great Sin**. Cyrillic tokenizes at roughly 2.5 chars/token, so reading the spine alone is ~48k tokens and writing the English back is ~35k more. End to end, translation plus diagnostic is ~300–400k tokens with at least one context compaction partway.

The risk is not cost, it is **drift**: if context compacts mid-translation, the register set in the early chapters is lost and the later ones wander. For a text whose entire purpose is being a consistent fidelity ruler, that is a defect. Hence:

| Batch | Chapters | Paras | Share |
|---|---|---|---|
| 1 | I–IV | 59 | 25% |
| 2 | V–VIII | 72 | 30% |
| 3 | IX–XII | 53 | 24% |
| 4 | XIII–XVI | 28 | 21% |

Commit each batch. Re-read the previous batch's last chapter for continuity before starting the next. **The `translation-diagnostic.md` is its own session** — it needs both finished texts loaded side by side and is comparison work, not composition. Bundling it into the translation is what pushes this over the edge.

## Translation conventions settled this session

From the Great Sin plan's Tasks 2–3, plus decisions this work forced:

- **Paragraph-for-paragraph**, never merge, split, or reorder. Output paragraph *n* of chapter *k* translates spine paragraph *n* of chapter *k*.
- **Fidelity over elegance.** Keep Tolstoy's repetitions — he repeats deliberately, and smoothing it falsifies the ruler.
- **Raw by design.** One pass, no proofing, no polish. Roughness is the feature; do not file it as a defect.
- **Source is `confession.ru.md`**, never the TEI extract — the spine carries proofread repairs the extract lacks.
- **Title:** «Исповедь» is literally *A Confession*. Wiener chose *My Confession*; that divergence is itself diagnostic material.
- **Headings:** the spine carries no title line, only `## I` … `## XVI`. Mirror exactly.
- **Typography:** «…» → curly double quotes; spaced em-dashes ` — ` (Tolstoy's dashes are a rhythm device and spacing preserves the breathing); no wikilinks, footnotes, translator's notes, or bracketed glosses.
- **Quoted material comes through the Russian.** Tolstoy quotes Solomon, Schopenhauer, Socrates, the Buddha legend — translate the Russian as it stands, do not substitute the KJV or Schopenhauer's German. The ruler must show what the *Russian* reader saw.

**Recurring-term glossary** (pin these; consistency across 16 chapters is the whole point):

| Russian | English |
|---|---|
| вера | faith |
| вероучение | religious teaching |
| разум / разумное знание | reason / rational knowledge |
| знание опытное · умозрительное | experimental · speculative knowledge |
| совершенствование | perfecting (not "perfection") |
| бессмыслица | senselessness |
| суета / томление духа | vanity / vexation of spirit (Ecclesiastes) |
| обман | deception |
| соблазн | temptation |
| простой / трудовой народ | the simple / working people |
| тожество | identity (mathematical: a = a) |
| переворот | upheaval |

## Open questions — decide before or during batch 1

1. **Capitalize "God"?** The PSS text lowercases `бог` throughout («бога нет», «бог есть жизнь»). That is almost certainly a Soviet editorial convention, not Tolstoy's manuscript — so lowercasing in English would propagate an edition artifact as if it were authorial. Recommendation: **capitalize God**, and record the reasoning. Worth Johan's nod since it touches how the ruler reads.
2. **`слитком` (ch. I, para 4)** is a typo for `слишком` ("too" — "should not take all this *too* seriously"). A letter substitution, so the homoglyph sweep would not have caught it. Translated as intended; flag for the spine's own errata.
3. **Unclosed `«` (ch. III, para 14)** — the paragraph opens `«Случилось то, что случается…` with no closing quote. Reads as a transmission artifact. Rendering without the stray mark, noted rather than silently mirrored.
4. **`бог 1 и 3` (ch. IX)** — carried over from July, still unverified. Reads as OCR-mangled "God, one and threefold".

## One diagnostic finding already banked

Wiener, ch. I para 11: the Russian says only «я очень рано стал много читать и думать» ("I began very early to read and think a great deal"). Wiener renders it *"since I began to read philosophical works at fifteen years of age"* — inventing both the subject matter and a specific age the Russian does not give. Put this in `translation-diagnostic.md` when that session runs.

## Resume

Read this note, confirm `git log` matches, then start batch 1 (chapters I–IV). Pure Read/Write authoring — no Bash needed until the segmenter check at the end of each batch:

```
python3 -m reader.segment <bundle>/confession.en-machine.md --version en-machine --work confession \
  --spine-json <bundle>/build/segments.ru.json -o <bundle>/build/segments.en-machine.json
```

`build/` is gitignored and the spine segments file is already there from this session, but it regenerates in seconds if missing.
