---
layer: reference
lastUpdated: 2026-05-30
tags: [research]
---

# Cross-dive evidence index

Generated aggregate of every corpus-dive dossier, keyed by entity. It collates the verified primary-source citations already gathered across all dives so wiki ingestion reuses them instead of re-collating by hand. Generated — do not hand-edit; regenerate with `python3 docs/research/lib/build_evidence_index.py`. Writing the wiki pages remains a separate, human-in-the-loop step.

## 1. At a glance

- 5 dives · 41 distinct entities · 41 evidence rows · 46 visuals
- By vault status: 7 exists · 3 stub · 31 missing
- 4 entities recur across ≥2 dives

## 2. Ingestion work-order

Entities not yet written (or only stubbed) that already have verified evidence, ranked by ingestion priority then evidence count. These are ready to write — the citations are collated in §3.

| Entity | Type | Status | Dives | #Ev | Depends on |
|---|---|---|---|---|---|
| Paul Eltzbacher | person | missing | christian-anarchism | 3 | leo-tolstoy |
| Gabriel Sacy | person | missing | christian-anarchism | 2 | christian-anarchism, leo-tolstoy |
| Varvara Mac-Gahan | person | missing | tolstoyanism | 2 | leo-tolstoy |
| Dushan Makovicky | person | missing | tolstoyanism | 1 | leo-tolstoy |
| Eugen Heinrich Schmitt | person | missing | christian-anarchism | 1 | christian-anarchism, leo-tolstoy |
| Mikhail Stakhovich | person | missing | tolstoyanism | 1 | leo-tolstoy |
| Non-resistance | concept | missing | christian-anarchism | 1 | christian-anarchism |
| Henry George | person | missing | tolstoyanism | 1 | — |
| I. Ivanov | person | missing | tolstoyanism | 1 | leo-tolstoy |
| John Coleman Kenworthy | person | missing | christian-anarchism | 1 | christian-anarchism |
| John Morrison Davidson | person | missing | christian-anarchism | 1 | christian-anarchism |
| Confession | work | stub | crisis | 3 | — |
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
| Nikolai Strakhov | person | missing | crisis | 1 | — |
| State Tolstoy Museum | institution | missing | copyright-renunciation | 1 | — |
| The Burning of Arms | event | missing | doukhobors | 1 | — |
| What I Believe (В чём моя вера?) | work | missing | crisis | 1 | — |

9 entities are named across the dives but carry no evidence rows yet (research gaps, not ready to ingest): Alexandra Tolstaya, Aylmer Maude, Ernest Howard Crosby, Felix Ortt, Leopold Sulerzhitsky, Resurrection, Sergei Tolstoy, Society of Friends, The Kingdom of God Is Within You.

## 3. Collated citations, by entity

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

work · stub · dives: crisis

_crisis_: the keystone text; the dive's central vocabulary (переворот, остановка жизни) lives here

> Так я жил, но пять лет тому назад со мною стало случаться что-то очень странное: на меня стали находить минуты сначала недоумения, остановки жизни, как будто я не знал, как мне жить, что мне делать, и я терялся и впадал в уныние. […] Эти остановки жизни выражались всегда одинаковыми вопросами: Зачем? Ну, а потом?
> So I lived, but five years ago something very strange began to happen to me: at first there came over me moments of bewilderment, of life coming to a stop, as though I did not know how to live or what to do, and I lost my footing and fell into dejection. […] These stoppages of life always expressed themselves in the same questions: Why? And then what? (working English)
> — PSS Tom 23, pp. 10 · TEI v23_001_059_Ispoved · crisis · 1882

> Я жил так года два, и со мной случился переворот, который давно готовился во мне и задатки которого всегда были во мне. Со мной случилось то, что жизнь нашего круга — богатых, ученых — не только опротивела мне, но потеряла всякий смысл.
> I lived like that for a couple of years, and there occurred in me an upheaval [переворот] that had long been preparing within me, and whose seeds had always been in me. What happened to me was that the life of our circle — the rich, the learned — not only grew repugnant to me, but lost all meaning. (working English)
> — PSS Tom 23, pp. 40 · TEI v23_001_059_Ispoved · crisis · 1882

> И я спасся от самоубийства. Когда и как совершился во мне этот переворот, я не мог бы сказать. […] так же постепенно, незаметно возвратилась ко мне эта сила жизни. И странно, что та сила жизни, которая возвратилась ко мне, была не новая, а самая старая, — та самая, которая влекла меня на первых порах моей жизни.
> And I was saved from suicide. When and how this upheaval [переворот] took place in me, I could not say. […] just as gradually, imperceptibly, the force of life returned to me. And it is strange that the force of life which returned to me was not a new one, but the very oldest — the same that had drawn me in the first days of my life. (working English)
> — PSS Tom 23, pp. 46 · TEI v23_001_059_Ispoved · crisis · 1882

### Dmitri Khilkov

person · missing · dives: doukhobors

_doukhobors_: Exiled prince whose reports first brought the atrocity news to Tolstoy; the named eyewitness source of the 1895 open letter.

> После этого, 28 июня 1895 года, духоборцы, живущие в Ахалкалакском уезде Тифлисской губернии, снесли в одну кучу в поле, около села Спасского, всё свое имевшееся у них оружие и, обложив его дровами и углем и облив керосином, сожгли
> After this, on 28 June 1895, the Doukhobors living in the Akhalkalaki district of the Tiflis province carried all the weapons they had into a single heap in a field near the village of Spasskoye and, having piled wood and coal upon them and doused them with kerosene, burned them. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

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

### I. Ivanov

person · missing · dives: tolstoyanism

_tolstoyanism_: Obscure 1909 correspondent (addressed via his nephew); identity beyond the PSS header unresolved — see needsReview. Addressee of the 'some sort of Tolstoyans' letter.

> православные не любят толстовцев, а толстовцы не любят православных. В этом вы, я думаю, ошибаетесь, во-первых, в том, что признаете каких-то толстовцев. Что же до меня касается, то хотя я и сам Толстой
> [you say that] the Orthodox do not love the Tolstoyans, and the Tolstoyans do not love the Orthodox. In this, I think, you are mistaken — first of all, in that you acknowledge some sort of Tolstoyans. As for myself, though I am Tolstoy myself… (working English)
> — PSS Tom 80, pp. 50–53 · tolstoyanism · 1909-08-04

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

person · missing · dives: christian-anarchism

_christian-anarchism_: John Coleman Kenworthy (1861–1948), English founder of the Brotherhood Church, Croydon (from 1894); visited Yasnaya Polyana in 1896 and held UK rights to Tolstoy's works. A node of the 1890s Christian-anarchist circle; named in the Schmitt correspondence.

> Ваше дело, наше дело, т. е. божье дело, у вас делает успехи.
> Your work, our work, that is, God's work, is making progress with you. (working English)
> — PSS Tom 68, pp. 26–28 · christian-anarchism · 1895-02-01

### John Morrison Davidson

person · missing · dives: christian-anarchism

_christian-anarchism_: John Morrison Davidson (1843–1916), Scottish radical journalist and barrister; author of The Old Order and the New, The Gospel of the Poor and Anarchist Socialism v. State Socialism. Tolstoy praises him in 1894 for subordinating socialist/communist/anarchist theory to Christian truth.

> социалистическая, коммунистическая и анархическая теории приводятся в подкрепление христианской истины, которая составляет ее главную часть.
> the socialist, communist and anarchist theories are brought in to corroborate the Christian truth, which forms its chief part. (working English)
> — PSS Tom 67, pp. 178–180 · christian-anarchism · 1894-07-23

### Leo Tolstoy

person · exists · dives: christian-anarchism, copyright-renunciation, crisis, doukhobors, tolstoyanism

_christian-anarchism_: The author refusing the political label 'anarchist' while affirming the religious substance, and the sole user of «христианский анархизм» in his own voice (once).
_copyright-renunciation_: author renouncing copyright; subject of the dive
_crisis_: subject of the dive; author of the keystone confessional works
_doukhobors_: Author of the public appeals, organiser and partial funder of the relief and emigration.
_tolstoyanism_: The author disowning the label and the movement named after him.

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

> Я рад был случаю сказать ему и уяснить себе, что говорить о толстовстве, искать моего руководительства, спрашивать моего решения вопросов — большая и грубая ошибка. — Никакого толстовства и моего учения не было и нет, есть одно вечное, всеобщее, всемирное учение истины, для меня, для нас особенно ясно выраженное в евангелиях.
> I was glad of the chance to tell him, and to clarify for myself, that to speak of Tolstoyism, to seek my guidance, to ask me to decide questions — is a great and crude error. There was and is no Tolstoyism and no teaching of mine; there is one eternal, universal, world-wide teaching of truth, which for me, for us, is especially clearly expressed in the Gospels. (working English)
> — PSS Tom 53, pp. 167–169 · tolstoyanism · 1897-12-02

> Вы вот пишете о «толстовцах» и других моих последователях, о движении, поднятом моей проповедью, и о том, почему толстовцы проявляют мало рвения к пропаганде мыслей, которые осчастливят человечество; а я не знаю не только каких-либо других последователей, но и толстовцев
> You write about 'the Tolstoyans' and my other followers, about the movement raised by my preaching, and about why the Tolstoyans show so little zeal in propagating the ideas that would make mankind happy; but I know of no other followers, nor of any Tolstoyans. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

> православные не любят толстовцев, а толстовцы не любят православных. В этом вы, я думаю, ошибаетесь, во-первых, в том, что признаете каких-то толстовцев. Что же до меня касается, то хотя я и сам Толстой
> [you say that] the Orthodox do not love the Tolstoyans, and the Tolstoyans do not love the Orthodox. In this, I think, you are mistaken — first of all, in that you acknowledge some sort of Tolstoyans. As for myself, though I am Tolstoy myself… (working English)
> — PSS Tom 80, pp. 50–53 · tolstoyanism · 1909-08-04

Visuals: 9 (5 usable) — Diary page, 27 March 1895 (the will-as-diary-entry) [rights-reserved], Leo Tolstoy, 1906 (photograph by V. G. Chertkov) [PD], Manuscript / draft page of Исповедь (A Confession) [rights-reserved], Portrait of Leo Tolstoy (oil), Ivan Kramskoy, 1873 [PD], PSS Tom 23, p. 40 — the «случился переворот» passage of A Confession [PD], Photographic portraits of Tolstoy, c. 1878–1885 (crisis years) [unknown], Tolstoy Digital timeline cards (work on A Confession #175; banning of A Confession #192; Optina Pustyn with Strakhov #166; first acquaintance with Chertkov #198) [unknown], Leo Tolstoy, 1895 — the year of the Burning of Arms [PD], Leo Tolstoy at Yasnaya Polyana, colour photograph, 1908 [PD]

### Leonila Annenkova

person · missing · dives: crisis

_crisis_: correspondent; recipient of the 'эти кризисы / родился вновь' letter (1894)

> …я, к счастию, этого отчаяния никогда не знал с тех пор, как родился вновь […] то каждый, проходя эти возрасты, эти кризисы, не будет пугаться, а будет ждать следующего состояния, будет знать, что то же было и с другими.
> …I, fortunately, have never known this despair since I was born anew… so that everyone, passing through these ages, these crises, would not take fright, but would wait for the next state, knowing that the same was so for others. (working English)
> — PSS Tom 67, pp. 213–214 · TEI v67_214_L_F_Annenkovoj · crisis · 1894-09-04

### Mikhail Stakhovich

person · missing · dives: tolstoyanism

_tolstoyanism_: Oryol marshal of the nobility, Duma politician and friend of the Tolstoy family; addressee of the 1907 New-Year letter in which the 'ridicule of Tolstoyism' appears.

> сказал бы, не есть мяса, если бы не боялся ridicul’a⁴ толстовства
> [I] would say, eat no meat — were I not afraid of the ridicule of Tolstoyism. (working English)
> — PSS Tom 77, pp. 5–6 · tolstoyanism · 1907-01-01

### Nicholas II

person · missing · dives: doukhobors

_doukhobors_: Addressee of two petitions citing the Doukhobors as the emblem of religious persecution (1898, 1900).

> И потому, если мы не можем исполнять того, без чего нас нельзя терпеть в государстве, мы просим одно: отпустите нас.
> And so, if we cannot fulfil that without which we cannot be tolerated in the state, we ask one thing only: let us go. (working English)
> — PSS Tom 71, pp. 345–348 · doukhobors · 1898-04-02

> уже давнымъ давно пора: во-первыхъ, пересмотрѣть и уничтожить существующіе теперь законы о гоненіяхъ за вѣру; во-вторыхъ, прекратить всѣ преслѣдованія за отступленія отъ принятаго государствомъ исповѣданія; въ-третьихъ, освободить всѣхъ на основаніи прежнихъ законовъ заключенныхъ и изгнанныхъ за преступленіе противъ вѣры, и въ-четвертыхъ, не казнить, какъ преступленіе, несогласіе религіозной совѣсти съ требованіями государства
> it is long, long since high time: first, to review and abolish the laws now existing on persecution for faith; second, to stop all prosecutions for departure from the state-accepted confession; third, to release all those imprisoned and exiled under the former laws for offences against faith; and fourth, not to punish as a crime the disagreement of religious conscience with the demands of the state. (working English)
> — PSS Tom 72, pp. 514–521 · doukhobors · 1900-12-07

### Nikolai Strakhov

person · missing · dives: crisis

_crisis_: philosopher, close correspondent; recipient of the 'medical кризис' letter (1894); accompanied Tolstoy to Optina Pustyn, 1881

> Вы знаете, что Марья Петровна Фет при смерти — крупозное воспаление легких. До сих пор нет кризиса, и шансов смерти, говорят, больше, чем жизни.
> You know that Marya Petrovna Fet is dying — lobar pneumonia. So far there is no crisis, and the chances of death, they say, are greater than of life. (working English)
> — PSS Tom 67, pp. 84 · TEI v67_083_H_N_Straxovu · crisis · 1894-03-16

Visuals: 1 (1 usable) — Portrait/photograph of N. N. Strakhov [PD]

### Non-resistance

concept · missing · dives: christian-anarchism

_christian-anarchism_: The religious substance Tolstoy affirms in place of the political label. The Eltzbacher index argument turns on it: Eltzbacher's book has no Tolstoy reference under 'violence' because Tolstoy treated the matter as non-resistance (religion), not violence (politics).

> Мне кажется только, что я не анархист в смысле политического реформатора. В оглавлении вашей книги под словом «насилие» сделаны указания на разные страницы из других сочинений, но ни одной ссылки на мои. Не доказательство ли это того, что то учение, которое вы мне приписываете и которое, в сущности, есть не что иное, как учение Христа, вовсе не политическое, а религиозное учение?
> It seems to me only that I am not an anarchist in the sense of a political reformer. In the index of your book under the word 'violence' references are made to various pages of the other writers, but not one to mine. Is this not proof that the teaching which you ascribe to me, and which is, in essence, nothing other than the teaching of Christ, is not a political but a religious teaching? (working English)
> — PSS Tom 72, pp. 424–426 · christian-anarchism · 1900-08-01

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

person · exists · dives: copyright-renunciation, crisis, doukhobors · names: Pavel Birukoff / Pavel Biryukov

_copyright-renunciation_: correspondent in the earliest sustained free-publication discussion (1885); later biographer
_crisis_: biographer; the framing source is his Swedish ed. (Leo Tolstoj: Hans liv och verk) Book IV «Kritisk period» ch.14 «Krisen» p.262 — names the chapter 'crisis' while reporting Tolstoy's denial of one (user-provided photograph)
_doukhobors_: Sent to the Caucasus 1895 to verify the facts; wrote the article Tolstoy afterworded; co-signed «Help!» and was exiled. Tolstoy's biographer.

- PSS Tom 63, pp. 295–298 · copyright-renunciation · 1885-10-19 — Earliest sustained discussion of free publication in the letters (the Posrednik / cheap-edition circle). Cited by id and PSS pages; not quoted verbatim because the clean extract of this early-volume pre-reform text renders unreliably (see needsReview).

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

> Сколько бы ни набрасывали на горящую кучу хвороста дров, думая этим затушить огонь, — огонь, непотухающий огонь истины, только на время приглохнет, но разгорится еще сильнее и сожжет всё то, что наложено на него.
> However much firewood is thrown onto the burning heap of brush in the hope of putting the fire out, the fire — the unquenchable fire of truth — will only die down for a time, then blaze up the more strongly and burn everything that has been piled upon it. (working English)
> — PSS Tom 39, pp. 99–105 · doukhobors · 1895-10-01

Visuals: 1 (1 usable) — Pavel Ivanovich Biryukov, c.1913 [PD]

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

### Sophia Tolstaya

person · exists · dives: copyright-renunciation

_copyright-renunciation_: opposed the 1891 renunciation; redacted 19 lines of the 22 July 1891 diary entry

> И вчера же был разговор с женой о напечатании письма в газетах об отказе от права авторской собственности. Трудно вспомнить, а главное, описать всё, что тут было: [Вымарано 19 строк.]
> And yesterday too there was a conversation with my wife about printing in the newspapers the letter renouncing the right of literary property. It is difficult to recall, and chiefly to describe, everything that was said: [19 lines erased.] (working English)
> — PSS Tom 52, pp. 45–47 · copyright-renunciation · 1891-07-22

### State Tolstoy Museum

institution · missing · dives: copyright-renunciation

_copyright-renunciation_: holds the diary and letter manuscripts cited here (manuscript fond, the 'steel room')

> 4) Право на издание моих сочинений прежних: десяти томов и азбуки прошу моих наследников передать обществу, т. е. отказаться от авторского права. Но только прошу об этом и никак не завещаю. […] То, что сочинения мои продавались эти последние 10 лет, было самым тяжелым для меня делом в жизни.
> 4) I ask my heirs to hand over to the public the right of publication of my earlier works — the ten volumes and the Azbuka — that is, to renounce the copyright. But I only ask this and in no way bequeath it. […] That my writings have been sold during these last ten years was the heaviest thing in my life. (working English)
> — PSS Tom 53, pp. 14–18 · copyright-renunciation · 1895-03-27

Visuals: 1 (0 usable) — State Tolstoy Museum digital collection (manuscripts, photographs, portraits) [rights-reserved]

### The Burning of Arms

event · missing · dives: doukhobors

_doukhobors_: The coordinated mass destruction of weapons by ~7,000 Doukhobors, night of 28–29 June 1895 (OS); the catalysing event.

> После этого, 28 июня 1895 года, духоборцы, живущие в Ахалкалакском уезде Тифлисской губернии, снесли в одну кучу в поле, около села Спасского, всё свое имевшееся у них оружие и, обложив его дровами и углем и облив керосином, сожгли
> After this, on 28 June 1895, the Doukhobors living in the Akhalkalaki district of the Tiflis province carried all the weapons they had into a single heap in a field near the village of Spasskoye and, having piled wood and coal upon them and doused them with kerosene, burned them. (working English)
> — PSS Tom 39, pp. 209–215 · doukhobors · 1895-08-14

Visuals: 1 (1 usable) — PSS Tom 39 p.209 — the Burning of Arms paragraph (rendered from the local PD PSS PDF) [PD]

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

### Varvara Mac-Gahan

person · missing · dives: tolstoyanism

_tolstoyanism_: Russian-American journalist (1850–1904), widow of war correspondent Januarius MacGahan; addressee of the 1894 letter. Her writing about 'the Tolstoyans' and 'the movement' is what Tolstoy answers by denying both exist.

> Вы вот пишете о «толстовцах» и других моих последователях, о движении, поднятом моей проповедью, и о том, почему толстовцы проявляют мало рвения к пропаганде мыслей, которые осчастливят человечество; а я не знаю не только каких-либо других последователей, но и толстовцев
> You write about 'the Tolstoyans' and my other followers, about the movement raised by my preaching, and about why the Tolstoyans show so little zeal in propagating the ideas that would make mankind happy; but I know of no other followers, nor of any Tolstoyans. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

> А о толстовцах, движении и т. п. я ничего не знаю, или даже знаю, что этого ничего нет.
> As for Tolstoyans, a movement, and so forth — I know nothing of it, or rather I know that there is no such thing. (working English)
> — PSS Tom 67, pp. 225–227 · tolstoyanism · 1894-09-22

### Vladimir Chertkov

person · exists · dives: christian-anarchism, copyright-renunciation, crisis, doukhobors, tolstoyanism

_christian-anarchism_: Tolstoy's closest disciple and publisher; gave «христианский анархизм» programmatic Russian form in the 1905 booklet O khristianskom anarkhizme (Svobodnoe Slovo), the in-circle frame the Sacy phrase points to. The 1905 booklet is not held locally.
_copyright-renunciation_: co-drafter of the six wills; drafted the 1910 Explanatory Note; held Tolstoy's post-1881 rights
_crisis_: disciple/correspondent from 1883; the PSS Tom 85 apparatus that carries the editors' 'кризис своих воззрений' annotates the Chertkov letters
_doukhobors_: Co-author of «Help!»; expelled to England 1897, where he became the organising hub of the relief effort.
_tolstoyanism_: Not named in the four quotes, but the focal point of the ambivalence: the de facto organiser, dogmatist and publisher (Free Age Press) of the very movement Tolstoy disowns. The gap between Tolstoy's 'there is no such thing' and Chertkov's institution-building is the dive's central tension.

> 1) Все его сочинения, литературные произведения и писания всякого рода, как уже где-либо напечатанные, так и еще не изданные, не составляли после его смерти ничьей частной собственности, а могли бы быть издаваемы и перепечатываемы всеми, кто этого захочет.
> (working English) 1) That all his compositions, literary works and writings of every kind, whether already published anywhere or not yet issued, should after his death be no one's private property, but might be published and reprinted by anyone who wishes.
> — PSS Tom 82, pp. 227–231 · copyright-renunciation · 1910-07-31

> …21 мая 1883 г. Толстой, пережив уже кризис своих воззрений и отстраняясь от всяких дел материального характера, выдал ей нотариально засвидетельствованную доверенность…
> …on 21 May 1883 Tolstoy, having already lived through the crisis of his views and withdrawing from all affairs of a material character, issued her a notarised power of attorney… (working English) — EDITORIAL voice: Jubilee Edition apparatus, not Tolstoy.
> — PSS Tom 85, pp. 193–196 (editorial note) · TEI v85_059_a10_11 · crisis · 1885

> Среди духоборов, или, скорее, христианского всемирного братства, как они теперь называют себя, происходит ведь не что-нибудь новое, а только произрастание того семени, которое посеяно Христом 1800 лет тому назад, — воскресение самого Христа.
> Among the Doukhobors — or rather the universal Christian brotherhood, as they now call themselves — what is taking place is nothing new, but only the sprouting of that seed which was sown by Christ 1,800 years ago: the resurrection of Christ himself. (working English)
> — PSS Tom 39, pp. 192–196 · doukhobors · 1896-12-26

Visuals: 5 (4 usable) — Vladimir Chertkov, portrait by Ilya Repin (1890s) [PD], Tolstoy and Chertkov together, Yasnaya Polyana, 29 March 1909 [PD], V. G. Chertkov, 1883 (photograph by A. F. Eichenvald) [PD], Portrait of V. G. Chertkov, Ivan Kramskoy, 1881 [unknown], Tolstoy and Chertkov at Yasnaya Polyana, 1909 [PD]

### What I Believe (В чём моя вера?)

work · missing · dives: crisis

_crisis_: companion confessional work; 'жизнь моя вдруг переменилась'

> Пять лет тому назад я поверил в учение Христа — и жизнь моя вдруг переменилась […] Со мной случилось то, что случается с человеком, который вышел за делом и вдруг дорогой решил, что дело это ему совсем не нужно,— и повернул домой.
> Five years ago I came to believe in Christ's teaching — and my life suddenly changed […] What happened to me was what happens to a man who goes out on some errand and then suddenly decides on the way that the errand is of no use to him at all — and turns back home. (working English)
> — PSS Tom 23, pp. 304 · TEI v23_304_465_V_chem_moja_vera · crisis · 1884

## 4. Integrity report

**Unresolved evidenceRefs** (0)

- none

**Name conflicts (same key, multiple spellings)** (1)

- pavel-birukoff: Pavel Birukoff / Pavel Biryukov (copyright-renunciation, crisis, doukhobors)

**wikiType conflicts** (1)

- aylmer-maude: person / translator

**Works routed to works/ (not a wiki type)** (2)

- confession (work)
- what-i-believe-в-чём-моя-вера (work)

**vaultStatus drift (dossier vs live)** (2)

- confession: dossier ['exists'] → live stub
- the-kingdom-of-god-is-within-you: dossier ['exists'] → live stub

**Entities with zero evidence** (9)

- alexandra-tolstaya (copyright-renunciation)
- aylmer-maude (copyright-renunciation, doukhobors)
- ernest-howard-crosby (christian-anarchism)
- felix-ortt (christian-anarchism)
- leopold-sulerzhitsky (doukhobors)
- resurrection (doukhobors)
- sergei-tolstoy (doukhobors)
- society-of-friends (doukhobors)
- the-kingdom-of-god-is-within-you (doukhobors)

**Missing wikilinkTarget** (1)

- What I Believe (В чём моя вера?) (crisis)

**Slug ≠ page id** (0)

- none

## 5. Method

Built by `docs/research/lib/build_evidence_index.py`, which walks every `docs/research/*/dossier.yaml`. Entity key = slug of `wikilinkTarget` (`.md` stripped), equal to the eventual wiki/works slug. Each entity's `evidenceRefs` are resolved against its own dive's `evidence[]`; visuals are attached by `relatedEntity` and deduped across dives. `vaultStatus` is re-derived live against `website/src/wiki/` and `website/src/works/` (stub = prose body < 60 words, or a `draft` with < 120). Output is deterministic. Regenerate: `python3 docs/research/lib/build_evidence_index.py`.

