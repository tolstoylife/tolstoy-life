---
layer: reference
lastUpdated: 2026-05-27
tags: [research, biryukov]
---

# English translation — in progress

This folder holds the English translation of Biryukov's *Biography of
L. N. Tolstoy*, Volume III: one `chapter-NN.md` per Russian source file in
[`../ru/`](../ru/). **[Chapter 18](chapter-18.md) is done as an approved quality
sample** and is the worked reference for the conventions below. Chapters 13–22 are
complete (Parts III–IV); the remaining 12 (Parts I–II) are
translated in batches (≈4 per session). See the
[volume index](../index.md) for chapter titles, word counts, and capture notes.

## Translation spec

Carry over the approach that worked for the Doukhobor sections
([`../../extracts/biryukov-biography-doukhobors-EN.md`](../../extracts/biryukov-biography-doukhobors-EN.md)):

- **Faithful and complete** — no abridging, no summarising.
- Render Biryukov's verbatim quotations of Tolstoy's letters and diaries as
  Markdown block quotes (they are primary Tolstoy text, public domain).
- **Names:** standard English / Library of Congress forms — Doukhobors, Verigin,
  Khilkov, Chertkov, Tregubov, Maude, Sulerzhitsky; the Caucasus, Tiflis, Kars,
  Cyprus, Canada.
- Preserve dates, paragraph structure, and footnote numbering.
- Keep each chapter's `# H1` and any `## Часть` divider, translated.
- The `ru/` capture is continuous (the JS-encoded fragments were decoded), so the
  bracketed "[… the source drops the opening of this sentence …]" notes used in
  the earlier Doukhobor-only translation should rarely be needed; add such a note
  only where a genuine gap remains, and flag any non-narrative cruft.
- **Source fidelity for suspect readings.** Silently restore only *garbled /
  nonsense* tokens to their obviously-intended word (e.g. *издержать* → "preserve",
  *flans* → *flancs*, "Commonnal wealth" → "Commonwealth", Коппе → Coppée). But for
  source values that are themselves *valid* yet probably mistaken — a real title, a
  plausible numeral, a name — reproduce the source **literally** (e.g. Bjørnson's
  «Король» → *The King*, not the conjectural *Beyond Human Power*; *Resurrection*
  "chapters XXXIX and XI", not the conjectural XL). No conjectural substitution, and
  no inline editorial bracket inside quotes.

## Suggested execution

≈178k Russian words → ≈235k English (chapter 18 ran 1.33× — Russian is the more
compact language, so the English is *longer*, not shorter). Dispatch per-chapter
translation agents in parallel (model `opus`), each writing its own
`chapter-NN.md` against the locked conventions above; verify each against the
Russian before presenting. Budget ≈30k Russian words (≈4 average chapters) per
session to keep the verification pass honest. Keep these files
public-self-contained — no links into `_generated/`.
