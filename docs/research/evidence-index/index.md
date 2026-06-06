---
layer: reference
lastUpdated: 2026-06-06
tags: [research]
---

# Cross-dive evidence index

Generated aggregate of every corpus-dive dossier, keyed by entity. It collates the verified primary-source citations already gathered across all dives so wiki ingestion reuses them instead of re-collating by hand. Generated — do not hand-edit; regenerate with `python3 docs/research/lib/build_evidence_index.py`. Writing the wiki pages remains a separate, human-in-the-loop step.

## 1. At a glance

- 14 dives · 132 distinct entities · 281 evidence rows · 153 visuals
- By vault status: 10 exists · 4 stub · 118 missing
- 18 entities recur across ≥2 dives

## 2. Ingestion work-order

Entities not yet written (or only stubbed) that already have verified evidence, ranked by ingestion priority then evidence count. These are ready to write — the citations are collated in §3.

| Entity | Type | Status | Dives | #Ev | Depends on |
|---|---|---|---|---|---|
| Soedinenie i perevod chetyrekh Evangelij | work | missing | fire-metaphor, gospel-translation, lords-prayer | 31 | — |
| Fire of conscience | concept | missing | fire-metaphor | 12 | light-of-reason-свет-разума |
| Kratkoe izlozhenie Evangelija | work | missing | gospel-translation, lords-prayer | 11 | union-and-translation-of-the-four-gospels-соединение-и-перевод-четырёх-евангелий |
| Nikolai Strakhov | person | missing | 1879-1882-a-confession, crisis, gospel-translation, lords-prayer | 11 | lev-tolstoy |
| Nikolai Ge | person | missing | tolstoy-in-art | 9 | — |
| Ilya Repin | person | missing | tolstoy-in-art | 6 | — |
| Jubilee Edition | edition | missing | gospel-translation, jubilee-edition-tei-corpus | 6 | vladimir-chertkov |
| Otche nash (Tolstoy) | concept | missing | lords-prayer | 6 | the-gospel-in-brief-краткое-изложение-евангелия, union-and-translation-of-the-four-gospels-соединение-и-перевод-четырёх-евангелий |
| Tolstoy Digital | institution | missing | jubilee-edition-tei-corpus | 6 | the-jubilee-edition-полное-собрание-сочинений |
| True Christianity (Tolstoy) | concept | missing | christian | 5 | — |
| V chem moja vera | work | missing | fire-metaphor, gospel-translation | 5 | union-and-translation-of-the-four-gospels-соединение-и-перевод-четырёх-евангелий |
| Ivan Kramskoy | person | missing | tolstoy-in-art | 4 | — |
| Light of reason | concept | missing | fire-metaphor | 4 | — |
| Spiritual crisis (perevorot) | concept | missing | 1879-1882-a-confession | 3 | lev-tolstoy |
| Excommunication of Leo Tolstoy | event | missing | christian | 1 | true-vs-church-christianity |
| Sergei Prokudin-Gorsky | person | missing | tolstoy-in-photographs | 1 | leo-tolstoy |
| Confession | work | stub | crisis, fire-metaphor, gospel-translation | 6 | — |
| Na kazhdyj den | work | missing | fire-metaphor | 4 | fire-of-conscience-the-luke-1249-motif, light-of-reason-свет-разума |
| Four Gospels Harmonised and Translated (1895) | edition | missing | gospel-translation | 3 | union-and-translation-of-the-four-gospels-соединение-и-перевод-четырёх-евангелий |
| Paul Eltzbacher | person | missing | christian-anarchism | 3 | leo-tolstoy |
| Put zhizni | work | missing | fire-metaphor | 3 | fire-of-conscience-the-luke-1249-motif |
| Valeria Arsenyeva | person | missing | biryukov-sofia-relationship | 3 | pavel-biryukov, sofia-tolstaya |
| All Tolstoy in One Click | event | missing | jubilee-edition-tei-corpus | 2 | fyokla-tolstaya, the-jubilee-edition-полное-собрание-сочинений |
| Biography of Leo Tolstoy (Biryukov) | criticalWork | missing | biryukov-sofia-relationship | 2 | pavel-biryukov |
| Burning of Arms | event | missing | fire-metaphor | 2 | fire-of-conscience-the-luke-1249-motif |
| Dmitry Khilkov | person | missing | christian | 2 | — |
| Gabriel Sacy | person | missing | christian-anarchism | 2 | christian-anarchism, leo-tolstoy |
| Ilya Ginzburg | person | missing | tolstoy-in-art | 2 | — |
| Nikolai Fedorov | person | missing | 1879-1882-a-confession | 2 | lev-tolstoy |
| O zhizni | work | missing | fire-metaphor | 2 | light-of-reason-свет-разума |
| razumenie | concept | missing | lords-prayer | 2 | — |
| State Tolstoy Museum | institution | missing | copyright-renunciation, jubilee-edition-tei-corpus | 2 | — |
| State Tretyakov Gallery | institution | missing | tolstoy-in-art | 2 | — |
| The Kingdom of God Is Within You | criticalWork | stub | doukhobors, fire-metaphor | 2 | — |
| Varvara Mac-Gahan | person | missing | tolstoyanism | 2 | leo-tolstoy |
| Vasily Sutaev | person | missing | 1879-1882-a-confession | 2 | — |
| Afanasy Fet | person | missing | 1879-1882-a-confession | 1 | — |
| Alexandra Andreyevna Tolstaya | person | missing | 1879-1882-a-confession | 1 | lev-tolstoy |
| Anastasia Bonch-Osmolovskaya | person | missing | jubilee-edition-tei-corpus | 1 | — |
| Dushan Makovicky | person | missing | tolstoyanism | 1 | leo-tolstoy |
| Eugen Heinrich Schmitt | person | missing | christian-anarchism | 1 | christian-anarchism, leo-tolstoy |
| Fyokla Tolstaya | person | missing | jubilee-edition-tei-corpus | 1 | — |
| Issledovanie dogmaticheskogo bogoslovija | work | missing | gospel-translation | 1 | — |
| Leonid Pasternak | person | missing | tolstoy-in-art | 1 | — |
| Mikhail Elpidin | person | missing | 1879-1882-a-confession, gospel-translation | 1 | — |
| Mikhail Stakhovich | person | missing | tolstoyanism | 1 | leo-tolstoy |
| Most Holy Synod | institution | missing | 1879-1882-a-confession | 1 | — |
| Nikolai Orlov (painter) | person | missing | tolstoy-in-art | 1 | — |
| Nikolai Yaroshenko | person | missing | tolstoy-in-art | 1 | — |
| Non-resistance | concept | missing | christian-anarchism | 1 | christian-anarchism |
| Pavel Tretyakov | person | missing | tolstoy-in-art | 1 | — |
| Sergei Levitsky | person | missing | tolstoy-in-photographs | 1 | leo-tolstoy |
| Thomas Tapsell | person | missing | tolstoy-in-photographs | 1 | vladimir-chertkov |
| Constantin von Tischendorf | person | missing | lords-prayer | 2 | — |
| John Coleman Kenworthy | person | missing | christian-anarchism, gospel-translation | 2 | christian-anarchism, the-four-gospels-harmonised-and-translated-brotherhood-/-walter-scott-1895–96 |
| John Van der Veer | person | missing | christian | 2 | — |
| Abrege de l'Evangile | work | missing | lords-prayer | 1 | the-gospel-in-brief-краткое-изложение-евангелия |
| Aleksandr Drankov | person | missing | tolstoy-in-photographs | 1 | leo-tolstoy |
| Boris Orekhov | person | missing | jubilee-edition-tei-corpus | 1 | — |
| Chem ljudi zhivy | work | missing | fire-metaphor | 1 | — |
| Excommunication of Tolstoy | event | missing | gospel-translation | 1 | — |
| Henry George | person | missing | tolstoyanism | 1 | — |
| Higher School of Economics | institution | missing | jubilee-edition-tei-corpus | 1 | tolstoy-digital-/-«слово-толстого» |
| Hodite v svete poka est svet | work | missing | fire-metaphor | 1 | fire-of-conscience-the-luke-1249-motif |
| I. Ivanov | person | missing | tolstoyanism | 1 | leo-tolstoy |
| Ivan Ivakin | person | missing | gospel-translation | 1 | — |
| Ivan Nazhivin | person | missing | christian | 1 | — |
| John Morrison Davidson | person | missing | christian-anarchism | 1 | christian-anarchism |
| Krekshino | place | missing | tolstoy-in-photographs | 1 | — |
| Leeds Russian Archive Chertkov Tapsell fond | archival-fond | missing | tolstoy-in-photographs | 1 | — |
| Marian Zdziechowski | person | missing | christian | 1 | — |
| Mikhail Engelhardt | person | missing | 1879-1882-a-confession | 1 | — |
| Optina Pustyn | place | missing | 1879-1882-a-confession | 1 | — |
| Otets Sergij | work | missing | fire-metaphor | 1 | light-of-reason-свет-разума |
| Pavel Biryukov | person | missing | fire-metaphor | 1 | — |
| Prokudin-Gorsky Collection Library of Congress | archival-fond | missing | tolstoy-in-photographs | 1 | — |
| Rumyantsev Museum | place | missing | 1879-1882-a-confession | 1 | n-f-fedorov |
| Russian State Library | institution | missing | jubilee-edition-tei-corpus | 1 | — |
| Smert Ivana Ilicha | work | missing | fire-metaphor | 1 | — |
| Vasily Alekseev | person | missing | 1879-1882-a-confession | 1 | — |
| Vladimir Molochnikov | person | missing | tolstoy-in-photographs | 1 | leo-tolstoy |
| Vladimir Stasov | person | missing | tolstoy-in-art | 1 | — |
| Tolstoys religious conversion | concept | missing | crisis | 3 | — |
| Doukhobor Emigration to Canada | event | missing | doukhobors | 2 | — |
| Doukhobors | concept | missing | doukhobors | 2 | — |
| Ivan Tregubov | person | missing | doukhobors | 2 | — |
| Nicholas II | person | missing | doukhobors | 2 | — |
| Pyotr Verigin | person | missing | doukhobors | 2 | — |
| Dmitri Khilkov | person | missing | doukhobors | 1 | — |
| Grigory Golitsyn | person | missing | doukhobors | 1 | — |
| Help (Pomogite) | criticalWork | missing | doukhobors | 1 | — |
| Leonila Annenkova | person | missing | crisis | 1 | — |
| The Burning of Arms | event | missing | doukhobors | 1 | — |
| What I Believe | work | missing | crisis | 1 | — |

30 entities are named across the dives but carry no evidence rows yet (research gaps, not ready to ingest): ABBYY, Aksinya Bazykina, Alexandra Tolstaya, Astapovo, Aylmer Maude, Ernest Howard Crosby, Felix Ortt, Ivan Turgenev, Jan Styka, Karl Bulla, Konstantin Pobedonostsev, Leo Wiener, Leonid Urusov, Leopold Sulerzhitsky, Mikhail Nesterov, Naum Aronson, Nikolai Gudzy, Nikolai Gusev, Paolo Trubetskoy, Peredvizhniki, Resurrection, Russkaya Mysl (journal), Sergei Tolstoy, Sergei Yuryev, Society of Friends, State Museum of Leo Tolstoy, State Russian Museum, Tatyana Tolstaya, TsGAKFFD Bulla collection, Valentin Serov.

## 3. Collated citations, by entity

### Abrege de l'Evangile

work · missing · dives: lords-prayer

_lords-prayer_: Tolstoy's own French condensation; carries Version D — the prayer as anti-petitionary section-headings. Cross-linked by the fire-metaphor dive too.

> La prière ne peut pas consister dans les demandes que nous faisons à Dieu. Notre Père connaît tous nos besoins avant même que nous ne les ayons formulés.
> Prayer cannot consist in the requests we make to God. Our Father knows all our needs even before we have formulated them. (working English, from Tolstoy's French — Abrégé de l'Évangile)
> — PSS Tom 24, pp. 941–969 · lords-prayer · 1881-1883

### Afanasy Fet

person · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: Poet and neighbour; correspondent and pessimist foil during the crisis.

> Я очень занят. Из занятия моего ничего не выйдет, кроме моего удовлетворения, но все-таки очень занят.
> (working English) I am very busy. Nothing will come of my occupation except my own satisfaction, but I am very busy all the same.
> — PSS Tom 62, pp. 503–504 · 1879-1882-a-confession · 1879-11-22 (OS)

Visuals: 1 (1 usable) — A. A. Fet (Repin, 1882) [PD]

### Aleksandr Drankov

person · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: filmed Tolstoy's 80th jubilee (1908) with a hidden camera after being refused; early newsreel pioneer

> Неприятно и то, что вызывает сознание себя не божественного, а пакостного Льва Николаевича.
> Unpleasant, too, in that it arouses the consciousness of oneself as not the divine but the vile Lev Nikolaevich. (working English)
> — PSS Tom 57, pp. 141–142 · tolstoy-in-photographs · 1909-09-17

Visuals: 1 (0 usable) — Drankov's 1908 hidden-camera jubilee footage; Pathé/Mundviller 1909 station departure; the 1910 death-and-funeral newsreels [unknown]

### Alexandra Andreyevna Tolstaya

person · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: Lady-in-waiting and Orthodox interlocutor; the believer Tolstoy argued his new faith against; recipient of two key (unsent) confessional letters.

> Обличаемые спрятались за цензуру и штыки
> (working English) Those exposed have hidden behind censorship and bayonets.
> — PSS Tom 63, pp. 90–91 · 1879-1882-a-confession · 1882-03-03 (OS, unsent)

### All Tolstoy in One Click

event · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: 2013–2014 crowdsourced OCR+proofreading of the 90 volumes (ABBYY FineReader; ~3,249 volunteers, 49 countries; 46,820 pages); produced the free e-texts on tolstoy.ru

> Публикуемые документы был получены с сайта tolstoy.ru в формате html, переведены в формат TEI. Исправлены некоторые ошибки распознавания. Тексты, написанные в дореформенной орфографии, сопоставлены с их версиями в современной орфографии.
> The published documents were obtained from the site tolstoy.ru in html format and converted to TEI. Some recognition (OCR) errors were corrected. Texts written in pre-reform orthography were collated with their modern-orthography versions. (working English)
> — jubilee-edition-tei-corpus

> Подготовлено на основе электронной копии 53-го тома Полного собрания сочинений Л. Н. Толстого, предоставленной Российской государственной библиотекой
> Prepared on the basis of an electronic copy of volume 53 of the Complete Collected Works of L. N. Tolstoy, provided by the Russian State Library. (working English)
> — PSS Tom 53 · jubilee-edition-tei-corpus

### Anastasia Bonch-Osmolovskaya

person · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: HSE linguist; co-founder/lead of Tolstoy Digital; principal author of the 'Tolstoy semanticized' (2019) methodology

> Анастасия Бонч-Осмоловская, Фёкла Толстая, Борис Орехов, Тимофей Лукашевский
> Anastasia Bonch-Osmolovskaya, Fyokla Tolstaya, Boris Orekhov, Timofey Lukashevsky (under "Idea, task-setting, leadership"). (working English)
> — jubilee-edition-tei-corpus

### Bethink Yourselves!

work · exists · dives: fire-metaphor

_fire-metaphor_: The 1904 anti-war essay closing on the Luke 12:49 keystone the user cited

> Чего желал Христос, совершается. Огонь возгорается. Не будем же противиться, а будем служить ему.
> What Christ wished for is coming to pass. The fire is blazing up. Let us then not resist it, but serve it. (working English)
> — PSS Tom 36, pp. 100–148 · fire-metaphor · 1904

> Христос, тогда еще, в свое время томился ожиданием и говорил: «Огонь пришел низвесть я на землю, и как желал бы, чтобы он возгорелся». (Лука XII, 49.)
> Christ, even then, in his time, was in anguish of expectation and said: "Fire I came to cast upon the earth, and how I would wish that it were kindled." (Luke XII, 49.) (working English)
> — PSS Tom 36, pp. 100–148 · fire-metaphor · 1904

> это искра того огня, который Христос низвел на землю и который начинает возгораться.
> this is a spark of that fire which Christ brought down to the earth and which is beginning to blaze up. (working English)
> — PSS Tom 36, pp. 100–148 · fire-metaphor · 1904

### Biography of Leo Tolstoy (Biryukov)

criticalWork · missing · dives: biryukov-sofia-relationship

_biryukov-sofia-relationship_: The four-volume authorized biography; Vol II (1908) carries the dedication; editions settled in the biryukov-biography-editions dive

> Ni har ock afvärjt mycken ofärd från hans hufvud.
> You have also averted much misfortune from his head. (working English) — source language Swedish.
> — Vol II front matter · biryukov-sofia-relationship · 1908-01-11

> S. A. Tolstojs arkiv.
> The archive of S. A. Tolstaya. (working English) — footnote sourcing the volume's closing quotation; documentary sign of Sofia's cooperation.
> — Vol II p. 453 · biryukov-sofia-relationship · 1908-08-27

Visuals: 4 (4 usable) — Biryukov biography Tom 1, 1911 Moscow (Kushnerov) cover [PD], Biryukov biography Tom 1, 1921 Berlin (Ladyzhnikov) cover [PD], Tolstoy youth (1848), biography plate [PD], The four Tolstoy brothers, biography plate [PD]

### Boris Orekhov

person · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: HSE; technology lead of Tolstoy Digital; author of the '91st volume' (2020) paper on index.tolstoy.ru

> Анастасия Бонч-Осмоловская, Фёкла Толстая, Борис Орехов, Тимофей Лукашевский
> Anastasia Bonch-Osmolovskaya, Fyokla Tolstaya, Boris Orekhov, Timofey Lukashevsky (under "Idea, task-setting, leadership"). (working English)
> — jubilee-edition-tei-corpus

### Burning of Arms

event · missing · dives: fire-metaphor

_fire-metaphor_: The literal fire that became the emblem of conscientious refusal Tolstoy championed; the metaphor made historical fact

> это искра того огня, который Христос низвел на землю и который начинает возгораться.
> this is a spark of that fire which Christ brought down to the earth and which is beginning to blaze up. (working English)
> — PSS Tom 36, pp. 100–148 · fire-metaphor · 1904

> это искра того огня, который Христос низвел на землю и который начинает возгораться.
> this is a spark of that fire which Christ brought down to the earth and which is beginning to blaze up. (working English)
> — PSS Tom 88, pp. 718 · fire-metaphor · 1904-05-08

Visuals: 1 (0 usable) — The Doukhobor Burning of Arms, 1895 (the literal fire of conscientious refusal) [unknown]

### Chem ljudi zhivy

work · missing · dives: fire-metaphor

_fire-metaphor_: Folk-tale: the angel emits divine light when he understands («от Михайлы свет идет»)

> И видят хозяева, что от Михайлы свет идет.
> And the masters see that light comes from Mikhaila. (working English)
> — PSS Tom 25, pp. 7–25 · fire-metaphor · 1881

### Christian Anarchism

concept · exists · dives: christian-anarchism

_christian-anarchism_: The central concept. The vault page (recordStatus: draft) carries a <!-- NEEDS PRIMARY SOURCE --> block for exactly Tolstoy's rejection of the political label — which the Eltzbacher letter here anchors — and lacks the unique Sacy self-attestation and the phrase-genealogy this dive supplies.

> Ответ не может быть дан на вопрос, потому что он дурно поставлен. Вопрос не в том — устроить государство: по нынешнему, или по новому. Я и никто из нас не приставлен к решению этого вопроса.
> The answer cannot be given to the question, because it is badly posed. The question is not whether to arrange the state in the present way or in a new way. Neither I nor any of us is appointed to the solving of that question. (working English)
> — PSS Tom 52, pp. 138–140 · christian-anarchism · 1894-09-10

> социалистическая, коммунистическая и анархическая теории приводятся в подкрепление христианской истины, которая составляет ее главную часть.
> the socialist, communist and anarchist theories are brought in to corroborate the Christian truth, which forms its chief part. (working English)
> — PSS Tom 67, pp. 178–180 · christian-anarchism · 1894-07-23

> Мне кажется только, что я не анархист в смысле политического реформатора. В оглавлении вашей книги под словом «насилие» сделаны указания на разные страницы из других сочинений, но ни одной ссылки на мои. Не доказательство ли это того, что то учение, которое вы мне приписываете и которое, в сущности, есть не что иное, как учение Христа, вовсе не политическое, а религиозное учение?
> It seems to me only that I am not an anarchist in the sense of a political reformer. In the index of your book under the word 'violence' references are made to various pages of the other writers, but not one to mine. Is this not proof that the teaching which you ascribe to me, and which is, in essence, nothing other than the teaching of Christ, is not a political but a religious teaching? (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

> я все-таки думаю, что бабизм, как нравственное и гуманитарное учение, имеет большое будущее в восточном мире. Имея много общего с христианским анархизмом, он должен рано или поздно с ним слиться.
> I still think that Babism, as a moral and humanitarian doctrine, has a great future in the eastern world. Having much in common with Christian anarchism, it must sooner or later merge with it. (working English)
> — PSS Tom 73, pp. 109–110 · christian-anarchism · 1901-07-28

### Confession

work · stub · dives: crisis, fire-metaphor, gospel-translation · names: A Confession (Исповедь) / Confession (Исповедь)

_crisis_: the keystone text; the dive's central vocabulary (переворот, остановка жизни) lives here
_fire-metaphor_: The light of reason in autobiographical form; the crisis source
_gospel-translation_: Project part 1 — the autobiographical account of the crisis; the translator's note calls it 'an introduction to the present work'

> Так я жил, но пять лет тому назад со мною стало случаться что-то очень странное: на меня стали находить минуты сначала недоумения, остановки жизни, как будто я не знал, как мне жить, что мне делать, и я терялся и впадал в уныние. […] Эти остановки жизни выражались всегда одинаковыми вопросами: Зачем? Ну, а потом?
> So I lived, but five years ago something very strange began to happen to me: at first there came over me moments of bewilderment, of life coming to a stop, as though I did not know how to live or what to do, and I lost my footing and fell into dejection. […] These stoppages of life always expressed themselves in the same questions: Why? And then what? (working English)
> — PSS Tom 23, pp. 10 · TEI v23_001_059_Ispoved · crisis · 1882

> Я жил так года два, и со мной случился переворот, который давно готовился во мне и задатки которого всегда были во мне. Со мной случилось то, что жизнь нашего круга — богатых, ученых — не только опротивела мне, но потеряла всякий смысл.
> I lived like that for a couple of years, and there occurred in me an upheaval [переворот] that had long been preparing within me, and whose seeds had always been in me. What happened to me was that the life of our circle — the rich, the learned — not only grew repugnant to me, but lost all meaning. (working English)
> — PSS Tom 23, pp. 40 · TEI v23_001_059_Ispoved · crisis · 1882

> И я спасся от самоубийства. Когда и как совершился во мне этот переворот, я не мог бы сказать. […] так же постепенно, незаметно возвратилась ко мне эта сила жизни. И странно, что та сила жизни, которая возвратилась ко мне, была не новая, а самая старая, — та самая, которая влекла меня на первых порах моей жизни.
> And I was saved from suicide. When and how this upheaval [переворот] took place in me, I could not say. […] just as gradually, imperceptibly, the force of life returned to me. And it is strange that the force of life which returned to me was not a new one, but the very oldest — the same that had drawn me in the first days of my life. (working English)
> — PSS Tom 23, pp. 46 · TEI v23_001_059_Ispoved · crisis · 1882

> что люди более возлюбили тьму, нежели свет, потому что дела их были злы. Ибо всякий, делающий худые дела, ненавидит свет и не идет к свету, чтобы не обличились дела его.
> that people loved the darkness more than the light, because their deeds were evil. For everyone who does wicked deeds hates the light and does not come to the light, lest his deeds be exposed. (working English)
> — PSS Tom 23, pp. 1–59 · fire-metaphor · 1882

> И перед светом разума всё прежнее объяснение разлетелось прахом.
> And before the light of reason all the former explanation scattered to dust. (working English)
> — PSS Tom 23, pp. 1–59 · fire-metaphor · 1882

> Я был приведен к христианству не богословскими, не историческими исследованиями, а тем, что пятидесяти лет от роду [...] я пришел в отчаяние и хотел убить себя [...] И я стал изучать христианство
> I was brought to Christianity not by theological or historical investigations, but by the fact that, at fifty years of age […] I fell into despair and wanted to kill myself […] And I began to study Christianity. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

### Constantin von Tischendorf

person · missing · dives: lords-prayer

_lords-prayer_: His critical Greek New Testament is the text Tolstoy worked from and cites by name in the Luke footnote; Strakhov sent it to him in 1880.

> слова: да сойдет дух твой в нас и очистит нас встречаются в цитатах древних церковных писателей.
> the words 'may thy spirit descend into us and cleanse us' are found in citations of ancient church writers. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Очень благодарен вам за Тишендорфское евангелие.
> I am very grateful to you for the Tischendorf gospel. (working English)
> — PSS Tom 63, pp. 21–22 · lords-prayer · 1880-09-01

### Dmitri Khilkov

person · missing · dives: doukhobors

_doukhobors_: Exiled prince whose reports first brought the atrocity news to Tolstoy; the named eyewitness source of the 1895 open letter.

> После этого, 28 июня 1895 года, духоборцы, живущие в Ахалкалакском уезде Тифлисской губернии, снесли в одну кучу в поле, около села Спасского, всё свое имевшееся у них оружие и, обложив его дровами и углем и облив керосином, сожгли
> After this, on 28 June 1895, the Doukhobors living in the Akhalkalaki district of the Tiflis province carried all the weapons they had into a single heap in a field near the village of Spasskoye and, having piled wood and coal upon them and doused them with kerosene, burned them. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

### Dmitry Khilkov

person · missing · dives: christian

_christian_: Correspondent (former officer, Tolstoyan) to whom Tolstoy explains one cannot 'be' a Christian

> И потому христианином нельзя быть так же, как можно быть евреем, магометанином, церковником. Нельзя сказать про себя или про другого, что я или он христианин, потому что нет таких поступков, которыми бы я себя отличил от других как христианин. Еврей обрезался, соблюл субботу, магометанин помолился 5 раз, отдал десятину бедным, церковник окрестился, поговел; но христианину нечего такого сделать.
> And so one cannot BE a Christian the way one can be a Jew, a Mohammedan, a churchman. One cannot say of oneself or of another that I or he is a Christian, because there are no acts by which I might mark myself off from others as a Christian. (working English)
> — PSS Tom 65, pp. 76–78 · christian · 1890-04-09

> Но и тут нельзя про себя сказать, что я христианин больше, чем не христианин, — татарин, поп и т. п. Как сказал какой-то писатель, «душа человека христианка».
> But even here one cannot say of oneself that I am more a Christian than a non-Christian — a Tatar, a priest, and so on. As some writer said, 'the soul of man is a Christian.' (working English)
> — PSS Tom 65, pp. 76–78 · christian · 1890-04-09

### Doukhobor Emigration to Canada

event · missing · dives: doukhobors

_doukhobors_: The 1898–99 exodus of ~7,400 to Saskatchewan/Assiniboia via Cyprus and Batum on the Lake Huron and Lake Superior.

> Но нынешнее русское правительство употребило против духоборов еще третий, казалось бы оставленный в наше время, выход из этого противоречия. Оно, кроме того, что подвергает самым тяжелым страданиям самих отказывающихся, заставляет еще систематически страдать отцов, матерей, детей отказывающихся, вероятно с тем, чтобы пытками этих невинных семей поколебать решимость несогласных их членов.
> But the present Russian government has used against the Doukhobors a third way out of this contradiction, one seemingly abandoned in our time. Besides subjecting the refusers themselves to the heaviest sufferings, it forces the fathers, mothers, and children of the refusers to suffer systematically as well — probably so as to shake the resolve of the dissenting members by the torture of these innocent families. (working English)
> — PSS Tom 71, pp. 322–327 · doukhobors · 1898-03-19

> И потому, если мы не можем исполнять того, без чего нас нельзя терпеть в государстве, мы просим одно: отпустите нас.
> And so, if we cannot fulfil that without which we cannot be tolerated in the state, we ask one thing only: let us go. (working English)
> — PSS Tom 71, pp. 345–348 · doukhobors · 1898-04-02

Visuals: 9 (4 usable) — Doukhobor camp before arriving at Yorkton, 1899 [CC0], Athalassa farm, Cyprus — the temporary Doukhobor camp, 1898–99 [unknown], Pier at Grosse Île quarantine station, Quebec, where Doukhobors disembarked, 1899 [PD], Geographic movements of the Doukhobors in western Canada, 1898–1913 [PD], Immigration buildings by the railway, Quebec City, c.1899 [PD], Doukhobors travelling by rail to western Canada, 1899 [unknown], Doukhobors on the deck of SS Lake Huron, 1899 [unknown], SS Lake Huron, the Beaver Line steamer that carried Doukhobors from Batum, Dec 1898 [unknown], SS Lake Superior, the Beaver Line steamer that carried Doukhobors from Batum, Apr 1899 [unknown]

### Doukhobors

concept · missing · dives: doukhobors

_doukhobors_: The pacifist Christian sect at the centre of the affair; ~20,000 in the Transcaucasus, ~7,400 emigrated to Canada in 1899.

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

> С духоборцами случилось то, что обыкновенно случается с замыкающимися в самих себя и вследствие того процветающими религиозными общинами: материальное благосостояние их увеличивается, но религиозное сознание понижается.
> What happened with the Doukhobors is what usually happens with religious communities that close in upon themselves and prosper as a result: their material well-being increases, but their religious consciousness declines. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

Visuals: 7 (7 usable) — Sketch of the Doukhobor village Gorelovka, Tiflis province, 1893 [PD], Sirotski Dom (Orphan's House), Doukhobor spiritual complex, Gorelovka, Georgia (building of 1847) [PD], Doukhobor women in the Caucasus, 1887 (travelogue engraving) [PD], Doukhobor pilgrims at prayer near Yorkton, 1902 [PD], Doukhobor village of Vosnesenya, Thunder Hill Colony, c.1900 [PD], Doukhobor women pulling a plough, Thunder Hill Colony, c.1899 (the iconic image) [PD], Doukhobor women winnowing grain, Saskatchewan, 1899 [PD]

### Dushan Makovicky

person · missing · dives: tolstoyanism

_tolstoyanism_: Slovak doctor and disciple; his 1897 question (how to act as Tolstoy's 'representative in Hungary') is the occasion of the keystone denial. Personal physician at Yasnaya Polyana from 1904; the only doctor at Tolstoy's deathbed (Astapovo, 1910); compiler of the Yasnopolianskie zapiski.

> Я рад был случаю сказать ему и уяснить себе, что говорить о толстовстве, искать моего руководительства, спрашивать моего решения вопросов — большая и грубая ошибка. — Никакого толстовства и моего учения не было и нет, есть одно вечное, всеобщее, всемирное учение истины, для меня, для нас особенно ясно выраженное в евангелиях.
> I was glad of the chance to tell him, and to clarify for myself, that to speak of Tolstoyism, to seek my guidance, to ask me to decide questions — is a great and crude error. There was and is no Tolstoyism and no teaching of mine; there is one eternal, universal, world-wide teaching of truth, which for me, for us, is especially clearly expressed in the Gospels. (working English)
> — PSS Tom 53, pp. 167–169 · tolstoyanism · 1897-12-02

### Eugen Heinrich Schmitt

person · missing · dives: christian-anarchism

_christian-anarchism_: Hungarian philosopher (1851–1916), editor of the Religion des Geistes circle in Budapest; a principal node of the foreign Christian-anarchist correspondence. Addressee of the 1895 'God's work' letter.

> Ваше дело, наше дело, т. е. божье дело, у вас делает успехи.
> Your work, our work, that is, God's work, is making progress with you. (working English)
> — PSS Tom 68, pp. 26–28 · christian-anarchism · 1895-02-01

Visuals: 1 (1 usable) — Eugen Heinrich Schmitt (Jenő Schmitt), portrait [PD]

### Excommunication of Leo Tolstoy

event · missing · dives: christian

_christian_: The Synod edict of 20–22 Feb 1901 and Tolstoy's public Reply (Tom 34) — the capstone of the self-attestation question

> То, что я отрекся от церкви, называющей себя православной, это совершенно справедливо. Но отрекся я от нее не потому, что я восстал на господа, а напротив, только потому, что всеми силами души желал служить ему.
> That I have renounced the church that calls itself Orthodox is perfectly true. But I renounced it not because I rose up against the Lord, but, on the contrary, only because with all the strength of my soul I wished to serve him. (working English)
> — PSS Tom 34, pp. 245–253 · christian · 1901-04-04

### Excommunication of Tolstoy

event · missing · dives: gospel-translation

_gospel-translation_: The Holy Synod's 1901 decree — the institutional bookend of the religious project the gospel translation began

> В православном вероучении я нашел изложение самых непонятных, кощунственных и безнравственных положений, не только не допускаемых разумом, но совершенно непостижимых и противных нравственности, и — никакого учения о жизни и о смысле ее.
> In the Orthodox creed I found an exposition of the most incomprehensible, blasphemous and immoral propositions — not only inadmissible to reason but utterly incomprehensible and contrary to morality — and no teaching whatever about life or its meaning. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

### Fire of conscience

concept · missing · dives: fire-metaphor

_fire-metaphor_: The unifying fire metaphor: Christ's fire as the kindling, contagious, unquenchable conscience

> Но мир горит уж 1800 лет, горит с тех пор, как Христос сказал: я огонь низвел на землю; и как томлюсь, пока он не разгорится, — и будет гореть, пока не спасутся люди.
> But the world has been burning for 1800 years now, burning ever since Christ said: I brought fire down to the earth; and how I am in anguish until it blazes up — and it will burn until people are saved. (working English)
> — PSS Tom 23, pp. 304–465 · fire-metaphor · 1884

> что этот талант есть огонь, который только тогда огонь, когда он жжет. Я верю, что я — Ниневия по отношению к другим Ионам, от которых я узнал и узнаю истину, но что и я Иона по отношению к другим ниневитянам, которым я должен передать истину.
> that this talent is a fire which is only a fire when it burns. I believe that I am a Nineveh in relation to other Jonahs, from whom I have learned and learn the truth, but that I too am a Jonah in relation to other Ninevites, to whom I must pass the truth on. (working English)
> — PSS Tom 23, pp. 461 · fire-metaphor · 1884

> Я пришел сбросить огонь на землю. И как желаю, чтобы он разгорелся.
> I came to cast fire upon the earth. And how I wish that it would blaze up. (working English)
> — PSS Tom 24, pp. 292 · fire-metaphor · 1880-1881

> он знал, что его учение — не учение, но искра, которая зажигает сознание Бога в сердцах людей и, раз загоревшись, не может потухнуть.
> he knew that his teaching was not a doctrine but a spark that kindles the consciousness of God in people's hearts and, once lit, cannot go out. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> «Огонь принес я на землю, — сказал Христос, — и как томлюсь, когда он возгорится».
> "Fire I brought to the earth," said Christ, "and how I am in anguish for it to blaze up." (working English)
> — PSS Tom 28, pp. 1–293 · fire-metaphor · 1893

> Чего желал Христос, совершается. Огонь возгорается. Не будем же противиться, а будем служить ему.
> What Christ wished for is coming to pass. The fire is blazing up. Let us then not resist it, but serve it. (working English)
> — PSS Tom 36, pp. 100–148 · fire-metaphor · 1904

> Христос, тогда еще, в свое время томился ожиданием и говорил: «Огонь пришел низвесть я на землю, и как желал бы, чтобы он возгорелся». (Лука XII, 49.)
> Christ, even then, in his time, was in anguish of expectation and said: "Fire I came to cast upon the earth, and how I would wish that it were kindled." (Luke XII, 49.) (working English)
> — PSS Tom 36, pp. 100–148 · fire-metaphor · 1904

> «Огонь пришел я низвесть на землю: и как желал бы, чтобы он уже возгорелся» (Луки XII, 49). Но почему же огонь этот так медленно разгорается?
> "Fire I came to cast upon the earth: and how I would wish that it were already kindled" (Luke XII, 49). But why does this fire blaze up so slowly? (working English)
> — PSS Tom 45, pp. 13–496 · fire-metaphor · 1910

> Мир зажжен Христом и горит. Если каждый из нас сознает то, что он горит, не препятствует, а радуется и содействует своему горению, то это всё, что нужно.
> The world is set alight by Christ and is burning. If each of us is conscious that he is burning, does not hinder it, but rejoices and assists his own burning, then that is all that is needed. (working English)
> — PSS Tom 64, pp. 387 · fire-metaphor · 1889-06-18

> Я думаю, что время это пришло, и что мир уже горит, и дело наше только в том, чтоб гореть и, по возможности, соединяться с другими горящими точками, и это я намерен делать весь остаток моей жизни.
> I think that this time has come, and that the world is already burning, and that our task is only to burn and, as far as possible, to unite with other burning points — and this I intend to do for the whole remainder of my life. (working English)
> — PSS Tom 64, pp. 391 · fire-metaphor · 1889-06-22

> Огонь принес я на землю, сказал Христос, и он разгорается и в нас и в наших плотских и духовных детях; только бы нам тихо сгореть в нем, а что он зажигает других, это не может быть иначе.
> Fire I brought to the earth, said Christ, and it is blazing up both in us and in our children of flesh and of spirit; only let us quietly burn up in it — and that it sets others alight, this cannot be otherwise. (working English)
> — PSS Tom 70, pp. 30 · fire-metaphor · 1897-02-22

> Наше дело только в том, чтобы в себе разжечь огонь: гореть самому, и тогда окружающие нас сами собой будут согреваться и зажигаться.
> Our task is only to kindle the fire in ourselves: to burn oneself, and then those around us will of their own accord be warmed and set alight. (working English)
> — PSS Tom 75, pp. 90 · fire-metaphor · 1904-04-15

### Four Gospels Harmonised and Translated (1895)

edition · missing · dives: gospel-translation

_gospel-translation_: The first English translation of the harmony — anonymous, from the Geneva text, authorized by Tolstoy's imprimatur; Parts I–II only, Part III never published

> The right of translation I freely accord, without exception, to everyone who would like to undertake the trouble of translating. But being eager to have my ideas spread, I also wish them to be correctly interpreted.
> — gospel-translation · 1894-08-30

> I hereby certify that this rendering of my work, The Four Gospels Harmonised and Translated, has been made by a competent translator and with my consent. — Leo Tolstoy. October 19/31, 1894.
> — gospel-translation · 1894-10

> It is at Count Tolstoy's express wish that I have undertaken the translation of his book on the Gospels. [...] owing to the impossibility of its being published in Russia, the Genevan edition is disfigured by numerous typographical mistakes.
> — gospel-translation · 1894-09-21

Visuals: 2 (2 usable) — Tolstoy's autograph imprimatur authorizing the English translation (1894) [PD], Title page: 'In Three Parts … at the request of the author', Brotherhood Publishing Co. / Walter Scott, 1895 [PD]

### Fyokla Tolstaya

person · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: Tolstoy's great-great-granddaughter; initiator of «Весь Толстой в один клик» and a leader of Tolstoy Digital

> Анастасия Бонч-Осмоловская, Фёкла Толстая, Борис Орехов, Тимофей Лукашевский
> Anastasia Bonch-Osmolovskaya, Fyokla Tolstaya, Boris Orekhov, Timofey Lukashevsky (under "Idea, task-setting, leadership"). (working English)
> — jubilee-edition-tei-corpus

Visuals: 1 (1 usable) — Fyokla Tolstaya, initiator of «Весь Толстой в один клик» [CC-BY-SA]

### Gabriel Sacy

person · missing · dives: christian-anarchism

_christian-anarchism_: Gabriel Sacy (1858–1903), Syrian-born head of the personnel office at the Egyptian Ministry of Finance, Cairo; a Bábí moving toward the Baháʼí branch. His letter on messianism draws the reply that contains Tolstoy's unique self-voiced «христианский анархизм». (The PSS calls him «бабист»; see needsReview for the Bábí/Baháʼí nuance.)

> je crois tout de même que le Babisme comme doctrine morale et humanitaire a un grand avenir dans le monde oriental ayant beaucoup de rapports avec l’anarchisme chrétien et tôt ou tard doit s’unir à lui.
> [Tolstoy's French original] ...I still believe that Babism, as a moral and humanitarian doctrine, has a great future in the eastern world, having much in common with Christian anarchism (l'anarchisme chrétien) and sooner or later must unite with it. (working English)
> — PSS Tom 73, pp. 109–110 · christian-anarchism · 1901-07-28

> я все-таки думаю, что бабизм, как нравственное и гуманитарное учение, имеет большое будущее в восточном мире. Имея много общего с христианским анархизмом, он должен рано или поздно с ним слиться.
> I still think that Babism, as a moral and humanitarian doctrine, has a great future in the eastern world. Having much in common with Christian anarchism, it must sooner or later merge with it. (working English)
> — PSS Tom 73, pp. 109–110 · christian-anarchism · 1901-07-28

Visuals: 1 (1 usable) — PSS Tom 73 p.154 — the Sacy letter, the «христианским анархизмом» passage (rendered from the local PD PSS PDF) [PD]

### Grigory Golitsyn

person · missing · dives: doukhobors

_doukhobors_: Caucasus viceroy who set the emigration conditions (own cost, no return) and to whom Tolstoy petitioned for Sulerzhitsky's travel permit.

> Но нынешнее русское правительство употребило против духоборов еще третий, казалось бы оставленный в наше время, выход из этого противоречия. Оно, кроме того, что подвергает самым тяжелым страданиям самих отказывающихся, заставляет еще систематически страдать отцов, матерей, детей отказывающихся, вероятно с тем, чтобы пытками этих невинных семей поколебать решимость несогласных их членов.
> But the present Russian government has used against the Doukhobors a third way out of this contradiction, one seemingly abandoned in our time. Besides subjecting the refusers themselves to the heaviest sufferings, it forces the fathers, mothers, and children of the refusers to suffer systematically as well — probably so as to shake the resolve of the dissenting members by the torture of these innocent families. (working English)
> — PSS Tom 71, pp. 322–327 · doukhobors · 1898-03-19

### Help (Pomogite)

criticalWork · missing · dives: doukhobors

_doukhobors_: The 1896 documentary appeal by Chertkov, Biryukov and Tregubov, with Tolstoy's afterword; its authors were exiled.

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

### Henry George

person · missing · dives: tolstoyanism

_tolstoyanism_: Tangential: the Mac-Gahan letter's long second half praises George's single-tax economics (the 'multiplication table' analogy). Mentioned, not part of the толстовство theme — low ingestion priority.

> Вы вот пишете о «толстовцах» и других моих последователях, о движении, поднятом моей проповедью, и о том, почему толстовцы проявляют мало рвения к пропаганде мыслей, которые осчастливят человечество; а я не знаю не только каких-либо других последователей, но и толстовцев
> You write about 'the Tolstoyans' and my other followers, about the movement raised by my preaching, and about why the Tolstoyans show so little zeal in propagating the ideas that would make mankind happy; but I know of no other followers, nor of any Tolstoyans. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

### Higher School of Economics

institution · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: Moscow university; home of the digital-humanities group behind Tolstoy Digital

> Проект «Слово Толстого»
> The "Word of Tolstoy" project. (working English)
> — jubilee-edition-tei-corpus

### Hodite v svete poka est svet

work · missing · dives: fire-metaphor

_fire-metaphor_: Fiction whose title is John 12:35; faith as a fire kept alive by adding wood

> как огонь никогда не потухнет, когда на него подкладывают дрова. В этом-то и вера.
> as a fire never goes out when wood is laid on it. That is exactly what faith is. (working English)
> — PSS Tom 26, pp. 250–301 · fire-metaphor · 1887

### I. Ivanov

person · missing · dives: tolstoyanism

_tolstoyanism_: Obscure 1909 correspondent (addressed via his nephew); identity beyond the PSS header unresolved — see needsReview. Addressee of the 'some sort of Tolstoyans' letter.

> православные не любят толстовцев, а толстовцы не любят православных. В этом вы, я думаю, ошибаетесь, во-первых, в том, что признаете каких-то толстовцев. Что же до меня касается, то хотя я и сам Толстой
> [you say that] the Orthodox do not love the Tolstoyans, and the Tolstoyans do not love the Orthodox. In this, I think, you are mistaken — first of all, in that you acknowledge some sort of Tolstoyans. As for myself, though I am Tolstoy myself… (working English)
> — PSS Tom 80, pp. 50–53 · tolstoyanism · 1909-08-04

### Ilya Ginzburg

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Sculptor; statuette 'Tolstoy at work' (1891) and a bust; GMT holds 51 of his Tolstoy works

> Приехал Репин и Гинзбург. За это время они меня лепят и пишут, а я написал статью об обжорстве и много подвинулся в большой статье.
> Repin and Ginzburg have arrived. During this time they sculpt and paint me, while I have written an article on gluttony and made much progress on the big article. (working English)
> — PSS Tom 52, pp. 44 · tolstoy-in-art · 1891-07-13

> Бюст сделал большой Гинцбург, нехорош. Репинский похож, но, не для того, чтобы вам сказать приятное, а потому, что так есть, ваш лучше всех.
> Ginzburg has made a large bust [of me], not good. Repin's is a likeness, but — not to flatter you, but because it is so — yours is the best of all. (working English)
> — PSS Tom 66, pp. 24–25 · tolstoy-in-art · 1891-07-30

Visuals: 1 (1 usable) — Tolstoy at Work (statuette) [CC0]

### Ilya Repin

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Painter; the most prolific depicter of Tolstoy (~12 portraits, 25 drawings, 3 busts, 1883–1910); disagreed with Tolstoy's art theory

> Дома Репин. С ним очень хорошо говорил, за работой.
> At home — Repin. Talked with him very well, while he was at work. (working English)
> — PSS Tom 49, pp. 77 · tolstoy-in-art · 1883-04-03

> Картина Репина невозможна — всё выдумано. Ге хорош очень.
> Repin's picture is impossible — it is all made up. Ge is very good. (working English)
> — PSS Tom 50, pp. 67–68 · tolstoy-in-art · 1889-04-15

> Приехал Репин и Гинзбург. За это время они меня лепят и пишут, а я написал статью об обжорстве и много подвинулся в большой статье.
> Repin and Ginzburg have arrived. During this time they sculpt and paint me, while I have written an article on gluttony and made much progress on the big article. (working English)
> — PSS Tom 52, pp. 44 · tolstoy-in-art · 1891-07-13

> Был Репин, уехал нынче.
> Repin was here; he left today. (working English)
> — PSS Tom 52, pp. 63 · tolstoy-in-art · 1892-02-24

> Портрет Репина уложен и завтра отсылается.
> Repin's portrait is packed and is being sent off tomorrow. (working English)
> — PSS Tom 64, pp. 66–67 · tolstoy-in-art · 1887-09-08

> Если моя книга помогла уяснить вопросы искусства такому художнику, как Репин, то труд ее писания не пропал даром.
> If my book helped to clarify questions of art for an artist such as Repin, then the labour of writing it was not in vain. (working English)
> — PSS Tom 71, pp. 334–335 · tolstoy-in-art · 1898-03-24

Visuals: 6 (6 usable) — Portrait of Tolstoy [PD], Tolstoy Barefoot [PD], Tolstoy Resting in the Forest [PD], Tolstoy in the Pink Armchair [PD], Tolstoy Ploughing (Пахарь) [PD], Tolstoy in his Study [PD]

### Issledovanie dogmaticheskogo bogoslovija

work · missing · dives: gospel-translation

_gospel-translation_: Project part 2 — the polemical demolition of Orthodox dogma that cleared the ground for the harmony

> кощунственные сочинения Вольтера, Юма, но никогда я не испытывал того несомненного убеждения в полном безверии человека, как то, которое я испытывал относительно составителей катехизисов и богословии
> the blasphemous writings of Voltaire and Hume — yet never did I feel such a certain conviction of a man's complete unbelief as the one I felt regarding the composers of catechisms and theologies. (working English)
> — PSS Tom 23, pp. 60–303 · gospel-translation · 1880

### Ivan Ivakin

person · missing · dives: gospel-translation

_gospel-translation_: Tolstoy's Greek tutor at Yasnaya Polyana during the gospel work (per secondary literature — unconfirmed)

> Читал я по-гречески, на том языке, на котором оно есть у нас, и переводил так, как указывал смысл и лексиконы
> I read in Greek, the language in which we have it, and translated as the sense and the lexicons indicated. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

### Ivan Kramskoy

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Painter; made the two 1873 portraits of Tolstoy; model for Mikhailov in Anna Karenina; praised in What Is Art?

> Портрет с пятого сеанса поразил всех, в особенности Вронского, не только сходством, но и особенною красотою. Странно было, как мог Михайлов найти ту ее особенную красоту.
> The portrait, after the fifth sitting, struck everyone, Vronsky especially, not only by its likeness but by a particular beauty. It was strange how Mikhailov could have found that particular beauty of hers. (working English)
> — PSS Tom 19, pp. Part 5, ch. IX–XIII · tolstoy-in-art · 1875-1876

> Таков рисунок Крамского, стоящий многих его картин [...] Образцами же в области живописи произведений, вызывающих негодование, ужас пред нарушением любви к Богу и ближнему, могут служить картина Ге — суд
> Such is Kramskoy's drawing, worth many of his paintings [...] As models in painting of works that arouse indignation and horror at the violation of love of God and neighbour, Ge's picture 'The Judgement' can serve. (working English)
> — PSS Tom 30, pp. 27–203 (here ~p.150) · tolstoy-in-art · 1897

> У меня каждый день, вот уже с неделю, живописец Крамской [...] делает мой портрет в Третьяковскую галлерею, и я сижу и болтаю с ним и из Петербургской стараюсь обращать его в крещеную веру.
> Every day now, for a week already, the painter Kramskoy has been making my portrait for the Tretyakov gallery, and I sit and chat with him and try to convert him from the Petersburg faith to the baptized one. (working English)
> — PSS Tom 62, pp. 48–49 · tolstoy-in-art · 1873-09-23

> Он теперь кончает оба портрета и ездит каждый день, и мешает мне заниматься. Я же во время сидений обращаю его из петербургской в христианскую веру и, кажется, успешно.
> He is now finishing both portraits and comes every day, keeping me from my work. During the sittings I am converting him from the Petersburg to the Christian faith — successfully, it seems. (working English)
> — PSS Tom 62, pp. 49–51 · tolstoy-in-art · 1873-09-23

Visuals: 2 (2 usable) — Portrait of L. N. Tolstoy [PD], Portrait of Tolstoy (family version) [PD]

### Ivan Nazhivin

person · missing · dives: christian

_christian_: Writer; recipient of the true-vs-social-religion definition

> Христианство, истинное христианство, по моему мнению, тем и отличается от религий, которые можно называть общественными, как католичество, православие, магометанство, я думаю даже конфуцианство, что оно обращается к душе каждого отдельного человека, для каждого отдельного человека разрешает его вопрос жизни, указывает ему его назначение, состоящее в исполнении воли бога, в слиянии с ней своей воли, в служении для бога богу и людям и тем дает ему спокойствие и благо.
> Christianity, true Christianity, in my opinion, differs from the religions one may call social — such as Catholicism, Orthodoxy, Mohammedanism, and I think even Confucianism — in that it addresses the soul of each individual person. (working English)
> — PSS Tom 75, pp. 60–62 · christian · 1904-03-17

### Ivan Tregubov

person · missing · dives: doukhobors

_doukhobors_: Co-author of «Help!»; exiled to the Baltic provinces. Verigin's letter reached Tolstoy through him.

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

> теперь же нельзя предоставлять одним врагам это могущественное орудие для обмана, и не пользоваться книгой или письмом для передачи своих мыслей и восприятия мыслей других людей
> but now one cannot leave this mighty instrument of deception to the enemies alone, and not make use of the book or the letter to convey one's own thoughts and to receive the thoughts of others. (working English)
> — PSS Tom 68, pp. 262–266 · doukhobors · 1895-11-21

### John Coleman Kenworthy

person · missing · dives: christian-anarchism, gospel-translation

_christian-anarchism_: John Coleman Kenworthy (1861–1948), English founder of the Brotherhood Church, Croydon (from 1894); visited Yasnaya Polyana in 1896 and held UK rights to Tolstoy's works. A node of the 1890s Christian-anarchist circle; named in the Schmitt correspondence.
_gospel-translation_: Leader of the Croydon Brotherhood Church; attributed (secondary sources, unconfirmed) as the anonymous translator of the 1895–96 edition

> Ваше дело, наше дело, т. е. божье дело, у вас делает успехи.
> Your work, our work, that is, God's work, is making progress with you. (working English)
> — PSS Tom 68, pp. 26–28 · christian-anarchism · 1895-02-01

> It is at Count Tolstoy's express wish that I have undertaken the translation of his book on the Gospels. [...] owing to the impossibility of its being published in Russia, the Genevan edition is disfigured by numerous typographical mistakes.
> — gospel-translation · 1894-09-21

### John Morrison Davidson

person · missing · dives: christian-anarchism

_christian-anarchism_: John Morrison Davidson (1843–1916), Scottish radical journalist and barrister; author of The Old Order and the New, The Gospel of the Poor and Anarchist Socialism v. State Socialism. Tolstoy praises him in 1894 for subordinating socialist/communist/anarchist theory to Christian truth.

> социалистическая, коммунистическая и анархическая теории приводятся в подкрепление христианской истины, которая составляет ее главную часть.
> the socialist, communist and anarchist theories are brought in to corroborate the Christian truth, which forms its chief part. (working English)
> — PSS Tom 67, pp. 178–180 · christian-anarchism · 1894-07-23

### John Van der Veer

person · missing · dives: christian

_christian_: Dutch conscientious objector; Tolstoy tells him he 'cannot but be' a Christian

> До сих пор все отказы от военной службы бывали основаны на мотивах, вытекающих из религиозных верований, и правительства объясняли их как последствия сектантского фанатизма, тогда как отказ Вандервера, который даже не называет себя христианином (вероятно, в том смысле, который церкви обычно придают этому слову, в сущности же я считаю его более христианином, чем все епископы, которые будут осуждать его поступок), не дает правительству никакой возможности объяснить его поступок, как исключение, и ясно обнаруживает противоречие между христианством, к которому причисляют себя правительства, и существующим порядком, который они поддерживают постоянными армиями, не имеющими другого назначения, кроме насилия и убийства.
> ...Van der Veer, who does not even call himself a Christian (probably in the sense the churches usually give the word, though in essence I consider him more of a Christian than all the bishops who will condemn his act)... (working English)
> — PSS Tom 69, pp. 122–124 · christian · 1896-08-23

> Дорогой друг, Называю вас так, потому что, прочитав ваше письмо к командиру полка,³ По этому письму я вижу, что ваше понимание жизни и наших обязанностей к богу и ближнему тождественно с моим. Вы говорите в вашем письме, что вы не христианин; но вы не можете не быть таковым, так как поступок ваш мог вытечь только из христианского начала, заключающегося в признании цели своего существования не в благе своей личности, но в осуществлении истины и общего блага, иначе говоря — в осуществлении воли божьей и установлении его царства на земле.
> You say in your letter that you are not a Christian; but you cannot but be one, since your act could only have flowed from the Christian principle. (working English)
> — PSS Tom 69, pp. 124–127 · christian · 1896-08-23

### Jubilee Edition

edition · missing · dives: gospel-translation, jubilee-edition-tei-corpus · names: Jubilee Edition (Полное собрание сочинений) / The Jubilee Edition (Полное собрание сочинений)

_gospel-translation_: The 90-vol PSS; Tom 24 (1957) is the first legal Russian publication of the full harmony. Fully mapped in the sibling jubilee-edition-tei-corpus dive
_jubilee-edition-tei-corpus_: the 90-volume complete works (1928–1958) + 1964 index volume; the platform's base text for all Russian-language citation

> Толстой Л. Н. Детство // Толстой Л. Н. Полное собрание сочинений: в 90 тт. Т. 1. М.: Гос. изд. «Художественная литература», 1935.
> Tolstoy L. N. Childhood // Tolstoy L. N. Complete Collected Works: in 90 vols. Vol. 1. Moscow: State Publishing House "Khudozhestvennaya Literatura", 1935. (working English)
> — PSS Tom 1, pp. 3–95 · jubilee-edition-tei-corpus

> Перепечатка разрешается безвозмездно
> Reprinting is permitted gratis [free of charge]. (Followed by "Reproduction libre pour tous les pays.") (working English)
> — PSS Tom 1, pp. iv · jubilee-edition-tei-corpus · 1935-01-01

> непосредственную работу по редактированию тому другу покойного писателя, которого он сам выбрал для этой цели
> …the direct work of editing to that friend of the deceased writer whom he himself chose for this purpose… (i.e. V. G. Chertkov). (working English)
> — PSS Tom 1, pp. v · jubilee-edition-tei-corpus · 1928-01-01

> нам в настоящем издании приходится именно в таком полном виде воспроизводить решительно все, написанное Толстым.
> …in the present edition we have to reproduce, in exactly such complete form, absolutely everything written by Tolstoy. (working English)
> — PSS Tom 1, pp. vi · jubilee-edition-tei-corpus · 1928-01-01

> Полное собрание сочинений. Том 53.
> Complete Collected Works. Volume 53. (the auto-generated cover header). (working English)
> — PSS Tom 53 · jubilee-edition-tei-corpus · 1953-01-01

> Полное собрание сочинений. Том 91.
> Complete Collected Works. Volume 91 — "Указатели" (Indexes). (working English)
> — PSS Tom 91 · jubilee-edition-tei-corpus · 1964-01-01

Visuals: 2 (2 usable) — PSS Tom 1 — the free-reproduction notice («Перепечатка разрешается безвозмездно») [PD], PSS Tom 1 — «ОТ ГОСУДАРСТВЕННОЙ РЕДАКЦИОННОЙ КОМИССИИ» (State Editorial Commission) [PD]

### Kratkoe izlozhenie Evangelija

work · missing · dives: gospel-translation, lords-prayer

_gospel-translation_: The condensed redaction of the harmony; its preface narrates the crisis, the method, the 12-chapter structure and the four-part plan
_lords-prayer_: The condensed redaction — holds Version C (the twelve-fold correspondence in its preface and the recitable prayer in its body). The base text for the Swedish rendering.

> Разделение Евангелия на 12 или на 6 глав (соединяя по две главы в одну) вытекло само собою из смысла учения.
> The division of the Gospel into 12 chapters (or into 6, joining two chapters into one) emerged of itself from the meaning of the teaching. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

> разночтений евангельских книг насчитывают до пятидесяти тысяч.
> the variant readings of the Gospel books are counted at up to fifty thousand. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

> Я был приведен к христианству не богословскими, не историческими исследованиями, а тем, что пятидесяти лет от роду [...] я пришел в отчаяние и хотел убить себя [...] И я стал изучать христианство
> I was brought to Christianity not by theological or historical investigations, but by the fact that, at fifty years of age […] I fell into despair and wanted to kill myself […] And I began to study Christianity. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

> перевод четырех Евангелий и соединение их в одно.
> the translation of the four Gospels and their combination into one. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

> так называемая молитва господня есть не что иное, как в самой сжатой форме выраженное всё учение Иисуса в том самом порядке, в котором были расположены мною главы, и что каждое выражение молитвы соответствует смыслу и порядку глав.
> the so-called Lord's Prayer is nothing other than the whole teaching of Jesus expressed in the most condensed form, in the very order in which I had arranged the chapters, and each phrase of the prayer corresponds to the sense and order of the chapters. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

> нашел незаконно соединенную с ним грязь и тину, которая одна заслоняла для меня его чистоту; рядом с высоким христианским учением я нашел связанное с ним чуждое ему безобразное учение еврейское и церковное.
> I found, illegitimately joined to it, mud and silt which alone obscured its purity for me; beside the lofty Christian teaching I found bound up with it an alien, ugly Jewish and ecclesiastical teaching. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

> Окончив свою работу, я к удивлению и радости своей нашел, что так называемая молитва господня есть не что иное, как в самой сжатой форме выраженное всё учение Иисуса в том самом порядке, в котором были расположены мною главы, и что каждое выражение молитвы соответствует смыслу и порядку глав.
> On finishing my work I found, to my surprise and joy, that the so-called Lord's Prayer is nothing other than the whole teaching of Jesus expressed in the most condensed form, in the very order in which I had arranged the chapters, and that each phrase of the prayer corresponds to the sense and order of the chapters. (working English)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

> А будет твоя власть, и сила, и разум.
> But there will be thy power, and strength, and reason. (working English) — Tolstoy's meaning for the doxology (phrase 12 of 12)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

> Человек — сын Бога.
> Man is the son of God. (working English) — Tolstoy's meaning for "Отче наш" (phrase 1 of 12)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

> Молитесь только так: Отец наш безначальный и бесконечный, как небо! Пусть будет свято только твое существо. Пусть будет власть только твоя, так, чтобы воля твоя совершалась безначально и бесконечно на земле. Дай мне пищу жизни в настоящем. Ошибки мои прежние загладь и сотри так же, как и я заглаживаю и стираю все ошибки братьев моих, чтобы я не попал в соблазн, избавился от зла. Потому что твоя власть и сила и твое решение.
> Pray only thus: Our Father, without beginning and without end, like the sky! May thy being alone be holy. May power alone be thine, so that thy will be done, without beginning and without end, on earth. Give me the food of life in the present. My former mistakes, efface and wipe them out, just as I efface and wipe out all the mistakes of my brothers, so that I may not fall into temptation, and may be delivered from evil. Because thine is the power and the strength and thine the decision. (working English)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

> Ни молиться, ни поститься не нужно. Молиться не нужно потому, что отец знает всё, что людям нужно.
> Neither to pray nor to fast is needed. To pray is not needed, because the Father knows everything that people need. (working English)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

### Krekshino

place · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: Pashkov estate; site of Tapsell's Sept-1909 photographs of Tolstoy and grandchildren and of the filmed departure

> Фотографии Тапселя превосходны — нас с детьми.
> Tapsell's photographs are superb — of us with the children. (working English)
> — PSS Tom 89, pp. 143–146 · tolstoy-in-photographs · 1909-09-26

### Leeds Russian Archive Chertkov Tapsell fond

archival-fond · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: Tuckton House / Free Age Press negatives and prints, incl. Tapsell's 1908 Yasnaya Polyana series

> Фотографии Тапселя превосходны — нас с детьми.
> Tapsell's photographs are superb — of us with the children. (working English)
> — PSS Tom 89, pp. 143–146 · tolstoy-in-photographs · 1909-09-26

### Leo Tolstoy

person · exists · dives: 1879-1882-a-confession, biryukov-sofia-relationship, christian-anarchism, copyright-renunciation, crisis, doukhobors, tolstoy-in-photographs, tolstoyanism · names: Lev Tolstoy / Leo Tolstoy

_1879-1882-a-confession_: Author.
_biryukov-sofia-relationship_: Subject; author of the letters, diaries, and testament
_christian-anarchism_: The author refusing the political label 'anarchist' while affirming the religious substance, and the sole user of «христианский анархизм» in his own voice (once).
_copyright-renunciation_: author renouncing copyright; subject of the dive
_crisis_: subject of the dive; author of the keystone confessional works
_doukhobors_: Author of the public appeals, organiser and partial funder of the relief and emigration.
_tolstoy-in-photographs_: subject — the most-photographed Russian of his age; ambivalent sitter and occasional initiator
_tolstoyanism_: The author disowning the label and the movement named after him.

> Я был крещен и воспитан в православной христианской вере. Меня учили ей и с детства и во всё время моего отрочества и юности. Но когда я 18-ти лет вышел со второго курса университета, я не верил уже ни во что из того, чему меня учили.
> (working English) I was baptized and brought up in the Orthodox Christian faith. I was taught it from childhood and throughout my boyhood and youth. But when, at eighteen, I left the second year of university, I no longer believed in anything I had been taught.
> — PSS Tom 23, pp. 1 (ch. I) · 1879-1882-a-confession · 1879–1882

> Начал писать «свою жизнь».
> (working English) Began to write 'my life'.
> — PSS Tom 48, pp. 69–70 · 1879-1882-a-confession · 1878-05-22 (OS)

> Разум мне ничего не говорит и не может сказать на три вопроса, которые легко выразить одним: что я такое?
> (working English) Reason tells me nothing, and can say nothing, to the three questions that may easily be put as one: what am I?
> — PSS Tom 62, pp. 379–383 · 1879-1882-a-confession · 1878-01-27 (OS)

> не будет тайн для одного, а тайны для двух, она будет всё читать.
> there will be no secrets for one, but secrets for two; she will read everything. (working English)
> — PSS Tom 48, pp. 45 · biryukov-sofia-relationship · 1862-09-15

> отказаться от авторского права.
> to renounce the author's right. (working English)
> — PSS Tom 53, pp. 14-18 · biryukov-sofia-relationship · 1895-03-27

> это была Арсеньева Валерия. Она теперь жива, за Волковым была, живет в Париже.
> that was Arsenyeva, Valeria. She is alive now, was married to Volkov, lives in Paris. (working English)
> — PSS Tom 74, pp. 319 · biryukov-sofia-relationship · 1903-11-27

> Ответ не может быть дан на вопрос, потому что он дурно поставлен. Вопрос не в том — устроить государство: по нынешнему, или по новому. Я и никто из нас не приставлен к решению этого вопроса.
> The answer cannot be given to the question, because it is badly posed. The question is not whether to arrange the state in the present way or in a new way. Neither I nor any of us is appointed to the solving of that question. (working English)
> — PSS Tom 52, pp. 138–140 · christian-anarchism · 1894-09-10

> Мне кажется только, что я не анархист в смысле политического реформатора. В оглавлении вашей книги под словом «насилие» сделаны указания на разные страницы из других сочинений, но ни одной ссылки на мои. Не доказательство ли это того, что то учение, которое вы мне приписываете и которое, в сущности, есть не что иное, как учение Христа, вовсе не политическое, а религиозное учение?
> It seems to me only that I am not an anarchist in the sense of a political reformer. In the index of your book under the word 'violence' references are made to various pages of the other writers, but not one to mine. Is this not proof that the teaching which you ascribe to me, and which is, in essence, nothing other than the teaching of Christ, is not a political but a religious teaching? (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

> я все-таки думаю, что бабизм, как нравственное и гуманитарное учение, имеет большое будущее в восточном мире. Имея много общего с христианским анархизмом, он должен рано или поздно с ним слиться.
> I still think that Babism, as a moral and humanitarian doctrine, has a great future in the eastern world. Having much in common with Christian anarchism, it must sooner or later merge with it. (working English)
> — PSS Tom 73, pp. 109–110 · christian-anarchism · 1901-07-28

> Собственность, как она теперь — зло. А собственность сама по себе — радость на то, что тем, что я сделал, добро. […] Но собственность, ограждаемая насилием — городовым с пистолетом — это зло. Сделай ложку и ешь ею, но пока она другому не нужна.
> Property as it is now — is evil. Property in itself — is joy in the good one has made. […] But property defended by violence — by the policeman with a pistol — that is evil. Make a spoon and eat with it, but only until another needs it. (working English)
> — PSS Tom 49, pp. 59 · copyright-renunciation · 1883-01-01

> И вчера же был разговор с женой о напечатании письма в газетах об отказе от права авторской собственности. Трудно вспомнить, а главное, описать всё, что тут было: [Вымарано 19 строк.]
> And yesterday too there was a conversation with my wife about printing in the newspapers the letter renouncing the right of literary property. It is difficult to recall, and chiefly to describe, everything that was said: [19 lines erased.] (working English)
> — PSS Tom 52, pp. 45–47 · copyright-renunciation · 1891-07-22

> 4) Право на издание моих сочинений прежних: десяти томов и азбуки прошу моих наследников передать обществу, т. е. отказаться от авторского права. Но только прошу об этом и никак не завещаю. […] То, что сочинения мои продавались эти последние 10 лет, было самым тяжелым для меня делом в жизни.
> 4) I ask my heirs to hand over to the public the right of publication of my earlier works — the ten volumes and the Azbuka — that is, to renounce the copyright. But I only ask this and in no way bequeath it. […] That my writings have been sold during these last ten years was the heaviest thing in my life. (working English)
> — PSS Tom 53, pp. 14–18 · copyright-renunciation · 1895-03-27

> Предоставляю всем желающим право безвозмездно издавать в России и за границей, по-русски и в переводах, а равно и ставить на сценах все те из моих сочинений, которые были написаны мною с 1881 года и напечатаны в XII томе моих полных сочинений издания 1886 года, и в XIII томе, изданном в нынешнем 1891 году, равно и все мои неизданные в России и могущие вновь появиться после нынешнего дня сочинения.
> I grant to all who so wish the right to publish gratis, in Russia and abroad, in Russian and in translations, and likewise to perform on stage, all those of my writings which were written by me from 1881 onward and printed in vol. XII of my complete works of the 1886 edition, and in vol. XIII, published in this present year 1891, and likewise all my works unpublished in Russia and any that may newly appear after the present day. (working English)
> — PSS Tom 66, pp. 47–48 · copyright-renunciation · 1891-09-16

> Так я жил, но пять лет тому назад со мною стало случаться что-то очень странное: на меня стали находить минуты сначала недоумения, остановки жизни, как будто я не знал, как мне жить, что мне делать, и я терялся и впадал в уныние. […] Эти остановки жизни выражались всегда одинаковыми вопросами: Зачем? Ну, а потом?
> So I lived, but five years ago something very strange began to happen to me: at first there came over me moments of bewilderment, of life coming to a stop, as though I did not know how to live or what to do, and I lost my footing and fell into dejection. […] These stoppages of life always expressed themselves in the same questions: Why? And then what? (working English)
> — PSS Tom 23, pp. 10 · TEI v23_001_059_Ispoved · crisis · 1882

> Пять лет тому назад я поверил в учение Христа — и жизнь моя вдруг переменилась […] Со мной случилось то, что случается с человеком, который вышел за делом и вдруг дорогой решил, что дело это ему совсем не нужно,— и повернул домой.
> Five years ago I came to believe in Christ's teaching — and my life suddenly changed […] What happened to me was what happens to a man who goes out on some errand and then suddenly decides on the way that the errand is of no use to him at all — and turns back home. (working English)
> — PSS Tom 23, pp. 304 · TEI v23_304_465_V_chem_moja_vera · crisis · 1884

> Я жил так года два, и со мной случился переворот, который давно готовился во мне и задатки которого всегда были во мне. Со мной случилось то, что жизнь нашего круга — богатых, ученых — не только опротивела мне, но потеряла всякий смысл.
> I lived like that for a couple of years, and there occurred in me an upheaval [переворот] that had long been preparing within me, and whose seeds had always been in me. What happened to me was that the life of our circle — the rich, the learned — not only grew repugnant to me, but lost all meaning. (working English)
> — PSS Tom 23, pp. 40 · TEI v23_001_059_Ispoved · crisis · 1882

> И я спасся от самоубийства. Когда и как совершился во мне этот переворот, я не мог бы сказать. […] так же постепенно, незаметно возвратилась ко мне эта сила жизни. И странно, что та сила жизни, которая возвратилась ко мне, была не новая, а самая старая, — та самая, которая влекла меня на первых порах моей жизни.
> And I was saved from suicide. When and how this upheaval [переворот] took place in me, I could not say. […] just as gradually, imperceptibly, the force of life returned to me. And it is strange that the force of life which returned to me was not a new one, but the very oldest — the same that had drawn me in the first days of my life. (working English)
> — PSS Tom 23, pp. 46 · TEI v23_001_059_Ispoved · crisis · 1882

> …я, к счастию, этого отчаяния никогда не знал с тех пор, как родился вновь […] то каждый, проходя эти возрасты, эти кризисы, не будет пугаться, а будет ждать следующего состояния, будет знать, что то же было и с другими.
> …I, fortunately, have never known this despair since I was born anew… so that everyone, passing through these ages, these crises, would not take fright, but would wait for the next state, knowing that the same was so for others. (working English)
> — PSS Tom 67, pp. 213–214 · TEI v67_214_L_F_Annenkovoj · crisis · 1894-09-04

> Вы знаете, что Марья Петровна Фет при смерти — крупозное воспаление легких. До сих пор нет кризиса, и шансов смерти, говорят, больше, чем жизни.
> You know that Marya Petrovna Fet is dying — lobar pneumonia. So far there is no crisis, and the chances of death, they say, are greater than of life. (working English)
> — PSS Tom 67, pp. 84 · TEI v67_083_H_N_Straxovu · crisis · 1894-03-16

> Русское государство выставило против духоборов все те орудия, которыми оно может бороться. Орудия эти: полицейские меры арестов, непозволения выезда из места жительства, запрещение общения друг с другом, перехватывание писем, шпионство, запрещение печатания в газетах сведений о всем, касающемся духоборов, клевета на них, печатаемая в журналах, подкупы, сечения, тюрьмы, ссылки, разорение семей.
> The Russian state brought against the Doukhobors every weapon it can fight with. These weapons are: police measures of arrest, prohibition of travel from one's place of residence, the banning of communication with one another, the interception of letters, espionage, the suppression of newspaper reports of anything touching the Doukhobors, slander printed against them in the journals, bribery, floggings, prisons, exiles, the ruin of families. (working English)
> — PSS Tom 31, pp. 97–101 · doukhobors · 1898-08-15

> После этого, 28 июня 1895 года, духоборцы, живущие в Ахалкалакском уезде Тифлисской губернии, снесли в одну кучу в поле, около села Спасского, всё свое имевшееся у них оружие и, обложив его дровами и углем и облив керосином, сожгли
> After this, on 28 June 1895, the Doukhobors living in the Akhalkalaki district of the Tiflis province carried all the weapons they had into a single heap in a field near the village of Spasskoye and, having piled wood and coal upon them and doused them with kerosene, burned them. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

> Но нынешнее русское правительство употребило против духоборов еще третий, казалось бы оставленный в наше время, выход из этого противоречия. Оно, кроме того, что подвергает самым тяжелым страданиям самих отказывающихся, заставляет еще систематически страдать отцов, матерей, детей отказывающихся, вероятно с тем, чтобы пытками этих невинных семей поколебать решимость несогласных их членов.
> But the present Russian government has used against the Doukhobors a third way out of this contradiction, one seemingly abandoned in our time. Besides subjecting the refusers themselves to the heaviest sufferings, it forces the fathers, mothers, and children of the refusers to suffer systematically as well — probably so as to shake the resolve of the dissenting members by the torture of these innocent families. (working English)
> — PSS Tom 71, pp. 322–327 · doukhobors · 1898-03-19

> Неприятно и то, что вызывает сознание себя не божественного, а пакостного Льва Николаевича.
> Unpleasant, too, in that it arouses the consciousness of oneself as not the divine but the vile Lev Nikolaevich. (working English)
> — PSS Tom 57, pp. 141–142 · tolstoy-in-photographs · 1909-09-17

> по моему предложению, все литераторы сделали фотографическую группу
> at my proposal, all the literary men had a photographic group made (working English)
> — PSS Tom 61, pp. 372–374 · tolstoy-in-photographs · 1856-04-14

> Не прислал до сих пор карточки потому, что забыл, а забыл потому, что не могу приписать этому значения
> I have not sent the card until now because I forgot, and I forgot because I cannot attach any importance to it (working English)
> — PSS Tom 78, pp. 191 · tolstoy-in-photographs · 1908-07-23

> Я рад был случаю сказать ему и уяснить себе, что говорить о толстовстве, искать моего руководительства, спрашивать моего решения вопросов — большая и грубая ошибка. — Никакого толстовства и моего учения не было и нет, есть одно вечное, всеобщее, всемирное учение истины, для меня, для нас особенно ясно выраженное в евангелиях.
> I was glad of the chance to tell him, and to clarify for myself, that to speak of Tolstoyism, to seek my guidance, to ask me to decide questions — is a great and crude error. There was and is no Tolstoyism and no teaching of mine; there is one eternal, universal, world-wide teaching of truth, which for me, for us, is especially clearly expressed in the Gospels. (working English)
> — PSS Tom 53, pp. 167–169 · tolstoyanism · 1897-12-02

> Вы вот пишете о «толстовцах» и других моих последователях, о движении, поднятом моей проповедью, и о том, почему толстовцы проявляют мало рвения к пропаганде мыслей, которые осчастливят человечество; а я не знаю не только каких-либо других последователей, но и толстовцев
> You write about 'the Tolstoyans' and my other followers, about the movement raised by my preaching, and about why the Tolstoyans show so little zeal in propagating the ideas that would make mankind happy; but I know of no other followers, nor of any Tolstoyans. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

> православные не любят толстовцев, а толстовцы не любят православных. В этом вы, я думаю, ошибаетесь, во-первых, в том, что признаете каких-то толстовцев. Что же до меня касается, то хотя я и сам Толстой
> [you say that] the Orthodox do not love the Tolstoyans, and the Tolstoyans do not love the Orthodox. In this, I think, you are mistaken — first of all, in that you acknowledge some sort of Tolstoyans. As for myself, though I am Tolstoy myself… (working English)
> — PSS Tom 80, pp. 50–53 · tolstoyanism · 1909-08-04

Visuals: 22 (18 usable) — Portrait of Lev Tolstoy (Kramskoy, 1873) [PD], Portrait of Lev Tolstoy (Repin, 1887) [PD], Tolstoy, half-length (Sass studio, c.1880–1886) [PD], Tolstoy mowing (Repin sketch, 1880–1881) [PD], 1895 testament, PSS Tom 53 [PD], Diary for myself alone, Oct 1910, PSS Tom 58 [PD], Yasnaya Polyana main house [PD], Diary page, 27 March 1895 (the will-as-diary-entry) [rights-reserved], Leo Tolstoy, 1906 (photograph by V. G. Chertkov) [PD], Manuscript / draft page of Исповедь (A Confession) [rights-reserved], Portrait of Leo Tolstoy (oil), Ivan Kramskoy, 1873 [PD], PSS Tom 23, p. 40 — the «случился переворот» passage of A Confession [PD], Photographic portraits of Tolstoy, c. 1878–1885 (crisis years) [unknown], Tolstoy Digital timeline cards (work on A Confession #175; banning of A Confession #192; Optina Pustyn with Strakhov #166; first acquaintance with Chertkov #198) [unknown], Leo Tolstoy, 1895 — the year of the Burning of Arms [PD], Leo Tolstoy at Yasnaya Polyana, colour photograph, 1908 [PD], Tolstoy, wedding-period portrait (married Sept 1862) [PD], Tolstoy standing portrait in heavy coat, mid-career [PD], Tolstoy at the opening of the Savelyev library [PD], Tolstoy studio portrait, full-length seated [PD], Tolstoy seated formal portrait [PD], Tolstoy and Anton Chekhov (group, outdoor) [PD]

### Leonid Pasternak

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Painter; illustrated Resurrection (1898–99); many Tolstoy drawings

> Но вообще прекрасный, как все ваши рисунки, и я вам благодарен за них.
> But on the whole splendid, like all your drawings, and I am grateful to you for them. (working English)
> — PSS Tom 75, pp. 186–187 · tolstoy-in-art · 1904-11-22

Visuals: 3 (3 usable) — Illustrations for Resurrection [PD], Tolstoy, Solovyov and Fyodorov [PD], Tolstoy reading by a lamp [PD]

### Leonila Annenkova

person · missing · dives: crisis

_crisis_: correspondent; recipient of the 'эти кризисы / родился вновь' letter (1894)

> …я, к счастию, этого отчаяния никогда не знал с тех пор, как родился вновь […] то каждый, проходя эти возрасты, эти кризисы, не будет пугаться, а будет ждать следующего состояния, будет знать, что то же было и с другими.
> …I, fortunately, have never known this despair since I was born anew… so that everyone, passing through these ages, these crises, would not take fright, but would wait for the next state, knowing that the same was so for others. (working English)
> — PSS Tom 67, pp. 213–214 · TEI v67_214_L_F_Annenkovoj · crisis · 1894-09-04

### Light of reason

concept · missing · dives: fire-metaphor

_fire-metaphor_: Tolstoy's signature equation light = reason (разумение); the spine of the light axis

> И перед светом разума всё прежнее объяснение разлетелось прахом.
> And before the light of reason all the former explanation scattered to dust. (working English)
> — PSS Tom 23, pp. 1–59 · fire-metaphor · 1882

> в человеке живет божественный свет, сошедший с неба, и свет этот есть разум, — и что ему одному надо служить и в нем одном искать благо.
> in man there lives a divine light, come down from heaven, and this light is reason — and that it alone must be served and in it alone must good be sought. (working English)
> — PSS Tom 23, pp. 304–465 · fire-metaphor · 1884

> 9) Φῶς — свет — по всем контекстам означает истинное разумение жизни.
> 9) Φῶς — light — in all contexts means the true reason/understanding of life. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> свет солнца разума есть только незначущая случайность, сентиментальные, мистические слова.
> the light of the sun of reason is only an insignificant accident — sentimental, mystical words — so it appears to those not yet awake to it. (working English)
> — PSS Tom 26, pp. 313–442 · fire-metaphor · 1887

### Marian Zdziechowski

person · missing · dives: christian

_christian_: Polish scholar; recipient of 'I try to be a Christian'

> ⁹ В данном случае, например, я, не будучи поляком, поспорю с каждым поляком в степени отвращения, негодования к тем диким и глупым мерам русских правительственных лиц, которые употребляются против веры и языка поляков; поспорю, и в желании противодействовать этим мерам, и не потому, что я люблю католичество больше, чем другие веры, или польский язык больше, чем другие языки, а потому, что я стараюсь быть христианином. И потому, для того чтобы ничего подобного не было ни в Польше, ни в Эльзасе, ни в Чехии, нужно не распространение патриотизма, а распространение истинного христианства.
> ...not because I love Catholicism more than other faiths, or the Polish language more than other languages, but because I try to be a Christian. And therefore... what is needed is the spread of true Christianity. (working English)
> — PSS Tom 68, pp. 165–173 · christian · 1895-09-10

### Mikhail Elpidin

person · missing · dives: 1879-1882-a-confession, gospel-translation · names: M. K. Elpidin / Mikhail Elpidin (М. К. Эльпидин)

_1879-1882-a-confession_: Émigré publisher in Geneva; the first separate edition of «Исповедь» (1884), where the title first appears in print.
_gospel-translation_: Geneva émigré publisher; the censored full harmony first appeared abroad through this network (1892–94, per scholarship — confirm)

> It is at Count Tolstoy's express wish that I have undertaken the translation of his book on the Gospels. [...] owing to the impossibility of its being published in Russia, the Genevan edition is disfigured by numerous typographical mistakes.
> — gospel-translation · 1894-09-21

Visuals: 1 (0 usable) — The censored Geneva (Elpidin) first edition of the Russian harmony [unknown]

### Mikhail Engelhardt

person · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: Young radical and addressee of Tolstoy's longest epistolary statement of the new doctrine (the 'five commandments' letter).

> значение его в том, чтобы найти смысл жизни в этом мире. Исполнение пяти заповедей дает этот смысл.
> (working English) its significance is in finding the meaning of life in this world. Fulfilment of the five commandments gives that meaning.
> — PSS Tom 63, pp. 112–128 · 1879-1882-a-confession · 1882-12 (OS)

### Mikhail Stakhovich

person · missing · dives: tolstoyanism

_tolstoyanism_: Oryol marshal of the nobility, Duma politician and friend of the Tolstoy family; addressee of the 1907 New-Year letter in which the 'ridicule of Tolstoyism' appears.

> сказал бы, не есть мяса, если бы не боялся ridicul’a⁴ толстовства
> [I] would say, eat no meat — were I not afraid of the ridicule of Tolstoyism. (working English)
> — PSS Tom 77, pp. 5–6 · tolstoyanism · 1907-01-01

### Most Holy Synod

institution · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: The governing body of the Russian Orthodox Church; its spiritual censorship banned the work (1882); its 1901 edict declared Tolstoy fallen away from the Church (naming no works).

> И русские стали во имя христианской любви убивать своих братьев.
> (working English) And Russians began, in the name of Christian love, to kill their brothers.
> — PSS Tom 23, pp. ch. XV · 1879-1882-a-confession · 1879–1882

### Na kazhdyj den

work · missing · dives: fire-metaphor

_fire-metaphor_: The daily-wisdom anthology (1906–10) that recasts the fire/light credo as maxims (truth-is-fire, one-fire-equality, light of reason)

> Нет в человеке ничего драгоценнее, нужнее ему света разума.
> There is nothing in a person more precious, more needful to him, than the light of reason. (working English)
> — PSS Tom 43, pp. 3–361 · fire-metaphor · 1909

> истина христианства, как огонь в костре, который, заглушенный на время наваленным сырым хворостом, уже высушил сырые прутья, начинает охватывать их и выбиваться наружу.
> the truth of Christianity, like a fire in a bonfire which, smothered for a time by piled-on damp brushwood, has already dried the wet twigs and begins to catch them and break out. (working English)
> — PSS Tom 44, pp. 3–390 · fire-metaphor · 1909

> огонь в печи, на пожаре, в свече неравны между собою. В каждом человеке живет дух Божий.
> fire in a stove, in a conflagration, in a candle [are not] unequal to one another. In every person lives the spirit of God. (working English)
> — PSS Tom 44, pp. 3–390 · fire-metaphor · 1909

> Как огонь не бывает немножко горячий, немножко холодный, а бывает огонь только тогда, когда он жжет, так и истина не бывает немножко истина, немножко ложь, а всегда истина
> As fire is never a little hot, a little cold, but is fire only when it burns, so truth is never a little truth, a little falsehood, but is always truth. (working English)
> — PSS Tom 44, pp. 3–390 · fire-metaphor · 1909

### Nicholas II

person · missing · dives: doukhobors

_doukhobors_: Addressee of two petitions citing the Doukhobors as the emblem of religious persecution (1898, 1900).

> И потому, если мы не можем исполнять того, без чего нас нельзя терпеть в государстве, мы просим одно: отпустите нас.
> And so, if we cannot fulfil that without which we cannot be tolerated in the state, we ask one thing only: let us go. (working English)
> — PSS Tom 71, pp. 345–348 · doukhobors · 1898-04-02

> уже давнымъ давно пора: во-первыхъ, пересмотрѣть и уничтожить существующіе теперь законы о гоненіяхъ за вѣру; во-вторыхъ, прекратить всѣ преслѣдованія за отступленія отъ принятаго государствомъ исповѣданія; въ-третьихъ, освободить всѣхъ на основаніи прежнихъ законовъ заключенныхъ и изгнанныхъ за преступленіе противъ вѣры, и въ-четвертыхъ, не казнить, какъ преступленіе, несогласіе религіозной совѣсти съ требованіями государства
> it is long, long since high time: first, to review and abolish the laws now existing on persecution for faith; second, to stop all prosecutions for departure from the state-accepted confession; third, to release all those imprisoned and exiled under the former laws for offences against faith; and fourth, not to punish as a crime the disagreement of religious conscience with the demands of the state. (working English)
> — PSS Tom 72, pp. 514–521 · doukhobors · 1900-12-07

### Nikolai Fedorov

person · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: Librarian of the Rumyantsev Museum and philosopher of the 'Common Task'; an early reader of the gospel synthesis; Tolstoy called him «святой».

> Прошел месяц — самый мучительный в моей жизни. Переезд в Москву.
> (working English) A month has passed — the most agonizing of my life. The move to Moscow.
> — PSS Tom 49, pp. 58 · 1879-1882-a-confession · 1881-10-05 (OS)

> Мне очень тяжело в Москве.
> (working English) Things are very hard for me in Moscow.
> — PSS Tom 63, pp. 80–83 · 1879-1882-a-confession · 1881-11 (OS)

Visuals: 1 (1 usable) — N. F. Fedorov (pastel by L. Pasternak, pre-1903) [PD]

### Nikolai Ge

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Painter and sculptor; Tolstoy's closest artist friend (1882–94); made the 1884 portrait and a bust; his late religious canvases were shaped in dialogue with Tolstoy

> Таков рисунок Крамского, стоящий многих его картин [...] Образцами же в области живописи произведений, вызывающих негодование, ужас пред нарушением любви к Богу и ближнему, могут служить картина Ге — суд
> Such is Kramskoy's drawing, worth many of his paintings [...] As models in painting of works that arouse indignation and horror at the violation of love of God and neighbour, Ge's picture 'The Judgement' can serve. (working English)
> — PSS Tom 30, pp. 27–203 (here ~p.150) · tolstoy-in-art · 1897

> Картина Репина невозможна — всё выдумано. Ге хорош очень.
> Repin's picture is impossible — it is all made up. Ge is very good. (working English)
> — PSS Tom 50, pp. 67–68 · tolstoy-in-art · 1889-04-15

> Приехал Ге старший, привез рисунок картины — очень хорошо.
> Ge the elder arrived, brought a drawing of the picture — very good. (working English)
> — PSS Tom 51, pp. 15 · tolstoy-in-art · 1890-01-28

> Ге всё лепит.
> Ge keeps sculpting. (working English)
> — PSS Tom 51, pp. 95–96 · tolstoy-in-art · 1890-10-23

> которая хороша не потому, что я ее люблю, а всем хороша будет, потому что очень задушевна.
> ...which is good not because I love it but because it will be good for everyone, since it is very heartfelt. (working English)
> — PSS Tom 64, pp. 217–218 · tolstoy-in-art · 1889-01-31

> Я знал эскиз, слышал про картину, но когда увидал, я умилился. Картина делает то, что нужно — раскрывает целый мир той жизни Христа, вне знакомых моментов, и показывает его там таким, каким каждый может себе его представить по своей духовной силе.
> I knew the sketch, had heard about the picture, but when I saw it I was moved to tenderness. The picture does what is needed — it opens up a whole world of that life of Christ, outside the familiar moments, and shows him as each may picture him by his own spiritual strength. (working English)
> — PSS Tom 64, pp. 248–250 · tolstoy-in-art · 1889-04-21

> Бюст сделал большой Гинцбург, нехорош. Репинский похож, но, не для того, чтобы вам сказать приятное, а потому, что так есть, ваш лучше всех.
> Ginzburg has made a large bust [of me], not good. Repin's is a likeness, but — not to flatter you, but because it is so — yours is the best of all. (working English)
> — PSS Tom 66, pp. 24–25 · tolstoy-in-art · 1891-07-30

> «Повинен смерти» необходимо переписать Христа: сделать его с простым, добрым лицом и с выражением сострадания
> ['Guilty of Death'] — Christ must be repainted: make him with a simple, kind face and an expression of compassion. (working English)
> — PSS Tom 66, pp. 258–259 · tolstoy-in-art · 1892-09-22

> Я нынче зимою был три раза в вашей галлерее и всякий раз невольно останавливался перед «Что есть истина»
> This winter I was three times in your gallery and each time involuntarily stopped before 'What Is Truth?'. (working English)
> — PSS Tom 67, pp. 153–155 · tolstoy-in-art · 1894-06-14

Visuals: 4 (4 usable) — Bust of Tolstoy [PD], Portrait of Sofia Andreevna Tolstaya [PD], Portrait of Tolstoy at his desk [PD], What Is Truth? (Christ and Pilate) [PD]

### Nikolai Orlov (painter)

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Peasant-genre painter; Tolstoy's self-declared 'favourite artist'; Tolstoy wrote the preface to his album Russian Peasants (1909)

> Орлов мой любимый художник, а любимый он мой художник потому, что предмет его картин — мой любимый предмет.
> Orlov is my favourite artist, and my favourite because the subject of his pictures is my favourite subject. (working English)
> — PSS Tom 37, pp. 273–277 · tolstoy-in-art · 1908

Visuals: 1 (1 usable) — Russian Peasants (album) — peasant-genre scenes [PD]

### Nikolai Strakhov

person · missing · dives: 1879-1882-a-confession, crisis, gospel-translation, lords-prayer · names: N. N. Strakhov / Nikolai Strakhov

_1879-1882-a-confession_: Philosopher and critic; Tolstoy's chief correspondent through the composition and first reader; accompanied him to Optina Pustyn.
_crisis_: philosopher, close correspondent; recipient of the 'medical кризис' letter (1894); accompanied Tolstoy to Optina Pustyn, 1881
_gospel-translation_: Tolstoy's confidant and critical interlocutor during the gospel years; the addressee who hears the work described as consuming and unpublishable
_lords-prayer_: The confidant who hears the composition-year reactions and supplies the Tischendorf Greek NT — the philological instrument of the translation. Already mapped by the parent dive.

> Разум мне ничего не говорит и не может сказать на три вопроса, которые легко выразить одним: что я такое?
> (working English) Reason tells me nothing, and can say nothing, to the three questions that may easily be put as one: what am I?
> — PSS Tom 62, pp. 379–383 · 1879-1882-a-confession · 1878-01-27 (OS)

> Я очень занят, но не скажу, что пишу
> (working English) I am very busy, but I will not say what I am writing.
> — PSS Tom 62, pp. 500–501 · 1879-1882-a-confession · 1879-11-01 (OS)

> Я очень занят работой для себя, которой никогда не напечатаю
> (working English) I am very busy with work for myself, which I will never print.
> — PSS Tom 62, pp. 501–503 · 1879-1882-a-confession · 1879-11-19 (OS, unsent)

> Из большего сочинения, которое я после вас и кончил, и еще раз все прошел, я сделал еще из Евангелия извлечение без примечаний
> (working English) Out of the larger work, which I finished after seeing you and have gone through once more, I have made besides an extract from the Gospel without notes.
> — PSS Tom 63, pp. 71–73 · 1879-1882-a-confession · 1881-07-01/08 (OS)

> Вы знаете, что Марья Петровна Фет при смерти — крупозное воспаление легких. До сих пор нет кризиса, и шансов смерти, говорят, больше, чем жизни.
> You know that Marya Petrovna Fet is dying — lobar pneumonia. So far there is no crisis, and the chances of death, they say, are greater than of life. (working English)
> — PSS Tom 67, pp. 84 · TEI v67_083_H_N_Straxovu · crisis · 1894-03-16

> работаю очень много и страстно, хотя ничего не пишу.
> I work very much and passionately, though I write nothing. (working English)
> — PSS Tom 62, pp. 471–472 · gospel-translation · 1879-02-13

> занят работой для себя, которой никогда не напечатаю.
> I am occupied with work for myself, which I shall never print. (working English)
> — PSS Tom 62, pp. 501–503 · gospel-translation · 1879-11

> Бумаги измарал много с большим напряжением и не скажу радостью, но с уверенностью, что это так нужно.
> I have covered much paper, with great strain and — I will not say joy, but — with the conviction that it is necessary. (working English)
> — PSS Tom 63, pp. 12–13 · lords-prayer · 1880-02-29

> Я все работаю и не могу оторваться и часто счастлив своей работой, но очень часто слабею головой.
> I keep working and cannot tear myself away, and am often happy in my work, but very often my head grows weak. (working English)
> — PSS Tom 63, pp. 15–16 · lords-prayer · 1880-03-23

> Очень благодарен вам за Тишендорфское евангелие.
> I am very grateful to you for the Tischendorf gospel. (working English)
> — PSS Tom 63, pp. 21–22 · lords-prayer · 1880-09-01

> Из большего сочинения, которое я после вас и кончил, и еще раз все прошел, я сделал еще из Евангелия извлечение без примечаний, но с коротким предисловием
> Out of the larger work, which I have finished since you were here and gone through once more, I have made an extract from the Gospel, without notes but with a short preface… (working English)
> — PSS Tom 63, pp. 71–73 · lords-prayer · 1881-07-01

Visuals: 2 (2 usable) — N. N. Strakhov [PD], Portrait/photograph of N. N. Strakhov [PD]

### Nikolai Yaroshenko

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Painter; portrait of Tolstoy 1894

> Провожали нас Соловьев и Ярошенко, с которым приятно сблизился.
> Solovyov and Yaroshenko saw us off — Yaroshenko, with whom I have grown pleasantly close. (working English)
> — PSS Tom 52, pp. 116–117 · tolstoy-in-art · 1894-05-03

Visuals: 1 (1 usable) — Portrait of Tolstoy [PD]

### Non-resistance

concept · missing · dives: christian-anarchism

_christian-anarchism_: The religious substance Tolstoy affirms in place of the political label. The Eltzbacher index argument turns on it: Eltzbacher's book has no Tolstoy reference under 'violence' because Tolstoy treated the matter as non-resistance (religion), not violence (politics).

> Мне кажется только, что я не анархист в смысле политического реформатора. В оглавлении вашей книги под словом «насилие» сделаны указания на разные страницы из других сочинений, но ни одной ссылки на мои. Не доказательство ли это того, что то учение, которое вы мне приписываете и которое, в сущности, есть не что иное, как учение Христа, вовсе не политическое, а религиозное учение?
> It seems to me only that I am not an anarchist in the sense of a political reformer. In the index of your book under the word 'violence' references are made to various pages of the other writers, but not one to mine. Is this not proof that the teaching which you ascribe to me, and which is, in essence, nothing other than the teaching of Christ, is not a political but a religious teaching? (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

### O zhizni

work · missing · dives: fire-metaphor

_fire-metaphor_: Fire/light fused as the continuous life-force; 'the sun of reason'

> Я видел свет от горевшей передо мной травы. Трава эта потухла, но свет только усилился: я не вижу причины этого света, не знаю, чтò горит, но могу заключить, что тот же огонь, который сжег эту траву, жжет теперь дальний лес, или что-то такое, чего я не могу видеть.
> I saw the light from the grass that burned before me. That grass went out, but the light only grew stronger: I do not see the cause of this light, I do not know what is burning, but I can conclude that the same fire that burned this grass is now burning the distant forest, or something of the kind that I cannot see. (working English)
> — PSS Tom 26, pp. 313–442 · fire-metaphor · 1887

> свет солнца разума есть только незначущая случайность, сентиментальные, мистические слова.
> the light of the sun of reason is only an insignificant accident — sentimental, mystical words — so it appears to those not yet awake to it. (working English)
> — PSS Tom 26, pp. 313–442 · fire-metaphor · 1887

### Optina Pustyn

place · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: The monastery Tolstoy visited (with Strakhov) in summer 1881 as the work neared its finished form.

> Из большего сочинения, которое я после вас и кончил, и еще раз все прошел, я сделал еще из Евангелия извлечение без примечаний
> (working English) Out of the larger work, which I finished after seeing you and have gone through once more, I have made besides an extract from the Gospel without notes.
> — PSS Tom 63, pp. 71–73 · 1879-1882-a-confession · 1881-07-01/08 (OS)

### Otche nash (Tolstoy)

concept · missing · dives: lords-prayer

_lords-prayer_: The subject of this dive: Tolstoy's family of renderings of the Lord's Prayer, his anti-petitionary reading, and the glory→reason / kingdom→spirit substitutions. A concept page anchored in the two works.

> Так вот как молитесь: Отец! Чтобы было твое царство. Пусть будет твоя воля в тебе и во мне.
> So pray thus: Father! That thy kingdom be. May thy will be in thee and in me. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> И Иисус сказал им: когда молитесь, говорите: Отец! да будешь ты свят в нас, да объявится царство твое, т. е. да будет воля твоя; да сойдет в нас дух твой и очистит нас.
> And Jesus said to them: when you pray, say: Father! mayest thou be holy in us, may thy kingdom be made manifest, that is, may thy will be done; may thy spirit descend into us and cleanse us. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Как еще яснее сказать, что не нужно молиться?
> How could it be said more plainly that one must not pray? (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Окончив свою работу, я к удивлению и радости своей нашел, что так называемая молитва господня есть не что иное, как в самой сжатой форме выраженное всё учение Иисуса в том самом порядке, в котором были расположены мною главы, и что каждое выражение молитвы соответствует смыслу и порядку глав.
> On finishing my work I found, to my surprise and joy, that the so-called Lord's Prayer is nothing other than the whole teaching of Jesus expressed in the most condensed form, in the very order in which I had arranged the chapters, and that each phrase of the prayer corresponds to the sense and order of the chapters. (working English)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

> А будет твоя власть, и сила, и разум.
> But there will be thy power, and strength, and reason. (working English) — Tolstoy's meaning for the doxology (phrase 12 of 12)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

> Молитесь только так: Отец наш безначальный и бесконечный, как небо! Пусть будет свято только твое существо. Пусть будет власть только твоя, так, чтобы воля твоя совершалась безначально и бесконечно на земле. Дай мне пищу жизни в настоящем. Ошибки мои прежние загладь и сотри так же, как и я заглаживаю и стираю все ошибки братьев моих, чтобы я не попал в соблазн, избавился от зла. Потому что твоя власть и сила и твое решение.
> Pray only thus: Our Father, without beginning and without end, like the sky! May thy being alone be holy. May power alone be thine, so that thy will be done, without beginning and without end, on earth. Give me the food of life in the present. My former mistakes, efface and wipe them out, just as I efface and wipe out all the mistakes of my brothers, so that I may not fall into temptation, and may be delivered from evil. Because thine is the power and the strength and thine the decision. (working English)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

### Otets Sergij

work · missing · dives: fire-metaphor

_fire-metaphor_: Fiction: the burning lamp whose «божеский свет истины» dims when holiness is performed for people

> Он думал о том, что он был светильник горящий, и чем больше он чувствовал это, тем больше он чувствовал ослабление, потухание божеского света истины, горящего в нем.
> He thought that he was a burning lamp, and the more he felt this, the more he felt the weakening, the dying-out of the divine light of truth burning within him. (working English)
> — PSS Tom 31, pp. 5–46 · fire-metaphor · 1898

### Paul Eltzbacher

person · missing · dives: christian-anarchism

_christian-anarchism_: Berlin legal scholar (1868–1928); his Der Anarchismus (1900) classified Tolstoy as one of seven principal anarchist thinkers. Addressee of the 1900 letter; his index is the evidence Tolstoy turns against the classification.

> Ваша книга делает для анархизма то, что 30 лет назад было сделано для социализма: вводит его в программу политических наук. Ваша книга мне чрезвычайно понравилась. Она совершенно объективна, понятна, и, насколько я могу судить, источники в ней отлично использованы.
> Your book does for anarchism what was done thirty years ago for socialism: it brings it into the programme of the political sciences. Your book pleased me exceedingly. It is entirely objective, intelligible, and — so far as I can judge — the sources in it are excellently handled. (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

> Mir scheint nur, dass ich kein Anarchist bin im Sinne eines politischen Reformators. Im Register Ihres Buches beim Worte: «Zwang» sind verschiedene Seiten bei allen anderen angegeben, aber keine in meinen Schriften. Ist das nicht ein Beweis, dass die Lehre, die Sie mir zuschreiben, aber die eigentlich nur die Lehre Christi ist, keine politische aber eine religiöse Lehre ist?
> [Tolstoy's German original of the same passage] It seems to me only that I am not an anarchist in the sense of a political reformer. In the register of your book under the word 'Zwang' [coercion] various pages are given for all the others, but none in my writings. Is this not a proof that the teaching you ascribe to me, but which is really only the teaching of Christ, is not a political but a religious teaching? (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

> Мне кажется только, что я не анархист в смысле политического реформатора. В оглавлении вашей книги под словом «насилие» сделаны указания на разные страницы из других сочинений, но ни одной ссылки на мои. Не доказательство ли это того, что то учение, которое вы мне приписываете и которое, в сущности, есть не что иное, как учение Христа, вовсе не политическое, а религиозное учение?
> It seems to me only that I am not an anarchist in the sense of a political reformer. In the index of your book under the word 'violence' references are made to various pages of the other writers, but not one to mine. Is this not proof that the teaching which you ascribe to me, and which is, in essence, nothing other than the teaching of Christ, is not a political but a religious teaching? (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

Visuals: 2 (2 usable) — Paul Eltzbacher, photographic portrait [PD], PSS Tom 72 p.442 — the Eltzbacher letter, the «я не анархист в смысле политического реформатора» passage (rendered from the local PD PSS PDF) [PD]

### Pavel Birukoff

person · exists · dives: 1879-1882-a-confession, biryukov-sofia-relationship, copyright-renunciation, crisis, doukhobors · names: Pavel Biryukov / Pavel Birukoff

_1879-1882-a-confession_: Biographer; the standard authorised Life is a key secondary anchor for the composition story.
_biryukov-sofia-relationship_: Tolstoy's disciple and authorized biographer; subject of the dive. (Vault file spells the name 'Pavel Birukoff'.)
_copyright-renunciation_: correspondent in the earliest sustained free-publication discussion (1885); later biographer
_crisis_: biographer; the framing source is his Swedish ed. (Leo Tolstoj: Hans liv och verk) Book IV «Kritisk period» ch.14 «Krisen» p.262 — names the chapter 'crisis' while reporting Tolstoy's denial of one (user-provided photograph)
_doukhobors_: Sent to the Caucasus 1895 to verify the facts; wrote the article Tolstoy afterworded; co-signed «Help!» and was exiled. Tolstoy's biographer.

> Ni har ock afvärjt mycken ofärd från hans hufvud.
> You have also averted much misfortune from his head. (working English) — source language Swedish.
> — Vol II front matter · biryukov-sofia-relationship · 1908-01-11

> S. A. Tolstojs arkiv.
> The archive of S. A. Tolstaya. (working English) — footnote sourcing the volume's closing quotation; documentary sign of Sofia's cooperation.
> — Vol II p. 453 · biryukov-sofia-relationship · 1908-08-27

> правдивее даже, чем Руссо
> more truthful even than Rousseau. (working English)
> — PSS Tom 73, pp. 315 · biryukov-sofia-relationship · 1902-08-20

> это была Арсеньева Валерия. Она теперь жива, за Волковым была, живет в Париже.
> that was Arsenyeva, Valeria. She is alive now, was married to Volkov, lives in Paris. (working English)
> — PSS Tom 74, pp. 319 · biryukov-sofia-relationship · 1903-11-27

> Неужели только биография?
> Surely not just for the biography? (working English)
> — PSS Tom 82, pp. 172 · biryukov-sofia-relationship · 1910-09-01

- PSS Tom 63, pp. 295–298 · copyright-renunciation · 1885-10-19 — Earliest sustained discussion of free publication in the letters (the Posrednik / cheap-edition circle). Cited by id and PSS pages; not quoted verbatim because the clean extract of this early-volume pre-reform text renders unreliably (see needsReview).

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

> Сколько бы ни набрасывали на горящую кучу хвороста дров, думая этим затушить огонь, — огонь, непотухающий огонь истины, только на время приглохнет, но разгорится еще сильнее и сожжет всё то, что наложено на него.
> However much firewood is thrown onto the burning heap of brush in the hope of putting the fire out, the fire — the unquenchable fire of truth — will only die down for a time, then blaze up the more strongly and burn everything that has been piled upon it. (working English)
> — PSS Tom 39, pp. 99–105 · doukhobors · 1895-10-01

Visuals: 4 (3 usable) — Maria (Masha) Lvovna Tolstaya, by P. Biryukov, Yasnaya Polyana 1895 [PD], Pavel Biryukov (1916) [PD], Pavel Biryukov [PD], Pavel Biryukov [unknown]

### Pavel Biryukov

person · missing · dives: fire-metaphor

_fire-metaphor_: Biographer who closed vol. II of his Tolstoy biography on the fire+light credo

> что этот талант есть огонь, который только тогда огонь, когда он жжет. Я верю, что я — Ниневия по отношению к другим Ионам, от которых я узнал и узнаю истину, но что и я Иона по отношению к другим ниневитянам, которым я должен передать истину.
> that this talent is a fire which is only a fire when it burns. I believe that I am a Nineveh in relation to other Jonahs, from whom I have learned and learn the truth, but that I too am a Jonah in relation to other Ninevites, to whom I must pass the truth on. (working English)
> — PSS Tom 23, pp. 461 · fire-metaphor · 1884

### Pavel Tretyakov

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Collector; commissioned the 1873 Kramskoy portrait; recipient of Tolstoy's 1894 plea to acquire Ge's estate

> Я нынче зимою был три раза в вашей галлерее и всякий раз невольно останавливался перед «Что есть истина»
> This winter I was three times in your gallery and each time involuntarily stopped before 'What Is Truth?'. (working English)
> — PSS Tom 67, pp. 153–155 · tolstoy-in-art · 1894-06-14

### Prokudin-Gorsky Collection Library of Congress

archival-fond · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: high-resolution master of the 1908 colour Tolstoy portrait; 'no known restrictions on publication'

> Прости, что не сам решил, а утруждаю тебя.
> Forgive me for not deciding myself but troubling you (working English)
> — PSS Tom 84, pp. 382 · tolstoy-in-photographs · 1908-03-30

### Put zhizni

work · missing · dives: fire-metaphor

_fire-metaphor_: His last book; the keystone returns; the candle/divine-fire aphorisms

> Как свеча не может гореть без огня, так человек не может жить без духовной силы.
> As a candle cannot burn without fire, so a person cannot live without spiritual force. (working English)
> — PSS Tom 45, pp. 13–496 · fire-metaphor · 1910

> Если я растоплюсь на божьем огне, то бог оттиснет на мне свой образ.
> If I am melted in God's fire, then God will stamp his image upon me. (working English)
> — PSS Tom 45, pp. 13–496 · fire-metaphor · 1910

> «Огонь пришел я низвесть на землю: и как желал бы, чтобы он уже возгорелся» (Луки XII, 49). Но почему же огонь этот так медленно разгорается?
> "Fire I came to cast upon the earth: and how I would wish that it were already kindled" (Luke XII, 49). But why does this fire blaze up so slowly? (working English)
> — PSS Tom 45, pp. 13–496 · fire-metaphor · 1910

### Pyotr Verigin

person · missing · dives: doukhobors

_doukhobors_: Doukhobor leader; exiled to Arkhangelsk then Siberia; from exile urged literal Christianity. Emigrated to Canada 1902.

> С духоборцами случилось то, что обыкновенно случается с замыкающимися в самих себя и вследствие того процветающими религиозными общинами: материальное благосостояние их увеличивается, но религиозное сознание понижается.
> What happened with the Doukhobors is what usually happens with religious communities that close in upon themselves and prosper as a result: their material well-being increases, but their religious consciousness declines. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

> теперь же нельзя предоставлять одним врагам это могущественное орудие для обмана, и не пользоваться книгой или письмом для передачи своих мыслей и восприятия мыслей других людей
> but now one cannot leave this mighty instrument of deception to the enemies alone, and not make use of the book or the letter to convey one's own thoughts and to receive the thoughts of others. (working English)
> — PSS Tom 68, pp. 262–266 · doukhobors · 1895-11-21

Visuals: 2 (2 usable) — Pyotr Verigin in British Columbia, 1907 [PD], Pyotr Verigin, portrait, 1922 [PD]

### razumenie

concept · missing · dives: lords-prayer

_lords-prayer_: Tolstoy's keyword: glory→разум in the prayer's close, and разумение as the creditor in the debt gloss. The same concept the sibling fire-metaphor dive tracks (John 1 Logos → разумение).

> Мы обязаны жизнью разумению, а не отдаем ему всю свою плотскую жизнь, и потому мы должники неоплатные.
> We owe our life to reason, yet do not give over to it our whole fleshly life, and so we are debtors who can never pay. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> А будет твоя власть, и сила, и разум.
> But there will be thy power, and strength, and reason. (working English) — Tolstoy's meaning for the doxology (phrase 12 of 12)
> — PSS Tom 24, pp. 801–938 · lords-prayer · 1881

### Rumyantsev Museum

place · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: Where Tolstoy read and met Fedorov while wrestling with the questions that became A Confession.

> Мне очень тяжело в Москве.
> (working English) Things are very hard for me in Moscow.
> — PSS Tom 63, pp. 80–83 · 1879-1882-a-confession · 1881-11 (OS)

### Russian State Library

institution · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: provided the electronic scans of the 90 volumes that the crowdsourcing project proofread

> Подготовлено на основе электронной копии 53-го тома Полного собрания сочинений Л. Н. Толстого, предоставленной Российской государственной библиотекой
> Prepared on the basis of an electronic copy of volume 53 of the Complete Collected Works of L. N. Tolstoy, provided by the Russian State Library. (working English)
> — PSS Tom 53 · jubilee-edition-tei-corpus

### Sergei Levitsky

person · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: photographer of the 1856 Sovremennik writers' group portrait and an 1856 solo officer portrait

> по моему предложению, все литераторы сделали фотографическую группу
> at my proposal, all the literary men had a photographic group made (working English)
> — PSS Tom 61, pp. 372–374 · tolstoy-in-photographs · 1856-04-14

Visuals: 2 (2 usable) — Tolstoy as a young army officer (solo) [PD], Sovremennik writers group: Goncharov, Turgenev, Tolstoy (in uniform), Grigorovich, Druzhinin, Ostrovsky [PD]

### Sergei Prokudin-Gorsky

person · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: made the only colour photograph of Tolstoy, Yasnaya Polyana, 23 May 1908 (OS)

> Прости, что не сам решил, а утруждаю тебя.
> Forgive me for not deciding myself but troubling you (working English)
> — PSS Tom 84, pp. 382 · tolstoy-in-photographs · 1908-03-30

Visuals: 1 (1 usable) — Tolstoy seated at Yasnaya Polyana — the only colour photograph of him [PD]

### Smert Ivana Ilicha

work · missing · dives: fire-metaphor

_fire-metaphor_: Fiction: life as light, death as its extinction («То свет был, а теперь мрак»)

> То свет был, а теперь мрак.
> Once there was light, and now there is darkness. (working English)
> — PSS Tom 26, pp. 61–113 · fire-metaphor · 1886

### Soedinenie i perevod chetyrekh Evangelij

work · missing · dives: fire-metaphor, gospel-translation, lords-prayer · names: The Gospel in Brief / The Four Gospels Harmonized (Соединение и перевод четырёх Евангелий) / Union and Translation of the Four Gospels (Соединение и перевод четырёх Евангелий)

_fire-metaphor_: The text where Tolstoy rewrites the Bible's fire/light language; the special-attention source
_gospel-translation_: The full harmony itself — the work this dive is about; composed 1880–81, first legal Russian printing 1957 (PSS Tom 24)
_lords-prayer_: The full harmony — holds Version A (Matthew) and Version B (Luke) of the prayer plus the anti-petitionary commentary. Owned by the parent gospel-translation dive; here it is the source of the prayer renderings.

> Я пришел сбросить огонь на землю. И как желаю, чтобы он разгорелся.
> I came to cast fire upon the earth. And how I wish that it would blaze up. (working English)
> — PSS Tom 24, pp. 292 · fire-metaphor · 1880-1881

> Есть перерождение, через которое я должен пройти, и я томлюсь, пока оно не совершится.
> There is a rebirth through which I must pass, and I am in anguish until it is accomplished. (working English)
> — PSS Tom 24, pp. 292 · fire-metaphor · 1880-1881

> была долина, в которой, принося жертву Молоху, жгли людей. В геенну отдать — значить сжечь.
> was a valley in which, offering sacrifice to Moloch, they burned people. To give over to Gehenna means to burn. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> Так же как свет в темноте светит, и темнота его не поглощает.
> Just as light shines in the darkness, and the darkness does not swallow it. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> И разумение-то жизни стало Бог.
> And the reason/understanding of life became God. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> 9) Φῶς — свет — по всем контекстам означает истинное разумение жизни.
> 9) Φῶς — light — in all contexts means the true reason/understanding of life. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> он знал, что его учение — не учение, но искра, которая зажигает сознание Бога в сердцах людей и, раз загоревшись, не может потухнуть.
> he knew that his teaching was not a doctrine but a spark that kindles the consciousness of God in people's hearts and, once lit, cannot go out. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> Тогда скажет тем, которые налево: идите от меня прочь вы, нелюбимые, в тьму внешнюю,
> Then he will say to those on the left: go away from me, you unloved ones, into the outer darkness, (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> Он говорил: очищаю вас водой, но после меня тот, кто сильнее меня, очистит вас духом. Когда он придет, он очистит вас, как хозяин очищает гумно свое: пшеницу соберет, а мякину сожжет.
> He said: I cleanse you with water, but after me the one stronger than me will cleanse you with spirit. When he comes, he will cleanse you as a master cleanses his threshing-floor: the wheat he will gather, and the chaff he will burn up. (working English)
> — PSS Tom 24, pp. 7–798 · fire-metaphor · 1880-1881

> Кто пойдет за мной, тот не будет во тьме, а у того будет жизнь. Жизнь и свет одно и то же.
> Whoever follows me will not be in darkness, but will have life. Life and light are one and the same. (working English)
> — PSS Tom 24, pp. 801–938 · fire-metaphor · 1881

> Разумение — это свет истины. А свет светит в темноте, и темнота не может погасить его.
> Reason/understanding is the light of truth. And the light shines in the darkness, and the darkness cannot extinguish it. (working English)
> — PSS Tom 24, pp. 801–938 · fire-metaphor · 1881

> Лук. XII, 49. Учение мое, как огонь, запалит мир.
> Luke XII, 49. My teaching, like fire, will set the world ablaze. (working English)
> — PSS Tom 24, pp. 801–938 · fire-metaphor · 1881

> Mon enseignement est comme le feu jeté dans le monde. Il fera beaucoup de ravages
> My teaching is like fire thrown into the world. It will do great damage [before it sets all men ablaze]. (working English) — source text is French
> — PSS Tom 24, pp. 941–969 · fire-metaphor · 1880-1881

> учение истинное представляет как бы круг, которого все части одинаково определяют значение друг друга и для изучения которого безразлично начинание изучения с одного или другого места.
> the true teaching presents itself as a kind of circle, all of whose parts equally define one another's meaning, and for the study of which it is a matter of indifference where one begins. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

> я неизбежно был приведен к необходимости свести четыре Евангелия в одно, так как все они излагают, хотя и разноречиво, одни и те же события и одно и то же учение.
> I was inevitably led to the necessity of bringing the four Gospels together into one, since all of them set out, however divergently, the same events and the same teaching. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

> Читал я по-гречески, на том языке, на котором оно есть у нас, и переводил так, как указывал смысл и лексиконы
> I read in Greek, the language in which we have it, and translated as the sense and the lexicons indicated. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

> Попыток соединения Евангелий в одно было много, но те все, которые я знаю, — Arnolde, de Vence, Фаррара, Рейса, Гречулевича, — все они берут исторические основы соединения, и все они безуспешны
> There have been many attempts to combine the Gospels into one, but all those I know — Arnolde, de Vence, Farrar, Reuss, Grechulevich — all take historical bases for the combination, and all are unsuccessful. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

> В православном вероучении я нашел изложение самых непонятных, кощунственных и безнравственных положений, не только не допускаемых разумом, но совершенно непостижимых и противных нравственности, и — никакого учения о жизни и о смысле ее.
> In the Orthodox creed I found an exposition of the most incomprehensible, blasphemous and immoral propositions — not only inadmissible to reason but utterly incomprehensible and contrary to morality — and no teaching whatever about life or its meaning. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

> искусственные и, вероятно, неправильные филологические разъяснения, которые не только не усиливают убедительность общего смысла, но должны ослаблять ее.
> artificial and probably incorrect philological explanations, which not only fail to strengthen the persuasiveness of the general sense but must weaken it. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1902

> обратился к изучению Евангелий.
> I turned to the study of the Gospels. (working English)
> — PSS Tom 24, pp. 7–798 · gospel-translation · 1880-1881

> неверно переведено: «насущный» — хлеб на этот день; слово это значит: необходимый.
> …wrongly translated 'daily' — bread for this day; this word means: necessary. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> И прости нам наши вины за то, что мы прощаем всякому, кто виноват перед нами.
> And forgive us our faults because we forgive everyone who is at fault before us. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> «Как на небе и на земле» я перевожу: «в тебе и во мне».
> 'As in heaven and on earth' I translate: 'in thee and in me'. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Так вот как молитесь: Отец! Чтобы было твое царство. Пусть будет твоя воля в тебе и во мне.
> So pray thus: Father! That thy kingdom be. May thy will be in thee and in me. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Дай нам питание духа, то, которое дает жизнь.
> Give us the nourishment of the spirit, that which gives life. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Мы обязаны жизнью разумению, а не отдаем ему всю свою плотскую жизнь, и потому мы должники неоплатные.
> We owe our life to reason, yet do not give over to it our whole fleshly life, and so we are debtors who can never pay. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> И не взыскивай с нас всё, чем мы должны, потому что и мы не взыскиваем с тех, что нам должны. И не считайся с нами.
> And do not exact from us all that we owe, because we too do not exact from those who owe us. And do not reckon with us. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> И Иисус сказал им: когда молитесь, говорите: Отец! да будешь ты свят в нас, да объявится царство твое, т. е. да будет воля твоя; да сойдет в нас дух твой и очистит нас.
> And Jesus said to them: when you pray, say: Father! mayest thou be holy in us, may thy kingdom be made manifest, that is, may thy will be done; may thy spirit descend into us and cleanse us. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> слова: да сойдет дух твой в нас и очистит нас встречаются в цитатах древних церковных писателей.
> the words 'may thy spirit descend into us and cleanse us' are found in citations of ancient church writers. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Вся молитва должна состоять в желании царства Божия и в исполнении его правил, а все правила в том, чтобы не считать никого виновным, а всех любить и прощать.
> The whole prayer must consist in the desire for God's kingdom and in the fulfilment of its rules, and all the rules are: to hold no one guilty, but to love and forgive everyone. (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

> Как еще яснее сказать, что не нужно молиться?
> How could it be said more plainly that one must not pray? (working English)
> — PSS Tom 24, pp. 7–798 · lords-prayer · 1880-1881

Visuals: 2 (2 usable) — Gospel harmony, Luke 12:49-50 — Tolstoy's translation beside the standard text (PSS Tom 24, printed p.292) [PD], Leo Tolstoy, half-length portrait, 1880 — the year he began the harmony [PD]

### Sophia Tolstaya

person · exists · dives: 1879-1882-a-confession, biryukov-sofia-relationship, copyright-renunciation, gospel-translation, tolstoy-in-photographs · names: S. A. Tolstaya (Sofia Andreyevna) / Sofia Tolstaya / Sophia Tolstaya / Sofia Andreevna Tolstaya

_1879-1882-a-confession_: Wife; copyist of several manuscripts; diarist of the crisis; sought to publish the work in her collected editions (1885, 1911).
_biryukov-sofia-relationship_: Dedicatee of Vol II; archive-keeper; vetoed the Arsenyeva letters; seized the 1910 diary. (Vault file spells the name 'Sophia Tolstaya'.)
_copyright-renunciation_: opposed the 1891 renunciation; redacted 19 lines of the 22 July 1891 diary entry
_gospel-translation_: Tolstoy's wife; her diaries are the primary witness to the work's domestic strain. The dive's evidence COMPLICATES the 'domestic-tragedy' frame (she names the cause yet accepts it as God's will)
_tolstoy-in-photographs_: prolific domestic photographer (~1,000 photos from late 1880s); destroyed the Dec-1894 negatives

> Прошел месяц — самый мучительный в моей жизни. Переезд в Москву.
> (working English) A month has passed — the most agonizing of my life. The move to Moscow.
> — PSS Tom 49, pp. 58 · 1879-1882-a-confession · 1881-10-05 (OS)

> Ni har ock afvärjt mycken ofärd från hans hufvud.
> You have also averted much misfortune from his head. (working English) — source language Swedish.
> — Vol II front matter · biryukov-sofia-relationship · 1908-01-11

> Соня без меня читала этот дневник, и ее очень огорчило то, что из него могут потом заключить о том, что она была нехорошей женой.
> Sonya read this diary while I was away, and it grieved her greatly that from it people might later conclude she had been a bad wife. (working English)
> — PSS Tom 53, pp. 132 · biryukov-sofia-relationship · 1897-02-04

> нашла и унесла мой дневник маленький.
> [she] found and carried off my little diary. (working English) — reconstructed from TEI reg, cross-checked vs facsimile.
> — PSS Tom 58, pp. 141 · biryukov-sofia-relationship · 1910-10-13

> Софья Андреевна всё так же любит вас, чему я очень радуюсь.
> Sofia Andreevna loves you just as before, at which I greatly rejoice. (working English)
> — PSS Tom 70, pp. 57 · biryukov-sofia-relationship · 1897-03-12

> протестовала против писем Арсеньевой.
> [Sofia Andreevna] protested against the Arsenyeva letters. (working English)
> — PSS Tom 76, pp. 65 · biryukov-sofia-relationship · 1905-10-18

> почти душевно больна — ненависть к Черткову, ревность к нему, и мне очень трудно.
> almost mentally ill — hatred of Chertkov, jealousy of him, and it is very hard for me. (working English)
> — PSS Tom 82, pp. 95 · biryukov-sofia-relationship · 1910-07-19

> И вчера же был разговор с женой о напечатании письма в газетах об отказе от права авторской собственности. Трудно вспомнить, а главное, описать всё, что тут было: [Вымарано 19 строк.]
> And yesterday too there was a conversation with my wife about printing in the newspapers the letter renouncing the right of literary property. It is difficult to recall, and chiefly to describe, everything that was said: [19 lines erased.] (working English)
> — PSS Tom 52, pp. 45–47 · copyright-renunciation · 1891-07-22

> Чувствую себя работающей машиной, хотелось бы жизни немного для себя, да нет ее.
> I feel like a working machine; I would like a little life for myself, but there is none. (working English)
> — gospel-translation · 1878-11-10

> он вял, молчалив и сосредоточен. Все читает.
> he is listless, silent and absorbed. He keeps reading. (working English)
> — gospel-translation · 1878-10-18

> Он много пишет о религиозном.
> He writes a great deal about the religious. (working English)
> — gospel-translation · 1879-12-18

> его христианское настроение слишком не уживается с условиями роскоши, тунеядства, борьбы городской жизни.
> his Christian mood is too incompatible with the conditions of luxury, idleness and the struggle of city life. (working English)
> — gospel-translation · 1882-02-28

> Он сегодня громко вскрикнул, что самая страстная мысль его о том, чтоб уйти от семьи. [...] Он проникся христианством и мыслями о самосовершенствованье. Я ревную его...
> Today he cried out aloud that his most passionate thought is to leave the family. […] He has become imbued with Christianity and with thoughts of self-perfection. I am jealous of it… (working English)
> — gospel-translation · 1882-08-26

> эта работа нескончаемая, потому что не может быть напечатана.
> this work is endless, because it cannot be printed. (working English)
> — gospel-translation · 1883-03-05

> она разложила карточки всех детей, кроме Ванички, и гордится и любуется. Трогательно.
> she laid out the cards of all the children except Vanichka, and takes pride and delight in them. Touching. (working English)
> — PSS Tom 52, pp. 19–20 · tolstoy-in-photographs · 1891-03-13

> История с фотографией очень грустная. Все они оскорблены. Я написал письмо Черткову.
> The story with the photograph is very sad. They are all offended. I wrote a letter to Chertkov. (working English)
> — PSS Tom 53, pp. 2 · tolstoy-in-photographs · 1895-01-03

> Мама целый день занимается фотографией. Она сняла несколько раз Козловку и группу нас всех.
> Mama spends the whole day on photography. She photographed Kozlovka [station] several times, and a group of all of us. (working English)
> — PSS Tom 69, pp. 161 · tolstoy-in-photographs · 1896-10-10

Visuals: 11 (11 usable) — Sofia Andreevna Tolstaya, 1908 [PD], Sofia Tolstaya (formal portrait) [PD], Sofia Tolstaya (oil, N. Ge 1886) [PD], Leo and Sofia Tolstoy, 1910 [PD], Leo and Sofia Tolstoy, 19 Sept 1910 [PD], Sofia Andreevna Tolstaya, photograph c.1875 (the 'before') [PD], The Tolstoy family — Nikolai Ge, 1886 [PD], Tolstoy with his wife, a son, and a dog at Yasnaya Polyana, c.1880s [PD], Tolstoy and Maxim Gorky at Yasnaya Polyana [PD], Tolstoy and Sofia Andreevna at Yasnaya Polyana [PD], Tolstoy and Sofya at Yasnaya Polyana, weeks before his flight [PD]

### Spiritual crisis (perevorot)

concept · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: The transformation A Confession narrates; Tolstoy's own word was «переворот», not 'crisis'/'conversion'.

> Эти остановки жизни выражались всегда одинаковыми вопросами: Зачем? Ну, а потом?
> (working English) These stoppages of life always expressed themselves in the same questions: Why? And then what?
> — PSS Tom 23, pp. ch. III · 1879-1882-a-confession · 1879–1882

> Жизнь моя остановилась. Я мог дышать, есть, пить, спать, и не мог не дышать, не есть, не пить, не спать; но жизни не было, потому что не было таких желаний, удовлетворение которых я находил бы разумным.
> (working English) My life came to a stop. I could breathe, eat, drink, sleep, and could not help breathing, eating, drinking, sleeping; but there was no life, because there were no desires whose satisfaction I found reasonable.
> — PSS Tom 23, pp. ch. IV · 1879-1882-a-confession · 1879–1882

> перемена, о которой я говорю в «Исповеди», произошла не сразу, но что те же идеи, которые яснее выражены в моих последних произведениях, находятся в зародыше в более ранних.
> (working English) the change I speak of in The Confession did not happen all at once, but the same ideas, expressed more clearly in my later works, are present in embryo in the earlier ones.
> — PSS Tom 66, pp. 188–189 · 1879-1882-a-confession · 1892-04-01 (OS)

### State Tolstoy Museum

institution · missing · dives: copyright-renunciation, jubilee-edition-tei-corpus · names: State Tolstoy Museum (GMT) / State Museum of L. N. Tolstoy (GMT)

_copyright-renunciation_: holds the diary and letter manuscripts cited here (manuscript fond, the 'steel room')
_jubilee-edition-tei-corpus_: Moscow museum (Prechistenka 11); co-initiator of the digitisation; holds the editorial archive and the photo collection catalogued in listMedia.xml

> 4) Право на издание моих сочинений прежних: десяти томов и азбуки прошу моих наследников передать обществу, т. е. отказаться от авторского права. Но только прошу об этом и никак не завещаю. […] То, что сочинения мои продавались эти последние 10 лет, было самым тяжелым для меня делом в жизни.
> 4) I ask my heirs to hand over to the public the right of publication of my earlier works — the ten volumes and the Azbuka — that is, to renounce the copyright. But I only ask this and in no way bequeath it. […] That my writings have been sold during these last ten years was the heaviest thing in my life. (working English)
> — PSS Tom 53, pp. 14–18 · copyright-renunciation · 1895-03-27

> Государственный музей Л. Н. Толстого
> State Museum of L. N. Tolstoy (the holding repository on a media record). (working English)
> — jubilee-edition-tei-corpus

Visuals: 2 (1 usable) — State Tolstoy Museum digital collection (manuscripts, photographs, portraits) [rights-reserved], State L. N. Tolstoy Museum, Prechistenka 11, Moscow (facade) [CC-BY-SA]

### State Tretyakov Gallery

institution · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Holds the Kramskoy 1873, Ge 1884, Ge 'What Is Truth?' 1890, Repin 1887/1887-ploughing/1891-forest portraits

> У меня каждый день, вот уже с неделю, живописец Крамской [...] делает мой портрет в Третьяковскую галлерею, и я сижу и болтаю с ним и из Петербургской стараюсь обращать его в крещеную веру.
> Every day now, for a week already, the painter Kramskoy has been making my portrait for the Tretyakov gallery, and I sit and chat with him and try to convert him from the Petersburg faith to the baptized one. (working English)
> — PSS Tom 62, pp. 48–49 · tolstoy-in-art · 1873-09-23

> Я нынче зимою был три раза в вашей галлерее и всякий раз невольно останавливался перед «Что есть истина»
> This winter I was three times in your gallery and each time involuntarily stopped before 'What Is Truth?'. (working English)
> — PSS Tom 67, pp. 153–155 · tolstoy-in-art · 1894-06-14

### The Burning of Arms

event · missing · dives: doukhobors

_doukhobors_: The coordinated mass destruction of weapons by ~7,000 Doukhobors, night of 28–29 June 1895 (OS); the catalysing event.

> После этого, 28 июня 1895 года, духоборцы, живущие в Ахалкалакском уезде Тифлисской губернии, снесли в одну кучу в поле, около села Спасского, всё свое имевшееся у них оружие и, обложив его дровами и углем и облив керосином, сожгли
> After this, on 28 June 1895, the Doukhobors living in the Akhalkalaki district of the Tiflis province carried all the weapons they had into a single heap in a field near the village of Spasskoye and, having piled wood and coal upon them and doused them with kerosene, burned them. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

Visuals: 1 (1 usable) — PSS Tom 39 p.209 — the Burning of Arms paragraph (rendered from the local PD PSS PDF) [PD]

### The Kingdom of God Is Within You

criticalWork · stub · dives: doukhobors, fire-metaphor · names: The Kingdom of God Is Within You / The Kingdom of God Is Within You (Царство Божие внутри вас)

_doukhobors_: The 1893 doctrinal foundation: refusal of military service, the position the Doukhobors enacted.
_fire-metaphor_: Takes Luke 12:49 as the motif of the spreading new consciousness

> Только что он затушит пожар в одном месте, загорается в двух других; только что он уступает огню, отломает то, что загорелось, от большого здания, — загорается с двух концов и это здание.
> No sooner does he put out the fire in one place than it flares up in two others; no sooner does he yield to the fire and break off what has caught from the large building than that building too catches at both ends. (working English)
> — PSS Tom 28, pp. 1–293 · fire-metaphor · 1893

> «Огонь принес я на землю, — сказал Христос, — и как томлюсь, когда он возгорится».
> "Fire I brought to the earth," said Christ, "and how I am in anguish for it to blaze up." (working English)
> — PSS Tom 28, pp. 1–293 · fire-metaphor · 1893

### Thomas Tapsell

person · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: English photographer brought by Chertkov; Krekshino 1909 photographs of Tolstoy with grandchildren; negatives at Leeds Russian Archive

> Фотографии Тапселя превосходны — нас с детьми.
> Tapsell's photographs are superb — of us with the children. (working English)
> — PSS Tom 89, pp. 143–146 · tolstoy-in-photographs · 1909-09-26

Visuals: 1 (1 usable) — Tolstoy near Krekshino [PD]

### Tolstoy Digital

institution · missing · dives: jubilee-edition-tei-corpus

_jubilee-edition-tei-corpus_: HSE digital-humanities project that TEI-encoded the 90 volumes (2015–2022) and added the semantic layers; source of the local corpus

> Проект «Слово Толстого»
> The "Word of Tolstoy" project. (working English)
> — jubilee-edition-tei-corpus

> Анастасия Бонч-Осмоловская, Фёкла Толстая, Борис Орехов, Тимофей Лукашевский
> Anastasia Bonch-Osmolovskaya, Fyokla Tolstaya, Boris Orekhov, Timofey Lukashevsky (under "Idea, task-setting, leadership"). (working English)
> — jubilee-edition-tei-corpus

> Тексты и метатекстовая разметка доступны для свободного использования и распространения по лицензии Creative Commons Attribution Share-Alike (cc by-sa)
> The texts and the metatextual markup are available for free use and distribution under the Creative Commons Attribution Share-Alike (cc by-sa) licence. (working English)
> — jubilee-edition-tei-corpus

> Крупный российский промышленник, археолог-любитель, автор сочинений.
> "A major Russian industrialist, amateur archaeologist, author of works." (description of S. S. Abamelek-Lazarev, person id 15). (working English)
> — jubilee-edition-tei-corpus

> Публикуемые документы был получены с сайта tolstoy.ru в формате html, переведены в формат TEI. Исправлены некоторые ошибки распознавания. Тексты, написанные в дореформенной орфографии, сопоставлены с их версиями в современной орфографии.
> The published documents were obtained from the site tolstoy.ru in html format and converted to TEI. Some recognition (OCR) errors were corrected. Texts written in pre-reform orthography were collated with their modern-orthography versions. (working English)
> — jubilee-edition-tei-corpus

> Религия и философия
> "Religion and philosophy" — one topic category. (working English)
> — jubilee-edition-tei-corpus

Visuals: 1 (0 usable) — index.tolstoy.ru — the '91st volume' web app [rights-reserved]

### Tolstoyanism

concept · exists · dives: tolstoyanism

_tolstoyanism_: The central concept — both the label «толстовство» and the «толстовцы» movement. The existing vault page (recordStatus: draft) carries a <!-- NEEDS PRIMARY SOURCE --> block flagging the exact 'great and gross error' rejection this dive now anchors; the page also MISATTRIBUTES it to 'a letter to an adherent' when it is the 1897-12-02 diary entry (re Makovický). This dive's evidence ledger resolves both gaps.

> Я рад был случаю сказать ему и уяснить себе, что говорить о толстовстве, искать моего руководительства, спрашивать моего решения вопросов — большая и грубая ошибка. — Никакого толстовства и моего учения не было и нет, есть одно вечное, всеобщее, всемирное учение истины, для меня, для нас особенно ясно выраженное в евангелиях.
> I was glad of the chance to tell him, and to clarify for myself, that to speak of Tolstoyism, to seek my guidance, to ask me to decide questions — is a great and crude error. There was and is no Tolstoyism and no teaching of mine; there is one eternal, universal, world-wide teaching of truth, which for me, for us, is especially clearly expressed in the Gospels. (working English)
> — PSS Tom 53, pp. 167–169 · tolstoyanism · 1897-12-02

> Вы вот пишете о «толстовцах» и других моих последователях, о движении, поднятом моей проповедью, и о том, почему толстовцы проявляют мало рвения к пропаганде мыслей, которые осчастливят человечество; а я не знаю не только каких-либо других последователей, но и толстовцев
> You write about 'the Tolstoyans' and my other followers, about the movement raised by my preaching, and about why the Tolstoyans show so little zeal in propagating the ideas that would make mankind happy; but I know of no other followers, nor of any Tolstoyans. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

> А о толстовцах, движении и т. п. я ничего не знаю, или даже знаю, что этого ничего нет.
> As for Tolstoyans, a movement, and so forth — I know nothing of it, or rather I know that there is no such thing. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

> сказал бы, не есть мяса, если бы не боялся ridicul’a⁴ толстовства
> [I] would say, eat no meat — were I not afraid of the ridicule of Tolstoyism. (working English)
> — PSS Tom 77, pp. 5–6 · tolstoyanism · 1907-01-01

> православные не любят толстовцев, а толстовцы не любят православных. В этом вы, я думаю, ошибаетесь, во-первых, в том, что признаете каких-то толстовцев. Что же до меня касается, то хотя я и сам Толстой
> [you say that] the Orthodox do not love the Tolstoyans, and the Tolstoyans do not love the Orthodox. In this, I think, you are mistaken — first of all, in that you acknowledge some sort of Tolstoyans. As for myself, though I am Tolstoy myself… (working English)
> — PSS Tom 80, pp. 50–53 · tolstoyanism · 1909-08-04

Visuals: 1 (1 usable) — PSS Tom 53 — the 2 December 1897 diary page carrying the Tolstoyism denial (rendered from the local PD PSS PDF) [PD]

### Tolstoys religious conversion

concept · missing · dives: crisis

_crisis_: the event this dive is about; candidate concept page — should foreground Tolstoy's own vocabulary (переворот / остановка жизни) over the received 'crisis' label

> Пять лет тому назад я поверил в учение Христа — и жизнь моя вдруг переменилась […] Со мной случилось то, что случается с человеком, который вышел за делом и вдруг дорогой решил, что дело это ему совсем не нужно,— и повернул домой.
> Five years ago I came to believe in Christ's teaching — and my life suddenly changed […] What happened to me was what happens to a man who goes out on some errand and then suddenly decides on the way that the errand is of no use to him at all — and turns back home. (working English)
> — PSS Tom 23, pp. 304 · TEI v23_304_465_V_chem_moja_vera · crisis · 1884

> Я жил так года два, и со мной случился переворот, который давно готовился во мне и задатки которого всегда были во мне. Со мной случилось то, что жизнь нашего круга — богатых, ученых — не только опротивела мне, но потеряла всякий смысл.
> I lived like that for a couple of years, and there occurred in me an upheaval [переворот] that had long been preparing within me, and whose seeds had always been in me. What happened to me was that the life of our circle — the rich, the learned — not only grew repugnant to me, but lost all meaning. (working English)
> — PSS Tom 23, pp. 40 · TEI v23_001_059_Ispoved · crisis · 1882

> И я спасся от самоубийства. Когда и как совершился во мне этот переворот, я не мог бы сказать. […] так же постепенно, незаметно возвратилась ко мне эта сила жизни. И странно, что та сила жизни, которая возвратилась ко мне, была не новая, а самая старая, — та самая, которая влекла меня на первых порах моей жизни.
> And I was saved from suicide. When and how this upheaval [переворот] took place in me, I could not say. […] just as gradually, imperceptibly, the force of life returned to me. And it is strange that the force of life which returned to me was not a new one, but the very oldest — the same that had drawn me in the first days of my life. (working English)
> — PSS Tom 23, pp. 46 · TEI v23_001_059_Ispoved · crisis · 1882

### True Christianity (Tolstoy)

concept · missing · dives: christian

_christian_: Tolstoy's governing distinction: истинное христианство (inward, universal) vs церковное христианство ('the greatest enemy of Christ')

> Православие и христианство имеют общего только название. Если церковники христиане, то я не христианин, и наоборот.
> Orthodoxy and Christianity have only the name in common. If churchmen are Christians, then I am not a Christian, and vice versa. (working English)
> — PSS Tom 51, pp. 71 · christian · 1890-08-03

> Как раз напротив: истинное христианство прежде всего требует высшее сознание своего достоинства, страшную силу и непоколебимость.
> The most ordinary judgement of Christianity, especially among the new Nietzschean reasoners, is that Christianity is renunciation of one's dignity, weakness, submission. On the contrary: true Christianity first of all requires the highest consciousness of one's dignity, terrible strength and steadfastness. (working English)
> — PSS Tom 53, pp. 159–160 · christian · 1897-11-10

> Чем больше я живу, чем более приближаюсь к смерти, тем более убеждаюсь в том, что церковное христианство есть величайший враг Христа, его учения и блага людей.
> The more I live, the closer I come to death, the more convinced I am that church Christianity is the greatest enemy of Christ, of his teaching, and of the good of men. (working English)
> — PSS Tom 73, pp. 23–25 · christian · 1901-01-28

> Христианство, истинное христианство, по моему мнению, тем и отличается от религий, которые можно называть общественными, как католичество, православие, магометанство, я думаю даже конфуцианство, что оно обращается к душе каждого отдельного человека, для каждого отдельного человека разрешает его вопрос жизни, указывает ему его назначение, состоящее в исполнении воли бога, в слиянии с ней своей воли, в служении для бога богу и людям и тем дает ему спокойствие и благо.
> Christianity, true Christianity, in my opinion, differs from the religions one may call social — such as Catholicism, Orthodoxy, Mohammedanism, and I think even Confucianism — in that it addresses the soul of each individual person. (working English)
> — PSS Tom 75, pp. 60–62 · christian · 1904-03-17

> Христианство же в его истинном значении я считаю не то, которое мне таковым кажется, но то, которое одинаково признавалось и признается всеми величайшими мыслителями мира до и после Христа. Истинное христианство это не есть какое-либо отдельное от других, исключительное учение, а есть наиболее полное и ясное для нашего времени выражение вечных, божеских истин, одинаково признаваемых всеми великими религиозными учениями мира: браминизмом, буддизмом, конфуцианством, маздеизмом, таосизмом, магометанством и другими.
> True Christianity is not some separate, exclusive teaching, but the fullest and clearest expression for our time of the eternal, divine truths equally acknowledged by all the great religious teachings of the world: Brahminism, Buddhism, Confucianism, Mazdeism, Taoism, Mohammedanism and others. (working English)
> — PSS Tom 79, pp. 53–59 · christian · 1909-01-29

### V chem moja vera

work · missing · dives: fire-metaphor, gospel-translation

_fire-metaphor_: Source of the fire+light credo quoted at the close of Biryukov vol. II
_gospel-translation_: Project part 4 — the positive exposition of the recovered teaching (also the fire+light credo of the sibling fire-metaphor dive)

> в человеке живет божественный свет, сошедший с неба, и свет этот есть разум, — и что ему одному надо служить и в нем одном искать благо.
> in man there lives a divine light, come down from heaven, and this light is reason — and that it alone must be served and in it alone must good be sought. (working English)
> — PSS Tom 23, pp. 304–465 · fire-metaphor · 1884

> Но мир горит уж 1800 лет, горит с тех пор, как Христос сказал: я огонь низвел на землю; и как томлюсь, пока он не разгорится, — и будет гореть, пока не спасутся люди.
> But the world has been burning for 1800 years now, burning ever since Christ said: I brought fire down to the earth; and how I am in anguish until it blazes up — and it will burn until people are saved. (working English)
> — PSS Tom 23, pp. 304–465 · fire-metaphor · 1884

> что этот талант есть огонь, который только тогда огонь, когда он жжет. Я верю, что я — Ниневия по отношению к другим Ионам, от которых я узнал и узнаю истину, но что и я Иона по отношению к другим ниневитянам, которым я должен передать истину.
> that this talent is a fire which is only a fire when it burns. I believe that I am a Nineveh in relation to other Jonahs, from whom I have learned and learn the truth, but that I too am a Jonah in relation to other Ninevites, to whom I must pass the truth on. (working English)
> — PSS Tom 23, pp. 461 · fire-metaphor · 1884

> Я верю, что единственный смысл моей жизни — в том, чтобы жить в том свете, который есть во мне, и ставить его не под спуд, но высоко перед людьми, так, чтобы люди видели его.
> I believe that the only meaning of my life is to live by the light that is in me, and to set it not under a bushel but high before people, so that people may see it. (working English)
> — PSS Tom 23, pp. 461 · fire-metaphor · 1884

> перевод четырех Евангелий и соединение их в одно.
> the translation of the four Gospels and their combination into one. (working English)
> — PSS Tom 24, pp. 801–938 · gospel-translation · 1881

Visuals: 3 (3 usable) — The 'Я верю' credo — 'a fire which is only a fire when it burns' + 'live by the light in me' (PSS Tom 23, printed p.461) [PD], Tolstoy writing — Nikolai Ge's 1884 portrait, painted while Tolstoy drafted What I Believe [PD], Tolstoy at Yasnaya Polyana, 1908 — first colour photo-portrait in Russia (seated + head crop) [PD]

### Valeria Arsenyeva

person · missing · dives: biryukov-sofia-relationship

_biryukov-sofia-relationship_: Tolstoy's near-fiancée of 1856–57; the withheld lover; the suppressed-chapter subject (basis of Family Happiness)

> это была Арсеньева Валерия. Она теперь жива, за Волковым была, живет в Париже.
> that was Arsenyeva, Valeria. She is alive now, was married to Volkov, lives in Paris. (working English)
> — PSS Tom 74, pp. 319 · biryukov-sofia-relationship · 1903-11-27

> есть целая пачка моих писем к ней.
> there is a whole packet of my letters to her. (working English)
> — PSS Tom 74, pp. 319 · biryukov-sofia-relationship · 1903-11-27

> протестовала против писем Арсеньевой.
> [Sofia Andreevna] protested against the Arsenyeva letters. (working English)
> — PSS Tom 76, pp. 65 · biryukov-sofia-relationship · 1905-10-18

### Varvara Mac-Gahan

person · missing · dives: tolstoyanism

_tolstoyanism_: Russian-American journalist (1850–1904), widow of war correspondent Januarius MacGahan; addressee of the 1894 letter. Her writing about 'the Tolstoyans' and 'the movement' is what Tolstoy answers by denying both exist.

> Вы вот пишете о «толстовцах» и других моих последователях, о движении, поднятом моей проповедью, и о том, почему толстовцы проявляют мало рвения к пропаганде мыслей, которые осчастливят человечество; а я не знаю не только каких-либо других последователей, но и толстовцев
> You write about 'the Tolstoyans' and my other followers, about the movement raised by my preaching, and about why the Tolstoyans show so little zeal in propagating the ideas that would make mankind happy; but I know of no other followers, nor of any Tolstoyans. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

> А о толстовцах, движении и т. п. я ничего не знаю, или даже знаю, что этого ничего нет.
> As for Tolstoyans, a movement, and so forth — I know nothing of it, or rather I know that there is no such thing. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

### Vasily Alekseev

person · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: The children's tutor and early convert; recipient of the 1881 circle letter; credited as the first educated man to confirm Tolstoy's new faith.

> Мне очень тяжело в Москве.
> (working English) Things are very hard for me in Moscow.
> — PSS Tom 63, pp. 80–83 · 1879-1882-a-confession · 1881-11 (OS)

### Vasily Sutaev

person · missing · dives: 1879-1882-a-confession

_1879-1882-a-confession_: Peasant sectarian from Tver; an exemplar of the simple living faith Tolstoy sought; visited 1881.

> Прошел месяц — самый мучительный в моей жизни. Переезд в Москву.
> (working English) A month has passed — the most agonizing of my life. The move to Moscow.
> — PSS Tom 49, pp. 58 · 1879-1882-a-confession · 1881-10-05 (OS)

> Мне очень тяжело в Москве.
> (working English) Things are very hard for me in Moscow.
> — PSS Tom 63, pp. 80–83 · 1879-1882-a-confession · 1881-11 (OS)

Visuals: 1 (1 usable) — V. K. Sutaev (Y. Steinberg, 1885) [PD]

### Vladimir Chertkov

person · exists · dives: 1879-1882-a-confession, biryukov-sofia-relationship, christian-anarchism, copyright-renunciation, crisis, doukhobors, fire-metaphor, gospel-translation, jubilee-edition-tei-corpus, tolstoy-in-art, tolstoy-in-photographs, tolstoyanism · names: V. G. Chertkov / Vladimir Chertkov

_1879-1882-a-confession_: Disciple and publisher; the «Свободное слово» (Christchurch, 1901) edition; the agent for distributing the suppressed text.
_biryukov-sofia-relationship_: Editor and close associate of Tolstoy, entrusted with his manuscripts and diaries; named diary-executor in the 1895 testament; on the opposing side of Sofia in the 1910 will crisis; first (censored) publisher of the diaries (1916)
_christian-anarchism_: Tolstoy's closest disciple and publisher; gave «христианский анархизм» programmatic Russian form in the 1905 booklet O khristianskom anarkhizme (Svobodnoe Slovo), the in-circle frame the Sacy phrase points to. The 1905 booklet is not held locally.
_copyright-renunciation_: co-drafter of the six wills; drafted the 1910 Explanatory Note; held Tolstoy's post-1881 rights
_crisis_: disciple/correspondent from 1883; the PSS Tom 85 apparatus that carries the editors' 'кризис своих воззрений' annotates the Chertkov letters
_doukhobors_: Co-author of «Help!»; expelled to England 1897, where he became the organising hub of the relief effort.
_fire-metaphor_: Closest disciple; conduit for the 1904 soldiers' letter; co-author of the Doukhobor record
_gospel-translation_: Later custodian/publisher of the banned works; his Croydon/Free Age circle stands behind the first English translation
_jubilee-edition-tei-corpus_: editor-in-chief (главный редактор) of the Jubilee Edition; Tolstoy's disciple and keeper of his manuscripts; d. 1936 mid-project
_tolstoy-in-art_: Disciple; ran the late photographic documentation of Tolstoy; party to the conflict over Tolstoy's portraits/image
_tolstoy-in-photographs_: built the largest photographic archive of Tolstoy; brought the photographer Tapsell; the public/prophet image-maker
_tolstoyanism_: Not named in the four quotes, but the focal point of the ambivalence: the de facto organiser, dogmatist and publisher (Free Age Press) of the very movement Tolstoy disowns. The gap between Tolstoy's 'there is no such thing' and Chertkov's institution-building is the dive's central tension.

> Обличаемые спрятались за цензуру и штыки
> (working English) Those exposed have hidden behind censorship and bayonets.
> — PSS Tom 63, pp. 90–91 · 1879-1882-a-confession · 1882-03-03 (OS, unsent)

> Чертков обещал мне еще при жизни моей сделать это.
> Chertkov promised me, while I am still alive, to do this [destroy/prune the diaries]. (working English)
> — PSS Tom 53, pp. 14-18 · biryukov-sofia-relationship · 1895-03-27

> завещание, если есть таковое.
> [to make my will invalid,] if such a will exists. (working English) — reconstructed from TEI reg, cross-checked vs facsimile.
> — PSS Tom 58, pp. 137 · biryukov-sofia-relationship · 1910-09-16

> почти душевно больна — ненависть к Черткову, ревность к нему, и мне очень трудно.
> almost mentally ill — hatred of Chertkov, jealousy of him, and it is very hard for me. (working English)
> — PSS Tom 82, pp. 95 · biryukov-sofia-relationship · 1910-07-19

> 1) Все его сочинения, литературные произведения и писания всякого рода, как уже где-либо напечатанные, так и еще не изданные, не составляли после его смерти ничьей частной собственности, а могли бы быть издаваемы и перепечатываемы всеми, кто этого захочет.
> (working English) 1) That all his compositions, literary works and writings of every kind, whether already published anywhere or not yet issued, should after his death be no one's private property, but might be published and reprinted by anyone who wishes.
> — PSS Tom 82, pp. 227–231 · copyright-renunciation · 1910-07-31

> …21 мая 1883 г. Толстой, пережив уже кризис своих воззрений и отстраняясь от всяких дел материального характера, выдал ей нотариально засвидетельствованную доверенность…
> …on 21 May 1883 Tolstoy, having already lived through the crisis of his views and withdrawing from all affairs of a material character, issued her a notarised power of attorney… (working English) — EDITORIAL voice: Jubilee Edition apparatus, not Tolstoy.
> — PSS Tom 85, pp. 193–196 (editorial note) · TEI v85_059_a10_11 · crisis · 1885

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

> это искра того огня, который Христос низвел на землю и который начинает возгораться.
> this is a spark of that fire which Christ brought down to the earth and which is beginning to blaze up. (working English)
> — PSS Tom 88, pp. 718 · fire-metaphor · 1904-05-08

> В 1910 году Толстой приехал в усадьбу Отрадное, где снимал дачу его друг, сподвижник и редактор В. Г. Чертков.
> In 1910 Tolstoy came to the Otradnoye estate, where his friend, associate and editor V. G. Chertkov was renting a dacha. (working English)
> — jubilee-edition-tei-corpus

> непосредственную работу по редактированию тому другу покойного писателя, которого он сам выбрал для этой цели
> …the direct work of editing to that friend of the deceased writer whom he himself chose for this purpose… (i.e. V. G. Chertkov). (working English)
> — PSS Tom 1, pp. v · jubilee-edition-tei-corpus · 1928-01-01

> нам в настоящем издании приходится именно в таком полном виде воспроизводить решительно все, написанное Толстым.
> …in the present edition we have to reproduce, in exactly such complete form, absolutely everything written by Tolstoy. (working English)
> — PSS Tom 1, pp. vi · jubilee-edition-tei-corpus · 1928-01-01

> Это же самое желание он затем подтвердил письменно в своем завещательном распоряжении от 31 июля 1910 г.
> This same wish he then confirmed in writing in his testamentary disposition of 31 July 1910. (working English)
> — PSS Tom 1, pp. vi · jubilee-edition-tei-corpus · 1928-01-01

> Был здесь Чертков. Вышло очень неприятное столкновение из-за портрета. Как всегда, Соня поступила решительно, но необдуманно и нехорошо.
> Chertkov was here. A very unpleasant clash arose over a portrait. As always, Sonya acted decisively but rashly and badly. (working English)
> — PSS Tom 52, pp. 157–159 · tolstoy-in-art · 1894-12-31

> История с фотографией очень грустная. Все они оскорблены. Я написал письмо Черткову.
> The story with the photograph is very sad. They are all offended. I wrote a letter to Chertkov. (working English)
> — PSS Tom 53, pp. 2 · tolstoy-in-photographs · 1895-01-03

> Фотографии Тапселя превосходны — нас с детьми.
> Tapsell's photographs are superb — of us with the children. (working English)
> — PSS Tom 89, pp. 143–146 · tolstoy-in-photographs · 1909-09-26

> Вы не можете представить себе, какой вред мне делают похвалы при моем тщеславии. Это пьянство.
> You cannot imagine what harm praise does me, given my vanity. It is drunkenness. (working English)
> — PSS Tom 89, pp. 46–48 · tolstoy-in-photographs · 1906-10-26

Visuals: 11 (10 usable) — V. G. Chertkov (Repin, c.1890) [PD], Vladimir Chertkov (1883) [PD], Chertkov with Tolstoy, Yasnaya Polyana 1909 [PD], Vladimir Chertkov, portrait by Ilya Repin (1890s) [PD], Tolstoy and Chertkov together, Yasnaya Polyana, 29 March 1909 [PD], Portrait of V. G. Chertkov, Ivan Kramskoy, 1881 [unknown], Tolstoy and Chertkov at Yasnaya Polyana, 1909 [PD], Tolstoy with his granddaughter, photographed by Vladimir Chertkov, 1910 (final year) [PD], V. G. Chertkov, editor-in-chief of the Jubilee Edition [PD], PSS Tom 1 — «ОТ ГЛАВНОГО РЕДАКТОРА» (Chertkov's editor-in-chief foreword) [PD], Tolstoy with his physician Dushan Makovitsky [PD]

### Vladimir Molochnikov

person · missing · dives: tolstoy-in-photographs

_tolstoy-in-photographs_: Tolstoyan correspondent; addressee of the 'cannot attach importance to it' card letter (1908)

> Не прислал до сих пор карточки потому, что забыл, а забыл потому, что не могу приписать этому значения
> I have not sent the card until now because I forgot, and I forgot because I cannot attach any importance to it (working English)
> — PSS Tom 78, pp. 191 · tolstoy-in-photographs · 1908-07-23

### Vladimir Stasov

person · missing · dives: tolstoy-in-art

_tolstoy-in-art_: Critic; mediated the Repin–Tolstoy relationship; recipient of the 1887 'portrait shipped' note

> Портрет Репина уложен и завтра отсылается.
> Repin's portrait is packed and is being sent off tomorrow. (working English)
> — PSS Tom 64, pp. 66–67 · tolstoy-in-art · 1887-09-08

### What I Believe

work · missing · dives: crisis

_crisis_: companion confessional work; 'жизнь моя вдруг переменилась'

> Пять лет тому назад я поверил в учение Христа — и жизнь моя вдруг переменилась […] Со мной случилось то, что случается с человеком, который вышел за делом и вдруг дорогой решил, что дело это ему совсем не нужно,— и повернул домой.
> Five years ago I came to believe in Christ's teaching — and my life suddenly changed […] What happened to me was what happens to a man who goes out on some errand and then suddenly decides on the way that the errand is of no use to him at all — and turns back home. (working English)
> — PSS Tom 23, pp. 304 · TEI v23_304_465_V_chem_moja_vera · crisis · 1884

### Yasnaya Polyana

place · exists · dives: jubilee-edition-tei-corpus, tolstoy-in-art, tolstoy-in-photographs

_jubilee-edition-tei-corpus_: Tolstoy's estate; co-initiator of the digitisation; the place from which most of the edition's manuscript base originates
_tolstoy-in-art_: The estate where most sittings happened (Kramskoy 1873, Repin 1887/1891, Ginzburg 1891, Nesterov, Aronson, Trubetskoy); holds the family version of the 1873 Kramskoy portrait
_tolstoy-in-photographs_: principal photographic location; an estate 'фотография' (photo room) attested by 1862; the 1908 sessions

> Приехал Репин и Гинзбург. За это время они меня лепят и пишут, а я написал статью об обжорстве и много подвинулся в большой статье.
> Repin and Ginzburg have arrived. During this time they sculpt and paint me, while I have written an article on gluttony and made much progress on the big article. (working English)
> — PSS Tom 52, pp. 44 · tolstoy-in-art · 1891-07-13

> У меня каждый день, вот уже с неделю, живописец Крамской [...] делает мой портрет в Третьяковскую галлерею, и я сижу и болтаю с ним и из Петербургской стараюсь обращать его в крещеную веру.
> Every day now, for a week already, the painter Kramskoy has been making my portrait for the Tretyakov gallery, and I sit and chat with him and try to convert him from the Petersburg faith to the baptized one. (working English)
> — PSS Tom 62, pp. 48–49 · tolstoy-in-art · 1873-09-23

> Мама целый день занимается фотографией. Она сняла несколько раз Козловку и группу нас всех.
> Mama spends the whole day on photography. She photographed Kozlovka [station] several times, and a group of all of us. (working English)
> — PSS Tom 69, pp. 161 · tolstoy-in-photographs · 1896-10-10

> Фотографии Тапселя превосходны — нас с детьми.
> Tapsell's photographs are superb — of us with the children. (working English)
> — PSS Tom 89, pp. 143–146 · tolstoy-in-photographs · 1909-09-26

Visuals: 1 (1 usable) — Yasnaya Polyana — Tolstoy's main house (source of the manuscript base) [PD]

## 4. Integrity report

**Unresolved evidenceRefs** (0)

- none

**Name conflicts (same key, multiple spellings)** (12)

- confession: A Confession (Исповедь) / Confession (Исповедь) (crisis, fire-metaphor, gospel-translation)
- jubilee-edition: Jubilee Edition (Полное собрание сочинений) / The Jubilee Edition (Полное собрание сочинений) (gospel-translation, jubilee-edition-tei-corpus)
- leo-tolstoy: Leo Tolstoy / Lev Tolstoy (1879-1882-a-confession, biryukov-sofia-relationship, christian-anarchism, copyright-renunciation, crisis, doukhobors, tolstoy-in-photographs, tolstoyanism)
- mikhail-elpidin: M. K. Elpidin / Mikhail Elpidin (М. К. Эльпидин) (1879-1882-a-confession, gospel-translation)
- nikolai-strakhov: N. N. Strakhov / Nikolai Strakhov (1879-1882-a-confession, crisis, gospel-translation, lords-prayer)
- pavel-birukoff: Pavel Birukoff / Pavel Biryukov (1879-1882-a-confession, biryukov-sofia-relationship, copyright-renunciation, crisis, doukhobors)
- soedinenie-i-perevod-chetyrekh-evangelij: The Gospel in Brief / The Four Gospels Harmonized (Соединение и перевод четырёх Евангелий) / Union and Translation of the Four Gospels (Соединение и перевод четырёх Евангелий) (fire-metaphor, gospel-translation, lords-prayer)
- sophia-tolstaya: S. A. Tolstaya (Sofia Andreyevna) / Sofia Andreevna Tolstaya / Sofia Tolstaya / Sophia Tolstaya (1879-1882-a-confession, biryukov-sofia-relationship, copyright-renunciation, gospel-translation, tolstoy-in-photographs)
- state-museum-of-leo-tolstoy: State Museum of L. N. Tolstoy (GMT) / State Museum of L. N. Tolstoy (Moscow) (tolstoy-in-art, tolstoy-in-photographs)
- state-tolstoy-museum: State Museum of L. N. Tolstoy (GMT) / State Tolstoy Museum (GMT) (copyright-renunciation, jubilee-edition-tei-corpus)
- the-kingdom-of-god-is-within-you: The Kingdom of God Is Within You / The Kingdom of God Is Within You (Царство Божие внутри вас) (doukhobors, fire-metaphor)
- vladimir-chertkov: V. G. Chertkov / Vladimir Chertkov (1879-1882-a-confession, biryukov-sofia-relationship, christian-anarchism, copyright-renunciation, crisis, doukhobors, fire-metaphor, gospel-translation, jubilee-edition-tei-corpus, tolstoy-in-art, tolstoy-in-photographs, tolstoyanism)

**wikiType conflicts** (3)

- jubilee-edition: concept / edition
- mikhail-elpidin: institution / person
- the-kingdom-of-god-is-within-you: criticalWork / work

**Works routed to works/ (not a wiki type)** (21)

- abrege-de-levangile (work)
- bethink-yourselves (work)
- chem-ljudi-zhivy (work)
- confession (work)
- four-gospels-harmonised-and-translated-1895 (edition)
- hodite-v-svete-poka-est-svet (work)
- issledovanie-dogmaticheskogo-bogoslovija (work)
- jubilee-edition (edition)
- kratkoe-izlozhenie-evangelija (work)
- leeds-russian-archive-chertkov-tapsell-fond (archival-fond)
- na-kazhdyj-den (work)
- o-zhizni (work)
- otets-sergij (work)
- prokudin-gorsky-collection-library-of-congress (archival-fond)
- put-zhizni (work)
- smert-ivana-ilicha (work)
- soedinenie-i-perevod-chetyrekh-evangelij (work)
- the-kingdom-of-god-is-within-you (work)
- tsgakffd-bulla-collection (archival-fond)
- v-chem-moja-vera (work)
- what-i-believe (work)

**vaultStatus drift (dossier vs live)** (3)

- confession: dossier ['exists'] → live stub
- tatyana-tolstaya: dossier ['exists'] → live stub
- the-kingdom-of-god-is-within-you: dossier ['exists'] → live stub

**Entities with zero evidence** (30)

- abbyy (jubilee-edition-tei-corpus)
- aksinya-bazykina (biryukov-sofia-relationship)
- alexandra-tolstaya (copyright-renunciation, jubilee-edition-tei-corpus)
- astapovo (tolstoy-in-photographs)
- aylmer-maude (copyright-renunciation, doukhobors, gospel-translation)
- ernest-howard-crosby (christian-anarchism)
- felix-ortt (christian-anarchism)
- ivan-turgenev (1879-1882-a-confession)
- jan-styka (tolstoy-in-art)
- karl-bulla (tolstoy-in-photographs)
- konstantin-pobedonostsev (1879-1882-a-confession)
- leo-wiener (gospel-translation)
- leonid-urusov (1879-1882-a-confession)
- leopold-sulerzhitsky (doukhobors)
- mikhail-nesterov (tolstoy-in-art)
- naum-aronson (tolstoy-in-art)
- nikolai-gudzy (jubilee-edition-tei-corpus)
- nikolai-gusev (jubilee-edition-tei-corpus)
- paolo-trubetskoy (tolstoy-in-art)
- peredvizhniki (tolstoy-in-art)
- resurrection (doukhobors)
- russkaya-mysl-journal (1879-1882-a-confession)
- sergei-tolstoy (doukhobors)
- sergei-yuryev (1879-1882-a-confession)
- society-of-friends (doukhobors)
- state-museum-of-leo-tolstoy (tolstoy-in-art, tolstoy-in-photographs)
- state-russian-museum (tolstoy-in-art)
- tatyana-tolstaya (tolstoy-in-art)
- tsgakffd-bulla-collection (tolstoy-in-photographs)
- valentin-serov (tolstoy-in-art)

**Missing wikilinkTarget** (0)

- none

**Slug ≠ page id** (0)

- none

## 5. Method

Built by `docs/research/lib/build_evidence_index.py`, which walks every `docs/research/*/dossier.yaml`. Entity key = slug of `wikilinkTarget` (`.md` stripped), equal to the eventual wiki/works slug. Each entity's `evidenceRefs` are resolved against its own dive's `evidence[]`; visuals are attached by `relatedEntity` and deduped across dives. `vaultStatus` is re-derived live against `website/src/wiki/` and `website/src/works/` (stub = prose body < 60 words, or a `draft` with < 120). Output is deterministic. Regenerate: `python3 docs/research/lib/build_evidence_index.py`.

