---
layer: reference
title: "Late texts — finished English translations"
lastUpdated: 2026-06-12
tags: [research, translation]
---

# Late texts — finished English translations

Finished, checked English for **37 late-Tolstoy passages** — letters, diary entries, and wisdom-anthology prose from 1902–1910 — that have **no published English translation**. They are the cited passages of the [encryption & compression dive](index.md); which late texts are untranslated, and why this matters for an English-language resource, is mapped in the [translation-gap ledger](translation-gaps.md). This file upgrades the dive's **"working English"** cribs into finished renderings — for most of these sentences, the only English that exists anywhere.

**Provenance.** Translated from the Russian of the *Полное собрание сочинений* (Jubilee Edition / PSS) as carried in the dive's extracts. The Russian below is the **byte-locked** text the dive verified (`verify_quotes.py`); the English is the site's own. Register: faithful, plain **British English** that keeps Tolstoy's directness. Editorial insertions are in [square brackets]. Each entry keys to its evidence `id` in `dossier.yaml`, and gives the PSS Tom; where the dive cites a fragment, the full sentence is translated for context.

**How it was made (2026-06-12).** One Opus pass drafted all 37; a second, independent Opus pass checked every rendering against the Russian source (locked-quote fidelity, full-sentence fidelity, accuracy, register). Verdict: **0 must-fix, 2 minor** — both folded in (see [Method](#method)). These are the project's own translations, not a published edition; offered under the open policy, corrections welcome.

## THREAD 1 — the constraint named

*Tolstoy naming, in his own words, what he could not print and why.*

### 1. 1903-05-06 · S. N. Rabinovich (Sholom Aleichem) — PSS Tom 74 (letter) {#key-sholom-aleichem}

**RU** «К сожалению, то, что я имею сказать, а именно, что виновник не только кишиневских ужасов, но всего того разлада, который поселяется в некоторой малой части — и не народной — русского населения — одно правительство. К сожалению, этого-то я не могу сказать в русском легальном издании.»

**EN** Unfortunately, what I have to say — namely, that the one to blame, not only for the Kishinev horrors but for the whole discord that is taking root among a certain small part — and not the common-people's part — of the Russian population, is the government alone. And unfortunately, this is precisely what I cannot say in a legal Russian publication.

<small>*Note.* «одно правительство» is emphatic — "the government, and the government alone"; rendered "the government alone". «поселяется» = settles in / takes root. «не народной» = "not the common-people's part" (Tolstoy exonerates the peasant masses).</small>

### 2. 1907-09-05 · Editorial board of «Час» — PSS Tom 77 (letter) {#con-chas-cant-print}

**RU** «В таком случае нельзя печатать.»

**EN** In that case it must not be printed.

<small>*Note.* «нельзя» here is a flat prohibition, not mere impossibility — "must not" rather than "cannot": if you can only run it with cuts, then don't run it at all.</small>

### 3. 1904-01-14 · diary — PSS Tom 55 (diary) {#con-censored-lit-idle}

**RU** «Какое праздное занятие вся наша подцензурная литература!»

**EN** What an idle pursuit all our censored literature is!

<small>*Note.* «подцензурная» = "subject to the censor"; rendered "censored" for plainness. «праздное» carries both "idle" and "futile" — kept "idle" to echo the play/child image that follows in the entry.</small>

### 4. 1902-08-20 · A. P. Naugolnikov — PSS Tom 73 (letter) {#con-banned-printed-england}

**RU** «Всё, что я думал о жизни и ее законах, я написал в своих сочинениях, запрещенных в России и печатаемых в Англии.»

**EN** Everything I have thought about life and its laws I have set down in my writings, which are banned in Russia and printed in England.

### 5. 1903-12-18 · M. A. Taube — PSS Tom 74 (letter) {#con-two-track-strategy}

**RU** «Для того же, чтобы статья была напечатана и внесла бы тот свет, который она должна внести в сознание людей, я бы предложил следующее: напечатать ее за границей по-русски или по-английски, если не найдется издателя для русского издания.»

**EN** But so that the article may be printed and bring into people's minds the light it ought to bring, I would suggest the following: print it abroad in Russian, or in English if no publisher can be found for a Russian edition.

### 6. 1909-01-11 · F. Tarsakov — PSS Tom 79 (letter) {#con-tarsakov-samizdat}

**RU** «Чтобы показать вам, как трудно теперь провести в печать такое письмо, как ваше, посылаю вам нынче переведенный мною из венской газеты листок, который также нельзя напечатать в России.»

**EN** To show you how hard it is nowadays to get a letter like yours into print, I am sending you today a leaflet I have translated from a Viennese newspaper, which likewise cannot be printed in Russia.

<small>*Note.* The hand-copying workaround sits a sentence earlier in the same letter: «Мы спишем его и будем давать читать» — "We shall copy it out and pass it round to be read."</small>

### 7. 1908-11-13 · N. V. Davydov — PSS Tom 78 (letter) {#con-davydov-uncensorable}

**RU** «Но эти, вероятно, не годятся и по содержанию и по нецензурности.»

**EN** But these would probably not do, both for their content and for their being unpassable by the censor.

<small>*Note.* «нецензурность» = the quality of being unprintable under censorship (not "indecency"); rendered "their being unpassable by the censor" to keep it matter-of-fact, as the dossier flags.</small>

### 8. 1909-03-05 · V. A. Posse — PSS Tom 79 (letter) {#con-gogol-double-bind}

**RU** «Боюсь только, что то, что думаю, и неюбилейно и нецензурно.»

**EN** I only fear that what I think is both unfit for an anniversary and unpassable by the censor.

<small>*Note.* «неюбилейно» — coined to pair with «нецензурно»: not in keeping with the jubilee/anniversary tribute being solicited (the Gogol centenary). Kept the parallel "unfit for an anniversary … unpassable by the censor."</small>

### 9. 1910-02-09 · M. G. Bolkvadze — PSS Tom 81 (letter) {#con-bolkvadze-predict}

**RU** «Боюсь, что всё, что мне придется написать, будет нецензурно.»

**EN** I fear that everything I shall have to write will be unpassable by the censor.

<small>*Note.* Followed in the letter by «Постараюсь, однако, сделать так, чтобы то, что напишу, могло бы быть напечатано» — "I shall try, however, to shape what I write so that it can be printed."</small>

### 10. 1909-07-23 · P. P. Kazmichov — PSS Tom 80 (letter) {#con-kazmichov-full-text}

**RU** «Так что, повторяю, рассказ очень хорош, и желательно, чтобы он получил наибольшее распространение без выпусков.»

**EN** So, I repeat, the story is very good, and it would be desirable for it to reach the widest possible circulation without the cuts.

<small>*Note.* «выпуски» here = the passages deleted by the censor ("cuts"), the same word Tolstoy uses earlier in the letter for what "weakened" the story.</small>

## THREAD 1 — the channel mechanics

*How the writing reached print — the abroad channel through Chertkov, and the posthumous reserve.*

### 11. 1900-12-12 · V. G. Chertkov — PSS Tom 88 (letter) {#chan-rule-only-through-you}

**RU** «Я знаю, как важно для дела и, главное, для вашего спокойствия, чтобы я твердо держался установленного порядка, чтобы за границу все мои писания проникали только через вас, и потому строго держусь и буду держаться этого.»

**EN** I know how important it is for the work, and above all for your peace of mind, that I should hold firmly to the established arrangement — that all my writings reach abroad only through you — and so I keep to it strictly, and shall go on keeping to it.

### 12. 1906-01-14 · Editors of «Новое время» and «Русские ведомости» (public notice) — PSS Tom 76 (letter) {#chan-public-sole-node}

**RU** «Ему одному я посылал и посылаю теперь для печатания за границей по-русски и в переводах все мои новые писания.»

**EN** To him alone I have sent, and still send now, for publication abroad — in Russian and in translation — all my new writings.

### 13. 1905-04-17 · V. G. Chertkov — PSS Tom 89 (letter) {#chan-abroad-rationale}

**RU** «Всё это, вероятно, не пройдет в России, но может быть напечатано за границей.»

**EN** All this will probably not get through in Russia, but it can be printed abroad.

<small>*Note.* «не пройдет» = will not pass [the censor] / get through; said of his prefaces (to Lamennais, Pascal, Chełčický, the Teaching of the Twelve Apostles) and Circle of Reading weekly-reading materials.</small>

### 14. 1906-02-13 · V. G. Chertkov — PSS Tom 89 (letter) {#chan-all-or-nothing}

**RU** «В России никто не печатает, и я поставил conditio sine qua non печатать всю или ничего.»

**EN** In Russia no one will print it, and I have laid down a conditio sine qua non — to print the whole thing or nothing.

<small>*Note.* Latin «conditio sine qua non» left in place (Tolstoy's own); «всю» refers to the article (статья), feminine — "the whole [article]".</small>

### 15. 1904-05-13 · V. G. Chertkov — PSS Tom 88 (letter) {#chan-posthumous-testament}

**RU** «Вас я прошу об этом, потому что знаю вашу большую любовь ко мне и нравственную чуткость, которая укажет вам, что выбросить, что оставить и когда и где и в какой форме издать.»

**EN** I ask this of you because I know your great love for me and your moral discernment, which will show you what to discard, what to keep, and when and where and in what form to publish.

### 16. 1909-02-04 · diary — PSS Tom 57 (diary) {#chan-posthumous-diary}

**RU** «Теперь же после моей смерти я прошу моих наследников отдать землю крестьянам и отдать мои сочинения, не только те, которые отданы мною, но и все, все в общее пользование.»

**EN** Now, after my death, I ask my heirs to give the land to the peasants, and to give my writings — not only those I have already given but all of them, all — into common use.

<small>*Note.* «в общее пользование» = into common/public use, i.e. free of copyright. The repeated «все, все» kept doubled for its emphasis.</small>

### 17. 1909-08-30 · P. A. Stolypin — PSS Tom 80 (letter) {#chan-stolypin-ultimatum}

**RU** «С первого же октября, если в вашей деятельности не будет никакого изменения, письмо это будет напечатано за границей.»

**EN** And from the first of October, if there is no change whatever in your conduct, this letter will be printed abroad.

<small>*Note.* «деятельность» = "conduct/activity" in office — Tolstoy's standing word through the letter for Stolypin's actions as Prime Minister.</small>

### 18. 1905-01-24 · B. I. Knirsha — PSS Tom 75 (letter) {#chan-router-svobodnoe-slovo}

**RU** «В ответ на ваш вопрос я выписываю заключение из небольшой статьи, которую я послал вчера для напечатания в «Свободном слове» за границей.»

**EN** In answer to your question I am copying out the conclusion of a short article that I sent yesterday to be printed in «Svobodnoe Slovo» [Free Word] abroad.

<small>*Note.* «Свободное слово» given transliterated with a gloss, as it names Chertkov's émigré press.</small>

### 19. 1908-06-01 · V. G. Chertkov — PSS Tom 89 (letter) {#chan-nemogu-molchat}

**RU** «Надеюсь, что вы поможете мне поместить это, если возможно, в русских газетах или по крайней мере за границей.»

**EN** I hope you will help me place this, if possible, in the Russian papers, or at least abroad.

<small>*Note.* Genesis of «Не могу молчать» (I Cannot Be Silent), against the 1908 executions.</small>

### 20. 1906-10-02 · diary — PSS Tom 55 (diary) {#chan-herzen-model}

**RU** «Можно и должно бороться уяснением мысли, нельзя у себя — за границей, как Герцен.»

**EN** One can and must fight by making thought clear — and where one cannot do so at home, then abroad, as Herzen did.

<small>*Note.* «у себя» = "at home / in one's own country"; the dash compresses "[and where it is] not [possible] at home — abroad", filled out for readability.</small>

### 21. 1905-09-25 · I. I. Gorbunov-Posadov — PSS Tom 76 (letter) {#chan-gorbunov-recycle-banned}

**RU** «Вообще недурно бы в Чтения выбирать из запрещенных моих, когда нужно заменить.»

**EN** Generally, it would not be a bad idea, when something needs replacing, to draw on my banned works for the Readings.

<small>*Note.* «Чтения» = the [Circle of] Reading anthology; «запрещенных моих» = "my banned [writings]," ellipsis filled with "works."</small>

### 22. 1909-12-19 · N. N. Ge (son) — PSS Tom 80 (letter) {#chan-chertkov-controls-all}

**RU** «Лучше же всего вам снестись об этом с Чертковым, который заведует печатанием всего мною писанного.»

**EN** Best of all would be for you to get in touch about this with Chertkov, who is in charge of the printing of everything I have written.

## THREAD 1 — genre as encryption

*The pull against the disguise: the late distaste for the fictional wrapper.*

### 23. 1908-11-09 · Paul Desjardins — PSS Tom 78 (letter) {#enc-inoskazatelno-rejected}

**RU** «...признаюсь вам, что в мои года, стоя одной ногой в гробу и постоянно созерцая то таинственное au delà, которое тянет к себе, как-то совестно говорить иносказательно: был прекрасный день, Иван Иванович гулял по саду и т. п.»

**EN** ...I confess to you that at my age, with one foot in the grave and forever contemplating that mysterious "au-delà" [the beyond] which draws one to itself, I somehow feel ashamed to speak in allegories: it was a fine day, Ivan Ivanovich was walking in the garden, and so on.

<small>*Note.* «иносказательно» = figuratively / by way of fiction; rendered "in allegories" to catch Tolstoy's disdain for the invented-story wrapper. French «au-delà» (the afterlife/beyond) kept and glossed, as in his own text.</small>

## THREAD 2 — the anthology in his own words

*The wisdom-anthology project — its genesis, purpose, and the mortality pressing it.*

### 24. 1903-04-01 · I. F. Timonov — PSS Tom 74 (letter) {#comp-mysli-announced}

**RU** «Я сделал такой сборник с изречениями на каждый день.»

**EN** I have made just such a collection, with sayings for every day.

<small>*Note.* «изречения» = sayings/maxims; «на каждый день» = for every day — the daily-reading form that names the whole series.</small>

### 25. 1904-01-19 · L. L. Tolstoy (son Lev) — PSS Tom 75 (letter) {#comp-krug-genesis}

**RU** «...и распространяю Мысли мудрых людей. Хочу сделать из них Круг чтения на каждый день.»

**EN** ...and I am circulating Thoughts of Wise People. I want to make of it a Circle of Reading for every day.

<small>*Note.* «из них» refers back to «Мысли мудрых людей» (a plural Russian title); rendered "of it" so the English reads as one book remade into the next. «распространяю» is ambiguous — most naturally "circulating/disseminating" (adopted here); the dive reads it as "enlarging," which the next sentence supports.</small>

### 26. 1904-12-19 · G. A. Rusanov — PSS Tom 75 (letter) {#comp-krug-abroad-uncensored}

**RU** «Я думаю издать полный «Круг чтения» за границей без цензурных соображений.»

**EN** I am thinking of publishing the complete Circle of Reading abroad, without regard for the censor.

<small>*Note.* «без цензурных соображений» = "without censorship considerations" — i.e. without having to weigh what the censor would allow; rendered "without regard for the censor."</small>

### 27. 1909-08-09 · Jan Styka — PSS Tom 80 (letter) {#comp-krug-design-principle}

**RU** «По этой книге, озаглавленной Круг чтения и состоящей из взятых у нескольких сот древних и современных авторов мыслей и изречений о религии и морали, между которыми имеется лишь несколько стихов из евангелия, по этой книге вы сможете судить, как я далек от того, чтобы придавать исключительное значение евангелию.»

**EN** From this book — entitled Circle of Reading and made up of thoughts and sayings on religion and morality taken from several hundred ancient and modern authors, among which there are only a few verses from the Gospel — from this book you will be able to judge how far I am from attaching exceptional importance to the Gospel.

<small>*Note.* Translated from Tolstoy's own Russian rendering of his French; in the French the title is given as «Pour tous les jours» (For Every Day), but the locked Russian span describes Круг чтения, so kept as Circle of Reading.</small>

### 28. 1910-07-20 · M. G. Bolkvadze — PSS Tom 82 (letter) {#comp-put-like-krug}

**RU** «Посылаю вам предисловие к книге «Пути жизни», составленной, как «Круг чтения», из изречений разных мыслителей.»

**EN** I am sending you the preface to the book The Path of Life, compiled — like Circle of Reading — from the sayings of various thinkers.

<small>*Note.* The locked title appears as «Пути жизни» in this letter but the work is Путь жизни (The Path of Life); kept the standard title.</small>

### 29. 1907-11-22 · diary — PSS Tom 56 (diary) {#comp-400-days-obligation}

**RU** «Чем ближе смерть, тем сильнее чувствую обязанность сказать то, что знаю, что через меня говорит Бог.»

**EN** The closer death comes, the more strongly I feel the duty to say what I know — that God speaks through me.

<small>*Note.* «обязанность» = duty/obligation. The "400 days" sit a few lines earlier: составить — исправить 5, 6 изречений в день means «работы больше, чем на год, на 400 дней» — "more than a year's work, four hundred days of it," which he is "almost certain" he will not live to finish.</small>

### 30. 1905-12-16 · diary — PSS Tom 55 (diary) {#comp-truth-simple-form-hard}

**RU** «Часто прямо чувствую, что через меня хочет пройти, требует выражения мне ясная истина, и я все не могу облечь ее в наиболее доступную форму.»

**EN** I often feel directly that a clear truth wants to pass through me, demands expression from me, and still I cannot clothe it in the most accessible form.

<small>*Note.* The truth itself he calls «до глупости простая» a line later — "simple to the point of foolishness"; the whole labour is the form.</small>

### 31. 1909-08-25 · diary — PSS Tom 57 (diary) {#comp-only-what-i-published}

**RU** «...очень прошу моих друзей, собирающих мои записки, письма, записывающих мои слова, не приписывать никакого значения тому, что мною сознательно не отдано в печать.»

**EN** ...I earnestly ask my friends who gather my notes and letters and write down my words to attach no significance to anything I have not consciously given to the press.

<small>*Note.* «сознательно не отдано в печать» = not deliberately released for publication — the authorised, finished text vs the unguarded private word.</small>

### 32. 1906-01-04 · diary — PSS Tom 55 (diary) {#comp-daily-spiritual-practice}

**RU** «Читаю Мысли Мудрых Людей ежедневно и с большой пользой для души.»

**EN** I read Thoughts of Wise People daily, and with great benefit to the soul.

### 33. 1909-03-20 · diary — PSS Tom 57 (diary) {#comp-grand-monde-turn}

**RU** «Всё живее и живее чувствую потребность писать для grand monde, и только для него.»

**EN** More and more keenly I feel the need to write for the "grand monde" [the great world], and for it alone.

<small>*Note.* French «grand monde» kept (Tolstoy's own) and glossed "the great world." In the entry he goes on to call the legend form «превосходно для народа» (excellent for the people); how "grand monde" relates to "the people" here is debatable — the phrase normally denotes high society.</small>

## THREAD 2 — the anthology architecture

*The anthologies themselves — method, the dropped attributions, the compressed doctrine.*

### 34. 1908-03 · Circle of Reading, Preface (PSS 41) — PSS Tom 41 (anthology) {#comp-krug-stated-aim}

**RU** «...так как цель моей книги состоит не в том, чтобы дать точные словесные переводы писателей, а в том, чтобы, воспользовавшись великими, плодотворными мыслями разных писателей, дать большому числу читателей доступный им ежедневный круг чтения, возбуждающего лучшие мысли и чувства.»

**EN** ...for the aim of my book is not to give exact verbal translations of these writers, but, drawing on the great and fruitful thoughts of various writers, to give a large number of readers an accessible daily round of reading that awakens the best thoughts and feelings.

<small>*Note.* «круг чтения» punned with the title — rendered "round of reading" to keep the cyclical (yearly-calendar) sense the title carries.</small>

### 35. 1910 · The Path of Life, note (PSS 45) — PSS Tom 45 (anthology) {#comp-put-drops-attributions}

**RU** «Большинство этих мыслей, как при переводах, так и при переделке, подверглись такому изменению, что я нахожу неудобным подписывать их именами их авторов.»

**EN** The greater part of these thoughts, both in translation and in reworking, have undergone such alteration that I find it awkward to sign them with their authors' names.

<small>*Note.* «неудобным» = "inconvenient/awkward"; here closer to "not right / not fitting" since the texts are no longer faithfully theirs. The next sentence: «Лучшие из этих неподписанных мыслей принадлежат не мне, а величайшим мудрецам мира» — "The best of these unsigned thoughts belong not to me but to the greatest sages of the world."</small>

### 36. 1910 · The Path of Life, preface (PSS 45) — PSS Tom 45 (anthology) {#comp-put-three-superstitions}

**RU** «Суеверия же, оправдывающие грехи и соблазны, суть: суеверие государства, суеверие церкви и суеверие науки.»

**EN** And the superstitions that justify sins and temptations are these: the superstition of the state, the superstition of the church, and the superstition of science.

<small>*Note.* «суеверие» kept as "superstition" (Tolstoy's deliberate, polemical word for a false belief held without reason), repeated three times as in the Russian.</small>

### 37. 1906 · Circle of Reading, weekly «Единение» (PSS 41) — PSS Tom 41 (anthology) {#comp-tat-tvam-asi-schopenhauer}

**RU** «Это познание, выражающееся в санскрите неизменной формулой tat-twam-asi, т. е. «всё это ты», проявляется в виде сострадания, на котором основывается поэтому всякая истинная, т. е. несвоекорыстная добродетель, и реальным выражением которого служит каждый добрый поступок.»

**EN** This knowledge, expressed in Sanskrit by the unchanging formula tat-twam-asi — that is, "all this is you" — shows itself as compassion, on which therefore all true (that is, unselfish) virtue rests, and whose real expression is every good deed.

<small>*Note.* This is Tolstoy's Russian of Schopenhauer; «познание» = "knowledge/cognition/insight" — kept "knowledge." «всё это ты» = "all this is you," the same formula the 1903 parable «Это ты» (This Is You) dramatises.</small>

## Method {#method}

Drafted in one Opus translation pass working from the dossier (`quoteRu` + each row's `extract:` file for full-sentence context), then audited by a separate, independent Opus pass that compared every `RU (locked)` span byte-for-byte against the dossier (all 37 matched), confirmed every full sentence against its extract, and checked each English rendering for accuracy and register. The audit returned **0 must-fix, 2 minor**, both folded into the text above: in **#key-sholom-aleichem**, «поселяется» now reads *"taking root"* rather than *"being sown"* (no unstated agent); in **#comp-krug-genesis**, «распространяю» now reads *"circulating"* rather than *"expanding"* (the more natural sense, with the ambiguity noted). One gloss was also neutralised: **#comp-grand-monde-turn**'s note no longer equates «grand monde» with народ. The working audit files (`_translations-draft.md`, `_translations-verify.md`) are retained in this folder.
