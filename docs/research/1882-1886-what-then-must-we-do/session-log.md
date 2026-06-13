# Session log — `1882-1886-what-then-must-we-do`

## 2026-06-06 — Session 1 (in-session unattended work-dive; complete)

Work-dive on Tolstoy's *What Then Must We Do?* (Так что же нам делать?), the fourth Prophet-period
panel and the economic/social application of the *What I Believe* ethic. Run on the A-Confession-pilot
model (in-session, accept-edits, no `AskUserQuestion` gating, judgment → `needsReview`, note `draft: true`),
medium visual intensity. Followed the handoff from the *What I Believe* session.

**Phase 0 — scope.** PSS Tom 25: work pp. 182–411; first printed variant of ch. XVII pp. 503–507;
variants pp. 614–652; commentary pp. 740–839; forerunner «О переписи в Москве» pp. 173–181. Diaries
Tom 49 (1882–87); letters Toms 63–64. Composition window 1882–1886. Slug year-prefixed.

**Phase 1–2 — sweep + extract.** Deep-read all 40 chapters of the work inline + the census appeal +
the commentary (genesis/dating/publication/reception). Three background sonnet sweeps:
- **Diaries** (Tom 49): 16 entries; verdict — the 1884–86 writing window is **near-silent** (no diary
  names the book, Bondarev, Sutaev, bread-labour or the census). Strongest: the 1 Jan 1883 property/
  violence entry and the 1884 estate-reform plan.
- **Letters** (Toms 63–64): 24 candidates + the v63_286 Alekseev bridge confirmed
  («Я теперь печатаю статью (ее не пропустят ) о собственности»). The Bondarev letters (v63_486 names
  the book's debt), the Kavelin/Engelhardt property letters, the Strakhov reception (v63_337).
- **Visuals** (medium): 8 PD images; keystone = Repin's 1887 *Tolstoy Ploughing*. To-request: Alekseev,
  Bondarev, Sutaev portraits; a Lyapinsky-house photo.

All quotes extracted with `extract_tei.py --choice=reg` (+ `--notes=auto` for diary/letter bodies).

**Phase 3 — scholarship.** Sonnet web sweep + triangulation. High-value: money-as-violence *mechanism*
complicates the received view; the Spencer/organic critique and the Sutaev integration extend beyond
English scholarship; the family-conflict record complicates the Sofia-centred "guilt-ridden patriarch"
frame; Nicolosi 2024 (slum-literature) is the newest angle. English title history pinned
(Hapgood 1887 → Wiener 1904 → Maude 1925 *What Then Must We Do?*).

**Phase 4 — synthesize.** `index.md` (layer: reference), `dossier.yaml` (21 evidence rows + entities +
visuals + scholarship + workRecord + coverage), draft note, rendered `index.html`.

**Phase 5 — verify.** `verify_quotes.py` → **21/21 PASS** (two superscript-marker fixes: wtmwd-let-03,
wtmwd-let-05). Opus verifier in fresh context → see `_verifier-report.md`.

**Key findings carried into the dossier:** begun early 1882 (not 1884); charity-impossibility + money-as-
slavery + division-of-labour-as-seizure + bread-labour (Bondarev/Sutaev) + the contested women chapter;
serialization-refused/cut/dispersed publication (no clean ban); the documented family conflict over the
book complicating the mainstream frame. No `works/` record exists — the dive proposes one.

**Open queue (see dossier `needsReview` / `notCovered`):** excommunicationRelated; which event
dateFirstPublished carries; the works/ folder; the cross-dive diary-dating ambiguity (28 Apr 1883 vs
1884); the un-extracted primary letter (Tom 83) behind the family-conflict quotes; the variants collation;
the wider press reception; Tolstoy's later verdict.
