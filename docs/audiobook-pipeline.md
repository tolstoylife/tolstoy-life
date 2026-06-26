# Audiobook pipeline — reference & findings

Agent-facing reference for the local TTS audiobook pipeline. The working code,
text, and a shorter README live in [`projects/audiobook/`](../projects/audiobook/).
This doc is the durable record of *what was learned* and *why each setting is
what it is*, so a future agent doesn't re-derive it.

Last updated: 2026-06-26.

## Goal

Publication-quality local audiobooks for tolstoy.life works — one `.m4b` per
work, beside the existing EPUBs. Long-term: an incremental nightly job that
generates audio only for new/changed works and writes `_generated/audio/<work>.m4b`.

## Status

- **A Great Iniquity** is fully built: `a_great_iniquity_bm_daniel.m4b`
  (54:45, 10 chapters, mastered, Books-importable).
- The central open question — *is Kokoro good enough, or do we need a heavier
  model?* — is **settled: Kokoro is enough.** No OpenAudio/Chatterbox needed.
- Narrator: **bm_daniel** (British male). Chosen deliberately over bm_emma, the
  strongest *performer*, because a narrator should disappear, not impress.

## Stack

- **kokoro-tts-tool** — Kokoro-82M, runs locally on Apple Silicon. 24 kHz native.
- **ffmpeg / ffprobe** — silence, concat, mastering, M4B mux.
- **espeak-ng** — Kokoro's g2p backend.

## Findings (the hard-won ones)

1. **Use `synthesize`, not `infinite`.** This was *the* fix that took the result
   from "improved" to "amazingly good." The `infinite` command (built for
   long-form streaming) adds a processing step that mangles the ends of long
   sentences — a pre-final pause plus a high-pitched last word. The plain
   `synthesize` command renders a single sentence cleanly. An A/B on two long
   sentences confirmed it; `synthesize` clips were also ~0.5 s tighter.

2. **Synthesize one sentence at a time; splice silence between.** Kokoro has no
   SSML. The W3C standard for pauses is SSML `<break>`, but Kokoro can't read
   markup — so explicit per-unit synthesis + inserted silence is the correct
   workaround, not a hack.

3. **Pause lengths** (seconds): sentence `0.45`, paragraph `0.85`, Part break
   `2.0`. Grounded in: ACX/Audible section breaks 2–2.5 s; TTS engine defaults
   ~0.3/0.4 s (too short for long-form); prosody research (period ≈ 0.8–1.2 s
   total incl. the voice's own fall). **Never insert silence at commas** —
   chopping intra-sentence destroys Kokoro's pitch contour and sounds robotic.

4. **Spell out Part headers.** Kokoro reads `Part II` as "Part two-eye." The
   build converts `Part <Roman>.` → "Part One/Two/…"; the M4B chapter *list*
   keeps Roman numerals (they read better visually).

5. **Spell out money.** `$1.40` → "one dollar forty" (done in the flow text, not
   the source — the source keeps the real characters).

6. **Respell the verb "live" → "liv".** Kokoro otherwise says /laɪv/ (as in "live
   broadcast"). Whole-word only; "lives/lived/living" untouched.

7. **Auto-join page-break-split paragraphs.** OCR/extraction splits some
   paragraphs mid-sentence. Rule: a paragraph not ending in `. ! ? " ) …` was
   split by a page break → glue it to the next. Replaces hardcoded per-chapter
   join indices.

8. **M4B must mux with `-movflags +faststart`** or iOS Books silently refuses to
   import it (moov atom must precede mdat).

9. **Mastering chain** (the LibriVox-fatigue fix — what makes spoken word
   pleasant): `highpass=f=70,deesser=i=0.4,loudnorm=I=-19:TP=-2:LRA=7`. Output
   44.1 kHz, 128k AAC. Kokoro is 24 kHz native — that's the fidelity ceiling;
   higher bitrate is wasted.

10. **Per-call model reload (~5 s).** `kokoro-tts-tool` reloads Kokoro on every
    invocation, so the 387-sentence book takes ~40 min cold. Fine for now (the
    build is resumable). For the nightly pipeline, batch synthesis in one process.

11. **Sideloaded audiobooks don't iCloud-sync** (by design). Manual import only:
    AirDrop → Files → Share → Copy to Books, or Finder cable sync. EPUBs/PDFs
    sync; audiobooks never have.

## Model landscape (June 2026), for the record

Better-than-Kokoro free models exist (Chatterbox, OpenAudio S1, Qwen3-TTS,
Orpheus) but they win on *expressiveness*, which is a liability for neutral
long-form Tolstoy (they "act," wander, and hallucinate words more). Kokoro ties
commercial engines on clean-read naturalness (UTMOS ~4.48) and is notably clean
— the right tool here. SSML only really exists in cloud engines; the one free
high-quality SSML path is `edge-tts`, rejected because it's online + an
undocumented endpoint (this pipeline is deliberately local).

## How to run

From `projects/audiobook/`:

- `python3 build_audiobook.py [voice]` — full book → `a_great_iniquity_<voice>.m4b`
  (resumable; reads `chapters_flow/`).
- `python3 build_audiobook.py --dry` — print chapter/sentence structure only.
- `python3 audition.py` — render the 3 hardest sentences in each listed voice.
- `python3 flow_preprocess.py` — semicolon/punctuation reshaping `chapters/` →
  `chapters_flow/`.

## Open questions / next

- **Semicolon fidelity** (philosophical, Johan's call): the build narrates the
  flow text, where George's semicolons are rewritten. Now that `synthesize`
  phrases well, test narrating the *original* punctuation and possibly retire
  `flow_preprocess` — resolving the fidelity question by making it moot.
- **Short-sentence pitch wobble** — minor Kokoro trait; try merging very short
  sentences with a neighbour so the model has more context.
- **Proper-noun pronunciation** — Yasnaya Polyana, Novikoff, Radischeff, etc. not
  yet validated. (Read-along would also let a reader *see* a fumbled name.)
- **Incremental nightly pipeline** — hash each work; regenerate on change;
  Whisper transcript validation (catches dropped/repeated/mispronounced words);
  per-work proper-noun substitution dict; `_generated/audio/<work>.m4b`.
- **Read-along** (synced text + audio highlight) — strongest for the philosophical
  works (anchors proper nouns). EPUB3 Media Overlays + per-sentence timing that
  falls out of this pipeline almost for free. See `projects/audiobook/IDEAS.md`.

## Decisions log

- Narrator is a **synthetic/actor voice, never Johan's own** (non-native; a
  publication edition needs a consistent neutral house voice).
- **Daniel over Emma** — fit over performance.
- Altering Tolstoy's punctuation for audio (semicolons → periods): **still open.**
