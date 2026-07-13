# Sweep — the four late wisdom-anthologies (the compression endpoint)

Structural read of Tolstoy's late anthology series, 1903 → 1910: the climax of Thread 2
(the compression of his late metaphysics from argument → story → aphorism).

**Method.** Extracted with `extract_tei.py … --choice=reg --notes=auto` (all pre-1918).
For Круг чтения (444 files) I read the preface + a spread of daily entries + 3 weekly
essays + the censorship-dropped-thoughts file — not the whole. For the three single-file
works I extracted the full text and read the preface + table-of-contents structure + a
sampled set of chapters/days. All quoted text is copied from the `.txt` extracts in this
folder, so the Russian is byte-verifiable.

**Files actually read (this step):**
- `v40_069_216_Mysli_mudryh_ljudej_na_kazhdyj_den.txt` (1903, full) + spot-check of
  `…_Novaja_redaktsija.xml` (the later trimmed redaction, read live, not saved)
- `v41_009_009_Krug_chtenija_Predislovie.txt` (preface)
- `v41_011_013_Krug_chtenija_daily_jan_1_1.txt` (opening day)
- `v41_065_069_…_weekly_jan_4_Suschnost_hristianskogo_uchenija.txt`
- `v41_160_161_…_weekly_mar_2_Edinenie.txt`
- `v41_174_175_…_weekly_mar_3_Neprotivlenie_zlu_nasiliem.txt`
- `v42_423_438_Krug_chtenija_Mysli_vypuschennye_tsenzura.txt` (publisher's censored-out thoughts)
- `v43_003_361_Na_kazhdyj_den_Chast_pervaja.txt` (1909, full)
- `v44_003_390_Na_kazhdyj_den_Chast_vtoraja.txt` (1909, full)
- `v45_013_496_Put_zhizni.txt` (1910, full)

(Working-English glosses below are mine, marked "(working English)". They are crib
translations for the parent dive, not finished renderings.)

---

## 1. The architecture of compression — how a unit is built in each anthology

The four books are the same project rebuilt four times, and the *unit* tightens at each
rebuild: from a bouquet of named quotations (1903) → a dated thematic gathering with a
weekly story (1906) → a day organised by one concept in mostly-anonymous numbered
statements (1909) → a fully thematic chapter-book of numbered aphorisms freed from the
calendar (1910).

### A. Мысли мудрых людей на каждый день (1903) — `v40_069_216`
- **Structure:** 12 months (`[head] ЯНВАРЬ` … `ДЕКАБРЬ`), each month split into days
  numbered `1`–`31` (`[head] 1`, `[head] 2`, …). No preface and no afterword in the main
  file — it opens cold on `ЯНВАРЬ / 1` and ends on `ДЕКАБРЬ / 31` (Ruskin + Spencer on the
  limits of knowledge).
- **The unit (one day):** a small bouquet of *attributed* sayings — each saying is followed
  by its author's name on its own line (Эпиктет, Влас Паскаль, Мф. VII, Dhammapada, Талмуд,
  Марк Аврелий, Джон Рёскин, Спенсер…). A day holds anywhere from one item to half a dozen.
  Some days are a single short parable instead (Jan 1 = the St-Francis "perfect joy" story).
- **Voice:** Tolstoy is the *compiler*; his own thoughts appear unsigned, mixed in. This is
  the most "anthology-like" of the four — closest to a commonplace book.
- **The compression is already visible across editions:** the later **Новая редакция**
  (`v40_451_465`, read live) reprints the same days in audibly trimmed form — e.g. the
  Jan-2 Epictetus entry loses whole clauses, and the Jan-3 Pascal entry is cut and gains a
  new closing maxim *«Бессмертно в нашей жизни то лучшее, что есть в нас, наше божественное
  начало любви.»* So the book was being squeezed even within its own life.

### B. Круг чтения (1906) — directory `krug_chtenija/`, Toms 41–42
- **Structure (three nested rhythms):** month → **week** (4–5 weeks per month) → **7 daily
  entries** per week, and each week closes with one or more **«Недельное чтение»** (weekly
  reading) — a longer story or essay. Filenames encode it exactly:
  `…daily_<month>_<week>_<n>.xml` (n = 1…7) and `…weekly_<month>_<week>_<Title>.xml`.
- **The unit (one daily entry):** a date head (`1-е января`), usually an **epigraph / опорная
  мысль** in italics at the top, then a column of *numbered* sayings `1`, `2`, `3`… each
  signed (Эмерсон, Локк, Сенека, Торо, Шопенгауэр…), frequently closing on an **unsigned**
  thought — the unsigned ones are Tolstoy's own. So a day is a *curated chord* of voices
  around one note, not a single maxim.
- **The weekly reading** is where the *story* lives: Tolstoy's own tales («Корней Васильев»,
  «Божеское и человеческое», «Суратская кофейная»), his doctrinal mini-essays («Сущность
  христианского учения», «Непротивление злу насилием», «Единение»), and borrowed fiction
  (Chekhov's «Душечка» with Tolstoy's afterword; Turgenev's «Живые мощи»; Hugo's bishop
  Myriel). This is the **argument-and-story layer still present** inside the anthology.
- **Encryption signature:** a whole file —
  `v42_423_438_…_Mysli_vypuschennye_izdatelem_po_tsenzurnym_soobrazhenijam` — is the set of
  thoughts the *publisher cut for censorship reasons* from the first edition (e.g. the whole
  «19-е января» entry on true vs. external religion). The forbidden material had to be
  routed around the censor; the PSS restores it as a separate appendix.
- **Two prefaces exist:** the short editorial-method «Предисловие» dated **Март 1908 г.**
  (`v41_009_009`, for the 2nd edition) and the famous reading-as-purpose opening of **Jan 1**
  itself, which is a day *about why and how to read* (Emerson, Schopenhauer on bad books).

### C. На каждый день (1906–1910, pub. 1909–10) — `v43_003_361` (ч. 1) + `v44_003_390` (ч. 2)
- **Structure:** organised by calendar day, but now each *day-of-the-month is a fixed theme*
  recurring across all 12 months (the day-number, not the date, carries the topic). ч. 1
  covers Jan–Jun, ч. 2 Jul–Dec. No preface in the body — opens cold on `1 ЯНВАРЯ / 1`.
- **The unit (one day):** a date head (`[head] 1 ЯНВАРЯ.`) then numbered statements
  (`[head] 1.` … `[head] 10.`). Crucially the statements are now **mostly Tolstoy's own,
  unsigned** — only a minority keep an attribution (Лессинг, По Рамакришне, Мат. гл. 22).
  The bouquet of named voices has thinned to a near-monologue. Each day is a tight cluster
  on one concept (Jan 1 = закон Бога / религия; Jan 2 = душа / the unchanging «я»).
- This is the **doctrine-as-day** stage: the metaphysics is now stated directly in short
  numbered prose, the calendar still the spine, the named anthology-voices receding.

### D. Путь жизни (1910) — `v45_013_496`
- **Structure:** the calendar is *gone*. The book is **30 thematic chapters** («главы»,
  `<head type="part">`), each a doctrine: I О ВЕРЕ · II ДУША · **III ОДНА ДУША ВО ВСЕХ** ·
  IV БОГ · V ЛЮБОВЬ · VI ГРЕХИ, СОБЛАЗНЫ, СУЕВЕРИЯ · VII ИЗЛИШЕСТВО · VIII ПОЛОВАЯ ПОХОТЬ ·
  IX ТУНЕЯДСТВО · X КОРЫСТОЛЮБИЕ · XI ГНЕВ · XII ГОРДОСТЬ · XIII НЕРАВЕНСТВО · **XIV НАСИЛИЕ** ·
  XV НАКАЗАНИЕ · XVI ТЩЕСЛАВИЕ · **XVII СУЕВЕРИЕ ГОСУДАРСТВА** · XVIII ЛОЖНАЯ ВЕРА ·
  XIX ЛОЖНАЯ НАУКА · XX УСИЛИЕ · XXI ЖИЗНЬ В НАСТОЯЩЕМ · XXII НЕДЕЛАНИЕ · XXIII СЛОВО ·
  XXIV МЫСЛЬ · XXV САМООТРЕЧЕНИЕ · XXVI СМИРЕНИЕ · XXVII ПРАВДИВОСТЬ · XXVIII ЗЛО ·
  XXIX СМЕРТЬ · XXX ПОСЛЕ СМЕРТИ.
- **The unit (one chapter):** chapter title → a one-paragraph **epigraph defining the theme**
  → Roman-numbered **sub-sections** (each a sub-thesis, e.g. III·I «СОЗНАНИЕ БОЖЕСТВЕННОСТИ
  ДУШИ СОЕДИНЯЕТ ЛЮДЕЙ») → **numbered short statements** `1`, `2`, `3`…, mostly unsigned,
  some signed (Ламенэ, По Шопенгауэру, По Чаннингу, Генри Джордж, Лабоэти).
- **The double preface is the whole system in miniature:** a long numbered **«ПРЕДИСЛОВИЕ»**
  (31 points) that is Tolstoy's *entire late metaphysics compressed to a single page* — душа
  / бог (pts 4–5), the three суеверия государства·церкви·науки (pts 17–19), «Зла нет» (pt 28),
  death dissolved (pts 29–31) — followed by a short **«ПРЕДИСЛОВИЕ к отдельным изданиям»** on
  authorship/anonymity. This is the most aphoristic, most systematic, least calendar-bound,
  and most fully *his-own-voice* of the four. The endpoint of the compression.

**The arc in one line:** named-quotations-by-day (1903) → dated chord + weekly story (1906)
→ themed day in his own numbered prose (1909) → calendar dropped, pure thematic aphorism-book
(1910).

---

## 2. The metaphysics as aphorism — representative passages, by theme

### 2a. Unity of all life · «это ты» / tat tvam asi

**Круг чтения (1906), weekly «Единение» (Schopenhauer, selected by Tolstoy)** — `v41_160_161`
> «Мое истинное внутреннее существо живет во всем живом столь же непосредственно, как в моем
> самосознании оно раскрывается лишь мне самому». Это познание, выражающееся в санскрите
> неизменной формулой tat-twam-asi, т. е. «всё это ты», проявляется в виде сострадания, на
> котором основывается поэтому всякая истинная, т. е. несвоекорыстная добродетель…
> *(Шопенгауэр.)*

*(working English)* "My true inner being lives in everything living just as immediately as,
in my self-consciousness, it discloses itself only to me." This knowledge — expressed in
Sanskrit by the unchanging formula *tat-twam-asi*, i.e. **"all this is you"** — manifests as
compassion, on which therefore rests every true, i.e. unselfish, virtue. *(Schopenhauer.)*
— **This is the single purest statement of the unity doctrine in the whole series, and the
only place the Sanskrit formula itself surfaces.**

**На каждый день (1909), ч. 1** — `v43_003_361` (the same doctrine, now in his own prose)
> Мало сказать, что в каждом человеке такая же душа, как и во мне; в каждом человеке живет
> одно и то же, что и во мне. Все люди отделены друг от друга своими телами, но во всех живет
> один и тот же дух Божий.

*(working English)* It is not enough to say that in each person there is a soul like mine; in
each person lives the very same thing that lives in me. All people are separated from one
another by their bodies, but in all of them lives one and the same spirit of God.

**Путь жизни (1910), ch. III «ОДНА ДУША ВО ВСЕХ» — epigraph** — `v45_013_496`
> Все живые существа телами своими отделены друг от друга, но то, что дает им жизнь — одно и
> то же во всех.

*(working English)* All living beings are separated from one another by their bodies, but
that which gives them life is one and the same in all.

**Путь жизни (1910), ch. III §8 and §13** — `v45_013_496`
> Только тогда человек понимает свою жизнь, когда он в каждом человеке видит себя.
> […]
> Если человек не видит в каждом ближнем тот же дух, который соединяет его со всеми людьми
> мира, он живет, как во сне. Только тот проснулся и живет по-настоящему, кто во всяком
> ближнем видит и себя и бога.

*(working English)* Only then does a person understand his life, when in every person he sees
himself. […] If a person does not see in every neighbour the same spirit that unites him with
all the people of the world, he lives as in a dream. Only he is awake and truly alive who in
every neighbour sees both himself and God.

**The recurring "vessels of water" image** (the unity doctrine as a folk simile) —
in **НКД** and again, near-identical, in **Путь жизни**:
- НКД ч. 1 `v43_003_361`: *«Про разные посуды с водой мы говорим: ведро, бочка, бутылка, ковш,
  но знаем, что вода во всех одна и та же. Так и про тела людей мы говорим: мальчик, девочка,
  женщина, старик, но знаем, что в телах этих то, чтò духовно, во всех одно и то же.»*
- Путь жизни ch. III §7 `v45_013_496`: *«Река не похожа на пруд, и пруд не похож на бочку…
  А и в реке, и в пруду, и в бочке, и в ковше одна и та же вода. Так же и все люди разные, но
  дух, живущий в них, во всех один и тот же.»*

*(working English)* Of different water-vessels we say: bucket, barrel, bottle, dipper — but we
know the water in all is one and the same; just so all people differ, yet the spirit living in
them is one and the same. — **The same maxim, carried forward and re-cut between the two books.**

### 2b. Non-resistance · love

**Мысли мудрых (1903)** — `v40_069_216` — the seed, still as bare scripture + Tao:
> Вы слышали, что сказано: око за око, и зуб за зуб. А я говорю вам: не противься злому. Но
> кто ударит тебя в правую щеку твою, обрати к нему и другую. *(Мф. V, 38—39.)*
> […]
> Тот, кто искусен в пользовании людьми, бывает смирен. Это называется добродетелью
> непротивления. Это называется согласованием с Небом. *(Лао-Тсе.)*

*(working English)* Ye have heard: an eye for an eye, a tooth for a tooth. But I say: resist
not evil; whoever strikes thy right cheek, turn to him the other. (Mt. 5:38–39.) … He who is
skilled in the use of men is humble. This is called the virtue of non-resistance; this is
called accord with Heaven. (Lao-Tzu.)

**Круг чтения (1906), weekly «Непротивление злу насилием» (Ballou, ed. Tolstoy)** — `v41_174_175`
> Поэтому непротивление злу злом есть единственное средство победить зло. Оно убивает злое
> чувство и в том, кто сделал зло, и в том, кто понес его.
> […]
> Непротивление сохраняет, противление разрушает.

*(working English)* Therefore non-resistance to evil by evil is the only means of conquering
evil. It kills the evil feeling both in him who did the evil and in him who bore it. …
**Non-resistance preserves, resistance destroys.**

**На каждый день (1909), ч. 2** — `v44_003_390` (compressed to a definition):
> Учение о непротивлении злу насилием не есть какой-либо новый закон, а есть только указание
> на неправильно допускаемое людьми отступление от закона любви… что всякое допущение насилия
> против ближнего… несовместимо с любовью.

*(working English)* The teaching of non-resistance to evil by force is no new law, but only a
pointing-out of a wrongly-permitted departure from the law of love … that any admission of
force against a neighbour is incompatible with love. — **Non-resistance is now folded *inside*
love, presented as a mere corollary, not a separate commandment.**

**Путь жизни (1910), ch. V «ЛЮБОВЬ» — epigraph** — `v45_013_496`
> Душа человеческая, будучи отделена телом от бога и душ других существ, стремится к
> соединению с тем, от чего она отделена. Соединяется душа с богом всё большим и большим
> сознанием в себе бога, с душами же других существ — всё большим и большим проявлением любви.

*(working English)* The human soul, being separated by the body from God and from the souls of
other beings, strives toward union with that from which it is separated. The soul unites with
God by an ever-greater consciousness of God within itself, and with the souls of other beings
by an ever-greater showing of love.

### 2c. Rejection of church-and-state · government & property

**Путь жизни (1910), «ПРЕДИСЛОВИЕ» pts 17–19 — the three "superstitions" named** — `v45_013_496`
> …Суеверия же, оправдывающие грехи и соблазны, суть: суеверие государства, суеверие церкви и
> суеверие науки. Суеверие государства состоит в вере в то, что необходимо и благотворно, чтобы
> меньшинство праздных людей властвовало над большинством рабочего народа. Суеверие церкви
> состоит в вере в то, что… известные люди, присвоившие себе право учить людей истинной вере,
> находятся в обладании единой, раз навсегда выраженной религиозной этой истины.

*(working English)* The superstitions justifying sins and temptations are: **the superstition
of the state, the superstition of the church, and the superstition of science.** The
superstition of the state consists in the belief that it is necessary and beneficial for a
minority of idle people to rule over the majority of working people. The superstition of the
church consists in the belief that certain people, having arrogated to themselves the right to
teach the true faith, possess the one, once-and-for-all-expressed religious truth.

**Путь жизни (1910), ch. XVII «СУЕВЕРИЕ ГОСУДАРСТВА» §5** — `v45_013_496`
> Только это укоренившееся лжеучение дает безумную, ничем не оправдываемую, власть сотням людей
> над миллионами и лишает истинной свободы эти миллионы… Главная и едва ли не единственная
> причина отсутствия свободы — лжеучение о необходимости государства… при принадлежности людей
> к государству не может быть свободы.

*(working English)* Only this entrenched false teaching gives mad, wholly unjustifiable power
to hundreds of people over millions and deprives those millions of true freedom … The chief
and almost the only cause of the absence of freedom is the false teaching of the necessity of
the state … so long as people belong to a state there can be no freedom. — **The same passage
appears, almost verbatim, three years earlier in НКД ч. 1 (`v43_003_361`), where it reads
"суеверие государства" rather than "лжеучение"** — a clean instance of one paragraph carried
and re-cut across the editions.

**Путь жизни (1910), ch. X «КОРЫСТОЛЮБИЕ» — epigraph + §4 (property)** — `v45_013_496`
> Грех корыстолюбия состоит в приобретении всё большего и большего количества предметов или
> денег, нужных другим людям, и в удержании в своей власти этих предметов или денег для того,
> чтобы пользоваться по своему желанию чужими трудами.
> […]
> Богатые это — грабители, бедные это — ограбленные… в царстве правды, которое он проповедовал,
> богатые и бедные были бы одинаково невозможны. *(Генри Джордж.)*

*(working English)* The sin of acquisitiveness consists in acquiring an ever-greater quantity
of objects or money needed by other people, and in keeping those objects or money in one's
power so as to use the labour of others at will. … The rich are robbers, the poor are the
robbed … in the kingdom of truth that he preached, rich and poor would be alike impossible.
*(Henry George.)*

---

## 3. The prefaces on purpose — what these collections are FOR (in his own voice)

**Круг чтения (1906), «Предисловие» (Март 1908)** — `v41_009_009`
> …выбирая часто отдельные мысли из длинного рассуждения, я должен был, для ясности и цельности
> впечатления, выпускать некоторые слова и предложения и иногда не только заменять одни слова
> другими, но и выражать мысль вполне своими словами, так как **цель моей книги состоит** не в
> том, чтобы дать точные словесные переводы писателей, а **в том, чтобы, воспользовавшись
> великими, плодотворными мыслями разных писателей, дать большому числу читателей доступный им
> ежедневный круг чтения, возбуждающего лучшие мысли и чувства.**

*(working English)* … choosing isolated thoughts out of a long argument, I had, for clarity
and wholeness of impression, to drop some words and sentences and sometimes not only to replace
some words with others but to express the thought wholly in my own words — because **the aim of
my book is** not to give exact verbal translations of writers, but **to use the great, fruitful
thoughts of various writers to give a large number of readers an accessible daily round of
reading that arouses the best thoughts and feelings.** — **This is the compression intent stated
outright: the source text is raw material, deliberately re-cut and re-worded for the daily
reader; fidelity to the original is explicitly subordinated to the daily effect.**

**Круг чтения (1906), Jan 1 (the opening day is itself about reading)** — `v41_011_013`
> Лучше знать немного истинно хорошего и нужного, чем очень много посредственного и ненужного.

*(working English)* Better to know a little that is truly good and needful than a great deal
that is mediocre and needless. — The book's first line is its own rationale: a deliberately
*narrow, repeated, daily* canon over wide reading.

**Путь жизни (1910), «ПРЕДИСЛОВИЕ» pt 1** — `v45_013_496`
> Для того, чтобы человеку хорошо прожить свою жизнь, ему надо знать, что он должен и чего не
> должен делать. Для того, чтобы знать это, ему надо понимать, что такое он сам и тот мир, среди
> которого он живет. Об этом учили во все времена самые мудрые и добрые люди всех народов.
> Учения эти все в самом главном сходятся между собою…

*(working English)* For a person to live his life well, he needs to know what he must and must
not do. To know this, he needs to understand what he himself is and what the world is in which
he lives. The wisest and best people of all nations have taught about this in every age, and
these teachings all agree in the main … — **The purpose is now stated as a single unified
doctrine ("they all agree in the main"), not as a chorus of voices.**

**Путь жизни (1910), «ПРЕДИСЛОВИЕ к отдельным изданиям»** — `v45_013_496`
> Мысли, собранные здесь, принадлежат самым разнообразным авторам… Большинство этих мыслей, как
> при переводах, так и при переделке, подверглись такому изменению, что **я нахожу неудобным
> подписывать их именами их авторов.** Лучшие из этих неподписанных мыслей принадлежат не мне, а
> величайшим мудрецам мира. *(Л. Толстой.)*

*(working English)* The thoughts gathered here belong to the most varied authors … The majority
of these thoughts, both in translation and in reworking, have undergone such alteration that **I
find it inconvenient to sign them with their authors' names.** The best of these unsigned
thoughts belong not to me but to the greatest sages of the world. — **The end-state of the
method: the named voices of 1903 have been re-worked so far into Tolstoy's own diction that he
drops the attributions altogether. The anthology has become his own compressed voice.**

**Мысли мудрых (1903):** the main file carries *no* preface (opens cold on ЯНВАРЬ/1). The
purpose-statement is therefore *absent* at the start of the series and only appears once Tolstoy
begins re-making the book — itself a marker of the arc.

---

## 4. The arc — the series tightening over 1903 → 1910 (his own evidence)

1. **No preface → two prefaces → a one-page system.** 1903 opens cold; by 1906 he adds a method
   preface and a reading-about-reading first day; by 1910 the preface *is* the whole metaphysics
   in 31 numbered points, plus a second note explaining why he has stopped attributing.
2. **Attributions thin out.** 1903: nearly every saying is signed. 1909 НКД: most statements are
   his own and unsigned. 1910 Путь жизни: he says outright he "finds it inconvenient to sign them"
   — the sources have been re-cut into his own diction.
3. **The calendar is dropped.** 1903/1906/1909 are all bound to the day of the year. 1910 abandons
   the calendar for 30 *thematic* chapters — the doctrine itself becomes the table of contents
   (ОДНА ДУША ВО ВСЕХ, НАСИЛИЕ, СУЕВЕРИЕ ГОСУДАРСТВА…).
4. **The story layer recedes.** Круг чтения (1906) still carries weekly *stories and essays*
   (argument + narrative) inside the anthology. By Путь жизни they are gone; only the aphorism
   remains. This is the compression "argument → story → aphorism" visible structurally.
5. **He says he kept improving it.** The 1906 Круг preface: *«…продолжаю испытывать теперь… при
   работе над улучшением ее второго издания»* (`v41_009_009`) — he frames the remaking as
   ongoing improvement, not replacement. The Новая редакция of Мысли мудрых (`v40_451_465`) shows
   the same hand visibly trimming the 1903 entries.
6. **Verbatim carry-over proves it is one squeezed text, not four books.** The «суеверие
   государства» paragraph (НКД ч.1, `v43_003_361`) reappears almost word-for-word as Путь жизни
   ch. XVII §5 (`v45_013_496`) with "суеверие" sharpened to "лжеучение"; the water-vessels unity
   simile passes from НКД into Путь жизни ch. III §7 re-cut. Each book is the previous one
   compressed and re-keyed.

---

## Note on the encryption theme (Thread 1 link)

The compression is not only stylistic — it is also evasive. `v42_423_438` is the file of thoughts
the **publisher cut from the first Круг чтения for censorship reasons** (e.g. the whole «19-е
января» entry on true vs. external religion), restored only in the PSS. The daily-anthology form
let Tolstoy place the church-and-state critique as one unsigned numbered line among foreign sages,
which is exactly the camouflage Thread 1 is tracking — the forbidden statement compressed to a
maxim and hidden in a devotional calendar.
