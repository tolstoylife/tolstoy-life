# Phase-5 Verifier Report — «Так что же нам делать?» (What Then Must We Do?)

**VERDICT: PASS-WITH-NITS**
**Must-fix items: 0**

Fresh-context adversarial judgement review of the completed work-dive. The mechanical
byte-fidelity gate (verify_quotes.py → 21/21) is taken as given; this report covers the
judgement-level checks the script cannot make. Reviewer: general-purpose agent, 2026-06-06.

Files reviewed:
- `docs/research/1882-1886-what-then-must-we-do/index.md`
- `docs/research/1882-1886-what-then-must-we-do/dossier.yaml`
- `website/src/posts/notes/2026-06-06-what-then-must-we-do.md`
- `docs/research/1882-1886-what-then-must-we-do/extracts/*.txt`
- Schemas: `website/schema/tolstoy-works-schema.md` (v7), `website/schema/wiki-schema.md` (v1.3)

---

## Item 1 — Byte-fidelity belt-and-braces — **PASS**

Spot-checked 8 citations (target was ~5) by opening the named extract and confirming the
`quoteRu` appears verbatim:

| id | extract | result |
|---|---|---|
| wtmwd-text-03 (keystone «Я сижу на шее») | v25_182_411 | FOUND |
| wtmwd-text-06 (захват чужого труда) | v25_182_411 | FOUND |
| wtmwd-text-10 (женский вопрос) | v25_182_411 | FOUND |
| wtmwd-perepis-01 (Деньги сами по себе зло) | v25_173_181 | FOUND |
| wtmwd-diary-01 (собственность ограждаемая) | v49_059_059_1883_01_01 | FOUND |
| wtmwd-let-03 (Bondarev «упомянул…») | v63_486 | FOUND |
| wtmwd-let-05 (Strakhov «[…]») | v63_337 | FOUND (see below) |
| wtmwd-let-04 (Книжки мои не пропускают) | v63_486 | FOUND |

**Two edge cases resolved honestly:**

- **wtmwd-let-03** (Bondarev): the quote begins mid-sentence at «упомянул…». The extract
  reads `…в той книге,³ которую я пишу об этом же предмете, упомянул о том, что я почерпнул это
  не от ученых и мудрых мира сего, но от крестьянина Т. М. Бондарева.` The quoteRu starts
  cleanly at «упомянул»; the working-English bracket-gloss `[in the book I am writing on this
  same subject]` accurately supplies the elided antecedent. Faithful, not embellished.

- **wtmwd-let-05** (Strakhov «[…]»): **the elision is honest.** The extract reads
  `…в этой статье,⁶ a тем, чтò в ней есть божеского…`. The dossier renders
  `…в этой статье, […] тем, чтò в ней есть божеского…`. The `[…]` elides exactly the
  superscript footnote-marker `⁶` plus the adversative conjunction `a` (transliterated «а»).
  Nothing substantive is dropped. The English gloss renders the «a» as "but" ("not what is
  mine… but what is God's"), which is the correct adversative sense.

**Gloss faithfulness:** all sampled working-English renderings are accurate and unembellished.
The figurative «I sit on a man's back» and «захват чужого труда» ("seizure of another's
labour") are rendered literally, not dramatized.

---

## Item 2 — Every PRIMARY claim source-anchored — **PASS**

19 block-quotes in index.md; 19 working-English attribution lines (exact 1:1). 18 carry an
inline `*(working English — PSS Tom N, ch./date)*` anchor; the 19th (Alekseev, Dec 1884) has
its attribution folded into the preceding sentence with full Tom 63 anchor. Every anchor
carries both the working-English label AND a PSS Tom + chapter-or-date attribution.

Inline prose primary quotes were also checked:
- «дело любовного общения богатых… с нищими» (l.48) → verbatim in v25_173_181 extract.
- «Книжки мои не пропускают и жгут» (afterlife) → verbatim in v63_486.

No free-floating primary factual claim was found without evidence behind it.

---

## Item 3 — Secondary/scholarly claims ATTRIBUTED, not asserted — **PASS**

Every scholarly claim names a source and has a References-list entry (index.md l.206;
dossier `references.background`): Simmons 1946, Bartlett 2011, Maude 1925, Donskov 2019,
Cruise 2002, Lounsbery 2022, Nicolosi 2024, Medzhibovskaya 2008, plus the Popoff /
*The Last Station* tradition named for the frame it is contrasted against. The "Scholarly
context" section consistently uses confirms/complicates/extends framing and never states a
secondary reading in the dive's own voice as fact. (One borderline voice point — the word
"reactionary" — is treated under Item 8.)

---

## Item 4 — scholarship.triangulation integrity — **PASS**

All 7 triangulation entries verified programmatically:
- Every `evidenceRef` (wtmwd-text-01, -05, -06, -08, -10; wtmwd-let-02, -05) exists in
  `evidence[]`.
- Every `relation` ∈ {confirms, complicates, contradicts, extends}: 2 confirms, 3 complicates,
  2 extends. All valid.

---

## Item 5 — Entities resolve to valid wikiType / vaultStatus — **PASS**

All 25 entities have valid `wikiType` (person, concept, event, place — all in the wiki-schema
type set) and valid `vaultStatus` ∈ {exists, stub, missing}. All entity `evidenceRefs`
resolve to real evidence ids.

`vaultStatus: exists` spot-check (filesystem):
- `website/src/wiki/Leo Tolstoy.md` — EXISTS
- `website/src/wiki/Vladimir Chertkov.md` — EXISTS
- `website/src/wiki/Sophia Tolstaya.md` — EXISTS
- `website/src/wiki/Yasnaya Polyana.md` — EXISTS

`vaultStatus: missing` spot-check — genuinely absent in `website/src/wiki/`:
- Bondarev / Timofei Bondarev — absent
- Alekseev / Vasily Alekseev — absent
- Sutaev, Henry George, "Bread labour", "Money as violence" — all absent

---

## Item 6 — workRecord proposals evidence-anchored & schema-valid — **PASS**

All 17 `field` names are real keys in tolstoy-works-schema.md v7 (titleRu, titleEn,
titleAlternatives, genre, dateWritingStarted, dateWritingCompleted, dateFirstPublished,
firstPublishedVenue, publishedDuringLifetime, publishedInRussiaDuringLifetime,
dateFirstPublishedInRussia, bans, censoredVersionExists, samizdatCirculation,
excommunicationRelated, relatedWorks, identifiers.jubileeEdition.volumes).

**CRITICAL controlled-vocab checks (all clean):**
- `genre: essay` — valid.
- `titleAlternatives[].type`: translation, translation, variant — all ∈ {working, translation,
  subtitle, variant}.
- `bans[]` (3 events):
  - imperial-state / serialization-refused — valid
  - imperial-state / passages-cut — valid
  - holy-synod / pre-publication-rejected — valid
  - All `authorityType` ∈ {imperial-state, holy-synod, foreign-government, periodical-editor,
    other}; all `scope` ∈ {complete-ban, passages-cut, serialization-refused, confiscation,
    pre-publication-rejected}. No value outside the sets.
- `relatedWorks[].relationshipType`: both `sequel` (what-i-believe, confession) — valid vocab.
  (See NIT below — semantic, not a violation.)

No fabricated dates/venues: each value carries a `confidence` flag and `note`; genuine
uncertainties (`dateFirstPublished` which-event, `excommunicationRelated`, folder) are routed
to `needsReview` rather than asserted. `excommunicationRelated: false` is the conservative,
correct call (the 1901 edict named no individual works).

---

## Item 7 — coverage ledger honest — **PASS**

The three flagged surfaces are correctly graded:
- "Redactions & textual history" → **partial** — correct: the 765 KB variants file
  (pp. 614–652) was explicitly not collated, only the commentary summarized. index.md l.138
  states this in-text ("the 765 KB variants file was not collated").
- "Reception & afterlife" → **partial** — correct: letter-network + censorship verdicts are
  grounded, but the wider critical/press reception and the Synod/excommunication tie are
  openly deferred (l.158, l.179).
- "The author's later verdict" → **not-covered** — correct: no post-1886 self-assessment was
  extracted; the note honestly says the 1889 Alekseev commune letter "is not a verdict on the
  text."

Nothing marked `covered` is overclaimed. "What the work says" (covered) is backed by 11
byte-faithful extracts across all four movements; "Publication, censorship & translation"
(covered) is densely sourced. The `contradictions` block (1884-vs-1882 dating) is honest and
evidence-anchored.

---

## Item 8 — Bare project voice / attribute-don't-assert — **PASS (with one NIT)**

The two editorially-sensitive bodies of material are handled with care:

**Final chapter on women** — presented FACTUALLY and in full: childbearing-as-the-woman's-law,
the attack on the «женский вопрос», the attack on contraception, salvation-placed-in-mothers,
with both closing quotes byte-faithful (wtmwd-text-10, -11). The doctrine is NOT softened, NOT
apologized for, and NOT euphemized — the checklist's "whitewash" failure mode is absent. The
critical *reading* is correctly attributed: "The retrograde reading is the scholarly consensus
(Cruise 2002; Lounsbery 2022)" (l.172).

**S. A. Tolstaya family conflict** — the dive does NOT adopt the Sofia-centred frame. It
explicitly states it "attributes rather than adopts" the "guilt-ridden patriarch" frame
(l.172), names it to the Popoff / *The Last Station* tradition, and grounds its own narrower
claim (she objected to the *naming of family members*, not the argument) in the apparatus, with
a needsReview flag that the underlying letter (Tom 83) was not byte-extracted. Balanced and
honest in both directions.

**NIT (non-blocking):** the value-laden label "reactionary" is used twice in the dive's *own*
unattributed voice — l.19 "its most reactionary-on-gender turn" and l.126 "is the book's most
reactionary turn" — and once in the draft note ("the famous, and reactionary, final chapter").
Only at l.172 is the label tied to scholarship. Per the project's attribute-don't-assert voice
rule and the corpus-dive "don't let labels stick" guidance, a one-word evaluative verdict
stated as bare fact is a minor voice leak. It is a NIT, not a FAIL, because (a) the descriptive
content beside it is accurate and complete, letting the reader judge, and (b) the critical
*reading* is attributed at l.172. Optional tightening: render the spine-text instances as a
factual descriptor (e.g. "the book's most gender-conservative turn") and reserve "reactionary"
for the attributed l.172 sentence.

---

## Item 9 — Rights hygiene — **PASS**

- `docs/.gitignore` carries `research/*/visuals/`; `git check-ignore` confirms both the
  `visuals/` dir and a sample file inside it are IGNORED.
- `git ls-files docs/research/1882-1886-what-then-must-we-do/visuals/` → empty (nothing tracked).
- Nothing written into `website/src/` except the one draft note: `git status` on the submodule
  shows only `?? src/posts/notes/2026-06-06-what-then-must-we-do.md`.
- Every `visuals[]` entry carries a `licence`: 8 PD (usable: yes, with url+localPath), 4 unknown
  (usable: no, empty url/localPath — request-only stubs for Alekseev, Bondarev, Sutaev, Lyapinsky
  house). No rights-reserved/unknown image was committed or referenced for display.

---

## Required fixes (punch-list)

None blocking. **0 must-fix items.**

Optional polish (NITs, author's discretion):
1. **[NIT, voice]** Soften the two spine-text occurrences of "reactionary" (index.md l.19,
   l.126) and the note's "and reactionary" to a factual descriptor, leaving the attributed
   characterization at index.md l.172 to carry the critical reading. Keeps the standing spine in
   bare project voice without softening the doctrine itself.
2. **[NIT, semantic — no action required]** `relatedWorks` types both predecessors as `sequel`;
   the dossier note already acknowledges this as "the closest fit" in the controlled set. Valid
   vocab; flagged only for the human ingestor's awareness (a future schema relation like
   "application"/"companion-in-sequence" would fit better, but `companion` is the nearest
   existing alternative).
