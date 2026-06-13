---
layer: reference
lastUpdated: 2026-06-03
tags: [research]
---

# Session log — fire-metaphor corpus-dive

Append-only record of what each session covered. The resume queue is the dossier's `notCovered` list.

## Session 1 — 2026-06-03 (initial dive)

Scope: the **fire + light axis** (candle/spark/lamp side-imagery de-scoped), gospel texts first-class, post-1880 default with letters and diaries first-class, plus an interpretive emblem reading for the tolstoy.life logo question. Fan-out sweep over five non-overlapping territories (gospel zone Tom 23–24; late works 25–45; letters; diaries; early fiction + *Круг чтения*). Produced `index.md` (narrative), `dossier.yaml` (51 evidence rows + entities + visuals + scholarship), two committed keystone facsimiles (Luke 12:49 harmony Tom 24 p.292; the *«Я верю»* credo Tom 23 p.461), and the draft dev-blog note. `verify_quotes.py`: 51/51. Parent-repo commit `78526d31`.

## Session 2 — 2026-06-03 (follow-up sweep, additive)

Worked the `notCovered` queue without re-sweeping or rewriting the locked narrative. Added **10 evidence rows** (51 → 61):

- **Cross-language Luke 12:49** (the special-attention angle, deepened): `brief-luke12-49` (condensed *Краткое изложение*: «Учение мое, как огонь, запалит мир» — yearning gone) and `abrege-luke12-49` (French *Abrégé*, locally held at `works/v24_941_969_Abrege_de_lEvangile.xml`). Maude English collated as published-PD. New comparison table + prose in §"Where the theme clusters"; only the full harmony keeps and amplifies the yearning.
- **Fuller fiction pass**: `ivan-ilyich-light-darkness` (Tom 26), `what-men-live-by-light` (Tom 25), `father-sergius-light-dimming` (Tom 31 — `localPdf: null`, unresolved Tom→PDF), `hodite-fire-wood` (Tom 26, title = John 12:35). *Resurrection* and *Hadji Murat* spot-checked — only literal/incidental fire, no row.
- **Daily-wisdom anthologies**: `nakazhdyj-truth-is-fire`, `nakazhdyj-one-fire`, `nakazhdyj-brushwood` (Tom 44), `nakazhdyj-light-of-reason` (Tom 43). Круг чтения proper (Tom 41–42, 444 files) swept but sparse — not exhaustively entered.

Added 5 work entities (На каждый день, Death of Ivan Ilyich, What Men Live By, Father Sergius, Walk in the Light) + one scholarship triangulation row.

**PDF-collation of the pre-reform / extractor-degraded entries** (against the PSS print; quoteRu kept verbatim against the TEI extracts so `verify_quotes` stays green; print readings recorded in `needsReview` for ingestion):
- `letter-yushko-1900` (vol36 p.490) — quoted sentence already complete; page corrected 403→490–492.
- **Misattribution corrected**: the 1886 Tom-85 letter (`letter-sofia-1886` → renamed `letter-chertkov-1886`) is to **V. G. Chertkov**, not S. A. Tolstaya (Tom 85 is the Chertkov correspondence). Print: «То тамъ, то здѣсь среди тьмы теперь загораются искры. Я **ихъ** вижу и радуюсь» (TEI drops «тамъ…здѣсь» and «ихъ»).
- `diary-1903-divine-spark` (vol20 p.194) — print «душа **человѣка** есть божеская искра» (TEI drops «человѣка»).
- 1896 «блюдение огня» (vol19 p.121) — TEI garbles it; print has a clean strong fire passage (recovered for future ingestion, not entered as a row).

`verify_quotes.py`: 61/61 verbatim, 0 label warnings. HTML rebuilt via `serve.py --build-only`. Independent verifier pass run in a fresh context.
