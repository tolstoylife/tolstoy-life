---
title: The Great Sin — a restored text, and telling the reader what was done to it
---

# The Great Sin — a restored text, and telling the reader what was done to it

**What this is.** The design for two pieces of work on the existing Great Sin reader bundle: a new standalone page carrying the passages Chertkov cut from the essay before publication, and a third movement in the overview's `## The cut` section telling the reader that the 1905 English softened the essay a second time. Written 2026-08-10.

**What this is not.** It is not a change to the reader engine, and not a change to any of the three version files. It is also not the project's method surface — the page that would tell a reader, once and site-wide, that this is how translation and editing were done to Tolstoy. That surface is wanted and was discussed, but where a reader meets it is a site-wide question that has not been decided, and it gets its own design rather than a corner of this one.

**Status.** Design approved 2026-08-10. Not built. Building is a separate, later session.

---

## Why this exists

The essay was finished in May 1905 and then made shorter. Chertkov came to Yasnaya Polyana that month and proposed cuts; Tolstoy accepted them and within days regretted it, writing in his diary on 6 June: «Сократил Великий Грех, выбросил многое. Мне жалко» (I shortened The Great Sin, threw out much. I am sorry for it). What came out survives among the discarded drafts printed in <abbr title="Полное собрание сочинений — the 90-volume Jubilee edition of the complete works">PSS</abbr> Tom 36.

Reading the machine-translation leg against the 1905 English then showed the same essay being softened a second time, in English, by the same man. That finding is recorded in the bundle's `translation-diagnostic.md`.

So the essay was reduced twice by the same hand, and a reader currently meets neither fact in the place they would meet it. This design closes both gaps for this one work. Whether the pattern runs through the rest of the Prophet period is a separate question and a programme, not a task.

## Where the material is, and what it actually says

The apparatus lives in `primary-sources/jubilee-edition/vol05/vol05.fb2`. Note the folder name: `vol05/` holds **PSS Tom 36**. The `jubilee-edition/volNN/` directory names are offset from the real Tom numbers, and this was verified rather than assumed — `vol36/` is in fact Tom 72.

The Great Sin's variants occupy roughly 27,000 characters and are printed as sixteen numbered fragments, `№ 1` through `№ 16`. The editorial commentary for the essay sits later in the same volume and is what keys them.

Two corrections to what an earlier session recorded, both established by reading the apparatus:

**The variants are not page- or line-keyed.** There are no `стр.`/`строка` references attaching a variant to a place in the printed text. The commentary keys them **by chapter**, in the essay's original numbering.

**The apparatus is in pre-reform orthography.** Variant № 9 opens «Въ Россіи происходятъ теперь неперестающія волненія» — hard signs, yat, i-decimal. The published spine in the bundle is modern orthography throughout.

## What gets restored

**In scope — variants №№ 9–12.** The commentary names these four as one set, and names them precisely: «Всё исключенное по инициативе Черткова и с согласия Толстого (первая глава, конец второй, шестая и конец седьмой — по первоначальному счету)» — everything excluded at Chertkov's initiative and with Tolstoy's consent: the first chapter, the end of the second, the sixth, and the end of the seventh, by the original numbering. This is not our inference about what was cut; it is the editors of Tom 36 saying so. The four run 5,730 + 829 + 2,421 + 343 characters, 9,323 in total.

**In scope — the «Необходимый переворот» paragraph**, the one Chertkov lifted out of the opening and printed separately under a title of his own giving. Only that paragraph, not the whole introduction variant it sits in: the rest of that variant is an earlier state of the introduction and belongs with the draft states below.

Which variant to take it from is an open question the build must settle first. The sentence the overview quotes — «жизнь народа слагается не вслѣдствіе внѣшнихъ формъ… а внутренней дѣятельностью отдѣльныхъ личностей» — is verified present in **№ 15**, the introduction as sent to Chertkov in England. But the commentary says what was printed in *Свободное слово* № 17–18 under the title «Необходимый переворот» was the **proof** variant of the introduction, a later stage, and it prints a variant from those proofs as **№ 16**. So № 15 is confirmed to contain the sentence, and is not yet confirmed to be the text that was published under that title. Resolve before restoring, and take the paragraph from whichever variant the apparatus supports.

**Out of scope — variants №№ 1–8, 13, 14.** These are earlier draft states, and some are successive passes at the same passage: № 4 and № 5 are two versions of one paragraph, opening «И что же — русскіе ученые…» and «И что же — русскіе люди…». They were never in the finished essay. Restoring them would be composing a text rather than repairing one.

**One claim to check rather than repeat.** The overview currently says Chertkov "lifted a single paragraph out of the opening" and printed it as «Необходимый переворот». The apparatus describes the whole first proof of the introduction being printed under that title, in *Свободное слово* № 17–18. Both may be true from different angles — the paragraph sits inside that introduction — but the restored page must not restate the overview's version until it has been checked against the record. If it turns out the overview overstates it, the overview gets corrected too.

## Decisions taken

**Orthography: keep the pre-reform text verbatim.** Every restored word stays pointable at the manuscript record, which was the condition set for this trial. The visible change of spelling also does honest work for free: a reader can see exactly where the published text stops and the recovered text begins, without our having to mark it. The cost — it reads as foreign, and it is a second obstacle between a Russian-reading eye and the prose — is accepted.

**Form: the passages with their seams.** Each restored passage appears in full, wrapped in the published paragraph before it and the published paragraph after it, so the reader reads the join: the sentence Chertkov cut away from, the restored text, the sentence he cut back to. This is where the trial's question actually lives — whether the essay reads better whole. The restored text itself is the 9,323 characters of the four excisions plus the «Необходимый переворот» paragraph; with the bridging paragraphs on either side of each, the page's Russian comes to roughly 14,000 characters, and it duplicates nothing beyond those bridges. The alternative of rebuilding the whole essay was rejected: it would mean a second 52,000-character copy of the spine that drifts from it, and the seven known spine defects would then need fixing in two places.

**What the "Editorial cuts" layer means.** The layer records **interference by others** — Chertkov's excisions, the censor's hand, a translator's softening. It never carries our own editorial hand; our work goes on pages that say plainly it is ours. Three things settled this. The name fits. It matches what the project is for. And it is the only reading the mechanics support: our restorations are passage-sized, and a passage cannot live in a mark at all (see the constraint below), so a layer meaning "our restorations" would be a layer that stays permanently empty.

This decision costs nothing to record and is separate from marking any text. No marks get added under the layer by this work.

## Mechanics that constrain the design

These were verified in this session, not assumed.

**The layer is empty everywhere.** No `{--…--}` or `{++…++}` mark exists in any reader bundle. Nothing to migrate, nothing to unpick.

**The layer only exists on version pages.** Its CSS is scoped to `body[data-kind="work"]` (`docs/reader/assets/shell.css:288`), and a page is a work page only when `work_version_of` matches it — that is, when it is named `<work>.<version>.md` and has built segments (`docs/serve.py:482`). Everything else in a bundle is a plain doc page.

**Therefore the new page is invisible to the machinery.** `bundle_editions` picks up only files named `<work>.<version>.md` (`docs/serve.py:376`). A page named `restored-text.md` gets no segmentation, no paragraph-count check, no audio, no EPUB. It cannot break the three parallel versions or the built clips, because nothing looks at it. This is what makes the standalone form safe, and it is why the form was chosen.

**Its editorial marks render always-visible.** Because it is a doc page, the layer CSS does not apply and `<del>`/`<ins>` simply show. For a page whose purpose is displaying what was removed, that is the wanted behaviour, and it needs no toggle and no new CSS.

**A mark can never hold a passage.** Paragraph splitting runs on the raw markdown and `resolve_reading_text` is applied per paragraph afterwards (`reader/segment.py:90` and `:93`), so any blank line inside a mark creates a new paragraph — including inside `{--…--}`, which strips to nothing but still counts. The paragraph coordinate is what the Russian spine, the 1905 English and the machine English all validate against. This is why restorations can never live in the version files.

**Which files could take a mark at all**, if we ever wanted one:

| File | Safe? |
|---|---|
| `the-great-sin.en-1905.md` | Frozen. Audio, timing and the EPUB are built from it, and the audio cache is keyed by clip ID rather than text, so any change to a clip's text under an unchanged ID silently keeps stale audio. Only `{>>comments<<}` are safe, because they are dropped before segmentation. |
| `the-great-sin.ru.md` | Safe within a paragraph. No audio is built from it — the build folder holds `timing.en-1905.json` only. Paragraph count must be preserved. |
| `the-great-sin.en-machine.md` | Same as the Russian: segments only, no audio, paragraph count preserved. |

None of these is touched by this work.

## The page

Location: `docs/reader/non-fiction/essays-and-criticism/the-great-sin/restored-text.md`, alongside `overview.md` and `translation-diagnostic.md`, and following their conventions — a plain `# Title` heading and a bold lead paragraph stating what the page is.

It opens with what it is and what it is not. The passages restored are only those the apparatus documents as removed. No project English is carried from them. No softening we merely suspect is reversed. A reader sees where our hand stops before reading a word of the text.

Then the restored passages in the order they belong in the essay. Each carries the apparatus's own number, where the editors say it belongs, the published paragraph before, the Russian verbatim in its pre-reform spelling, an English gloss beside it in the format the overview already uses, the published paragraph after, and a line on what the removal changed.

Tolstoy's own deletions inside the drafts are kept and explained. The apparatus marks them with angle brackets, and two of the five passages carry them — № 9 and № 10 both open on struck text. They matter because they show him cutting himself before Chertkov ever arrived, which is a fair thing for a reader to weigh against the story of a text taken from its author.

## Placement is the fallible step, and is treated as such

The excisions are keyed to the essay's original chapter numbering. That numbering cannot be reconciled to the published text by arithmetic: the commentary's own leaf counts show the final redaction had nine chapters, and the published essay has nine (Введение plus I–IX), so removing two chapters from an original count cannot land on nine. The essay grew between drafts as well as shrank.

So each passage is placed by reading it against the published text and finding where it fits. That is a judgment, and the page states the reasoning for each placement in a sentence, so a reader can disagree with it. Where a placement is uncertain, the page says it is uncertain rather than choosing silently. This is the one step in the trial that can be wrong, and it should be the easiest step for a reader to check.

## The third movement in "The cut"

The section presently ends on "It was cut with his assent, and against his own regret." The new movement follows that sentence and carries it into English: the essay was softened a second time, in translation, by the same man.

The evidence is already gathered in `translation-diagnostic.md`. Three distinct Russian words — «последствия», «следствием», «результатов» — are all rendered "result", collapsing a distinction the essay maintains. «лишь» is dropped from the Mazzini epigraph at VIII ¶1, turning an exclusive claim into a mild one. The overview's `## The title` section already shows *A Great Iniquity* doing the same work to the title, so the movement builds on that rather than repeating it.

The point is Chertkov's double role, and it is a fact rather than a reading: in *What Is Art?* he was the channel that rescued the uncensored text from the censor, and here he cut the Russian himself and then his English cut it again. It is written plainly, with no adjectives doing the arguing, per the overview page conventions.

## One repair while we are here

The overview links the corpus dive and the reading annotations under `## Around this work`, but not `translation-diagnostic.md` and not `alignment-notes.md`. Those pages are currently reachable only from the docs index, so a reader who finishes "The cut" has nowhere to go. The restored page would inherit the same dead end. All three companion pages get listed there.

## Where our hand stops

No version file is touched — no marks, no edits. The audio, the timing file and the EPUB are untouched by construction, since the only new file is one nothing reads.

No project English is carried from the restored Russian. The English glosses on the page are glosses, marked as such, and they exist for one reason: a Russian-only page is one Johan cannot evaluate as a reader and no English reader can use. They are never promoted to a translation leg by accident.

No softening we suspect but cannot document is reversed. Restoring what Tolstoy assented to and then regretted is defensible. Rewriting toward what we think he would have wanted makes us the next editor in the chain, which is the thing this whole piece of work exists to expose.

## What follows, and is not specified here

The method surface — Tolstoy's own preface to the English *What Is Art?* as the project's licence for all of this. He itemises there what was done to him: «всегда» made «иногда», «все» made «некоторые», «церковное» made «католическое», «патриотизм» made «лжепатриотизм», and the spiritual censor inserting the redemption dogma he rejected. Every one of those operations has a counterpart in our diagnostic findings, which is why it belongs at the front of the project rather than inside one work's pages. The preface is quoted in full in the dive at `docs/research/works/non-fiction/essays-and-criticism/1897-1898-what-is-art/index.md`. Where a reader meets this surface is undecided and needs its own conversation.

Checking the pattern across the Prophet period. A programme rather than a task, and it wants the method surface written first so there is something for the findings to attach to.
