---
layer: reference
status: design
created: 2026-05-29
topic: corpus-dive skill
---

# Design — `corpus-dive` skill

A repeatable primary-source research method for the Tolstoy Research Platform. Given one
**theme**, it produces a set of coordinated, ingestion-ready outputs grounded in the local
corpus (the tolstoydigital TEI edition + the Jubilee Edition PDFs), modeled on the existing
`docs/research/` prototypes — copyright-renunciation being the reference implementation.

This document is the brainstormed design. The implementation artifact it specifies is
`.claude/skills/corpus-dive/SKILL.md`.

---

## 1. Purpose & framing

The `docs/research/` thematic sweeps (copyright-renunciation, christian-communism-socialism,
doukhobors, tolstoyanism-christian-anarchism, biryukov-biography-editions) share one method:
a layered Russian keyword sweep across the TEI corpus → verbatim extraction → cross-check
against the printed PSS → a structured findings document where *every claim is anchored to its
TEI/PSS source*, plus an honest "what we didn't cover" section.

`corpus-dive` systematizes that method so any future session — by the project, a contributor,
or anyone else — can launch a dive on a new theme and get the same quality of output. It is
explicitly a **prototype for LLM wiki ingestion**: its structured dossier is designed to
*point a later ingestion session in the right direction*, not to write vault content itself.

**Goals**
- Reproduce the prototype's discipline: primary-source-grounded, verbatim-anchored, minimal editorial.
- Emit a machine-readable dossier that a later ingestion session (and eventually scripts / the
  LightRAG layer) can consume.
- Surface, for every theme, the **visual & archival materials** (photos, portraits, manuscript
  facsimiles, illustrations, paintings, maps) with provenance and rights — feeding the planned
  `website/src/images/` section the way the entity track feeds the wiki.

**Non-goals (YAGNI)**
- Does **not** write wiki / vault content. Ingestion stays a separate, human-in-the-loop step.
- Does **not** build a database or cross-dossier aggregator yet. Per-topic YAML is aggregatable
  later when there is a concrete reason.
- Does **not** reconcile the four already-forked `extract_tei.py` copies — that is a separate
  cleanup task this skill merely makes unnecessary going forward.

---

## 2. Unit & invocation

- **Unit:** one theme/concept traced across the corpus (e.g. *copyright renunciation*,
  *capital punishment*, *the Doukhobors*, *non-resistance*).
- **Invocation:** `/corpus-dive <theme or research question> [--auto] [--confirm-scope] [--model <tier>]`.
  `--auto` runs unattended (§12); `--model` sets the baseline tier (§14). Batch runs are driven by
  the headless CLI queue runner (§13), not by the skill itself.
- **Name rationale:** distinct from `oh-my-claudecode:deep-dive` (a code-tracing /
  requirements pipeline that shares only the word "deep dive"). `corpus-dive` has no trigger
  collision and reads naturally as "a dive into the corpus."

---

## 3. Deliverable contract

```
docs/research/<topic-slug>/
├── index.md          ← research artifact (layer: reference) — the proven spine (§6)
├── dossier.yaml      ← machine-readable, 3-layer dossier (§7)
├── extracts/         ← verbatim TEI prose + PSS page images rendered from PDFs we already hold
├── visuals/          ← externally-sourced imagery, downloaded only when open-licensed (§8)
├── run-report.md     ← autonomous runs only — what it chose, covered, deferred (§12)
└── session-log.md    ← multi-session dives only (optional)

website/src/posts/notes/YYYY-MM-DD-<topic-slug>.md   ← dev-blog note (draft: true) (§9)
docs/research/lib/corpus-dive-queue.sh               ← overnight queue runner (§13)
docs/research/_batch-<date>.md                       ← combined batch summary (queue runs)
```

Every dive produces `index.md`, `dossier.yaml`, `extracts/`, and the dev-blog note. `visuals/`
appears only when at least one openly-licensed image was downloaded; `run-report.md` only for
autonomous (`--auto`) runs; `session-log.md` only for multi-session work.

---

## 4. Approach — phased, scale-aware hybrid

One method with explicit phases. **Only the sweep phase scales**: a narrow theme runs the sweep
inline; a broad theme may fan it out across parallel subagents. Verification and synthesis
*always* run in the main context, to protect voice and citation discipline. The hard judgment in
primary-source work is the synthesis, not the grepping — so parallelism is an accelerator, not
the core.

---

## 5. The method (phases)

### Phase 0 — Scope (front-gate; requires user confirmation)
Produce a short **scoping contract** before any sweeping:
- Restate the precise question.
- Define the **corpus surface**: which genres (diaries / letters / works / notebooks /
  commentary) and which date-range. **Default bias: the post-1880 "Prophet" period, with
  letters/correspondence treated as a first-class surface** (the TEI corpus holds ~9,087 letter
  files vs ~4,584 diary files — correspondence is the larger and often richer surface for this
  period; see §11).
- Build the **layered Russian keyword set**: high-confidence anchors → broader combinable terms,
  including orthographic / pre-reform variants. (Tolstoy wrote in Russian; keywords are Russian.)
- Set a **stop-condition / time-box** and a "good enough" coverage target.
- Choose **sweep mode**: inline (narrow) vs fan-out (broad).

Show the contract to the user and confirm before proceeding (one interaction). In `--auto` mode
this confirmation is skipped: the contract is auto-derived from the theme + defaults and logged
to `run-report.md` (§12). The final "Method" section of `index.md` is this contract, updated with
what actually happened — which makes "material not covered" honest by design.

### Phase 1 — Sweep (scale-aware)
- **Inline:** sequential grep/extract over `primary-sources/tolstoydigital-TEI/texts/` using the
  keyword set; capture candidate hits with their TEI id (the filename encodes Tom + entry date).
- **Fan-out (optional, broad themes):** partition the corpus — diaries by decade, **letters by
  Tom-range with a dedicated Prophet-period pass**, works — and dispatch parallel subagents that
  each return *structured* candidate hits (TEI id, snippet, why-relevant). The main context
  dedupes and ranks.
- A post-1880 **letter-corpus pass always runs**, regardless of mode.

### Phase 2 — Extract & verify finalists
- Run the **canonical `extract_tei.py`** (`docs/research/lib/extract_tei.py`) on each finalist to
  produce clean verbatim Russian prose; save to `extracts/<tei-id>.txt`.
- Cross-check finalists against the printed PSS PDF (`pdftoppm` @ 220 dpi). For the single
  **keystone citation**, save the page image to `extracts/`.
- Produce **working-English** translations, explicitly labelled as such.
- Run the **visual-materials sweep** in parallel (§8).

### Phase 3 — Synthesize
Write the three outputs: `index.md` (spine, §6), `dossier.yaml` (§7), and the dev-blog note (§9).

### Phase 4 — Verify (separate pass; never self-approve)
A dedicated `verifier` pass (per the project's writer ≠ reviewer rule):
- Re-derives a sample of citations from TEI/PDF and checks **byte-fidelity** of every quote.
- Confirms **every claim in `index.md` is source-anchored**.
- Confirms **dossier entities resolve to valid wiki types** and that `vaultStatus` flags are
  accurate (checked against `website/src/wiki|works`).
- Flags **unlabelled translations** and any **editorializing** voice.
- Confirms **no rights-reserved image** was downloaded into `visuals/` (§8).
Iterate until the verdict is clean.

### Phase 5 — Handoff
Print a summary: what was covered, the `notCovered` queue, the **entity work-order** (which wiki
pages this dive feeds), the **visuals work-order** (which images/facsimiles to acquire or
request), and the draft note path. Remind that wiki ingestion is a separate, human-in-the-loop
step — the dossier is the pointer, not the writer. In autonomous runs this summary is written to
`run-report.md` (§12) rather than printed.

---

## 6. `index.md` spine (section template)

Frontmatter `layer: reference`. Sections, generalized from the copyright-renunciation prototype:

1. **Why this matters for tolstoy.life** — the editorial/contextual reason for the dive.
2. **The shape of the question** — the staged narrative, each stage carrying a verbatim primary
   quote (Russian) + working-English translation + the TEI id / PSS Tom + page citation.
3. **Where the theme clusters in the corpus** — tables by genre (diaries, **letters**, works,
   notebooks), each row a TEI id / PSS Tom + letter id / date / addressee / one-line material note.
4. **Material not covered** — the honest gap list; this is also the dossier `notCovered` queue.
5. **Visual & manuscript record** — photographs/portraits of the people, manuscript facsimiles,
   illustrations/paintings/maps tied to the theme; each with provenance, access, rights; plus
   "what is not openly available and where to request it." (Generalizes the prototype's §5.)
6. **Method** — the Phase-0 scoping contract, updated with what actually happened.
7. **References** — primary + background, plus companion-document links.

Closes with a link to the dev-blog note once published.

---

## 7. `dossier.yaml` schema

YAML (matches `sources.yaml` / `.data.yaml` house style; human-reviewable, diffs cleanly,
script-parseable). Three layers plus supporting blocks:

```yaml
topic:
  slug: copyright-renunciation
  title: "Tolstoy on copyright and the renunciation of literary property"
  question: "Where does Tolstoy discuss renouncing literary property?"
  date: 2026-05-29
  period: prophet                  # default bias marker
  corpusSurface: [diaries, letters, works, notebooks]
  dateRange: "1881–1910"

evidence:                          # Layer 1 — flat citation ledger (reusable evidence base)
  - id: v53_014_018_1895_03_27
    genre: diary                   # diary | letter | work | notebook | commentary
    pssTom: 53
    pages: "14–18"
    date: 1895-03-27
    addressee: null                # for letters
    localPdf: primary-sources/jubilee-edition/vol19/vol19.pdf
    extract: extracts/v53_014_018_1895_03_27.txt
    quoteRu: "Право на издание моих сочинений прежних…"
    quoteEn: "I ask my heirs… (working English)"
    significance: "Will-as-diary-entry; most plainly written first-person statement."
    facsimile: extracts/pss-vol53-pages/page-054.png   # optional, keystone only

entities:                          # Layer 2 — ingestion routing map (feeds the wiki)
  - name: "Vladimir Chertkov"
    wikiType: person               # one of the 9 wiki types (wiki-schema.md)
    wikilinkTarget: "Vladimir Chertkov.md"
    vaultStatus: missing           # exists | stub | missing
    role: "co-drafter of the six wills"
    sources: [jubilee-edition]     # ids from website/schema/sources.yaml
    evidenceRefs: [v82_305_Obyasnitelnaya, v66_036_Redaktoram]

visuals:                           # Layer 3 — visual & archival materials map (feeds images/)
  - id: diary-1895-03-27-ms
    type: manuscript-facsimile     # photograph | portrait | manuscript-facsimile | illustration | painting | map | graphic
    subject: "Diary page, 27 March 1895"
    relatedEntity: "Leo Tolstoy"
    relatedEvidence: v53_014_018_1895_03_27
    holding: "State Tolstoy Museum (GMT), Moscow — manuscript fond, 'steel room'"
    archiveId: null
    access: request-required       # held-locally | open-web | restricted | request-required
    rights: "© GMT, all rights reserved — permission needed"
    licence: null                  # PD | CC0 | CC-BY | CC-BY-SA | rights-reserved | unknown
    usable: false                  # can tolstoy.life PUBLISH it? (distinct from storable)
    url: null
    localPath: null                # set only when downloaded into visuals/ (open licences only)
    note: "High-res facsimile not on open web; request from museum manuscripts dept."

contradictions:                    # corrections to claims in secondary lit / the vault
  - claim: "'any works written after 1880' (secondary-literature paraphrase)"
    correction: "Russian reads 'с 1881 года' — inclusive of 1881"
    evidenceRef: v66_036_Redaktoram

notCovered:                        # the resume queue for a later session
  - "Krug chteniya / Put' zhizni anthologies"
  - "Goldenweiser / Makovický conversation transcripts"

needsReview:                       # deferred human-judgment items (autonomous runs never block)
  - item: "Attribution of the 1885 letter draft — two candidate addressees"
    phase: synthesis
    why: "Editorial judgment; both readings defensible from the source"

archivesConsulted:                 # honest record of where we looked (incl. dead ends)
  - "State Tolstoy Museum (tolstoy-iss.kamiscloud.ru)"
  - "Goskatalog (web.goskatalog.ru)"
  - "Wikimedia Commons"

references:
  primary: []
  background: []
```

The **evidence ledger** is source-centric and reusable; the **entity index** is the ingestion
routing map ("what does this dive say about Chertkov?"); the **visuals map** is the parallel
routing map for image metadata.

---

## 8. Visual-materials track

A first-class, recurring track — not an ad-hoc section.

**Behavior — locate & document always; download only when open-licensed.** Because
`docs/research/<topic>/visuals/` is **git-tracked and public**, downloading a rights-reserved
scan into it would itself be republication. The download gate is therefore a property of the
*licence*:

- **Download into `visuals/` only when the licence verifiably permits redistribution in a public
  repo** — public domain (age-expired, PD-tagged, CC0) or an open licence that allows it
  (CC-BY, CC-BY-SA, attribution recorded). Every downloaded file records `licence` + source `url`.
- **Everything else is mapped, never copied** — provenance, holding, access status, rights, and
  how-to-request go into the `visuals` entry with `localPath: null`.
- The `usable` flag answers the project's distinct question ("can tolstoy.life *publish* it?"),
  separate from "may we *store* it": a CC-BY-SA image is storable and usable-with-attribution; a
  rights-reserved one is neither.

**Known-archives checklist** (baked into the skill so the sweep is concrete, not vague):
- local `primary-sources/` holdings (incl. PSS page extraction via `pdftoppm`);
- State Tolstoy Museum collection (tolstoy-iss.kamiscloud.ru) + Goskatalog (web.goskatalog.ru);
- **Wikimedia Commons** — many late-period Tolstoy photographs are public domain, including
  Chertkov's own photographs (he was the chief photographer of Tolstoy's last decade);
- tolstoy.ru / "Весь Толстой в один клик" (digitised printed volumes);
- émigré scan archives (vtoraya-literatura.com, imwerden.de) for period material.

**Web access:** the visual track and the background-references work may use web search/fetch.
Core textual evidence stays primary-corpus-grounded — web is for archival provenance, image
location, and background, never a substitute for primary-source citation of textual claims.

---

## 9. Dev-blog note

`website/src/posts/notes/YYYY-MM-DD-<topic-slug>.md`, frontmatter `title` / `description` /
`date` / `tags` / `draft: true`. A short recap of the dive in the project voice — what the dive
found and why it matters — linking to the `index.md` artifact. Mirrors the existing
`2026-05-10-tolstoy-on-copyright-renunciation.md`. Stays `draft: true` until the user publishes.

---

## 10. Skill mechanics

- **Canonical extractor:** the skill references one shared `docs/research/lib/extract_tei.py`
  instead of forking a copy per dive. (Done — the four per-dive forks were removed and each
  dive's `index.md` now links to the shared copy via `../lib/extract_tei.py`.)
- **Skill file:** `.claude/skills/corpus-dive/SKILL.md` (project-scoped, version-controlled; the
  `.claude/skills/` directory does not yet exist and is created by this work).
- **Triggers:** "corpus dive", "corpus-dive", "research X across the corpus / PSS / TEI".
  Argument-hint: `<theme or research question>`.
- **Voice & language guard:** `index.md` and note in English; cited foreign titles kept verbatim;
  working-English translations labelled; minimal editorial; escalate genuine editorial judgment
  to the user (in `--auto`, defer to `needsReview` instead — §12).
- **Model routing:** the runner sets the baseline tier via `--model`; sub-steps are routed
  per-phase per §14 (balanced default, with escalate-on-low-confidence).

---

## 11. Standing emphasis — the Prophet period

Tolstoy's post-1880 religious-moral phase (after *A Confession*) is where every existing dive
already lives. The skill defaults its corpus surface to **1881–1910** and treats the
**letters/correspondence** of that period as a first-class sweep target — a dedicated
Prophet-period letter pass always runs. Correspondents surfaced in that pass become `person`
entities in the dossier's routing map.

---

## 12. Autonomy & unattended operation

The skill has a **mode switch** so it can run while the user is away.

- **Interactive (default):** Phase 0 shows the scoping contract and waits for confirmation;
  genuine editorial-judgment calls escalate to the user.
- **Autonomous (`--auto`):** Phase 0 **auto-derives** the scoping contract from the theme + the
  baked-in defaults and proceeds *without asking*. The skill **never calls `AskUserQuestion`**.
  Any decision that would otherwise need a human — an editorial judgment, an ambiguous
  attribution — is recorded in the dossier's `needsReview` queue and the run-report, and the run
  **moves past it rather than blocking**. Mode defaults to full fire-and-forget; a quick-approve
  path (`--confirm-scope`) lets the user approve the auto-drafted contract before detaching.

**Why high autonomy is safe here:** an unattended run cannot publish. The dev-blog note stays
`draft: true`, there are **no vault writes**, and the licence gate prevents rights-reserved image
downloads. The mandatory separate verify pass (§16) still runs. The worst case is a reviewable
draft that needs polish — never harm.

**Robustness invariants for unattended runs:**
- Honor the Phase 0 stop-condition / time-box; never run unbounded.
- Save partial progress incrementally so a crash or timeout still leaves a usable artifact.
- Terminate cleanly; never hang waiting on input.
- Emit `docs/research/<topic-slug>/run-report.md`: the chosen scope contract, coverage summary,
  the `notCovered` queue, the `needsReview` items, the models used (with a rough cost note), and
  the output paths.

## 13. Overnight queue (headless CLI runner)

The **skill stays single-theme**; the overnight queue is a thin orchestration layer that
**spawns a fresh session per theme** — the cleanest way to keep each dive's context isolated
(one shared session looping over the queue would accumulate corpus reads and bleed themes
together by the third or fourth dive).

- **`docs/research/lib/corpus-dive-queue.sh`** (a deliverable alongside `SKILL.md`): reads a
  themes file (one theme per line, `#` comments allowed) and runs, per theme:

  ```
  claude -p "/corpus-dive <theme> --auto" [--model <tier>]
  ```

  Each invocation is a brand-new process with a clean context → true isolation. The loop
  **continues on per-dive failure** (logs the error, moves to the next theme), and writes a
  **combined batch summary** (e.g. `docs/research/_batch-<date>.md`) linking each dive's
  `run-report.md`.
- **`/loop` is deliberately not used** — it reruns in the *same* session, reintroducing the
  context-pollution this design avoids.
- **Caveats:** runs sequentially (bounds cost and resource use); the headless environment must
  expose the tools the dive needs (notably web access for the visual track) — where it does not,
  the visual track **degrades gracefully**: it documents provenance but downloads nothing.

## 14. Model routing & cost

"Least expensive model for the task" is realized as **per-phase routing**, not one model per
dive — a dive is wildly non-uniform in difficulty. The runner sets a **baseline** model
(`--model`); within the dive, sub-steps are dispatched to cheaper or pricier subagent tiers via
the Agent tool's `model` param.

**Governing principle: optimize cost on mechanical steps, never on fidelity or judgment.** Cheap
models are fine for grep-hit triage, file/vault existence checks, and dedup — but translation,
synthesis, contradiction-detection, and the verify pass are where a downgrade produces the
misquotes and hallucinated citations this whole design exists to prevent.

**Default routing (balanced):**

| Phase / task | Tier | Why |
|---|---|---|
| Grep sweep, `extract_tei.py`, `pdftoppm`, file/vault checks, dedup, image download | *no model* / **haiku** | Pure tool calls or mechanical triage |
| Candidate-hit relevance triage; visual-archive web triage | **sonnet** | Moderate judgment, high volume |
| Scoping contract | **sonnet/opus** | Judgment, but bounded |
| Working-English translations | **opus** | Fidelity-critical |
| Synthesis (`index.md` + `dossier.yaml`) | **opus** | The hard judgment; the payload |
| Verify pass (separate context) | **opus** | Adversarial; the safety net |

- **`--model` override** forces a single tier for a whole dive/queue. This enables a **scout
  pass**: run the overnight queue cheap (draft dives across many themes), review in the morning,
  then re-run the valuable ones on opus.
- **Escalate-on-low-confidence:** a cheaper-tier phase that reports low confidence / high
  ambiguity (part of each subagent's structured return) auto-retries on opus. The verify pass
  applies its normal scrutiny to escalated work — escalation buys quality, not a fidelity pass.

---

## 15. Boundaries

- **Reads freely:** `primary-sources/**` is the skill's primary read surface (TEI corpus + PSS
  PDFs). Anywhere under `website/` may be *read* where useful — the vault (`wiki/`, `works/`,
  `sources/`), source texts, schema, and `_staging/**`.
- **The only writable path under `website/` is `website/src/posts/notes/`.** Everything else
  under `website/` is read-only to the skill — the entire vault (`website/src/wiki/`,
  `website/src/works/`, `website/src/sources/`), the TEXT zones (`works/**/text/*.md`),
  `website/src/_staging/`, and `website/schema/`. Wiki/works content is produced by a separate,
  later, human-in-the-loop ingestion step — never by a dive.
- **Never writes / modifies:** `primary-sources/**`, and anything under `website/` other than
  `website/src/posts/notes/`.
- **Write targets (the complete list):** `docs/research/<topic-slug>/`, `docs/research/lib/`,
  `docs/research/_batch-<date>.md`, and `website/src/posts/notes/`.

---

## 16. Verification & quality gates

- Citation byte-fidelity (quote ↔ extract ↔ TEI/PDF) on a sampled basis.
- Every `index.md` claim source-anchored.
- Dossier entities resolve to valid wiki types; `vaultStatus` accurate against the vault.
- No unlabelled translations; no editorializing voice.
- No rights-reserved image downloaded into the public `visuals/`.
- The verify pass runs in a separate context from authoring (writer ≠ reviewer).
- Work auto-escalated to opus (§14) gets the same scrutiny as any other — escalation buys
  quality, not a fidelity exemption.

**Validation against the prototype:** a `corpus-dive` re-run of "copyright renunciation" should
reproduce the existing `docs/research/copyright-renunciation/index.md` findings (same staged
moments, same TEI ids, same corrected "с 1881 года" reading) — a useful acceptance check.

---

## 17. Future / out of scope (noted, not built)

- A cross-dossier aggregator (harvest every `dossier.yaml` into a combined index) once several
  dives exist.
- ~~Reconciling the four forked `extract_tei.py` copies against the new canonical one.~~ Done: forks removed; dives link to `docs/research/lib/extract_tei.py`.
- Wiring the `visuals` layer into the planned `website/src/images/` section when it lands.

---

## 18. Reference prototypes

- `docs/research/copyright-renunciation/` — the reference implementation (index.md, extracts/,
  the §5 manuscript record; the extractor is the shared `docs/research/lib/extract_tei.py`).
- `docs/research/biryukov-biography-editions/` — the multi-session shape (session-log + handoff).
- `docs/research/{christian-communism-socialism,doukhobors,tolstoyanism-christian-anarchism}/` —
  further worked examples of the same spine.
