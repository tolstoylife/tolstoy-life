# Handoff — The Great Sin, the machine-translation leg

**The script already exists and is still correct: `_generated/Fable-plan-great-sin-machine-translation.md`.** Written 2026-07-07, seven tasks, every path exact. Follow it top to bottom. This note only records what has changed since it was written, so read the plan first and this second.

**Branch:** `great-sin-redive-pass2`, pushed through `da68b066`. **Bundle:** `docs/reader/non-fiction/essays-and-criticism/the-great-sin/`.

## What changed: the leg is no longer the first one

When the plan was written, no machine leg existed anywhere in the project. One does now — **A Confession's, finished 2026-08-10** (`a8a4573f` → `de4403e8`), and it is the precedent. Read `docs/reader/non-fiction/personal-papers/confession/confession.en-machine.md` before starting, and the conventions section of `_generated/sessions/session-confession-b3-2026-08-09-handoff.md`. The plan's Task 2 rules and those conventions agree everywhere they overlap, including the rule that matters most — quoted material is translated from Tolstoy's Russian, never swapped for the source author's original wording. The plan states it for Henry George; A Confession applied it to Ecclesiastes, Schopenhauer, Socrates and the Orthodox liturgy.

Three things A Confession settled that the plan does not carry:

- **Pin a recurring-term glossary before translating.** A short table of the words the essay turns on, fixed once and used throughout. Consistency across sections is most of what makes the layer usable as a ruler, and deciding a term twice is how it drifts. A Confession's table is in its handoff; The Great Sin needs its own — land, property, sin, the labouring people.
- **Expect to find defects in the spine.** Rendering every sentence is the closest reading anyone gives the text, and it surfaces transmission faults that proofreading missed — three in A Confession, including one nobody had caught before. Don't repair them in the Russian, that is a separate decision; translate as intended and record them in the bundle's `alignment-notes.md`.
- **A raw pass is finished when it is complete, not when it is good.** One pass, no proofing, no polish. The plan says this twice and it is still the thing most likely to go wrong.

## The one genuine judgment call

The plan bundles the translation and the diagnostic (Task 5) into one run. A Confession split them, because at 21,400 Russian words the pair would have needed a context compaction partway and the register set early would have been lost.

**The Great Sin is 7,774 Russian words — roughly a third of A Confession, and 10 sections / 135 paragraphs against 16 / 212.** So one session is plausible here where it was not there, and no batching is needed. Judge it live: if the translation alone eats more context than expected, stop at the commit and take the diagnostic separately rather than pushing through. Nothing downstream depends on them being in one session.

## Two inconsistencies to resolve, both small

- **The `translator` string.** The plan's Task 3 specifies `"Machine translation (Claude, 2026) — faithful one-pass, unproofed"`. A Confession's `meta.en-machine.json` says `"Project machine translation, raw first pass"`. Pick one and make both files match — this string is user-visible in the reader.
- **Capitalization of "God" does not arise here, and that is itself worth noting.** A Confession's spine lowercases `бог` throughout, and the English capitalizes it against the source on the grounds that the lowercasing is a Soviet editorial convention rather than Tolstoy's. The Great Sin's spine **already capitalizes** — `Бог`, `Бога`, `Богу`, every occurrence. So just follow the source here. It is also mild evidence that the Confession call was right: the same edition series capitalizes in Tom 36 and not in Tom 23, which looks like a per-volume house decision rather than anything authorial. Worth adding to the Confession bundle's `alignment-notes.md` if you touch it.

## Verify before building

The plan was written five weeks ago; confirm rather than assume. The spine still segments to **10 sections / 135 paragraphs** (checked 2026-08-10, matches the plan). `build/` is gitignored, so the spine segments file may be absent on this machine — the plan's Task 4 rebuilds it first, which is correct. Check `git log --oneline -5` matches the branch tip above before writing anything.

## Skills

Start with **`resume-handoff`** — it does the reality-check against the repo before any work begins. Close with **`end-of-day`** if the session ends the working day; `LOG.md`, `TODO.md` and the `project_reader_editions_workflow` memory all have live entries about this leg that will need updating. No dive skill is involved; this is pure Read/Write authoring with a segmenter check at the end.

## Do not

Do not edit `the-great-sin.en-1905.md` — the audio timing (338 clips) and the read-along EPUB are built from it, and the audio cache is keyed by clip ID rather than by text, so a change there silently keeps stale audio. This is why the diagnostic is a standalone report rather than in-text marks; the plan's Task 5 explains the reasoning and it still holds. Do not run the audiobook build against the machine edition. Do not push — Johan pushes.
