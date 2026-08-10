# az.lib.ru Vol I — "Глава 10. Роман" probe (and Vol I OCR provenance)

**Source URL:** http://az.lib.ru/b/birjukow_p_i/text_1905_tolstoy02.shtml (Vol I, 2-я часть)
**Source edition (per OCR header on `text_1905_tolstoy01.shtml`):** «Павел Бирюков. Биография Л. Н. Толстого, **книга первая** (Серия "Гений в искусстве"), М., "Алгоритм", 2000»
**OCR:** Виталий Адаменко, 3 октября – 24 декабря 2002. (Earlier than the Vol III OCR by the same person; Vol III is 10–20 January 2003.)
**Captured:** 2026-05-28 via `curl | iconv -f windows-1251 -t utf-8`.

---

## Why this probe was run

Mark Aldanov's 1921 review of the Berlin Ladyzhnikov reissue (see [`aldanov-1921-review-berlin-ladyzhnikov.md`](aldanov-1921-review-berlin-ladyzhnikov.md)) reports a chapter in the Berlin reissue *"не печатавшаяся при жизни Софьи Андреевны: предшествовавший женитьбе Льва Николаевича его роман и переписка с одной светской барышней, фамилию которой г. Бирюков не считает удобным назвать."* ("Not printed during Sofya Andreyevna's lifetime: Lev Nikolayevich's pre-marriage romance and correspondence with one society lady whose name Mr Birukoff did not consider it convenient to disclose.")

If the 2000 «Алгоритм» reprint descends from the first edition, the az.lib.ru capture should lack this chapter. If it descends from Berlin 1921, the chapter should be present. The probe was a cheap text-search across Vol I part 2 (the relevant period, 1851–1862) for chapter structure and romance content.

## Probe findings

### The «Алгоритм 2000» two-book division

The OCR header on Vol I part 1 names the source as "**книга первая**" of the 2000 Алгоритм reprint. The OCR header on Vol III names the source as "**книга вторая**". Therefore the Алгоритм 2000 two-book set splits as:
- **Book 1**: Russian Vols I–II (both parts of each).
- **Book 2**: Russian Vols III–IV.

The same OCR'er (Vitaly Adamenko) digitised both books. Book 1 OCR'd late 2002, Book 2 OCR'd early 2003. Both are deposited on az.lib.ru.

### Vol I chapter structure (chs 1–11, captured via az.lib.ru text_1905_tolstoy01.shtml + 02.shtml)

Numbering is continuous across the two HTML files.

**Part 1 (`text_1905_tolstoy01.shtml`, 452 kB):**
- Предисловие к первому изданию (Preface to the first edition)
- Глава 1. Предки Л. Н. Толстого со стороны его отца
- Глава 2. Предки Л. Н. Толстого со стороны его матери
- Глава 3. Родители Льва Николаевича
- Глава 4. Детство
- Глава 5. Отрочество
- Глава 6. Юность
- Глава 7. Кавказ
- Глава 8. Дунай и Севастополь

**Part 2 (`text_1905_tolstoy02.shtml`, 418 kB):**
- Глава 9. Петербург
- **Глава 10. Роман**
- Глава 11. Первое заграничное путешествие. Московская жизнь
- (further chapters continue through 1862; not enumerated in this probe)

### "Глава 10. Роман" — content

The chapter is **49 lines, 99 kB** of dense text. **24 references to letters/correspondence** (письме / письмо / пишет / пишу). Tolstoy's letters to and from Valeria Vladimirovna Arsenyeva are quoted at length.

The chapter opens with a survey paragraph of Tolstoy's pre-marriage romances:

> *"В предыдущей жизни его уже были попытки любви, кончившиеся, впрочем, ничем. Самая сильная любовь была детская, к Сонечке Калошиной. Потом была любовь в студенческие годы к Зинаиде Молоствовой. Любовь эта была больше в воображении. Зин. Мол. едва ли знала что-нибудь про это. Потом казачка в станице, о чем мы упоминали в своем месте. Потом светское увлечение Щербатовой, которая тоже, вероятно, мало знала про это чувство, так как Лев Николаевич всегда был робок, застенчив в этих делах. Наконец, еще более сильная и серьезная — это была любовь к Валерии Арсеньевой."*

(*"In his previous life there had already been attempts at love, ending however in nothing. The strongest was a childhood love for Sonechka Kaloshina. Then love in student years for Zinaida Molostvova. This love was more in imagination — Zin. Mol. hardly knew anything of it. Then the Cossack woman in the village, of which we mentioned in its place. Then a society infatuation with Shcherbatova, who likewise probably knew little of this feeling, since Lev Nikolayevich was always shy, bashful in these matters. Finally, an even stronger and more serious — this was the love for Valeria Arsenyeva."*)

After the survey, the chapter follows the Arsenyeva episode in detail:
- The Arsenyev family's social circle (aunt, three nieces Valeria/Olga/Zhenechka, French companion Mlle Vergani).
- Tolstoy's letters from Yasnaya Polyana to Arsenyeva in Moscow during the coronation of Alexander II (26 August 1856).
- The crisis when Tolstoy learns of Arsenyeva's infatuation with her music teacher **Mortier** — Birukoff names Mortier openly.
- Tolstoy's 8 November 1856 letter from Petersburg (the "Mortier letter").
- Direct address to Arsenyeva by full first name and patronymic — *"Прощайте, словами это не доказывается, а внушает Бог, когда приходит время. Христос с вами, милая, истинно милая **Валерия Владимировна**."* ("Farewell, this is not proved by words but inspired by God when the time comes. Christ be with you, dear, truly dear **Valeria Vladimirovna**.")

## The Aldanov contradiction

The az.lib.ru / 2000 Алгоритм / Vol I part 2 chapter **names Arsenyeva openly** in narrative and in the salutations of Tolstoy's letters. Aldanov reported the Berlin 1921 chapter as one in which Birukoff withheld the surname.

Three possible reconciliations:

1. **Aldanov simply misremembered.** His "если память мне не изменяет" ("if memory serves") explicitly hedges the entire Berlin-vs-first-edition comparison. He may have remembered the Mortier scandal as "a society lady whose name is withheld" when in fact she was named. This is the simplest reading.

2. **The 2000 Алгоритм reprint reproduces Berlin 1921 with the surname restored.** Birukoff may have published the Berlin 1921 chapter with the surname initially redacted (Arsenyeva died 13 April 1909; even twelve years later, a literary émigré edition might have kept the restraint out of habit or family-courtesy), and the 1923 or later reissues then restored the full name. The 2000 reprint would follow the later, name-restored text.

3. **Aldanov's "new chapter" was about a different woman entirely.** The chapter on Arsenyeva would then be a pre-1921 chapter (in the 1906 first edition), and the Berlin 1921 addition would be a separate chapter about another society lady — possible candidates include Princess Yekaterina Fyodorovna Tyutcheva (whom Tolstoy seriously considered marrying ~1858), Liza Behrs (Sophia Andreyevna's elder sister, whom Tolstoy briefly thought of), or another. The 2000 Алгоритм reprint, if it descends from the first edition, would lack this separate Berlin 1921 chapter; if from Berlin 1921, would have it. The az.lib.ru text does not visibly contain a self-contained chapter on Tyutcheva or Behrs as a separate marriage candidate, suggesting either omission or that the 2000 reprint descends from the first edition without Berlin 1921's addition.

## The practical implication for the §5 verdict on Vols I–II

Regardless of which reconciliation is correct, **the az.lib.ru capture already contains Tolstoy's pre-marriage romance material with Arsenyeva correspondence in full**. A TODO §9 audit recapture from az.lib.ru `text_1905_tolstoy01–04.shtml` will not be missing the Arsenyeva material.

The residual risk: if reconciliation (3) is correct and Berlin 1921 added a chapter on a different woman, the az.lib.ru capture lacks that specific chapter. The cheapest way to settle this would be to obtain a Berlin 1921 scan via WorldCat / a German national library / Russian émigré archives — a separate session.

**Recommendation:** proceed with TODO §9 audit using az.lib.ru as source, flag Aldanov's claim as a known open question in the §9 README, and if a Berlin 1921 scan surfaces later, do a one-time diff.

## Independent finding: Vol I preface evidence for §3 (Tolstoy review involvement)

The Vol I part 1 preface (*Предисловие к первому изданию*) contains direct documentary evidence for the Tolstoy-collaboration claim that the Swedish title page later announced ("granskade af Leo Tolstoj"). Three quoted documents:

### S. A. Tolstaya's authorisation, 19 July 1901
> *"...Конечно, хорошо бы вам заняться биографией; и сам бы Лев Николаевич мог бы еще ответить вам на многое, что вы запросите мне; только надо спешить. Чуть-чуть не угасла всем нам дорогая жизнь. Но теперь, слава Богу, Лев Николаевич хорошо поправляется и опять работает".*

(*"...Of course, it would be good if you took up the biography; and Lev Nikolayevich himself could still answer you on many things you might ask me; only one must hurry. The life dear to us all has very nearly gone out. But now, thank God, Lev Nikolayevich is recovering well and working again."*)

Context: Tolstoy had survived a severe illness; S. A. Tolstaya's authorisation explicitly invites Birukoff to address questions to Tolstoy himself.

### Tolstoy's direct undertaking, 2 December 1901
> *"...Очень рад позировать вам и буду категорически отвечать на ваши вопросы".*

(*"...Very glad to pose for you and will answer your questions categorically."*)

This is the documentary base for the Swedish title page's *"samt granskade af Leo Tolstoj"* claim and the Cassell 1911 Publishers' Note's "Tolstoy himself actually collaborated with him". Authorial collaboration on Vol I (1906) is directly evidenced; collaboration on Vols II–III is plausible by continuity but not separately documented from this preface.

### The seven-year-period scheme

Birukoff records that the seven-year-period structure used to organise Tolstoy's life was Tolstoy's own conception, communicated to Birukoff in conversation:

> *"Это деление я слышал от самого Льва Николаевича, который когда-то в разговоре при мне высказал мысль, что ему кажется, что, соответственно семилетним периодам физической жизни человека, признаваемым некоторыми физиологами, можно установить и семилетние периоды в развитии духовной жизни человека..."*

(*"This division I heard from Lev Nikolayevich himself, who once in a conversation in my presence expressed the thought that it seemed to him that, corresponding to the seven-year periods of physical human life recognised by some physiologists, one could establish seven-year periods in the development of the spiritual life of man..."*)

This is conceptual collaboration, not just fact-checking. Tolstoy supplied an organising frame for the biography.

### Birukoff's situation in exile

The Vol I preface also documents Birukoff's working conditions in exile:
- Exiled administratively from Russia for religious beliefs.
- Cut off from Russian libraries and archives — works from V. G. Chertkov's private archive and the Russian section of the British Museum.
- Petitioned the Minister of Internal Affairs for a two-month return — categorically refused.
- The biography was commissioned by Stock (Paris) for a French complete-works edition of Tolstoy; Birukoff was to supply the redacted Russian source and the biographical apparatus.

These conditions explain why Birukoff would have welcomed Tolstoy's "categorically" promised cooperation and explains the heavy reliance on letters, autobiographical notes, and Chertkov's archive throughout Vols I–III.

## Cross-reference

- The Aldanov 1921 review whose claim this probe tests: [`aldanov-1921-review-berlin-ladyzhnikov.md`](aldanov-1921-review-berlin-ladyzhnikov.md).
- The Vol III preface with parallel OCR provenance and the same "Алгоритм 2000 / Adamenko OCR" chain: [`az-lib-vol3-front-matter.md`](az-lib-vol3-front-matter.md).
- The Swedish witness for Vols I–II's pre-1908 textual state: [`swedish-andra-delen-titlepage.md`](swedish-andra-delen-titlepage.md) and [`swedish-andra-delen-slutord-p453.md`](swedish-andra-delen-slutord-p453.md).
