---
layer: reference
lastUpdated: 2026-05-29
tags: [research, annotations]
---

# Reader annotations — "crisis" dive

Interpretive guidance left by Johan on [`index.md`](index.md) (2026-05-29, via the docs annotation
UI). **Not part of the factual dive** — the dive's prose stays bare by design. These are preserved
as the kind of reader's steer meant to feed the eventual **wiki ingestion** of this dive (above all
the concept page `Tolstoys religious conversion.md`, flagged `missing` in `dossier.yaml`). Ingestion
is a separate, human-in-the-loop step; this file is *guidance for it*, not content for the vault.

## On «переворот»

> Perhaps a resurrection

## On "an upheaval"

> Yes, it's the dialectical endgame (Hegels highest form of dialectics) where you opt out of this
> world and become... something else. Upheavel is a good word, but the Swedish word "Upphäva" even
> better since it both means "get rid of" and "lift up". Same word in German: Aufhebung, that Marx
> used.
> We've both been through this religious passage, me and Tolstoy. I've also felt the sting of "not
> knowing anything anymore" that he talks about in A Confession.

### Corpus check that contextualises the Aufhebung reading (Claude, 2026-05-29)

The *Aufhebung* structure does fit *A Confession* — it negates the old life, **preserves** the oldest
("the force of life which returned was not new, but the very oldest"), and **lifts** ("I was saved
from suicide"). And *переворот* is also the ordinary Russian for a political *overturning / coup*, so
the word itself already carries the revolutionary register Marx's *Aufhebung* shadows.

But the frame is a **later reader's lens, not Tolstoy's**. The TEI corpus (48 files mention Гегель)
shows Tolstoy had no use for Hegel: in his own voice he throws arguing «о Спенсере и Гегеле» onto the
heap of empty pursuits he'd wish gone («то пропади оно совсем»), and a biographical note in the
apparatus records him reckoning Hegel «пустым набором фраз» (an empty set of phrases). So reading
*переворот* as *Aufhebung* re-enacts the dive's own caution about "crisis" — a powerful label brought
from outside. Carry it into ingestion **as an attributed reading**, never as Tolstoy's own framing.

## Threads these annotations open (for ingestion / future dives)

- **Rebirth vocabulary.** "Resurrection" belongs with *родился вновь* (born anew, the Annenkova
  letter, 1894), Tatyana's "second birth", and *Воскресение* (the 1899 novel) — Tolstoy's *own*
  alternatives to "crisis". Already queued in `dossier.yaml` `notCovered` as an un-run sweep.
- **The transformation concept page** (`Tolstoys religious conversion.md`) should foreground
  Tolstoy's own vocabulary (*переворот*, *остановка жизни*) and may *note* the Aufhebung /
  resurrection readings as later lenses — attributed, not asserted.

## Further guidance (Johan, 2026-05-29) — a life of changing views

- **Tolstoy held different views across his life.** The transformation developed from childhood and
  *finalised* in *A Confession*; much of what he believed growing up "vanished when he became a
  follower of Christ." For ingestion: don't flatten Tolstoy into one static doctrine — date his
  positions and mark the pre/post-transformation break. (Sits in productive tension with the
  continuity thesis in [`index.md`](index.md) §4: Gustafson's "the man is not two, but one" is about
  the underlying *search* — it shouldn't be read as "his views never changed", because they did.)

- **The outsider frame (John 15:19–20).** "Because you are not of the world … therefore the world
  hates you." Johan reads the convert's position through it: you know the mainstream from inside but
  the new place barely, and you remain an outsider because you know how well the mainstream guards
  its rule. It fits Tolstoy's late life literally — excommunicated by the Holy Synod (1901), at odds
  with both Church and State. A frame for the concept page, attributed.

- **Words as a weapon — keep the "why".** Johan's caution: word-choice can soften Tolstoy's
  radicalism — e.g. noting he gave up hunting without the *reason* (the ethical / religious turn).
  Keep the motive.
  **Primary-source anchor (Tolstoy documents exactly this mechanism, in his own voice):** the
  *Preface to the English edition of «Что такое искусство?»* (PSS Tom 30, pp. 204–206; TEI
  `v30_204_206`) protests that the Russian censor softened him word by word — «всегда»→«иногда»
  (always→sometimes), «все»→«некоторые» (all→some), «дворцы»→«палаты» (palaces→chambers),
  «патриотизм»→«лжепатриотизм» (patriotism→*false*-patriotism) — **cut his reasons while leaving the
  bald assertions** («причины… пропущены, а ни на чем не основанные утверждения оставлены»), and even
  inverted his meaning (Christ going to the cross «за исповедуемую им истину» / "for the truth he
  professed" rewritten as «за род человеческий», foisting the atonement dogma on him). His phrase:
  expressions «изменявшие смысл и приписывающие мне то, чего я не мог желать сказать» (altering the
  meaning and attributing to me what I could not have wished to say). This is the mechanism to watch
  for when ingesting *any* secondary framing of Tolstoy.
  *Checked (Claude):* the English Wikipedia "Hunting"/"Vegetarianism" subsections actually **keep**
  the ethical/spiritual "why" (added in 2023, not trimmed), so that specific suspicion isn't borne
  out — though the principle holds. On the diet term: Tolstoy's word is **вегетарианство** (139 TEI
  files; «Первая ступень», 1892); "веган" never occurs and is a 1944 coinage (he ate dairy/eggs), so
  "vegetarian" is accurate and "vegan" would be the anachronistic *hardening* — distortion in
  reverse. Accuracy over received framing, both ways; final term choice is Johan's.

- **Framing by ordering — baseline vs. deviation.** Beyond word-choice, *sequence* encodes a
  judgment. "Tolstoy was a huntsman who later became a vegetarian" frames the hunting as the
  authentic baseline and the conviction as a later deviation; foregrounding the arrived-at ethical
  position would honour where he ended up. *Checked (Claude):* the English Wikipedia article carried
  only a single decontextualised "believed in vegetarianism, like Gandhi" sentence from ≤2010 until
  2023, and **no hunting content at all** before the April-2023 restructure — which introduced both
  the ethical "why" *and* the huntsman→vegetarian baseline→deviation arc. So that framing is a 2023
  editorial choice, not old. Note that it **inverts Tolstoy's own sense of his authentic self**: in
  *A Confession* the переворот is a *return* to "the very oldest" force in him (§2.2) — by his own
  logic the ethical conviction is the recovered self and the hunting the corrected deviation, the
  reverse of the received order. For ingestion: watch the *ordering* a source imposes, not only its
  words.

- **On Aufhebung:** Johan's interest is the *word's* double sense (abolish + lift up / *upphäva*),
  not the Hegel–Marx lineage — Tolstoy dismissed Hegel. Carry it as an image, not a school.
