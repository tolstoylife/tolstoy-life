---
layer: reference
lastUpdated: 2026-06-12
tags: [research, planning]
title: "Prophet period — the four remaining corpus-dives (paste-ready prompts)"
---

The Prophet period (Period IV, 1880–1910) is nearly dived out. After the work-dives shipped through June 2026 — all the major non-fiction, all the major fiction, two of the three dramas, and the two folk-tale clusters — **four subjects remain**. This file holds a paste-ready `/corpus-dive` prompt for each, scoped against the corpus on 2026-06-12. Each runs in its own fresh session (plan-then-execute discipline); each prompt is self-contained because the new session won't see the conversation that produced it.

## The four, at a glance

| # | Dive | Main TEI text | PSS Tom | Mode | Slug |
|---|---|---|---|---|---|
| 1 | **Круг чтения weekly tales** (1905–06) | cluster (6 tales) | 41 / 42 / 36 | theme dive (multi-workRecord) — **not** `--novel` | `1905-1906-krug-chtenija-tales` |
| 2 | **After the Ball** (После бала, 1903) | `works/v34_116_125_Posle_bala.xml` | 34 | `--novel`, short-work flex (read in full) | `1903-after-the-ball` |
| 3 | **The Forged Coupon** (Фальшивый купон, ~1902–04) | `works/v36_005_053_Falshivyj_kupon.xml` | 36 | `--novel` (novella) | `1902-1904-the-forged-coupon` (verify start year) |
| 4 | **The Living Corpse** (Живой труп, 1900) | `works/v34_007_099_Zhivoj_trup.xml` | 34 | `--novel` + drama flex (read in full) | `1900-the-living-corpse` |

Decisions locked with Johan (2026-06-12):
- **Run order:** Круг чтения → After the Ball → Forged Coupon → Living Corpse.
- **Круг чтения scope:** all six tales (the four short ones + the two longer historical tales).
- **None has a `works/` record yet** → every dive PROPOSES its record's creation (the standard Prophet-period case); the dive never writes the vault.

Running them: paste a prompt as-is to run in-session with accept-edits (the proven path). To run one unattended, append `--auto --confirm-scope` to the first line — the scope is already pinned, so it confirms once and detaches.

---

## Session 1 — Круг чтения weekly tales (run first)

```
/corpus-dive The 1905–06 original tales Tolstoy wrote for the weekly-reading (недельное чтение) sections of Круг чтения — a multi-work theme dive, the third movement of the народный рассказ project after Stories for the People (1880s) and the 1903 folk tales. NOT --novel; this is a theme dive carrying several workRecord proposals, like docs/research/1903-folk-tales/ and docs/research/stories-for-the-people/.

SCOPE (Johan-confirmed, all six tales):
- Алёша Горшок — primary-sources/tolstoydigital-TEI/texts/works/v36_054_058_Alesha_Gorshok.xml (PSS Tom 36; written 1905, excluded by Tolstoy from the published anthology) — the marquee tale (the one the 1903 dive named as the sequel's headline).
- Корней Васильев — krug_chtenija/v41_205_220_Krug_chtenija_weekly_mar_5_Kornej_Vasilev.xml (Tom 41, 1905)
- Ягоды — krug_chtenija/v41_450_460_Krug_chtenija_weekly_jun_5_Jagody.xml (Tom 41, 1905)
- Молитва — krug_chtenija/v41_128_133_Krug_chtenija_weekly_feb_4_Molitva.xml (Tom 41, 1905)
- За что? — krug_chtenija/v42_084_106_Krug_chtenija_weekly_sep_5_Za_chto.xml (Tom 42, 1906; the Polish-exile historical tale)
- Божеское и человеческое — krug_chtenija/v42_194_227_Krug_chtenija_weekly_nov_1_Bozheskoe_i_chelovecheskoe.xml (Tom 42, 1906; the executed revolutionary) — cross-check the earlier reversed-title draft works/v54_204_208_Chelovecheskoe_i_bozheskoe.xml.

No works/ records exist for any of these yet → each workRecord PROPOSES the record's creation (derive recordPath from genre/category; anthology subcategory shelving is a known works-schema <TBD> — flag it in needsReview, don't invent vocab).

Read the prior sibling dives first and cross-link them (ground in the project before the mainstream): docs/research/stories-for-the-people/, docs/research/1903-folk-tales/, docs/research/late-voice-encryption-compression/ (which already maps Круг чтения's translation status — reuse it), docs/research/1897-1898-what-is-art/ (the theory these practise), docs/research/copyright-renunciation/ (Posrednik / the gift to the public domain). The 1903 dive's marquee — the 24 Oct 1910 letter to Gorbunov-Posadov grading the народные рассказы — reaches this cluster (Алёша among the graded); cross-reference, don't re-extract.

Gates as usual: extract_tei.py --choice=reg --notes=auto, verify_quotes.py exit 0, bare project voice, no vault writes (propose only), separate-pass verifier, Phase 6 run-report + Phase 7 handoff. Commit when done; do NOT push (Johan pushes). Plain language in anything I read.
```

---

## Session 2 — After the Ball

```
/corpus-dive --novel After the Ball (После бала), Tolstoy's 1903 short story — a work-subject dive in --novel mode with the short-work flex: the text is only ~10 pages (works/v34_116_125_Posle_bala.xml, PSS Tom 34), so READ IT IN FULL act-of-the-story by act rather than the locate-and-sample close-read novels need (same flex the Power of Darkness dive used for a short play). Keep every other --novel emphasis: heaviest genesis & reception, Characters & prototypes with prototypes[], promoted Themes, a marquee-question section, heavy visuals.

KEY FACTS to pin in Phase 0:
- Main text: works/v34_116_125_Posle_bala.xml (Tom 34). Variants: v34_484_490_Posle_bala_Varianty.xml. Commentary: comments/v34_550_551 (история писания и печатания) + v34_551_553 (описание рукописей).
- Written 1903; published posthumously 1911. No works/ record exists yet → the workRecord PROPOSES the record's creation (fiction/short-stories).
- Prototype is real and well-documented: built on Tolstoy's brother Sergei's courtship and the flogging-through-the-ranks Tolstoy heard of in his Kazan student years — route the prototype edge (character → person) per the novel-mode prototypes[] rule.
- Marquee-question candidate (test as hypothesis, don't assert): the story's «всё дело в случае» — moral life turned by chance/circumstance vs. responsibility — and the frame-tale's old-Tolstoy verdict on the young narrator's world. Triangulate confirms/complicates/extends.

Cross-link siblings: docs/research/1896-1904-hadji-murat/ (the Nicholas-I military-cruelty world, overlapping composition years) and the tolstoyanism dive. Ground in primary + prior dives before mainstream scholarship.

Gates: --choice=reg --notes=auto, verify_quotes.py exit 0, record-creating workRecord, bare voice, no vault writes, separate-pass verifier, Phase 6 + 7 handoffs. Commit, don't push. Plain language.
```

---

## Session 3 — The Forged Coupon

```
/corpus-dive --novel The Forged Coupon (Фальшивый купон), Tolstoy's posthumous novella — a --novel work-subject dive. Main text: works/v36_005_053_Falshivyj_kupon.xml (PSS Tom 36).

KEY FACTS to pin in Phase 0:
- Composition window spans roughly the late 1880s/1890s (first conception) with the main writing push 1902–1904; left somewhat unpolished, published posthumously 1911. Read the v36 commentary (история писания) to pin the exact start year, and set the dated slug from the COMPOSITION window — propose 1902-1904-the-forged-coupon but widen the start if the commentary shows earlier sustained work.
- No works/ record exists yet → the workRecord PROPOSES creation (fiction/novellas, or short-stories — judge by length/schema).
- Structure is the dive's centre: the doubled chain of consequence — one forged coupon propagates evil outward through a chain of people in Part I, then good propagates back through the same kind of chain in Part II. It is Tolstoy's most schematic dramatisation of how sin and redemption pass person to person. This echoes the chain-of-sin doctrine the Power of Darkness dive found («коготок увяз, всей птичке пропасть») — cross-link docs/research/1886-the-power-of-darkness/ and docs/research/1889-1899-resurrection/ (moral regeneration). Marquee-question candidate: the chain as the narrative proof of non-resistance / the kingdom-of-God ethic in action.

Cross-link the late-voice dive (docs/research/late-voice-encryption-compression/) for the 1900s voice. Ground in primary + prior dives first.

Gates: --choice=reg --notes=auto, verify_quotes.py exit 0, record-creating workRecord, Characters & prototypes + Themes + marquee sections, heavy visuals, bare voice, no vault writes, separate-pass verifier, Phase 6 + 7 handoffs. Commit, don't push. Plain language.
```

---

## Session 4 — The Living Corpse (run last)

```
/corpus-dive --novel The Living Corpse (Живой труп), Tolstoy's unfinished 1900 drama — a --novel work-subject dive with the DRAMA FLEX (read the whole play in full, act by act, as the Power of Darkness and Fruits of Enlightenment dives did; --novel's light close-read exists only because novels are too long, which a play isn't). Keep all other --novel emphases: heaviest genesis & reception, Characters & prototypes with prototypes[], promoted Themes, marquee-question, heavy visuals.

KEY FACTS to pin in Phase 0:
- Main text: works/v34_007_099_Zhivoj_trup.xml (PSS Tom 34). Plans/notes: v34_407_410. Variants: v34_411_483. Commentary: comments/v34_533_543 (история писания и печатания) + v34_543_545 (описание рукописей).
- Written 1900, left UNFINISHED and unpublished in his lifetime by his own choice; published posthumously 1911 and famously premiered at the Moscow Art Theatre (1911) — the reception story is the staging story, treat it heavily.
- No works/ record exists yet → the workRecord PROPOSES creation (plays/drama).
- Prototype is real and central: the play is based on the Gimer court case (the real false-suicide / bigamy-divorce affair) — route the prototype edge and note Tolstoy's reported reluctance to finish it for fear of wounding the living people involved.
- Marquee-question candidate (test, don't assert): the indictment of legal marriage and the divorce machinery — honesty vs. the institution — and why Tolstoy abandoned the play. Cross-link docs/research/1887-1889-the-kreutzer-sonata/, docs/research/1889-1909-the-devil/ (marriage), and docs/research/1889-1899-resurrection/ (the courts).

Ground in primary + prior dives before mainstream. Gates: --choice=reg --notes=auto, verify_quotes.py exit 0, record-creating workRecord, separate-pass verifier, Phase 6 + 7 handoffs. Commit, don't push. Plain language.
```

---

## After these four

Prophet-period fiction and drama are then fully dived. The only remainders the project has *never* queued: the mid-size late essays without a dedicated work-dive (*I Cannot Be Silent* 1908, *On Shakespeare and on Drama*, *Patriotism and Government* 1900), the *Reminiscences* (1903–06), and the unfinished late fragments (*Fyodor Kuzmich*, *Khodynka*, *Notes of a Madman*). None is on the declared backlog — raise with Johan only if the four above leave an appetite for more.
