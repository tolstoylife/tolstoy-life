# Verifier report — *Не могу молчать* (I Cannot Be Silent, 1908) corpus work-dive

**Verdict: CLEAN-WITH-MINORS** — 0 CRITICAL · 0 MAJOR · 3 MINOR · several confirmations.

Independent Phase-5 pass, 2026-06-13. I did not build this dive. Everything load-bearing
checks out: the mechanical gate passes, all five byte-fidelity spot-checks confirm verbatim
against the *genuine source TEI* (not just the extract files), scholarship is attributed,
translations are labelled, workRecord field names and enums are real, entity types and vault
statuses are accurate, and rights/voice hygiene is sound. Three MINOR items, none blocking.

---

## 1. Mechanical gate — PASS

`python3 docs/research/lib/verify_quotes.py docs/research/1908-i-cannot-be-silent/dossier.yaml`:

```
SUMMARY: 42/42 quotes verbatim, 2 facsimile(s) ok, 0 facsimile(s) missing, 0 skipped,
         0 label warning(s) — PASS
```

Matches the "42/42 PASS" stated in index.md Method (line 339) and the dossier header. Consistent.

## 2. Byte-fidelity spot-checks against source TEI — ALL VERBATIM

Re-extracted each source XML with `extract_tei.py --choice=reg --notes=auto` and grepped the
`quoteRu` against the source (not the committed extract):

| evidence id | source file | result |
|---|---|---|
| `marquee-hang-me-too` | works/v37_083_096_Ne_mogu_molchat.xml | FOUND verbatim |
| `draft1-names-stolypin-nicholas` | works/v37_391_399_..._Varianty.xml | FOUND verbatim |
| `hist-pub-fragments-fined` | comments/v37_425_427_..._Istorija_pisanija_i_pech.xml | FOUND verbatim |
| `diary-phonograph-12may` | diaries/v56_117_117_1908_05_12.xml | FOUND verbatim |
| `ms-chertkov-cut-coda` | comments/v37_427_432_..._Opisanie_rukopisej.xml | FOUND verbatim |

Also spot-confirmed `hist-names-cut` ("Имена политических деятелей…") verbatim in the source.
The two comment files use the full names `..._Istorija_pisanija_i_pech.xml` and
`..._Opisanie_rukopisej.xml` (the prompt's abbreviated paths do not resolve — extractor returns
empty silently on a missing file, which initially looked like a MISSING result; it was my path
error, not a dive defect). The cut-coda quote appears verbatim even without `--notes`.

## 3. Primary claims source-anchored — OK

Every factual assertion about the essay's text/genesis/publication traces to an evidence row or
to attributed editorial history. Spot-checked: Lubenko landowner name (anchored to
`hist-trigger-report-text`), the 8-vs-9 May distinction (handled correctly — see below),
"seventeen manuscripts" (flagged in needsReview as read-off-numbering), Stolypin's-necktie /
field-courts context (attributed, not in the dive's voice).

**Confirmed non-issue — the 8 May vs 9 May dates.** The essay's own text reads "Нынче, 9 мая"
(the newspaper dateline as Tolstoy quotes it); Eikhenbaum's reproduction of the source notice
reads "8 мая." index.md keeps these straight: line 110 attributes "the report of 9 May" to the
essay's text; the Genesis section notes the "9 May" is "the paper's dateline, not the day he read
it"; the key-findings bullet uses "8 May 1908" for the actual event (Eikhenbaum's date). The two
dossier rows (`kherson-report-in-text` = essay's 9 мая; `hist-trigger-report-text` = Eikhenbaum's
8 мая) are accurately sourced. Internally coherent.

## 4. Scholarship attributed, not asserted — OK

"Scholarly context", "Reception", "The marquee question" all attribute secondary claims (Knapp
2019, Trotsky 1908, Kropotkin 1909, Lenin 1908, Jones 1989, Bartlett 2010). The mainstream view
is never stated in the dive's own voice. The contested label "conservative anarchist" is
explicitly attributed to Trotsky (lines 272, 293); "Christian anarchism" and "Tolstoyanism" are
pointed at the project dives, not adopted. Both cross-links resolve to `../christian-anarchism/`
and `../tolstoyanism/` (3 occurrences each) and both target dirs exist. The superseded combined
survey is explicitly disclaimed (line 305).

## 5. Triangulation integrity — OK

All 6 `scholarship.triangulation[].evidenceRef` name real `evidence[].id`s; all relations are in
the valid set. Entity evidenceRefs: 0 bad. workRecord evidenceRefs: 0 bad. Relations are
defensible:

- `marquee-hang-me-too` → **confirms** — scholarship treats first-person implication as the core; sound.
- `draft1-names-stolypin-nicholas` → **extends** — the variant-level name-removal is corpus-only
  material no secondary source reaches. Genuinely "extends" (adds beyond scholarship). Sound.
- `ms-chertkov-cut-coda` → **complicates** — the cut of the most explicit demand complicates the
  "unmediated outburst" reading. Defensible: it does not contradict the marquee reading, it
  qualifies how literally to take it. Sound.
- `kherson-report-in-text` → **complicates** — single-notice factual base; honest.
- `corruption-spreads-fire` → **extends** — image-level reading beyond the biographical literature. Sound.

## 6. Translations labelled — OK

All 25 Russian blockquotes in index.md carry "(working English)" (25/25, 0 unlabelled by the
within-window heuristic). All 42 dossier `quoteEn` fields carry the label. No bare translations.

## 7. workRecord accuracy — OK (one MINOR)

Field names and enum values all cross-check against `website/schema/tolstoy-works-schema.md`:

- `mainCategory: Non-Fiction` ✓; `subcategory: Essays and Criticism` ✓ (valid under Non-Fiction);
  `genre: essay` ✓; `firstPublishedVenueType: newspaper` ✓ (enum: journal/newspaper/book/samizdat);
  `firstPublishedInRussiaVenueType: newspaper` ✓.
- `bans[]` object shape ✓: `banningAuthority`, `authorityType: imperial-state` (valid enum),
  `jurisdiction`, `scope: passages-cut` (valid enum), `banDate`/`banDateOldStyle`, `notes`.
- All other field names present in schema: `completionStatus`, `publishedDuringLifetime`,
  `publishedInRussiaDuringLifetime`, `dateWriting{Started,Completed}`, `dateFirstPublished(InRussia)`,
  `firstPublished(InRussia)Venue`, `excommunicationRelated`, `titleAlternatives`, `titleEn/Ru`.
- OS→NS arithmetic correct (verified by datetime): 13 May OS → 26 May NS ✓; 31 May OS → 13 June NS ✓;
  4 July OS → 17 July NS ✓.
- Edge cases (publishedInRussiaDuringLifetime=true, dateFirstPublished low-confidence, bans scope)
  are honestly flagged in `needsReview`. Good.

**MINOR-1 — OS sub-flag key name.** Each workRecord field object uses a bare `oldStyle:` meta-key
to carry the Old-Style date. The works schema names the OS companion fields explicitly:
`dateWritingStartedOldStyle`, `dateWritingCompletedOldStyle`, `dateFirstPublishedOldStyle`,
`dateFirstPublishedInRussiaOldStyle`. The dossier's `workRecord` is a *proposed* field set in a
custom `{field, value, …}` shape (not literal frontmatter), so this is not a schema violation —
but at ingestion the bare `oldStyle:` must be mapped to the correctly-named per-field companion
key, and the dossier does not say which. *Fix:* either rename each `oldStyle:` to the matching
`...OldStyle` companion field, or add one line to the workRecord preamble noting the mapping, so
the ingestor does not have to infer it.

## 8. Entities — OK (one expected FLAG)

All `vaultStatus` values accurate (checked `website/src/wiki/`):
- Chertkov → `exists` ✓ ("Vladimir Chertkov.md"); Yasnaya Polyana → `exists` ✓.
- Gusev, Stolypin, Nicholas II, Maude, Eikhenbaum, Ladyzhnikov, Free Age Press → all `missing` ✓
  (none present in the vault).

wikiTypes: 13 of 14 are among the 12 valid types. The Maude entity correctly uses `person`
(schema line 32 says notable translators like Maude use `type: person` + translator role). The one
non-standard type is **`work`** on "I Cannot Be Silent" — not one of the 12 wiki types. This is the
known Tolstoy-Lab convention (and matches established prior-dive precedent): the entity's `role`
states it "Routes to a NEW works/ record (see workRecord), not a wiki page," and the dossier
annotates the convention inline. The essay correctly has no wiki page and a record-creating
workRecord. **Acceptable as self-flagged**, not an error.

## 9. Coverage honesty — OK

- "Reception & afterlife (Russian society/church first)" → `partial` ✓ (honestly: censorship-as-
  reception, the 21+60 letters, Trotsky/Lenin/Kropotkin; no Synod statement on this essay located).
- "Independent corroboration of the Kherson execution" → `not-covered` ✓ (no archival source
  beyond Tolstoy's text + PSS; routed to needsReview). Honest.
- The `covered` surfaces are genuinely covered (the essay is short, read in full across all 7
  chapters; genesis, redactions, publication all evidence-backed). No over-claiming spotted.

## 10. Rights/voice hygiene — OK

- `extracts/` holds only PD material: 6 byte-faithful txt extracts (works/variants/2 comments/6
  diary), the 2 self-rendered PD facsimiles (.jpg), and the scholarship-notes pair
  (`_scholarship_reception.md/.html`). No rights-reserved images. ✓
- `visuals/` is git-ignored: `docs/.gitignore` rule `research/*/visuals/` matches; `git ls-files`
  returns nothing for the dir. ✓
- No image under `website/src/` for this dive (the only hit is the dev-blog note .md, expected). ✓
- Prose voice is bare/factual; no first-person dive voice or editorializing superlatives (grep for
  "stunning/brilliant/masterpiece/remarkable/…" returned only in-word false positives). ✓

## 11. Internal consistency — OK

- "42/42" in index.md Method matches verify_quotes output. ✓
- Both referenced facsimiles exist: `extracts/v37_083_..._opening_facsimile.jpg`,
  `extracts/v37_first_manuscript_facsimile.jpg`. ✓
- All 4 figure `<img src>` paths in index.md resolve (2 extracts/ facsimiles + 2 visuals/ images,
  both present locally though git-ignored). ✓
- All 8 cross-linked sibling/contested-label dive dirs exist. Dev-blog note exists
  (`website/src/posts/notes/2026-06-13-i-cannot-be-silent.md`). ✓

---

## Minor items (non-blocking)

- **MINOR-1 (workRecord, §7)** — bare `oldStyle:` meta-key should map to the schema's named
  `...OldStyle` companion fields; note the mapping in the workRecord preamble so the ingestor does
  not have to infer it. (Documentation-only; the dates themselves are correct.)
- **MINOR-2 (extracts housekeeping)** — two extracted diary txts are present but not cited as
  evidence rows: `v56_127_127_1908_05_13.txt` and `v56_133_133_1908_06_10.txt`. Harmless supporting
  extracts; either wire them to an evidence row or leave as-is (no action required).
- **MINOR-3 (entity wikiType, §8)** — the `work` wikiType on "I Cannot Be Silent" is the
  Lab-convention exception, already self-documented. No fix needed; noted so a future reviewer does
  not re-flag it as a schema break.

## Confirmed strengths (worth stating)

- Byte-fidelity holds against the real source TEI for the marquee passage, the named first draft
  (Stolypin/Nicholas), the editorial-history publication paragraph, the diary, and the cut coda.
- The redaction story (names cut; the explicit "do the same to me" coda cut by Chertkov with
  Tolstoy's telegraphed approval) is the dive's strongest corpus-only contribution and is correctly
  routed `extends`/`complicates`, not asserted as the mainstream reading.
- The Kherson-execution evidentiary limit is treated with unusual honesty (coverage `not-covered`,
  a needsReview entry, and a "single newspaper notice" caveat in three places).
