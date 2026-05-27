---
layer: reference
lastUpdated: 2026-05-27
tags: [research, biryukov]
---

# P. I. Biryukov, *Biography of L. N. Tolstoy* — Volume III

A complete capture of the Russian text of **Volume III** of Pavel Ivanovich
Biryukov's authorised biography of Tolstoy, «Биография Л. Н. Толстого», as
reproduced chapter-by-chapter on [tolstoy-lit.ru](https://tolstoy-lit.ru). The
volume covers **1884–1899** — from the aftermath of Tolstoy's spiritual crisis
through the famine-relief campaigns, the renunciation of literary property, the
Doukhobor affair, and the writing of *Resurrection*.

Biryukov (1860–1931) was one of Tolstoy's closest disciples and an eyewitness to
much of what he describes; the biography quotes Tolstoy's letters and diaries at
length, so it doubles as a primary source. The work is **public domain** (the
author died in 1931).

This folder exists because the project did not previously hold Vol. III at all.
It is the source base for a full English translation; the earlier
Doukhobor-focused survey in the parent folder drew on only three of these
chapters.

## Status

| | |
|---|---|
| **Russian source** | All 22 chapters captured — **177,657 words**. ✓ |
| **English translation** | Chs 9–22 done — Parts III–IV complete + Part II chs 9–12; 8 to go — Part I (chs 1–6) and Part II chs 7–8, in [`en/`](en/). |

The translation is a substantial job (≈178k Russian words → ≈235k English) and is
done in batches of ≈4 chapters per session; [chapter 18](en/chapter-18.md) is the
approved quality sample and style reference.

## Source & method

- **Source:** `https://tolstoy-lit.ru/tolstoy/bio/biryukov/biografiya-biryukov-3-NN.htm`, `NN` = 1…22.
- **Encoding:** pages are served in **windows-1251**; converted to UTF-8 on capture.
- **Recovered text:** the site embeds Tolstoy's interpolations and many footnotes
  as **hex-encoded JavaScript** (`coding_js_asc("…")`) rather than plain HTML. A
  naïve scrape silently drops these, which is why an earlier capture of the
  Doukhobor chapters resumed mid-sentence in several places. This capture decodes
  those fragments inline, so the text is continuous. (Example: ch. 18's sentence
  *«Можно с уверенностью сказать, что этот религиозный подъём среди духоборцев…»*
  — previously lost — is now intact.)
- **Stripped:** site navigation (the "Том 1–4. Глава:" link menus, the
  *Назад / Вперёд* footer). Biryukov's text, his numbered footnotes, and Tolstoy's
  marked insertions are kept.
- **Headings:** each chapter file carries the chapter title as an `# H1`; the four
  part-dividers (*Часть I–IV*) appear as `## H2` at the chapters where they open.

> **Caveat.** This is a web reproduction, not a critical edition. For citation
> against the printed biography, cross-check a chapter against `az.lib.ru`,
> `ru.wikisource.org`, or the original print volume.

## Contents

Each entry links to the Russian capture. English glosses are for navigation only;
work titles are italicised. Word counts are approximate.

### Часть I — 1884–1886: A new life. New thorns. New creative work.
*Часть I. 1884–1886 гг. Новая жизнь. Новые тернии. Новое творчество.* — chs 1–6, ≈36,400 w

1. [**Глава 1.** События 1884 г. Народная литература](ru/chapter-01.md) — Events of 1884; popular literature *(5,760 w)*
2. [**Глава 2.** «Так что же нам делать?»](ru/chapter-02.md) — *What Then Must We Do?* *(4,329 w)*
3. [**Глава 3.** Бремя жизни. Посланничество. Земельный вопрос](ru/chapter-03.md) — The burden of life; a sense of mission; the land question *(8,679 w)*
4. [**Глава 4.** Религия человечества. В Ясной Поляне. Переписка](ru/chapter-04.md) — The religion of humanity; at Yasnaya Polyana; correspondence *(5,355 w)*
5. [**Глава 5.** Бондарев. Палкин. Дерулед](ru/chapter-05.md) — Bondarev; Palkin; Déroulède *(5,975 w)*
6. [**Глава 6.** «Власть тьмы». Календарь. Переписка с друзьями](ru/chapter-06.md) — *The Power of Darkness*; the calendar; correspondence with friends *(6,302 w)*

### Часть II — 1887–1891: Philosophical grounding and the practice of life.
*Часть II. 1887–1891 гг. Философское обоснование и практика жизни* — chs 7–12, ≈50,600 w

7. [**Глава 7.** «О жизни». Новые посетители. Переписка](ru/chapter-07.md) — *On Life*; new visitors; correspondence *(9,825 w)*
8. [**Глава 8.** В Ясной Поляне за работой. В Москве. Новые друзья](ru/chapter-08.md) — At work in Yasnaya Polyana; in Moscow; new friends *(7,685 w)*
9. [**Глава 9.** Новые шаги. Голос обличения. «Крейцерова соната»](ru/chapter-09.md) — New steps; the voice of denunciation; *The Kreutzer Sonata* *(9,318 w)*
10. [**Глава 10.** Земледельческие общины](ru/chapter-10.md) — The agricultural communes *(4,615 w)*
11. [**Глава 11.** 1890 год. Оптина пустынь. «Что есть истина». Молитва](ru/chapter-11.md) — 1890; Optina Pustyn; *What Is Truth*; prayer *(11,055 w)*
12. [**Глава 12.** В семье. Гости. Отречение от литературных прав](ru/chapter-12.md) — In the family; guests; the renunciation of literary rights *(8,088 w)*

### Часть III — 1891–1895: The famine. The Kingdom of God.
*Часть III. 1891–1895. Голод. Царство Божие* — chs 13–17, ≈47,000 w

13. [**Глава 13.** Начало деятельности среди голодающих](ru/chapter-13.md) — The beginning of the work among the famine-stricken *(8,278 w)*
14. [**Глава 14.** 1892 год. Продолжение деятельности Льва Николаевича среди голодающих](ru/chapter-14.md) — 1892; the continuation of the famine-relief work *(11,410 w)*
15. [**Глава 15.** Вторая голодная зима. Царство Божие](ru/chapter-15.md) — The second famine winter; *The Kingdom of God Is Within You* *(6,112 w)*
16. [**Глава 16.** Окончание кормления голодающих. «Посредник» в Москве](ru/chapter-16.md) — The end of the famine relief; *The Intermediary* (Posrednik) in Moscow *(10,108 w)*
17. [**Глава 17.** Хилков. Дрожжин. «Распятие»](ru/chapter-17.md) — Khilkov; Drozhzhin; *The Crucifixion* (Ge's painting) *(11,068 w)*

### Часть IV — 1896–1899: The Doukhobors. *Resurrection*.
*Часть IV. 1896–1899 гг. Духоборы. «Воскресенье»* — chs 18–22, ≈43,700 w

18. [**Глава 18.** Смерть Вани. «Хозяин и работник». Начало духоборческого движения](ru/chapter-18.md) — The death of Vanechka; *Master and Man*; the beginning of the Doukhobor movement *(9,130 w)*
19. [**Глава 19.** Три смерти. Коронация. Наша ссылка](ru/chapter-19.md) — Three deaths; the coronation; our exile *(10,199 w)*
20. [**Глава 20.** Молокане. «Что такое искусство?»](ru/chapter-20.md) — The Molokans; *What Is Art?* *(10,059 w)*
21. [**Глава 21.** Духоборы. Опять голод. Христианское учение](ru/chapter-21.md) — The Doukhobors; famine again; *The Christian Teaching* *(7,649 w)*
22. [**Глава 22.** Конференция в Гааге. «Воскресение»](ru/chapter-22.md) — The Hague Conference; *Resurrection* *(6,658 w)*

## Related

- [Tolstoy and the Doukhobors](../index.md) — the survey this capture supports.
- [Biryukov, the Doukhobor sections (English)](../extracts/biryukov-biography-doukhobors-EN.md)
  — an earlier translation of only the Doukhobor passages of chs 18, 19, 21. The
  forthcoming `en/` translation of the full chapters will supersede it.
- [Biryukov, the Doukhobor chapters (Russian, flat capture)](../extracts/biryukov-biography-doukhobors-RU.txt)
  — the earlier single-file capture of chs 18/19/21, retained for provenance; the
  `ru/` files here are cleaner and more complete.
