---
layer: reference
lastUpdated: 2026-05-27
tags: [research, biryukov]
---

# English translation — complete

This folder holds the complete English translation of Biryukov's *Biography of
L. N. Tolstoy*, **Volume IV** (1900–1910): one `chapter-NN.md` per Russian
source file in [`../ru/`](../ru/). **All 19 chapters are translated** (Parts
I–IV), covering Tolstoy from the Boer War and the renewed Doukhobor question
through to his flight from Yasnaya Polyana and his death at Astapovo on
7 November 1910.

Combined with [Volume III](../../biryukov-vol3/en/README.md), the project now
holds the English translation of **Biryukov's complete four-volume biography**
end to end — 41 chapters, ≈421,000 English words.

See the [volume index](../index.md) for chapter titles, word counts, and
capture notes, and the shared editorial ledger at
[`../../biryukov-vol3/en/translation-notes.md`](../../biryukov-vol3/en/translation-notes.md)
for the per-chapter editorial calls (Volume IV entries follow the Volume III
ones).

## Translation spec (carried over from Volume III)

The same locked conventions as Vol III (see
[Vol III README](../../biryukov-vol3/en/README.md) for the original
formulation):

- **Faithful and complete** — no abridging, no summarising.
- **Set-off quotations as Markdown `>` block quotes.** Biryukov's verbatim
  quotations of Tolstoy's letters and diaries, and reminiscences he introduces
  with an introducing line ending in a colon, are rendered as Markdown block
  quotes. Multi-paragraph quotations: every line starts `> `, blank separators
  are a bare `>`, and **one** outer `"…"` pair wraps the whole block.
  Quotations woven inline into Biryukov's own sentence stay inline.
- **Names:** standard English / Library of Congress forms — Chertkov,
  Maude, Makovitsky (D. P.) / Dušan, Goldenweiser, Gusev, Bulgakov,
  the Doukhobors, Verigin; the Caucasus, Tiflis, Astapovo, Yasnaya Polyana,
  Kochety, Shchekino, Kozlova Zaseka, Krekshino, Optina Pustyn, Shamordino.
- **Recognised work-titles** in conventional English, italic: *I Cannot Be
  Silent*, *The Circle of Reading*, *For Every Day*, *The Path of Life*,
  *Bethink Yourselves!*, *What Is My Faith?*, *What Is Truth* (no question
  mark, after the painting's deliberate Ge-titling — applied corpus-wide).
- Preserve dates, paragraph structure, and footnote numbering. Biryukov's
  asterisk footnotes are kept in the source's own style — an inline `(*)`
  marker and the note as `(* … *)`, with the Russian text translated to
  English.
- **Policy A** source fidelity. Silently repair only **nonsense / garbled**
  tokens (OCR garble; foreign-language fragments with dropped accents
  restored to standard form; stray glyphs that are not a valid value).
  Reproduce **valid-but-suspect** real names / titles / numerals / dates
  literally — no conjectural substitution, no editorial bracket inside
  quotes. Preserve source defects (orphan markers, dangling colons) where
  they recur.
- **Embedded primary documents** translated faithfully from Biryukov's
  reproduced Russian — no original-language / published-English substitution.
  This rule is most consequential in chapter 13 (the «Океан приветствий»
  greetings anthology), chapter 14 (the two short Tolstoy appeals), and
  chapter 17 (the text of Tolstoy's secret will).

## Notable features of Volume IV

- **Three embedded primary documents under `## H2`.** Chapter 13 embeds the
  Gorbunov-Posadov greetings anthology («Из океана приветствий Льву
  Толстому»); chapter 14 embeds two short Tolstoy appeals (*A Greeting to
  Those Who Have Refused Military Service*; *There Is No Evil Without Some
  Good*); chapter 17 embeds the text of Tolstoy's secret will of
  18 September 1909. All four are rendered as ordinary translated prose
  under their H2 (not as `>` block quotes), with the documents' own outer
  `"…"` quote pairs preserved as the source prints them.
- **The 1922 dedication signature.** Chapter 19 closes with Biryukov's
  signed dedication line «П. Бирюков. 15 декабря 1922 года.» — preserved
  faithfully in the EN as "P. Biryukov. / 15 December 1922." It marks the
  end not only of Volume IV but of the whole four-volume biography Biryukov
  spent twenty years writing.

## Production notes

Translated in five sessions on 2026-05-27 by per-chapter
`oh-my-claudecode:executor` (opus) translators dispatched in parallel
foreground, followed by per-chapter `oh-my-claudecode:verifier` (opus,
read-only) EN↔RU verification, with the orchestrator applying flagged fixes
and maintaining the editorial ledger and the volume index as single-writer.

Mean expansion ratio across the 19 chapters: **≈1.33×** (chapter-by-chapter
1.27–1.39); 140,171 RU words → ≈186,200 EN words. The 5-session breakdown:
chs 1–4 · chs 5–7 · chs 8–10 · chs 11–13 · chs 14–16 (opens Часть IV) ·
chs 17–19 (closes Часть IV and the biography).

## Related

- [Biryukov, *Biography*, Volume III — English translation](../../biryukov-vol3/en/README.md)
  — the preceding volume, also complete. Vol III's chapter 18 is the
  approved quality sample and the worked reference for the conventions used
  in both volumes.
- [Volume IV index (Russian source overview)](../index.md) — provenance,
  capture notes, and OCR caveats.
- [Tolstoy and the Doukhobors](../../index.md) — the survey these captures
  support.
