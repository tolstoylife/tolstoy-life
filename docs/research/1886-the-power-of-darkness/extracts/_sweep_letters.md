# The Power of Darkness — composition-years witness sweep: LETTERS

**Method.** Swept the local tolstoydigital TEI letters in Tom 63 (1886) and Tom 64 (1887)
— `primary-sources/tolstoydigital-TEI/texts/letters/v63_*.xml`, `v64_*.xml` — for the
composition window (autumn 1886) and the censorship/staging struggle (winter 1886–1887).
Keyword set: `Власт|тьм|драм|пьес|комед|цензур|запрет|Савин|Феоктист|Победонос|Стахович|Давыдов|Посредн|Сытин|театр|представл|поставит`.
Candidate files were date-filtered by the extractor's title line (the `when="1934/1953"`
attribute is only the PSS publication year, not the letter date), then extracted verbatim
with `python3 docs/research/lib/extract_tei.py <xml> --choice=reg --notes=auto`.

**Hit count: 10 materially-relevant letters** (4 in Tom 63 / 1886, 6 in Tom 64 / 1887),
plus negative findings recorded at the end so the dive does not re-chase them.

The play was begun **late October 1886** and the cheap «Посредник» edition + the
society/court readings + the staging attempt + the censorship ban all fall inside this
window. Tolstoy's own 1886 diary is nearly silent (see `_sweep_diaries.md`); the letters
are the primary witness, exactly as the brief anticipated.

---

## 1. To N. N. Strakhov, 19 October 1886 — `v63_559_H_N_Straxovu` (PSS 63, pp. 397–399)

**Genre:** letter · **PSS Tom:** 63 · **Addressee:** N. N. Strakhov · **Significance:**
The pre-composition restlessness, days before he picked up the play — he is "still feeling
for the work" that will "swallow him whole." Establishes the work-mood baseline.

> Теперь все еще примериваюсь к работе и все еще не могу сказать, чтобы напал на такую,
> какую мне нужно для спокойствия — такую, чтобы поглотила меня всего. — Если нужно то Бог даст.

*(working English)* "Even now I am still feeling my way toward the work, and still cannot
say I have hit on the kind I need for peace of mind — the kind that would swallow me whole.
— If it is needed, God will grant it."

*(The bulk of this letter is about the «Посредник» project for popular science textbooks —
the same publishing house that would print the cheap edition of the play — and about his
recovery from the leg injury that marked this autumn.)*

---

## 2. To N. N. Ge (the elder), 31 October – 1 November 1886 — `v63_563_l` (PSS 63, pp. 402–404)

**Genre:** letter · **PSS Tom:** 63 · **Addressee:** N. N. Ge (painter, the elder) ·
**Significance:** The start-of-composition announcement — "I have begun an artistic work
that occupies me very much." Per the PSS note this "artistic work" is the play. Also maps
the surrounding circle (Dzhunkovsky leaving for Khilkov; Faynerman; Chertkov's marriage).

> Я теперь хожу свободно, только прихрамывая и начал художественную работу,⁴ которая
> очень меня занимает.

*(working English)* "I now walk freely, only with a slight limp, and have begun an
artistic work that occupies me very much."

Surrounding network in the same letter:

> Ныне уехал один лейб-уланский блестящий офицер Джунковский,² едет к Хилкову;³ Хилков же
> еще более блестящей богатый князь 22 лет, полковник, который бросил все и живет на
> крестьянском наделе... Чертков женат и писал счастливое письмо.

*(working English)* "Today the brilliant Life-Guard Uhlan officer Dzhunkovsky left, going
to Khilkov; and Khilkov, an even more brilliant, rich prince of 22, a colonel, who has
thrown everything up and lives on a peasant allotment... Chertkov is married and wrote a
happy letter."

---

## 3. To N. N. Strakhov, 14 November 1886 — `v63_571_H_H_Straxovu` (PSS 63, pp. 408–409)

**Genre:** letter · **PSS Tom:** 63 · **Addressee:** N. N. Strakhov · **Significance:**
The clearest single statement of the work-mood and the **intent**: written joyfully, and
explicitly *for the popular/folk theatres* (для народных театров). This is the anchor
quote for "why he wrote it."

> Я живу очень хорошо, радостно — пишу. Написал пьесу² для народных театров.

*(working English)* "I am living very well, joyfully — writing. I have written a play for
the folk theatres."

---

## 4. To A. A. Tolstaya, ~20 January 1887 — `v64_010_A_A_Tolstoj` (PSS 64, p. 6)

**Genre:** letter · **PSS Tom:** 64 · **Addressee:** Countess A. A. Tolstaya ·
**Significance:** The play is circulating by ear in St-Petersburg high society (she is being
made to *listen* to it — the Stakhovich-driven aristocratic readings). Tolstoy names his
target audience outright: the "great world" / большой свет. Self-deprecating about the work
("my dreadful composition") yet defends its purpose.

> ...знал, что вы — несчастная — слушаете мое ужасное сочинение.² ... Надеюсь, что она
> (пьеса) будет полезна для тех, для «большого света»,³ для которого я писал ее, но вам
> она совсем не нужна.

*(working English)* "...I knew that you — poor thing — are listening to my dreadful
composition... I hope that it (the play) will be useful for those, for the 'great world,'
for whom I wrote it, but you have no need of it at all."

---

## 5. To A. A. Stakhovich, 23–31 January 1887 — `v64_017_A_A_Staxovichu` (PSS 64, p. 9)

**Genre:** letter · **PSS Tom:** 64 · **Addressee:** A. A. Stakhovich · **Significance:**
Direct thanks to Stakhovich — the man who read the play aloud in society (and, per the
genesis tradition, to Alexander III) — for "your efforts about the drama." Tolstoy's stance:
grateful for the involvement but *utterly indifferent to the outcome* ("whatever comes out,
it is all splendid"). The text is lacunose (the TEI carries the editors' bracketed
reconstructions and ellipses). Also: the play was read to the Dyakovs.

> [Спасибо вам], дорогой Александр [Александрович], за ваши [хлопоты о драме]. Сейчас
> получил....¹ ее. Меня очень ра[дует т]о участие, к[оторое] вы прини[мае]те в деле пьесы,
> но к результатам совершенно, совершенно равнодушен. Что ни выйдет, всё отлично. Я это не
> говорю только, но чувствую. Очень благодарю вас за то, что вы обещали и, вероятно,
> прочли уже Дьякову.²

*(working English)* "[Thank you], dear Aleksandr [Aleksandrovich], for your [efforts about
the drama]. I have just received... it. I am much gladdened by the part you are taking in
the matter of the play, but I am completely, completely indifferent to the results. Whatever
comes out, it is all splendid. I do not just say this — I feel it. Thank you very much for
what you promised and have probably already read to Dyakov."

---

## 6. To M. A. Stakhovich, 4 February 1887 — `v64_019_M_A_Staxovichu` (PSS 64, p. 10)

**Genre:** letter (postcard) · **PSS Tom:** 64 · **Addressee:** M. A. Stakhovich ·
**Significance:** Brief, warm acknowledgement — confirms M. A. Stakhovich (the younger, of
Pal'na, Yelets) is inside the play's circle of readers/promoters alongside A. A. Stakhovich.
Content is thin; included only to fix the addressee in the network.

> Я не посмеялся, а умилился вашим письмом и благодарю вас за него.

*(working English)* "I did not laugh, but was touched by your letter, and thank you for it."

---

## 7. To A. A. Potekhin, 18 February 1887 — `v64_024_A_A_Potexinu` (PSS 64, pp. 13–14)

**Genre:** letter · **PSS Tom:** 64 · **Addressee:** A. A. Potekhin (playwright, theatre
authority) · **Significance:** The hand-off of theatrical authority. Tolstoy disclaims all
competence in stagecraft and gives Potekhin a free hand to cut, recast and alter the play
for production — naming him the best judge of drama "after Ostrovsky." Confirms the chain
Tolstoy set up: he told **Savina** to ask **Potekhin** to make the needed changes.

> Вот на основании этих-то воспоминаний я и написал Савиной, что прошу вас сделать нужные в
> пьесе изменения, если она пойдет, во что я не верил. ... будьте так добры, делайте во всем
> — в изменениях, в назначениях ролей как вы найдете нужным и удобным. Я ничего в
> театральном да и в драматическом деле не смыслю... Полагаю, что в драматическом и
> театральном деле после Островского¹ нет знатока лучше вас.

*(working English)* "It was on the basis of these recollections that I wrote to Savina that
I ask you to make the necessary changes in the play, if it goes on — which I did not believe
it would. ... be so kind as to do everything — in the changes, in the casting — as you find
necessary and convenient. I understand nothing of the theatrical or the dramatic craft... I
suppose that in dramatic and theatrical matters there is no better expert than you after
Ostrovsky."

---

## 8. To N. N. Strakhov, 3 March 1887 — `v64_032_H_N_Straxovu` (PSS 64, p. 23)

**Genre:** letter · **PSS Tom:** 64 · **Addressee:** N. N. Strakhov · **Significance:** The
turn in the work-mood — by March the play has become "my unhappy drama," a regret over the
time it has cost him, and a barbed reflection on his own social class's idle fascination with
it. The strongest evidence of Tolstoy's *retrospective* ambivalence about having published it.

> Про себя скажу, что я последнее время решительно мучим последствиями моей несчастной
> драмы.⁴ Если бы знал, что столько это у меня отнимет времени, ни за что бы не печатал.

*(working English)* "Of myself I will say that lately I am decidedly tormented by the
consequences of my unhappy drama. Had I known how much time it would take from me, I would
never have printed it."

---

## 9. To P. M. Svobodin, 5 March 1887 — `v64_035_P_M_Svobodinu` (PSS 64, pp. 24–25)

**Genre:** letter · **PSS Tom:** 64 · **Addressee:** P. M. Svobodin (actor) ·
**Significance:** A working theatrical document — Tolstoy's detailed direction to the actor
on how to play **Akim** (appearance, the "тае"/"таё" speech tic, gait, the physical
suffering in Act 3, the transfiguration in Act 5). Concrete proof the play was being cast
and prepared for the Petersburg stage despite the looming ban.

> В моем представлении Аким русый, совсем не седой и не плешивый... Говорит с запинкой, и
> вдруг вырываются фразы, и опять запинка и «тае» и «значит». «Тае» я выговариваю «тае».
> ... В 3-м действии при виде безобразия сына он должен физически страдать. ... В 5-м
> действии он должен упираться, гнушаясь видом сватьбы, потом начать понимать, в чем дело,
> потом придти в восторг от поступка сына...

*(working English)* "In my conception Akim is fair-haired, not at all grey or bald... He
speaks haltingly, and phrases suddenly burst out, then again a stumble and 'tae' and
'znachit.' I pronounce 'tae' as 'tae.' ... In Act 3, at the sight of his son's vileness, he
must physically suffer. ... In Act 5 he must resist, loathing the sight of the wedding, then
begin to understand what is happening, then come to rapture at his son's deed..."

---

## 10. To M. G. Savina, 22–31 December 1886 — `v63_609_Savinoj_M_G` (PSS 63, pp. 455–456)

**Genre:** letter · **PSS Tom:** 63 · **Addressee:** M. G. Savina (actress) ·
**Significance:** The manuscript-transmittal letter — Tolstoy *sends Savina the play itself*,
casts her as **Marina**, flags the heavily-revised Act 4 (the passage marked in red pencil),
and pre-authorises any softening the theatre censorship demands **provided Potekhin approves**
— the same hand-off later confirmed in #7. The single most load-bearing staging document of
the whole window: it links Savina (the actress who sought to stage it), the variant Act 4, the
theatre censorship, and Potekhin in one breath.

> Посылаю вам, Марья Гавриловна, свою пьесу.¹ Очень желал бы, чтоб она вам понравилась.
> Боюсь, что она покажется петербургской публике и вам слишком грубою. Четвертый акт с того
> места, где отчеркнуто красным карандашом, много² изменен. ... Все, чтò найдет нужным
> театральная цензура изменить, чтобы смягчить, я на все согласен, если такие изменения
> будут одобрены А. А. Потехиным,³ которому я вполне доверяю. Роль ваша мне представляется
> — Марина.

*(working English)* "I am sending you, Marya Gavrilovna, my play. I should very much like it
to please you. I fear it will seem to the Petersburg public, and to you, too coarse. The
fourth act, from the place marked in red pencil, is much altered. ... Everything the theatre
censorship finds necessary to change, to soften, I agree to it all, provided such changes are
approved by A. A. Potekhin, whom I fully trust. Your role, as I see it, is — Marina."

---

## Bonus context (work-mood, indirect)

### To N. N. Ge (the elder), 14–15 December 1886 — `v63_586_l` (PSS 63, pp. 427–428)

**Genre:** letter · **PSS Tom:** 63 · **Significance:** Two things at once — (a) the
self-understanding/vanity Tolstoy watches in himself when praised for the play, and (b) the
**onset of the censorship**, which he meets with deliberate detachment ("the printing
business has died down from the censorship. They are all blotting things out. I find this is
good"). The censorship attitude here is the counterweight to the "несчастная драма" regret of #8.

> ...как только начнут другие хвалить (как у меня теперь с драмой),³ так сейчас является
> личное желание награды за свой труд и глупое самодовольство: Каков я! Что сделал.
>
> Дело печатания затихло от цензуры.⁶ Все марают. Я нахожу, что это хорошо. Ведь то, что
> насилием ничего нельзя сделать, есть не⁷ фраза, а самая очевидная истина.

*(working English)* "...as soon as others begin to praise (as now with me over the drama),
at once there arises a personal desire for reward for one's labour and a stupid
self-satisfaction: What a fellow I am! What I have done.
The printing business has died down because of the censorship. They blot everything out. I
find this is good. For the fact that nothing can be done by force is no mere phrase but the
most evident truth."

---

## Negative findings (recorded so the dive does not re-chase them)

- **N. V. Davydov, the Tula prosecutor (the Koloskov / Колосков case source):** NOT present
  in a 1886–87 play-window letter in this corpus. The corpus has many N. V. Davydov letters
  but the only ones near the play are `v63_169` (10 Nov 1883) and `v63_373` (May 1885) —
  both *predate* the play and concern unrelated criminal-mercy requests. The string
  `Колоск*` appears **nowhere** in Tom 63/64. ⚠ Note also that `v63_521` is to a *different*
  person — **V. N.** Davydov (Vladimir Nikolaevich), a positivist correspondent — not the
  prosecutor N. V. Davydov; do not conflate. Davydov-as-source belongs to the genesis/memoir
  layer, not the letters.
- **E. M. Feoktistov (Press Affairs directorate — the ban):** the only `Феоктист` hit in
  Tom 63/64 is in `v63_184` (to A. N. Pypin, 10 Jan 1884), unrelated to the play.
- **K. P. Pobedonostsev:** all `Победонос` hits in Tom 63 (`v63_040`, `v63_041`, `v63_042`,
  `v63_044`) are the **1881** letters (the plea to Alexander III and Pobedonostsev to pardon
  the regicides) — they predate the play by five years and are not about it.
- **I. D. Sytin / «Посредник» cheap edition:** the two Sytin letters that surface
  (`v63_576`, 24 Nov 1886; `v64_177`, 1887) are about the **«Посредник» calendar**
  (Календарь с пословицами) and an unrelated job request for N. I. Bunin, respectively —
  NOT the cheap edition of the play. The whole Biryukov calendar thread
  (`v63_573/577/578/579`, `v64_020`) is likewise the *calendar*, not the play. Do not
  conflate the Posrednik calendar with the Posrednik edition of the play.
