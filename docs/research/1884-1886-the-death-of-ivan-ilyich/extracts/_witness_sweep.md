# Composition-window witness sweep — «Смерть Ивана Ильича» (The Death of Ivan Ilyich)

**Window swept:** 1881 (death of the prototype) through Mar 1886 (повесть finished), focused on the 1884–1886 writing window.
**Sources:** Tolstoy's own diaries (PSS Tom 49) and letters (Toms 63 / 83 / 85), extracted with `extract_tei.py … --choice=reg`. Prototype/people facts cross-checked against the PSS Tom 26 editorial commentary (`v26_679_691_Smert_Ivana_Ilicha_commentary.txt`).
**What was confirmed:** every diary and letter genesis-quote in the editorial spine was located in the corpus and verified against a saved extract, EXCEPT the March 1886 N. N. Ge letter ("...Крестник легенда и Смерть Ивана Ильича"), which is **not present** in this TEI corpus (see notes).

All Russian below is byte-verbatim from the saved `extracts/<tei-id>.txt` files. Translations are labelled **(working English)** and are not authoritative.

> **Dating crux (applies to all three diary entries below).** The PSS Tom 49 diary files carrying the genesis entries are named `…_1883_04_27`, `…_1883_04_30`, `…_1883_05_01`, and the entry openers give dual-style dates ("27 апреля/9 мая", "30 апреля/12 мая", "1/13 мая"). But each file's `# bibl` line reads **"Дневник 1884 г."**, and the Tom 26 editorial commentary explicitly dates them **1884** (calling the 27 Apr entry "Первое упоминание о повести «Смерть Ивана Ильича»" and the 30 Apr entry the record of the "второй приступ"). The editorial brief follows the commentary (1884). The filename year (1883) appears to be a TEI cataloguing artifact; treat the entries as **April–May 1884** but flag the filename/header mismatch.

---

## Genesis & progress

### G1 — Diary, working-title decision ("либо смерть судьи")
- **RU (verbatim):** «Хочу начать и кончить новое. Либо смерть судьи, либо записки несумашедшего.»
- **(working English):** "I want to begin and finish something new. Either *the death of a judge*, or *the notes of a madman*."
- `tei-id`: `v49_087_087_1883_04_27` · Tom 49, p. 87 · **date: 27 Apr 1884** (file/header say "27 апреля/9 мая, 1883"; bibl + commentary = 1884) · diary
- **Significance:** the first recorded conception of the novella under its working title «Смерть судьи»; per Tom 26 commentary this is "Первое упоминание о повести «Смерть Ивана Ильича»."

### G2 — Diary, second approach ("Смерть Ивана Ильича достал")
- **RU (verbatim):** «Пробовал писать — нейдет. Смерть Ивана Ильича достал — хорошо и скорее могу.»
- **(working English):** "Tried to write — it won't come. Got out *The Death of Ivan Ilyich* — good, and I can [do it] more quickly."
- `tei-id`: `v49_088_089_1883_04_30` · Tom 49, pp. 88–89 · **date: 30 Apr 1884** · diary
- **Significance:** the title has shifted from «смерть судьи» to «Смерть Ивана Ильича»; "достал" ("got out / dug out") shows earlier embryonic drafts already existed. Same entry opens with the Ge family delivering a letter from "young Nikolai" (N. N. Ge the son).

### G3 — Diary, first real writing session
- **RU (verbatim):** «Стал поправлять Ивана Ильича и хорошо работал. Вероятно, мне нужен отдых от той работы, и эта, художественная, такая.»
- **(working English):** "Began correcting *Ivan Ilyich* and worked well. Probably I need a rest from that [other] work, and this, the artistic kind, is such [a rest]."
- `tei-id`: `v49_089_089_1883_05_01` · Tom 49, p. 89 · **date: 1 May 1884** · diary
- **Significance:** frames the повесть as restorative "artistic" work set against his treatise labour (*Так что же нам делать?*). Same entry notes a letter from Urusov.

### G4 — To Chertkov: the повесть as the "last" address to his circle + the promise to S. A. Tolstaya
- **RU (verbatim):** «(Еще будет (если буду жив ) смерть Ивана Ильича.² Эту я обещал кончить жене для нового изданья, но эта статья только по форме ( как она начата) относится к нашему кружку — по содержанию ко всем ).»
- **(working English):** "(There will still be (if I live) *the death of Ivan Ilyich*. This one I promised my wife I would finish for her new edition, but this piece relates to our circle only in form (as it was begun) — in content, to everyone.)"
- `tei-id`: `v85_067_iyunya1_2` · Tom 85 · **date: 1–2 June 1885** · to V. G. Chertkov
- **Significance:** ties the повесть to S. A. Tolstaya's "new edition" obligation a full year into the work, and positions it as transcending his "кружок заблудших"; embedded in his self-reckoning with the "художественный, ученый" world he is leaving.

### G5 — To Urusov: the genesis/resumption letter ("Началъ нынче кончать")
- **RU (verbatim):** «Началъ нынче кончать и продолжать смерть И[вана] И[льича].² Я, кажется, разсказывалъ вамъ планъ: описаніе простой смерти простого человѣка, описывая изъ него. Жены рожденье 22-го и всѣ наши ей готовятъ подарки, а она просила кончить эту вещь къ ея новому изданію, и вотъ я хочу сдѣлать ей «сюрприз» и от себя.»
- **(working English):** "Today I began to finish and continue *the death of I[van] I[lyich]*. I think I told you the plan: a description of the simple death of a simple man, describing [it] from within him. My wife's birthday is the 22nd and all of us are preparing presents for her, and she asked me to finish this thing for her new edition, and so I want to make her a 'surprise' from myself too."
- `tei-id`: `v63_408_Kn_L_D_Urusovu` · Tom 63, pp. 282–283 · **date: ~20 Aug 1885** · to L. D. Urusov
- **Significance:** the "surprise"-for-the-new-edition genesis letter; states the artistic programme ("описаніе простой смерти простого человѣка") and the immediate motive (S. A. Tolstaya's name-day/edition deadline).

### G6 — To S. A. Tolstaya: wants to finish "именно Ивана Ильича"
- **RU (verbatim):** «Постараюсь вести себя во всех отношениях — пищи, сна, работы самым благоразумным образом, — с тем, чтобы побольше работать, и желаю кончить именно Ивана Ильича.»
- **(working English):** "I will try to conduct myself sensibly in every respect — food, sleep, work — so as to work more, and I wish to finish *Ivan Ilyich* in particular."
- `tei-id`: `v83_327_oktyabrya12` · Tom 83 · **date: 12 Oct 1885** · to S. A. Tolstaya
- **Significance:** opening of the intense Oct 1885 push at Yasnaya; names the повесть as the priority target.

### G7 — To S. A. Tolstaya: wrote, but "к сожалению не Ивана Ильича"
- **RU (verbatim):** «нынче я встал рано и, убравшись, много писал, к сожалению не Ивана Ильича, а о том, почему мы не видим незаконности, неразумности и несчастия нашей жизни.»
- **(working English):** "today I rose early and, having tidied up, wrote much, unfortunately not *Ivan Ilyich*, but about why we do not see the unlawfulness, irrationality and unhappiness of our life."
- `tei-id`: `v83_328_a13` · Tom 83 · **date: 13 Oct 1885** · to S. A. Tolstaya
- **Significance:** the повесть keeps losing to the treatise work — documents the "большие перерывы" the editors note.

### G8 — To S. A. Tolstaya: will try, but the повесть "можно бы в конце всего"
- **RU (verbatim):** «Завтра постараюсь заняться Иваном Ильичом, но это лучше не обещать, a сделать. Впрочем Иван Ильича можно бы в конце всего, как самое последнее.»
- **(working English):** "Tomorrow I'll try to take up *Ivan Ilyich*, but better not to promise this, but to do it. Though *Ivan Ilyich* could come at the very end, as the very last thing."
- `tei-id`: `v83_330_a16` · Tom 83 · **date: 16 Oct 1885** · to S. A. Tolstaya
- **Significance:** shows him ranking the повесть behind the treatise in his work queue.

### G9 — To S. A. Tolstaya: the "весь поглощен" passage
- **RU (verbatim):** «Я не отчаиваюсь, и ужасно желаю написать Ивана Ильича, и сейчас ездил и думал о нем, но не могу тебе выразить, до какой степени я весь поглощен теперь этой работой, уже тянущейся несколько лет и теперь приближающейся к концу: Нужно самому себе выяснить то, что было неясно, и отложить в сторону целый ряд вопросов, как это случилось со мной с вопросами богословскими.»
- **(working English):** "I do not despair, and terribly wish to write *Ivan Ilyich*, and just now rode out and thought about it, but I cannot express to you to what degree I am now wholly absorbed in this work, already dragging on for several years and now nearing its end: I must clarify to myself what was unclear, and set aside a whole series of questions, as happened with me over the theological questions."
- `tei-id`: `v83_336_oktyabrya23` · Tom 83 · **date: 23 Oct 1885** · to S. A. Tolstaya
- **Significance:** the canonical "весь поглощен … уже тянущейся несколько лет … приближающейся к концу" statement; explicitly likens the повесть's resolution to his theological breakthrough.

### G10 — To S. A. Tolstaya: stalled in December
- **RU (verbatim):** «Я ничего не писал все это время. Один раз немного Ивана Ильича, и то скоро остановился. Я сплю все эти дни совсем хорошо и нахожусь в упадке нерв.»
- **(working English):** "I have written nothing all this time. Once a little of *Ivan Ilyich*, and even then I soon stopped. I sleep quite well these days and am in a state of nervous decline."
- `tei-id`: `v83_349_a23` · Tom 83 · **date: 23 Dec 1885** · to S. A. Tolstaya
- **Significance:** documents the late-1885 stall and the physical/nervous strain of the work.

### G11 — To Chertkov: "пописал … и скоро стал путаться"
- **RU (verbatim):** «Нынче немножко пописал «Ивана Ильича»³ и скоро сталь путаться.»
- **(working English):** "Today I wrote a little of *Ivan Ilyich* and soon got confused/tangled."
- `tei-id`: `v85_095_yanvarya16_17` · Tom 85 · **date: 16–17 Jan 1886** · to V. G. Chertkov
- **Significance:** the early-1886 strain quote; same letter notes "Милый Ге … старший" living at Yasnaya and "все работает" (Ge the elder among the helpers/copyists in this period).

### G12 — To Urusov: "Я плохо подвигаюсь в своей работе" (context note)
- **RU (verbatim):** «Я плохо подвигаюсь в своей работе.³ Но интерес не ослабевает и, если буду жив, выскажу то, чтò имею сказать.»
- **(working English):** "I am making poor progress in my work. But the interest does not flag, and if I live, I will say what I have to say."
- `tei-id`: `v63_344_Kn_L_D_Urusovu` · Tom 63, pp. 234–235 · **date: 11 Apr 1885** · to L. D. Urusov
- **Significance:** a progress-and-strain note from the spring before the August resumption; the editorial commentary attaches Tolstoy's "своей работе" of this period to both *Так что же нам делать?* and «Смерть Ивана Ильича», so this is corroborating, not novella-exclusive — flagged as **context** rather than a hard novella quote.

---

## People around the work

| Person (RU) | Role in the work's making | Source `tei-id`(s) | Why they matter |
|---|---|---|---|
| **Иван Ильич Мечников** (Ivan Ilyich Mechnikov) | Prototype of the protagonist; prosecutor of the Tula court (тульский прокурор); b. 13 June 1836, d. 2 July 1881 (of cancer, aged 45) | `v26_679_691_Smert_Ivana_Ilicha_commentary` | His death is the chronological starting point of the conception; Tolstoy: «…даже моя повесть … имеет некоторое отношение к покойному … бывшему прокурору тульского суда». Hero's age/name track Mechnikov's; clinical accuracy of the cancer death traced to him. |
| **Илья Ильич Мечников** (Ilya Ilyich Mechnikov) | Scientist brother of the prototype; his visit to Yasnaya Polyana (from Paris) prompted Tolstoy's own statement about the prototype | `v26_679_691_Smert_Ivana_Ilicha_commentary` | The occasion on which Tolstoy publicly confirmed the prototype connection ("В разговоре мы вспомнили, что я знал его брата Ивана Ильича"). |
| **Т. А. Кузминская** (Tatyana A. Kuzminskaya) | Tolstoy's sister-in-law; conduit of the prototype material — relayed the dying Mechnikov's reflections "о бесплодности проведенной им жизни" (from the widow) to Tolstoy | `v26_679_691_Smert_Ivana_Ilicha_commentary` | The human source of the повесть's core theme; her memoirs («Моя жизнь дома и в Ясной поляне», ч. III) are a primary witness. Also the addressee of S. A. Tolstaya's 4 Dec 1884 letter naming the rasskaz. |
| **С. А. Толстая** (S. A. Tolstaya) | Commissioned the повесть as a "surprise" for her **new edition** (the deadline/motive); also one of the manuscript copyists | `v63_408_Kn_L_D_Urusovu`, `v85_067_iyunya1_2`, `v83_327/328/330/336/349`, `v26_…_commentary` | The practical driver of completion ("она просила кончить эту вещь къ ея новому изданію"); the entire Oct–Dec 1885 progress record is in letters to her; she copied part of the final fair copy and added the typesetter's note ("12-я часть. Присылать гранки"). |
| **Л. Д. Урусов** (Prince Leonid D. Urusov) | Confidant to whom Tolstoy had earlier described the "plan"; addressee of the ~20 Aug 1885 genesis/resumption letter | `v63_408_Kn_L_D_Urusovu`, `v63_344_…`, `v49_089…05_01` | Received the clearest statement of the artistic programme ("описаніе простой смерти простого человѣка"); Tolstoy "разсказывалъ вамъ планъ". (The Tom 26 commentary also lists Urusov's own grave illness, 1885, among the personal experiences that focused Tolstoy on the death theme.) |
| **В. Г. Чертков** (V. G. Chertkov) | Correspondent on the work's meaning/audience; one of the manuscript copyists | `v85_067_iyunya1_2`, `v85_095_yanvarya16_17`, `v26_…_commentary` | Recipient of the "last address to my circle" framing (June 1885) and the "пописал … стал путаться" strain note (Jan 1886); copied part of the final fair copy (рукою … В. Г. Черткова). |
| **Н. Н. Ге (отец / старший)** (N. N. Ge the elder, painter) | Present at Yasnaya during the writing; one of the manuscript copyists | `v85_095_yanvarya16_17`, `v26_…_commentary` | Jan 1886 letter: "Милый Ге все у нас, старший, все работает"; copied part of the final fair copy (рукою … H. H. Ге). (The March 1886 Ge letter naming the повесть is **absent** from this corpus — see notes.) |
| **Н. Н. Ге (сын / молодой Николай)** (N. N. Ge the younger) | Peripheral; his letter "к брату" was delivered to Tolstoy on the day of the second writing approach | `v49_088_089_1883_04_30` | Places the Ge family at Yasnaya at the exact moment work resumed (30 Apr); "Утром барышня от Ге принесла письмо молодого Николая к брату." |
| **А. П. Иванов** (A. P. Ivanov) | Principal copyist of the повесть's manuscripts | `v26_679_691_Smert_Ivana_Ilicha_commentary` | Named repeatedly as the hand behind the copies ("Копия … рукою А. П. Иванова"; the 81-leaf fair copy исписан … рукою А. П. Иванова …). |
| **Г. А. Захарьин** (G. A. Zakharyin, physician) | Doctor who treated the dying Mechnikov; named source for the clinical fidelity of the death | `v26_679_691_Smert_Ivana_Ilicha_commentary` | Per N. F. Golubov's lecture, the illness/death details reached the literary record via Zakharyin, who treated Ivan Ilyich Mechnikov. |
| **И. С. Тургенев** (I. S. Turgenev) | Not a maker of the work; his death (1883) is named by the editors as one of the personal bereavements that focused Tolstoy on the death theme | `v26_679_691_Smert_Ivana_Ilicha_commentary` | Background/atmosphere only; flagged for completeness, not a participant. |

**Naming note:** the fictional surname is **Головин** (Ivan Ilyich Golovin); the first-redaction frame-narrator (the colleague who visits the widow) was **Творогов**, later renamed **Петр Иванович** (Pyotr Ivanovich), with the widow **Прасковья Федоровна** — all per `v26_679_691…commentary`.

---

## Notes / uncertainties (for `needsReview`)

1. **Diary year mismatch (G1–G3).** Files `v49_087…1883_04_27`, `v49_088…1883_04_30`, `v49_089…1883_05_01` are named 1883 and their openers give dual-style dates, but every `# bibl` line says "Дневник 1884 г." and the Tom 26 commentary dates them 1884. Adopted **1884** (per bibl + commentary + editorial brief); the 1883 in the filename appears to be a cataloguing artifact. Worth a one-line verification against the PDF.
2. **March 1886 N. N. Ge letter — NOT in corpus.** The editorial-spine quote "…Крестник легенда и Смерть Ивана Ильича" (to N. N. Ge) could not be located: no Ge-otcu/Ge-synu TEI file is dated 1885–1886, and a corpus-wide grep for «Крестник» surfaced only the unrelated 1891 S. A. Tolstaya copyright-renunciation list (`v84_453_a11`). This witness must be sourced from the PDF/another edition if needed.
3. **No 1884 daily diary for late Apr–early May beyond the three entries above.** Tom 49's bulk "1884" diary material is the two topical/excerpt files (`v49_060_063_1884`, `v49_122_123_1884`), neither of which mentions the повесть; the genesis is captured only in the three dated entries (G1–G3). The 1884 diary is fragmentary in this corpus.
4. **S. A. Tolstaya 1885 letters live in Tom 83, not Tom 84.** The brief pointed at `v84_*`; the v84 set contains **no 1885 letters** (it begins 1891). All Oct–Dec 1885 progress letters to her are in Tom 83 (`v83_327/328/330/336/349`). The «весь поглощен» quote is `v83_336_oktyabrya23` (23 Oct 1885) — note the brief rendered it slightly abbreviated; the full sentence is given verbatim in G9.
5. **G12 (Urusov, 11 Apr 1885) is context, not a hard novella quote.** "Своей работе" in spring 1885 covers both the treatise and the повесть per the Tom 26 commentary; included as corroborating progress/strain, not as an exclusive Ivan-Ilyich reference.
6. **N. N. Strakhov — no novella mention found.** No 1884–1886 Strakhov letter in the corpus references the повесть; he appears in the editorial spine but is not corroborated as a maker/witness here. Omitted from the People table.
7. **Dates are inferred from `# bibl` / opener lines** (TEI filenames encode Tom+page+addressee, not date). All letter dates above carry the PSS editors' "?" qualifier in the originals (e.g. "Августа 20?"), i.e. they are the editors' own approximate datings.
