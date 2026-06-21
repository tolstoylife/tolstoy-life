# Session log — 1905-the-great-sin

## 2026-06-21 — full dive, one session (interactive, accept-edits)

P8 from `docs/research/_prophet-period-nonfiction-dives.md`. Built the dive end-to-end:

- Extracted the essay, variants, and commentary (PSS Tom 36) + seven 1905 diary entries (Tom 55) + the 17 Apr 1905 Chertkov letter (Tom 89), all `--choice=reg --notes=auto`.
- Pinned composition: begun 21 Apr 1905 as «Народные заступники», merged with the Henry George piece; finished 4 May; cut at Chertkov's suggestion (24 May–6 Jun); introduction reworked into July; published July 1905 in Русская мысль.
- Marquee resolved **complicates, not contradicts**: the conditional single-tax clause (ch. IX) + Chertkov's cut of the anarchist sentence (variant № 15), with the commentary recording his stated motivation. Scholarship (Wenzer 1997) corroborates ("concession/weakness", unresolved).
- Two background subagents: scholarship sweep (anchor Wenzer 1997; "A Great Iniquity" = Chertkov & I. F. Mayo, The Times 1 Aug 1905; the twin paragraph-cuts) and visuals sweep (8 PD images; Tolstoy c.1905 photo sourced from the A Great Iniquity pamphlet itself).
- `verify_quotes.py` 27/27 PASS. Separate-pass verifier (opus): NEEDS-FIXES → all 3 fixed (two prose date-sequencing slips + `firstPublishedVenueType` magazine→journal) → CLEAN.

**Status:** complete; committed, not pushed. The dossier proposes a `works/` record (`the-great-sin`) and routes 10 entities — no vault writes (ingestion is the separate step). Seeds the P9 `land-question-henry-george` theme-dive.

**Open (see run-report / needsReview):** named Russian critical replies; Maria Tolstaya disambiguation; vault transliterations for the peripheral persons; the Fels/Land-Values pamphlet question.
