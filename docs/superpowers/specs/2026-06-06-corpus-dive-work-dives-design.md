---
layer: reference
status: design
created: 2026-06-06
topic: corpus-dive skill — work-focused refinement
supersedes-partial: docs/superpowers/specs/2026-05-29-corpus-dive-design.md
---

# Design — `corpus-dive` refinement for work-focused dives

A refinement of the existing `corpus-dive` skill so that running it on a **single major
work** — *A Confession* first, then the rest of the Prophet-period canon, one at a time —
yields markedly more information per dive. This builds on the original design
(`docs/superpowers/specs/2026-05-29-corpus-dive-design.md`), which it amends rather than
replaces: the 6-phase structure, the boundaries, the verify discipline, and the theme
spine all stand. The implementation artifacts are `.claude/skills/corpus-dive/SKILL.md`
and `docs/research/lib/extract_tei.py`.

---

## 1. Purpose & the unit decision

The existing dives are **theme-shaped** — "the fire metaphor," "copyright renunciation,"
"the crisis." The skill's spine reflects that (*The shape of the question* → *Where the
theme clusters*). What we now want is **work-shaped** dives: one known text (a known PSS
Tom) read deeply, with everything the corpus says *around* it mapped — genesis, redactions,
censorship, family strain, reception, and its place in the cluster. The strongest existing
dive, `gospel-translation`, is already a de-facto work-dive; the project is drifting this
way and the skill should catch up.

**Decision (settled in brainstorming): do not add a new unit or mode.** We strengthen the
one theme-shaped skill so it serves a work well, and run it with the work as the "theme."
The work-ness is expressed in the **Phase-0 scope contract** ("subject: a work; PSS Tom X;
composition window Y; redactions: …"), not in a flag. Every addition below is written as a
**standing concern that scales to evidence** and **degrades gracefully back to a pure theme
dive**: a section with nothing real to say is dropped and recorded in the coverage ledger,
preserving the bare-dive voice the reader annotations defend.

**Goal:** more information per dive, in three senses at once — more *depth/coverage*
(exhaust the work's surfaces), more *structured output* (fill the work record, not just wiki
pages), and more *measurable thoroughness* (a coverage ledger instead of a prose
afterthought).

**Non-goals (unchanged from the original):** no vault/`works/` writes; no cross-dossier
aggregator; no overnight batch queue (per the *human-present* memory, runs stay interactive —
the canon is worked one at a time, not fired unattended).

---

## 2. The four levers

### Lever 1 — Richer standing spine

**Phase 1 — add a composition-years witness sweep (high priority).** Once the work's
writing window is known (from the `works/` record + the scope contract), the dive **always**
sweeps that window's diaries + letters, standardizing what `lords-prayer` §6 ("Reactions
while he worked") did by hand. This is a first-class surface, not an optional extra. It
captures two things, not one:

- **Tolstoy's own genesis & reaction** — the strain, urgency, and self-understanding while
  writing (the lords-prayer §6 register).
- **The people around the work** — whom Tolstoy **met, corresponded with, and talked to**
  during the writing: visitors to Yasnaya Polyana / Moscow, key correspondents, conversation
  partners, named readers of drafts. Each surfaces as a `person` entity in the dossier's
  routing map (with `ingestionPriority`), feeding both the Genesis section and the wiki's
  person universe. Diaries name visits and conversations; letters name the correspondence
  network — sweep both for *people*, not only for the work's themes.

This runs alongside the always-on post-1880 letter pass.

**Phase 4 — standing `index.md` sections.** When the subject is a work, the synthesis carries
the following sections, **each present only when the corpus supports it** (omit-if-empty;
the omission is logged in the coverage ledger, §Lever 4):

1. **Genesis & composition** — how/when/why the work was written, reconstructed from the
   composition-year diaries + letters, **including the people around the work**: whom
   Tolstoy met, corresponded with, and talked to while writing (visitors, key
   correspondents, conversation partners, named draft-readers). Names the human network of
   the writing period, each person carried into the dossier `entities` for the wiki.
2. **What the work says** — a structural map of the text itself: keystone passages
   chapter-by-chapter, read from the work's **own** TEI (the work is read deeply as the
   primary source, not merely grepped for mentions). For a work dive this is the spine's
   centre, augmenting/replacing the theme spine's "The shape of the question."
3. **Redactions & textual history** — enumerate the work's redactions/variants (cf. the
   gospel's three forms), which PSS Tom holds each, and what differs. Drives correct
   extraction (Lever 3).
4. **Publication, censorship & translation** — first publication, ban, foreign first
   edition, Russian first legal printing, and the translation lineage (gospel §6–7
   formalized).
5. **Reception & afterlife — the Russian society & church reaction first (high priority).**
   How Russian society and the Orthodox Church responded to the writing: the critical and
   public debate, the censorship apparatus, the reaction of clergy and the Holy Synod, and
   the 1901 excommunication where the work bears on it — then the wider influence and
   afterlife (foreign reception, later editions, downstream movements). Lead with the
   Russian reaction; the church/state response is a named, always-checked concern, not a
   sub-bullet of "controversy."
6. **Place in the cluster** — map the work to its sibling works (the tetralogy framing) and
   to the project's prior dives, via the existing cross-link discipline.
7. **The author's later verdict** — a standing micro-beat: Tolstoy's own later judgment on
   the work (e.g. the gospel's 1902 admission of "artificial, probably incorrect"
   philology). Cheap, high-signal; ties to the *changing-views* memory
   (`feedback_ingestion_accuracy_both_directions` / the crisis annotations).

The existing theme sections (*Key findings*, *Why this matters*, *Scholarly context*,
*Visual & manuscript record*, *Method*, *References*) are unchanged and continue to bracket
these.

### Lever 2 — Work-record field-fill (dossier)

A new `workRecord:` block in `dossier.yaml` that **mirrors the existing `works/` frontmatter
schema** — it introduces **no new schema or vocabulary**; it reflects the schema already
present (and almost entirely empty) in records like
`website/src/works/non-fiction/personal-papers/confession/Confession.md`.

The dive **reads** the work record to see which fields are empty, then **proposes** values.
It **never writes** to `website/src/works/` — the hard boundary stands; the human ingestion
step applies the fills. Every proposed field carries provenance and a confidence rating, so
ingestion can accept high-confidence fills quickly and adjudicate the rest.

```yaml
workRecord:                       # proposed fills for the works/ frontmatter — READ-ONLY to works/; human ingestion applies
  recordPath: website/src/works/non-fiction/personal-papers/confession/Confession.md
  workId: confession              # the record's id field
  fields:
    - field: dateWritingStarted   # mirrors a works/ frontmatter key
      value: "1879"
      oldStyle: ""                # when the source gives an O.S. date
      approximate: true          # maps to the record's *Approximate boolean
      evidenceRefs: [v49_…]       # ids from this dossier's evidence ledger
      source: null                # secondary attribution when not corpus-anchored
      confidence: medium          # high | medium | low
      note: ""
    # … one entry per field the dive can source, e.g.:
    # dateWritingCompleted, dateFirstPublished + firstPublishedVenue(+Type),
    # dateFirstPublishedInRussia + firstPublishedInRussiaVenue, bans,
    # censoredVersionExists(+Notes), censorshipNotes, excommunicationRelated,
    # samizdatCirculation, publishedDuringLifetime, publishedInRussiaDuringLifetime,
    # authoringLocations, relatedWorks, themes, subjectHeadings, synopsis,
    # epigraph(+Language/Author/Source), manuscripts, transcriptions,
    # identifiers.wikidata, wordCount(+Edition)
```

Fields the dive cannot determine are left out of `workRecord.fields` and recorded in the
coverage ledger / `needsReview`, so nothing is silently asserted. The Phase-6 handoff gains
a **work-record work-order**: the proposed fills grouped by confidence for human review.

### Lever 3 — Fold the pre-reform fix into `extract_tei.py`

Bake the logic of `lords-prayer`'s one-off `extracts/_reg_extract.py` into the canonical
`docs/research/lib/extract_tei.py`:

- **New flag `--choice=reg|orig|both`.** Default = **current behavior** (so every existing
  dive and test is unaffected). `reg` resolves `<choice><orig>/<reg>` pairs to the
  regularized (modern-orthography) reading; `orig` keeps the pre-reform original; `both`
  emits both. The skill recommends `reg` for any 1880s+ text.
- **Whitespace + ё handling** consistent with `verify_quotes.py` expectations — full
  whitespace collapse around resolved pairs; ё-handling that lets a dive pick ё-free
  substrings for byte-verification (per `reference_extract_tei_prereform_choice_gap`).
- **Test:** extend `docs/research/lib/test-extract-tei.sh` (or the harness it drives) with a
  small pre-reform `<choice>` fixture asserting the `reg` resolution.
- **Docs:** document the flag in `docs/research/lib/README.md`.
- **Memory:** update `reference_extract_tei_prereform_choice_gap` once folded in — it
  currently states the extractor *drops* these pairs; after the fix it resolves them under
  the flag, and the one-off helper is retired.

This makes the recurring tax on Prophet-period dives disappear: the canon is made entirely
of texts in the pre-reform/`<choice>` window, so this is load-bearing for every dive that
follows.

### Lever 4 — Coverage ledger (dossier + index.md)

A new `coverage:` block in `dossier.yaml` — a surfaces × status matrix that makes
thoroughness measurable and resume clean:

```yaml
coverage:                         # surfaces × status — derives index.md "Material not covered"; resume reads this
  - surface: "Redaction: <name> (PSS Tom NN)"
    status: covered               # covered | partial | not-covered
    note: ""
  - surface: "Composition-year diaries (1879–1882)"
    status: partial
    note: "1880 diary sparse; leans on letters"
  - surface: "Composition-year letters (Tom 63)"
    status: covered
  - surface: "Interlocutors & circle during composition (who he met/talked to)"
    status: partial
    note: "diaries name visitors; correspondence network mapped to entities"
  - surface: "Russian society & church reception"
    status: not-covered
    note: "critical/public debate, censorship, Synod, excommunication links"
  - surface: "Reception-period letters"
    status: not-covered
    note: "deferred to a later pass"
  - surface: "Witness diaries (S. A. Tolstaya)"
    status: partial
  - surface: "Secondary scholarship"
    status: covered
  - surface: "Visual & manuscript record"
    status: partial
```

The standard surface checklist for a work dive: **each redaction of the work**;
**composition-year diaries**; **composition-year letters**; **interlocutors & circle during
composition** (whom he met/talked to); **Russian society & church reception**;
**reception-period letters**; **witness diaries** (S. A. Tolstaya et al.); **secondary
scholarship**; **visual & manuscript record**. The `index.md` "Material not covered" section is **derived** from the
`partial`/`not-covered` rows (the prose stays, but it is now backed by the structured
ledger). Multi-session resume reads `coverage` first; the existing free-text `notCovered`
list is kept as overflow for items that don't map to a standard surface.

---

## 3. Changes by artifact (implementation surface)

- **`.claude/skills/corpus-dive/SKILL.md`**
  - Phase 0: scope contract gains explicit work fields (PSS Tom, composition window,
    redaction list) when the subject is a work.
  - Phase 1: add the **composition-years witness sweep**.
  - Phase 2: read the work's own TEI deeply (structural map); recommend `--choice=reg` for
    1880s+ extraction.
  - Phase 4 / Synthesize: the **standing spine sections** (Lever 1), the `workRecord:` block
    (Lever 2), and the `coverage:` block (Lever 4); update the dossier schema documentation
    in the skill to include both new blocks.
  - Phase 5 / Verify: the verifier additionally checks that `workRecord` proposals are
    evidence-anchored (no fabricated dates/venues), the `coverage` ledger is honest, and the
    standing sections obey the bare-voice / attribute-don't-assert rules.
  - Phase 6 / Handoff: add the **work-record work-order** (proposed fills by confidence) and
    surface the coverage ledger in the summary.
  - Multi-session: resume reads `coverage` first.
- **`docs/research/lib/extract_tei.py`** — the `--choice` flag (Lever 3).
- **`docs/research/lib/test-extract-tei.sh`** — pre-reform fixture/test.
- **`docs/research/lib/README.md`** — document `--choice`.
- **Memory** — update `reference_extract_tei_prereform_choice_gap` after the fold-in.

---

## 4. Acceptance test — run *A Confession*

After editing `SKILL.md` + `extract_tei.py`, run `/corpus-dive` on **A Confession** (Исповедь,
PSS Tom 23; dive slug `a-confession`; work id `confession`). It exercises every lever:

- composition-years sweep (≈1879–1882) — Tolstoy's own reactions **and** the people around
  the work: whom he met, corresponded with, and talked to while writing (surfaced as
  `person` entities);
- redaction & textual history of Исповедь (its multiple redactions);
- publication/censorship (banned in Russia; first published abroad — Geneva/Elpidin, 1884;
  legally in Russia 1906) — to be confirmed against the corpus + a light scholarship sweep,
  not asserted from memory;
- **Russian society & church reception** — the critical/public response and the Orthodox
  Church's reaction (censorship, clergy, the Synod), confirmed rather than assumed;
- the `workRecord:` field-fill against the empty `Confession.md`;
- the `coverage:` ledger.

Verified by `verify_quotes.py` (mechanical, exit 0) + the opus verifier pass (judgment).
Output: `docs/research/a-confession/` (`index.md`, `dossier.yaml` with `workRecord` +
`coverage` blocks, `extracts/`, `visuals/` if any open-licensed image is found, and the
`draft: true` dev-blog note). This is also the live proof that the new spine degrades
correctly and the extractor flag works on a real 1880s text.

### Evaluation gate (after A Confession, before the rest of the canon)

The *A Confession* dive is a pilot, not just a first deliverable: before rolling the refined
skill forward to *What I Believe* and the rest of §5, hold a short **evaluation /
retrospective** with the reader. It checks whether the four levers actually delivered and
feeds any fixes back into `SKILL.md` / `extract_tei.py` first — so a flaw is corrected once,
not repeated across a dozen dives. The evaluation asks, concretely:

- **Composition-years + interlocutors** — did the sweep surface *the people around the work*
  (visitors, correspondents, conversation partners), each as a usable `person` entity, and
  not just Tolstoy's own reactions?
- **Russian society & church reception** — is that reaction genuinely covered, led-with, and
  corpus/source-confirmed rather than assumed?
- **Work-record field-fill** — did `workRecord:` populate the empty `Confession.md` fields
  with provenance + confidence, and are the proposals accurate against the record schema?
- **Coverage ledger** — does it read honestly (no `covered` that is really `partial`), and
  is it usable as a resume queue?
- **Extractor** — did `--choice=reg` extract the 1880s text cleanly, with `verify_quotes.py`
  passing on the result?
- **Voice & length** — did the richer spine stay *bare* and evidence-scaled, or did standing
  sections get padded where the corpus was thin?

Output of the gate: a brief findings note + any adjustments to the skill, plus the reader's
`annotations.md` steer on the A-Confession dive (the usual ingestion-guidance loop). Only
after that does the canon proceed. The gate is a checkpoint, not a deliverable to
over-engineer — keep it to what changes the next dive.

---

## 5. The Prophet-period canon (reference checklist)

Worked **one at a time, interactively** (no overnight queue). An editable starting list:

1. **A Confession** (Исповедь) — *this effort*
2. What I Believe (В чём моя вера?)
3. Critique of Dogmatic Theology (Исследование догматического богословия)
4. Union and Translation of the Four Gospels / The Gospel in Brief — *partly done via*
   `gospel-translation` *and* `lords-prayer`; a dedicated work-dive would consolidate
5. What Then Must We Do? (Так что же нам делать?)
6. On Life (О жизни)
7. The Kingdom of God Is Within You (Царство Божие внутри вас)
8. The First Step (Первая ступень) · Christianity and Patriotism
9. What Is Art? (Что такое искусство?)
10. Resurrection (Воскресение)
11. I Cannot Be Silent (Не могу молчать)
12. The Law of Love and the Law of Violence (Закон насилия и закон любви)

Late fiction with a Prophet-period charge (*The Death of Ivan Ilyich*, *The Kreutzer
Sonata*, *Master and Man*, *Father Sergius*, *Hadji Murat*) can be folded in later if wanted;
they sit at the edge of the "major Prophet works" frame and are out of scope for this pass.

---

## 6. Boundaries & voice (unchanged, restated for safety)

- **Reads freely:** `primary-sources/**` and anywhere under `website/` (read-only — incl.
  the `works/` record being filled).
- **Writes only to:** `docs/research/<slug>/`, `docs/research/lib/`,
  `docs/research/_batch-<date>.md`, and `website/src/posts/notes/`.
- **Never writes/modifies:** `primary-sources/**`, the `works/` TEXT zone, or anything under
  `website/` except `website/src/posts/notes/`. The `workRecord:` block is a **proposal**,
  not a write.
- **Voice:** English; cited foreign titles verbatim; working-English translations labelled;
  minimal editorial; standing sections scale to evidence and are omitted when empty (logged
  in `coverage`), never padded.

---

## 7. Self-review checklist (for the spec author)

- No placeholders/TBDs left in the levers or the artifact-change list. ✔
- `workRecord` is a dossier proposal mirroring the *existing* schema — no schema/vocab change,
  consistent with the read-only `works/` boundary. ✔
- `--choice` default preserves current behavior — no regression to existing dives/tests. ✔
- Coverage ledger derives the existing prose section rather than replacing the honest-gaps
  principle. ✔
- Scope is one implementation plan (skill + extractor + one proof dive), not a decomposition. ✔
