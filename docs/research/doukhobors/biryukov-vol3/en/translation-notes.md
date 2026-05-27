---
layer: reference
lastUpdated: 2026-05-27
tags: [research, biryukov]
---

# Translation notes — editorial judgment calls

Editorial decisions made while translating Biryukov's *Biography of L. N.
Tolstoy*, Volume III, into English (see [`README.md`](README.md) for the locked
conventions and the Policy-A source-fidelity rule). This file records calls
where the source is ambiguous or suspect and a choice had to be made, so the
reasoning stays traceable.

## Chapter 9 — «соска» and «преувеличивать»

Two calls in the Part II batch (2026-05-27):

- **«соска» → "the dummy."** A first draft glossed the word inside Marya
  Lvovna's quoted letter as "the [infant's] dummy"; the bracket was removed in
  review, because the README forbids editorial brackets *inside* quotations (and
  the same word is rendered bracket-free, "a passage about the dummy," a few
  lines later in the chapter).
- **«преувеличивать» → "magnify."** Tolstoy's closing diary-prayer reads «Дело
  же Твое в том, чтобы преувеличивать силу Твою в себе и во всем мире».
  «Преувеличивать» literally means "to exaggerate" — a valid word, so strict
  Policy A would reproduce it as "exaggerate." But in English "exaggerate Thy
  power" carries a false connotation of overstatement that is absent in the
  devotional Russian, whereas "magnify" is the verb English prayer uses for
  enlarging/extolling divine power (cf. the Magnificat). **Decision (Johan,
  2026-05-27): keep "magnify"** as the more faithful rendering of the sense.

Also preserved literally: the two distinct working titles of *The Fruits of
Enlightenment* — «Исхитрилась» (sg.) → *She Got Out of It* and «Исхитрились»
(pl.) → *They Got Out of It* — reproducing the source's differing forms rather
than normalising them to one.

## Chapter 10 — «Перле»/«Кройдоне» and the Acts 4:32 citation

- **«Перле» → "Purleigh," «Кройдоне» → "Croydon."** The garbled transliterations
  are restored to the real English places — the Tolstoyan Brotherhood-Church
  agricultural colony at Purleigh, Essex (the source itself locates it «недалеко
  от Лондона, в Эссексе»), and Croydon. Under Policy A these are garbled tokens
  restored to their obviously-intended word, not valid-but-suspect values.
- **Acts IV, 32 rendered as a block quote.** Biryukov introduces the verse
  exactly as he introduces Tolstoy's verbatim letters (introduction + colon +
  quoted text), so it is set as a Markdown block quote like every other verbatim
  citation in the chapter. (A first draft left it inline, citing a ch.18
  precedent for run-in Scripture that does not actually exist.)

## Chapter 11 — *What Is Truth* (no question mark), and literal readings kept

- **«Что есть истина» → *What Is Truth*, without a question mark — applied
  corpus-wide.** The chapter narrates that N. N. Ge deliberately titled the
  painting «без вопросительного знака», reading Pilate's line as an ironic
  statement rather than a question; the RU never prints the "?". **Decision
  (Johan, 2026-05-27): drop the "?" everywhere** — ch.11 (H1 and in-text), the
  passing mention in ch.12, and the volume [index](../index.md) — for fidelity
  and internal consistency, even though the painting is conventionally known in
  English as "What Is Truth?".
- **Literal Scripture references.** «1 посл. Иоанн, 14» → "1 Epistle of John,
  14" is reproduced as the source gives it, though it is almost certainly meant
  as 1 John 3:14; likewise "John, XVIII, 38" and "Matt., ch. VI" — no
  conjectural correction (Policy A).
- **Garbled English inside Tolstoy's own quotations kept literal.** Emerson's "I
  can get alone without it" (for "get along") and Swift's "the best fruit which
  the birds have pitching it" sit *inside* Tolstoy's verbatim diary/letter, so
  they are kept as primary-text artifacts, with the RU's meaning-gloss carried in
  the `(* … *)` footnote, rather than silently corrected.
- **Out-of-order prayer-diary dates** (16 July → 30 June → 5 July → …) are
  reproduced in the source's order, not re-sorted.

## Chapter 12 — French OCR restoration, and the renunciation numerals

- **Heavy French restoration in Alexandra Andreyevna Tolstaya's quoted speech
  (and Turgenev's saying).** The source's French is badly corrupted (dropped
  accents, Cyrillic «се» for «ce», OCR garble such as «cuibite» → *culbuté*,
  «eronnee» → *étonnée*). Each token was repaired to standard accented French as
  garble-repair under Policy A; no grammar that was actually present was
  rewritten. Turgenev's saying is kept in French in the body with the Russian
  gloss rendered as an English footnote, parallel to the chapter's other two
  French passages (a first draft had translated it into the body, leaving the
  footnote redundant).
- **Literal numerals/dates kept:** "5,000" (the running-the-gauntlet diary
  entry); the renunciation declaration's "XIIth volume of the 1886 edition" and
  "XIIIth volume … 1891."
- **«Екатер. губ.» → "Yekaterinoslav Province"** — an obvious abbreviation
  expanded (consistent with Feinerman's documented move to that province).

## Chapter 16 — «Прудки осин» → "Prudki" (treated as a place name)

In a quoted diary/letter passage, L. N. writes that one evening he rode
«на Осиновую гору и Прудки осин». «Осиновую гору» is rendered as the toponym
**"Osinovaya Hill."** The parallel destination «Прудки осин» is ambiguous in the
source (lowercase, no capitalisation to mark a proper name):

- **Literal/common-noun sense:** «Прудки» = "little ponds," «осин» = genitive
  plural of *осина* (aspen) → "ponds of aspens" / "aspen ponds."
- **Toponym sense:** «Прудки» is a common Russian village name; paired with a
  named hill as a riding destination, the phrase most plausibly names a place.

**Decision (Johan, 2026-05-27): treat it as a place.** Rendered **"Prudki,"** for
consistency with the parallel toponym "Osinovaya Hill" and with Policy A (prefer
literal reproduction of a valid-but-suspect source value over a conjectural
common-noun gloss). The descriptive «осин» ("of aspens") is not separately
transliterated; it is recorded here as the residual ambiguity. The first draft
had read "the aspen ponds."

## Chapter 1 — preface, the 51-source bibliography, and literal numerals

The volume's structurally unusual opener (Biryukov's Author's Preface to Vol. III
+ a numbered 51-entry source bibliography + the `## Part I` divider + the chapter
narrative, in that order). Calls in the Part-I / Part-II-tail batch (2026-05-27):

- **«trouble fete» → *trouble-fête*, no reader gloss.** The dropped hyphen/accents
  are repaired to the real French (garble under Policy A), but the word is kept in
  the body without a bracketed gloss — Biryukov supplies none, and the README
  forbids editorial brackets inside quotations. (Translator and reviewer concurred.)
- **Bibliography entry 22: «т. 11» → "vol. 11" (literal).** A first draft silently
  normalised Koni's *On Life's Path* «т. 11» to the probably-intended "vol. II";
  reverted to the literal "vol. 11" under Policy A (reproduce plausible numerals
  literally; no conjectural substitution — cf. the *Resurrection* "XXXIX and XI"
  precedent). The likely "II" reading is recorded here, not in the text.
- **Other bibliography entries reproduced literally** (valid-but-suspect real-world
  strings, not nonsense garble): 30) "Staddling … James Clark et C№" (prob.
  Stadling / Clarke & Co.); 31) "Cassel & C№" (prob. Cassell); 37/38/44) French
  titles with dropped accents; 39) "Kuhne … Denkweis" (prob. Kühne / Denkweise);
  40) "Luxembourg, Rosa … Nachlasz" (prob. Luxemburg / Nachlass); 41) "G-ie"
  (= Cie); 42) "Esser" (?Essor); 51) "Tuckton House Tuckton" (repeated word kept).
- **«сочинения неопровержимыми» → "the works … irrefutable" (plural).** A first
  draft smoothed the plural to "the work"; restored to the literal plural.
- **«Симурден» → *Cimourdain*** (Hugo, *Quatrevingt-treize*), and the stray «ј» in
  «Библиографический указательј» dropped — garble-repairs under Policy A.
- Matt 5:45, quoted inside Biryukov's own sentence (not introduced as verbatim
  Tolstoy text), is rendered inline rather than as a block quote — per the ch.10
  principle that block-quoting is triggered by the introduce-and-colon framing.

## Chapter 7 — a mis-set narrative line, and a faithful dangling colon

- **Quote-boundary fix.** Biryukov's own remark «Какой парадокс! И, однако, он в
  него верил.» ("What a paradox! And yet he believed in it.") had been wrapped as
  a block quote with an orphan opening quote mark; reset to plain narrative. That
  orphan mark was the displaced *close* of Alexandra Andreyevna's preceding
  reminiscence, which is now closed at its proper end; her second excerpt, split by
  a `(* … *)` footnote, is treated as one quotation (no re-opening quote mark at
  the resumption).
- **Dangling colon kept.** The medicine letter to Chertkov ends in the source with
  «…решение их в душе каждого:» — a trailing colon with no continuation before the
  next paragraph. The RU capture itself dangles (verified), so the colon is
  reproduced literally rather than "completed" (Policy A).
- French OCR in Alexandra Andreyevna's quoted exchanges repaired to standard
  accented French (garble-repair, as in ch.12): «suis»→*sois*, «par»→*pas*,
  «та gloire»→*ma gloire*, «Nabuchodonsor»→*Nabuchodonosor*, and similar.

## Chapter 8 — «Николай Палкин» house form, and the *vinovat* pun

- **«Николай Палкин» → *Nikolai Palkin*, no gloss — applied corpus-wide.** A first
  draft glossed Tolstoy's article as *Nikolai the Stick*. **Decision (Johan,
  2026-05-27): use the standard transliterated title *Nikolai Palkin* everywhere,
  with no descriptive gloss** — for fidelity (Policy A favours the title value),
  for the conventional English title, and for consistency with the ch.5 index
  entry "Palkin". The pre-existing occurrence in ch.14 (« "Nicholas Stick"
  (*Nikolai Palkin*) ») was normalised to *Nikolai Palkin* to match.
- **The «Виноват…/вино» pun — diminuendo + a translator's footnote.** Tolstoy opens
  a letter «Виноват… винов… вино… вин…», trailing off from *vinovat* ("at fault")
  through *vino* ("wine") to the bare letter *в*. Rendered as the English
  diminuendo "Guilty… guilt… gui… gu… g…" (the *vino* layer cannot survive).
  **Decision (Johan, 2026-05-27): add a `(* … *)` translator's footnote** flagging
  the lost wordplay — the corpus's first *net-new* explanatory footnote (as
  opposed to footnotes that reproduce Biryukov's own). Russian terms are
  transliterated in it to keep the EN body Cyrillic-free.
- The source's own initial-switch in the Rakhmanov memoir («матери М. Н.» … then
  «матери П.») is reproduced literally, not normalised.
