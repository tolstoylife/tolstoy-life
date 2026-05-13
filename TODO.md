# Tolstoy Research Platform — Backlog

Last updated: 2026-05-13

---

## Active priorities

### 1. `tl`-kommandon för ebook-produktionspipelinen
Tre nya kommandon behöver byggas för att komplettera Phase A–C i Johan-workflow.md. Byggs i en sammanhållen session (alla tre parallellt). Birukoff-biografin är det tänkta första testet när kommandona är klara.

**Kommandon att bygga:**
- `tl convert-scans` — JP2 → JPEG + självständig `index.html` scan-browser för split-screen korrekturläsning
- `tl lint-ocr` — detekterar och auto-fixar OCR-artefakter (saknade apostrofer, avstavningar, misreads, löpande sidhuvuden); stöd för bokspecifik `.tl-lint-ocr.yaml`
- `tl detect-italics` — kursivigenkänning i två lägen: `--mode phrase-list` (kända titlar/fraser) och `--mode hocr` (Tesseract hOCR-konfidensbaserat); plus `tl ocr-confidence-report`

**Referens:** `projects/birukoff-biography/` + `uploads/johan-workflow.md`

### 2. LightRAG + Ollama — kvarstående steg
Grundinstallation klar (2026-04-18). Qwen2.5:7b + bge-m3 (1024d) operativt sedan 2026-04-25. Första ingestion av 29 filer OK (43 min, 192 noder, 196 kanter). Se `docs/architecture/lightrag-performance-report-2026-04-18.md`.

**Kvarstående:**
- ~~Byt embedding-modell till bge-m3 (1024d) för ryska+engelska~~ — Klart 2026-04-25 (commit `9775cab5`).
- Sätt upp nattligt cron-job för `sync.py`
- Testa inkrementell sync efter wiki-redigeringar
- ~~Committa LightRAG-scaffolden (staged i git)~~ — Klart 2026-04-25 (commit `9775cab5` tog med `config.py` + `requirements.txt` ändringarna och `diagnose.sh` + `start-ui.sh` helpers).

### 3. GitHub Projects för `projects/`-mappen
Bethink Yourselves, Birukoff-biografin och Korrektur ligger i `projects/` men är exkluderade från parent-repot via `.gitignore`. Undersök hur GitHub Projects kan användas för att tracka och organisera dessa produktionsprojekt — issues, boards, milestones. Kolla om varje projekt bör ha ett eget repo under `tolstoylife/` eller om ett gemensamt projekt-board räcker.

### 4. TEI-data ingestion (fas 3)
3 113 personer och 770 platser i tolstoydigital/TEI-repot. Börja med Tolstoys närmaste krets och arbeta utåt i tiers. Se implementationsplanen i CLAUDE.md.

**Nästa batch:**
- Skapa wiki-sidor för Ilya Lvovich Tolstoy och Mikhail Lvovich Tolstoy (saknas i TEI — källa: Birukoff)
- Nyckelplatser: Moscow Khamovniki house, Optina Pustyn, Shamordino
- Verifiera födelsedatum/-platser för befintliga barnsidor (Sergei, Lev, Maria, Andrei)
- Verifiera Alexandra Tolstayas deathPlace (Valley Cottage, NY)

### 5. PWA-arkitektur — follow-up efter 2026-04-23 review
Revisionen är klar. Se `docs/architecture/architecture-review.html` (renderad rapport) och `_generated/PWA/handoff-2026-04-23.md` (handoff). Följande gaps behöver åtgärdas innan Stage 1 kan skeppas — grupperade per arbetsområde.

**A. Blockers for Stage 1 (pipeline + spec fixes):**
- [x] **Fix the wiki-previews/manifest cascade** (critical) — spec updated 2026-04-24 in `tl-pipeline-integration.md`: removed `wikiPreviewsUrl` from per-work manifests, added §4.6 cross-reference isolation rule, updated §3.2 hash-input definition and §6.2 sketch with `HASH_EXCLUDE` filter. Follow-up (separate task C3): align `wiki-integration.md` §2.2 nested `relatedWiki` shape with the flat-slug-array shape now canonical in §4.3.
- [x] **Reconcile `yjs-schema-and-sync.md` §2.3 vs §8** — resolved 2026-04-24 in favour of §8's Y.Text decision. §2.3 rewritten to walk through the silent-duplicate failure mode with plain objects and show why Y.Map body items + Y.Text `value` fix it. §2.2 example updated, §8 item 1 wording tightened, `createTextualBody` factory specified, and a concurrent-edit regression test fixture is called out as required from the annotation-layer package's first commit. JSON-LD wire shape unchanged.
- [x] **Publish deterministic-build CI test** — wired in 2026-04-24 at `website/.github/scripts/check-determinism.mjs` + `website/.github/workflows/determinism.yml`. Runs `npm run build` twice, hashes every file under `dist/`, exits non-zero on mismatch. Spec promoted to `tl-pipeline-integration.md` §6.4. **Known drifts:**
  - ~~**`serviceworker.js`** — `CACHE_NAME = 'cache-{buildTime}'` uses build-time timestamp.~~ **Resolved 2026-05-12 (website `7ecdf4f`).** The whole eleventastic service worker (source, orphan include, base.njk registration, `buildTime` global) was deleted ahead of the eventual Workbox replacement, since the current implementation provides no benefit pre-Stage-1 and was the only thing keeping this CI check red. Local `check-determinism.mjs` run is ✓ green after removal. Workbox install is the natural follow-up (still pending — see 2026-05-12 LOG entry; surfaces in priority 5 subsection B as part of the Stage-1 PWA work).
  - **`feed.xml`** — Atom `<updated>` field falls back to `new Date()` because `collections.posts` is empty. Partial fix applied (`src/common/feed-atom.njk` — moved `{% set postslist = collections.posts %}` above the `<feed>` element so it's defined before use; a genuine correctness bug that would have surfaced once posts existed). Full determinism fix shelved pending a product decision on whether the project has a blog section and what the project's public-timeline start date is — either would give a stable fallback. See 2026-04-24 LOG entry for the full analysis. **2026-05-12 note:** with the `serviceworker.js` drift gone, this is now the *only* remaining drift; resolving it flips the workflow to "ready to be required."
  
  Action before flipping this workflow to a *required* status check in branch protection: resolve the `feed.xml` drift (either by writing the first post — the `notes` collection is live as of 2026-05-11 and could supply `<updated>` once feed-atom is repointed at it — or by committing to a stable fallback date), then re-run `node .github/scripts/check-determinism.mjs` locally to confirm ✓. Until then: workflow runs on every PR as a visible-but-non-blocking check, catches any *new* non-determinism regressions elsewhere in the build.
- [x] **Add `chapterUri` validator + one-shot migration** — resolved 2026-04-24 at smaller scope than originally planned. The corpus today has *zero* chapter files (no work has a `text/` subfolder yet), so no migration is needed — the rule is enforced prospectively. Augmented `website/.github/scripts/validate-frontmatter.mjs` with a `validateChapterFile()` function that checks four invariants on any chapter file (`work` + `chapter`/`part` frontmatter): (1) `chapterUri` present, (2) format `urn:tolstoy-life:<work-slug>:<chapter-id>` with both kebab-case, (3) work-slug in URI matches the `work` field, (4) globally unique across the corpus. Existing `validate.yml` workflow picks it up automatically on every PR touching `src/works/**/*.md`. Spec promoted to `tl-pipeline-integration.md` §8.2. Smoke-tested all four failure modes with temporary fixtures — each produces a specific, actionable error message and cites §8.1. When Phase 5 TEI ingestion begins, the import pipeline emits `chapterUri` from day one; a bulk-migration script can be added alongside *that* pipeline only if a batch of URI-less chapter files ever actually lands.
- [ ] **Replace `git_first_commit_date_for_dir` with stateful `contentDate`** in `works.json` — current approach breaks on Netlify's shallow clones. **Deferred 2026-04-24, pending Layer-1 pipeline:** this is a fix to `generate-asset-manifests.py`, which doesn't exist yet. Spec direction is already recorded — the §6.2 sketch uses a `resolve_content_date(work_dir, content_hash)` placeholder that calls out this task by reference. Implement alongside the first real version of the asset-manifest generator.
- [ ] **Adopt a canonical JSON encoder** (`rfc8785`) and NFC-normalise all strings before hashing. **Deferred 2026-04-24, pending Layer-1 pipeline:** applies to the four Layer-1 generators (`generate-wiki-previews.py`, `generate-related-wiki.py`, `generate-asset-manifests.py`, `generate-works-index.py`) — none of which exist yet. Land as part of their shared helpers module when the generators are first written (one canonical-json function imported by all four).

**B. UX components to build (scoped in review, not yet implemented):**
- [ ] **Install-UX web component** (~80-line vanilla, per handoff decision) — triggers on first "Make available offline" tap; per-platform copy drafted in architecture-review.html Part 3. Load-bearing for iOS (7-day ITP eviction makes install-before-download necessary for the "train reader" user story).
- [ ] **Sync-visibility glyph indicator** — five-state (synced / syncing / offline / error / needs attention) shape+animation component, WCAG 1.4.1 compliant (colour is reinforcement only). Full legend + toast mockup in architecture-review.html Part 4.
- [ ] **iOS install-before-download flow** — wire the install component into the Stage 1 download coordinator so iOS users are prompted before the first offline download.

**C. Spec propagation (update the 5 design docs with review findings):**
- [ ] Propagate findings #8–#14 from architecture-review.html back into the source documents so the specs stay coherent (currently only the review carries these corrections).
- [ ] Update `yjs-schema-and-sync.md` §6.2 — remove the `handle_links` / `capture_links` assumption (not available on iOS; QR scanning always lands in Safari first).
- [ ] Align `wiki-integration.md` §2.2 with `tl-pipeline-integration.md` §4.3 on the `relatedWiki` shape (pick one and propagate).
- [ ] Add a Phase-5 architecture note about the CF Pages + R2 split — the 20,000-file / 25 MB-per-file per-deployment cap makes the split load-bearing, not optional.
- [ ] Write a two-page **sync security spec** before Stage 4 coding — HKDF labels, SAS protocol, rate-limit numbers, device-registration authorisation, rotation-export atomicity.

**D. Infrastructure decisions (committed 2026-04-23):**
- [x] Sign up for Cloudflare Pages account (done)
- [ ] Connect `tolstoylife/website` repo to CF Pages as a parallel deploy target (verify builds match Netlify byte-for-byte)
- [ ] Transfer domain to Cloudflare Registrar at next Netlify renewal (~$22/yr saved; CF at $28.20, Netlify at ~$50)
- [ ] Add `netlify.toml` with `[build.processing] skip_processing = true` (minimum-change determinism fix — see architecture-review.html Part 8)
- [ ] Add `_headers` file with per-path Cache-Control (immutable for versioned, short max-age for `works.json`/`manifest.json`)
- [ ] Implement cached file-hashing in `generate-asset-manifests.py` (keyed by mtime+size) before Phase 3 ingestion
- [ ] Write the Hocuspocus-on-Fly fallback Dockerfile (committed to the repo, not deployed) — operationalises the "operator can be swapped" claim.

**E. Stage-4 fixes (before sync ships — not urgent yet):**
- [ ] HKDF key separation for HMAC / AEAD / export (currently one key used for multiple purposes — crypto footgun)
- [ ] SAS confirmation handshake replacing the yes/no pairing confirm (real MITM protection vs theatre)
- [ ] Device-registration authorisation — existing device must sign new-device registration (otherwise revocation is a placebo)
- [ ] Rate-limit pairing attempts at the Durable Object; one-use BIP-39 tokens
- [ ] Resolve the "relay doesn't parse user data" contradiction (can't be literally true if server-side snapshot compaction is enabled)
- [ ] Promote BIP-39 pairing to iOS-primary (BarcodeDetector is not available on iOS Safari as earlier drafts assumed) — ship a bundled JS decoder (jsQR / zxing-wasm), never hosted
- [ ] `history.replaceState` on `/pair` to mitigate iCloud Tabs fragment leak
- [ ] Dormant-user heartbeat (keep relay room alive while paired devices are active)

**Referens:** `docs/architecture/architecture-review.html` är den kanoniska renderingen; `_generated/PWA/handoff-2026-04-23.md` är orienteringsdokumentet för nästa session.

### 6. EPUB 3.3 & Accessibility 1.1 — compliance and wikilink strategy
*From W3C spec review 2026-04-22. Full findings: `docs/architecture/epub-a11y-w3c-review-2026-04-22.md`*

EPUB Accessibility 1.1 is now a W3C Recommendation and mandatory for all EPUB 3.3 publications. Several gaps identified in the `tl` toolset and in how wikilinks are handled in distributed EPUBs.

**Tasks:**

- [ ] **Audit `tl create-draft` templates** against EPUB A11y 1.1 mandatory metadata checklist — `accessMode`, `accessibilityFeature`, `accessibilityHazard`, `accessibilitySummary`
- [ ] **Add schema.org accessibility metadata defaults** to `content.opf` template (pre-populated with sensible values + clear placeholders for per-book overrides)
- [ ] **Add `<nav epub:type="page-list">` support** to `tl build-toc` — required for print-replica ebooks (Birukoff biography and similar scan-based projects); enables `printPageNumbers` accessibilityFeature declaration
- [ ] **Define wikilink strategy for distributed EPUBs** — choose between: (a) in-EPUB condensed wiki/glossary spine document linked via `doc-glossref`, or (b) strip wikilinks from distributed EPUBs and replace with endnotes. Decision needed before Birukoff epub goes to distribution.
- [ ] **Update chapter XHTML templates** to use `epub:type` + `role` pairs on all interactive reference elements — never `epub:type` alone. Key pairs: `noteref`/`doc-noteref`, `glossref`/`doc-glossref`, `footnote`/`doc-footnote`
- [ ] **Document `doc-glossref` as canonical wikilink representation** in the Manual of Style skill (`skills/manual/`) — the pattern for how wikilinks appear in EPUB output vs. in the PWA

### 7. timelinegraph — execute the implementation plan
*Spec: `docs/superpowers/specs/2026-04-29-timelinegraph-design.md` (`6ba0eec3`). Plan: `docs/superpowers/plans/2026-04-29-timelinegraph.md` (`7e987467`).*

A 2D knowledge-graph + timeline visualisation of Tolstoy's universe (`/graph/`), shipping privately first, surfaced on the landing page once the corpus passes ~200 nodes. Brainstormed, specced, and planned 2026-04-29; execution parked for a dedicated session.

**To resume:** invoke `superpowers:subagent-driven-development` against the plan. 35 tasks across 5 tracks (~15+ hours of subagent activity).

**Hard gate:** Task 21 (deuteranopia validation — Johan eyes-on the red↔green period transition at 1851) must pass before Track 3 starts.

**v1 launch criterion:** internal-tool gate per `projects/timelinegraph/QA.md`. Public landing-page placement is gated separately on corpus density (~200 nodes) + designer pass on cloud-type palette + Lighthouse / axe-core CI.

### 8. docs/ → dev-blog migration ("Notes" on eleventy)
*Plan + decisions: `docs/design/2026-05-11-docs-to-blog-migration.md`. Started 2026-05-11.*

Reframing `docs/` from a documentation hub into a dated build log, with content ported into the eleventy `notes` collection at `website/src/posts/notes/`. Phase 1–3.1 done in one session; remainder ports content and retires the temporary scaffolding.

**Done:**
- [x] **Phase 0 — decisions** (2026-05-11). Notes name + path, fully retire `docs/` eventually, git first-commit date for backdating, no RSS in `serve.py` (eleventy handles).
- [x] **Phase 1 — annotate frontmatter on every `docs/*.md`** (commit `f9d53d31`). 28 files: 14 reference, 14 blog.
- [x] **Phase 2 — rewrite `serve.py` INDEX** as chronological feed + reference appendix; drop `FEATURED` (commit `351bdb5c`).
- [x] **Phase 3 step 1 — scaffold eleventy `notes` collection** (website `79d2540`, parent pointer `ab8833a4`). `notes.json` + inaugural entry + Notes top-nav.
- [x] **Phase 3 step 2 — port 14 blog files** (website `3c748db`, parent `88e4d8dd`). YYYY-MM-DD-slug filenames, hand-written descriptions, normalized tags, `draft: false`. One file needed `templateEngineOverride: md` (source-mode-implementation — contains a `{%` Nunjucks reference in a table cell). Source files deleted from `docs/`.

**Done (continued):**
- [x] **Phase 3 step 3 — defer all 14 reference files** (2026-05-11). After reading the 14 reference files in full, they split into two groups by audience, neither of which has a natural eleventy home today:
  - **Group A (10 files): engineering/operational reference, stays in `docs/` indefinitely.** PWA specs (`pwa/` × 5), `architecture/internal-operations.md`, `design/penpot-tokens.md`, `development/README.md`, `editorial/conventions.md`, `research/pss-volume-mapping.md`. These are living docs that get updated when code ships — moving them to eleventy would make cross-referencing from the codebase harder.
  - **Group B (4 files): project transparency, candidates for a future `about/` or `project/` section.** `editorial/editorial.md`, `editorial/source-mode.md`, `research/tolstoydigital-tei-reference.md`, `research/copyright-renunciation/index.md`. Deferred until that section is built; reframing now would be premature.
  - `serve.py` reference-appendix label updated from "pending port to website/src/notes/" → "engineering specs and operational notes" to make the new posture explicit.
- [x] **Phase 4 — dropped generated `.html` siblings from git** (2026-05-11). 28 files removed: 14 with `.md` siblings (regenerated by `serve.py` on demand) + 14 stale renderings whose `.md` was ported to `website/src/posts/notes/` in step 2 and never cleaned up. `docs/.gitignore` ignores `*.html` with three exceptions: `/INDEX.html` (entry point), `/architecture/architecture-review.html` and `/design/period-colours-preview.html` (hand-authored orphans in `HTML_META`). The leading-slash anchors are load-bearing — without them, `!INDEX.html` would re-include `research/copyright-renunciation/index.html` on case-insensitive macOS.
- [x] **Phase 3 follow-up — fix notes URLs + duplicate h1 + stray tag chip** (2026-05-12, website `c98e7f0`). Three defects spotted once notes were live: permalink derived from `title | slugify` leaked `/` and `→` into URLs; layout's `<h1>` doubled the markdown `# Heading` on 14 entries; per-note tag loop missed `"posts"` so every page rendered a 404-linking "Posts" chip. Fixed: switched permalink to `page.fileSlug | slugify` (Eleventy strips the date prefix, giving clean date-less URLs); stripped the leading h1 from 14 files; widened the tag filter to exclude both `notes` and `posts`. Renamed `Starting a development blog.md` to the dated kebab-case form so `fileSlug` works for it too.

---

## Open questions (from log)

### Editorial — Tolstoy on property and copyright (2026-04-26)
Hitta en direkt Tolstoy-källa som binder hans religiösa hållning till avstående av litterär egendom. Behövs för att stärka stycke 2 i `docs/editorial/editorial.md` (markerat med inline `<!-- JE: -->`). Kandidatkällor: *The Kingdom of God Is Within You*; brevet 1891 till *Russkie Vedomosti*; dagboksanteckningar från sent 1880-tal och framåt. När citatet hittas: lyft in det i editorial.md och ta bort hedge-formuleringen.

### Concept pages (2026-04-10)
- "Tolstoyism"-avvisningsbrevet: vilken volym i Jubilee Edition? Mottagare? År?
- *On Anarchy* (1900): Jubilee Edition vol. 34 eller annanstans? Hitta den ryska fulltexten.
- Vilka specifika 1894-recensioner myntade "Christian anarchism"? Kolla Christoyannopoulos.
- Ska Aylmer Maude få en egen personsida? Refereras i båda konceptsidorna men saknar wiki-entry.

### Bethink Yourselves (2026-04-07)
- Första ryska publiceringsdatumet okänt — cirkulerade via Chertkovs London-kanaler.
- Wikidata QID saknas.
- Medöversättaren "I. F. M." oidentifierad — Isabel F. Mayo?

### TEI ingestion (2026-04-06–07)
- Tatyana Tolstaya: gift Sukhótin — vilken namnform ska vara primärtitel? Bör vara konsekvent med citeringar.
- Yasnaya Polyana: TEI anger "1847" för att Tolstoj ärvde godset — dubbelkolla mot Birukoff.
- TEI-personbeskrivningar är enbart ryska — engelsk prosa syntetiserad men overifierad. Alla sidor har `recordStatus: draft`.

---

## Brainstorming

### Institutionsgranskning — stresstesta projektet
Gå igenom projektet ur en kritisk akademisk institutions perspektiv. Identifiera svaga punkter innan de hittas utifrån. Fokusområden:

- **Källkritik:** Är varje faktapåstående i wikin spårbart till en namngiven primärkälla? Finns det sidor med ogrundade påståenden?
- **Upphovsrätt:** Finns det material i projektet som kan ifrågasättas juridiskt? Bilder, texter, skanningar — vad är public domain och vad är oklart?
- **Akademisk trovärdighet:** Hur ser projektet ut för en forskare som granskar det? Vilka svagheter skulle de peka på?
- **Tonläge:** Finns det formuleringar i wikin som kan uppfattas som ideologiska snarare än sakliga?

Se docs/editorial/editorial.md för projektets hållning till dessa frågor.


---

## Completed

- ~~Byproduct-capture convention (proposal)~~ — Accepted 2026-05-13. Proposal at `_generated/research/research-practices.md` (status: `accepted`); all four §7 questions resolved on the recommended defaults. Mechanical change committed: the next research-style task session creates its scratchpad at `_generated/research/<topic>/`, not `projects/<topic>/`. No tooling built — convention only.
- ~~Testa end-of-day-skillen~~ — Testad 2026-04-14. Triggar korrekt, flödet fungerar.
- ~~Korrektur-app: pipeline-design~~ — Pipeline-workflow (typogrify → clean → semanticate som batch) designat och testat 2026-04-15. 30 Playwright-tester gröna. Appen byggs vidare av Johan (se prio 1).
- ~~Skalbarhet-rapport~~ — Färdig 2026-04-15. Slutsats: Obsidian som redigeringsverktyg, LightRAG + Ollama som nödvändigt query-lager. LightRAG-setup nu aktiv prioritet (prio 2).
- ~~PRINCIPLES.md~~ — Skapad 2026-04-16. Redaktionell hållning, tonläge, förhållningssätt till institutioner, beredskap för kritik. *(2026-04-26: omstrukturerad till `docs/editorial/editorial.md` — public-statement-delar flyttade till MANIFEST.md, taktiska delar till `_generated/editorial/institutional-strategy.md`.)*
- ~~LightRAG grundinstallation~~ — 2026-04-18. Qwen2.5:7b (14B passar inte 24 GB). Första ingestion OK. Prestandarapport i `_generated/`.
- ~~Korrektur Slice 1.C~~ — 2026-04-18. Autosave, git checkpoint, search & replace. 19+59 tester gröna.
- ~~Korrektur-appen~~ — Lagd på is 2026-04-22. Ersätts av macOS split-screen + git som checkpoint-system (se johan-workflow.md).

---

## Deferred (low priority)

- 15 works saknar `.data.yaml`-sidecar-filer (skapas när djup metadata finns tillgänglig)
- De flesta works-sidor har minimal prosa — wikilink-densiteten ökar i takt med att prosa skrivs
- Byta till PR-workflow (fas 6 i implementationsplanen — inte aktuellt under R&D-fasen)
