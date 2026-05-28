# Tolstoy Research Platform — Backlog

Last updated: 2026-05-28

---

## Active priorities

### 1. LightRAG + Ollama — remaining steps
Base installation done (2026-04-18). Qwen2.5:7b + bge-m3 (1024d) operational since 2026-04-25. First ingestion of 29 files OK (43 min, 192 nodes, 196 edges). See `website/src/posts/notes/2026-04-18-lightrag-performance-report.md`.

**Remaining:**
- ~~Switch embedding model to bge-m3 (1024d) for Russian + English~~ — Done 2026-04-25 (commit `9775cab5`).
- Set up a nightly cron job for `sync.py`
- Test incremental sync after wiki edits
- ~~Commit the LightRAG scaffold (staged in git)~~ — Done 2026-04-25 (commit `9775cab5` carried the `config.py` + `requirements.txt` changes and the `diagnose.sh` + `start-ui.sh` helpers).

### 2. GitHub Projects for the `projects/` folder
Bethink Yourselves, the Birukoff biography, and Korrektur live in `projects/` but are excluded from the parent repo via `.gitignore`. Investigate how GitHub Projects can be used to track and organise these production projects — issues, boards, milestones. Decide whether each project should have its own repo under `tolstoylife/` or whether a shared project board is enough.

### 3. TEI data ingestion (phase 3)
3,113 persons and 770 locations in the tolstoydigital/TEI repo. Start with Tolstoy's closest circle and work outward in tiers. See the implementation plan in CLAUDE.md.

**Next batch:**
- Create wiki pages for Ilya Lvovich Tolstoy and Mikhail Lvovich Tolstoy (missing from TEI — source: Birukoff)
  - Birukoff source ready: all of Vol. III (`docs/research/doukhobors/biryukov-vol3/en/`, 22 chapters) AND all of Vol. IV (`docs/research/doukhobors/biryukov-vol4/en/`, 19 chapters) are now available in English — Biryukov's whole four-volume biography is held end-to-end. Ready as a primary source for Birukoff-based wiki pages and wiki source ingestion. **Vol III caveat:** translated from the `tolstoy-lit.ru` capture; `az.lib.ru` carries ~4.5% more material (author footnotes + embedded primary documents); recapture + targeted-patch plan in section 8 below.
- Key locations: Moscow Khamovniki house, Optina Pustyn, Shamordino
- Verify birth dates/places for existing children's pages (Sergei, Lev, Maria, Andrei)
- Verify Alexandra Tolstaya's deathPlace (Valley Cottage, NY)

### 4. PWA architecture — follow-up after the 2026-04-23 review
The review is complete. See `docs/architecture/architecture-review.html` (rendered report) and `_generated/PWA/handoff-2026-04-23.md` (handoff). The following gaps need to be addressed before Stage 1 can ship — grouped by work area.

**A. Blockers for Stage 1 (pipeline + spec fixes):**
- [x] **Fix the wiki-previews/manifest cascade** (critical) — spec updated 2026-04-24 in `tl-pipeline-integration.md`: removed `wikiPreviewsUrl` from per-work manifests, added §4.6 cross-reference isolation rule, updated §3.2 hash-input definition and §6.2 sketch with `HASH_EXCLUDE` filter. Follow-up (separate task C3): align `wiki-integration.md` §2.2 nested `relatedWiki` shape with the flat-slug-array shape now canonical in §4.3.
- [x] **Reconcile `yjs-schema-and-sync.md` §2.3 vs §8** — resolved 2026-04-24 in favour of §8's Y.Text decision. §2.3 rewritten to walk through the silent-duplicate failure mode with plain objects and show why Y.Map body items + Y.Text `value` fix it. §2.2 example updated, §8 item 1 wording tightened, `createTextualBody` factory specified, and a concurrent-edit regression test fixture is called out as required from the annotation-layer package's first commit. JSON-LD wire shape unchanged.
- [x] **Publish deterministic-build CI test** — wired in 2026-04-24 at `website/.github/scripts/check-determinism.mjs` + `website/.github/workflows/determinism.yml`. Runs `npm run build` twice, hashes every file under `dist/`, exits non-zero on mismatch. Spec promoted to `tl-pipeline-integration.md` §6.4. **Known drifts:**
  - ~~**`serviceworker.js`** — `CACHE_NAME = 'cache-{buildTime}'` uses build-time timestamp.~~ **Resolved 2026-05-12 (website `7ecdf4f`).** The whole eleventastic service worker (source, orphan include, base.njk registration, `buildTime` global) was deleted ahead of the eventual Workbox replacement, since the current implementation provides no benefit pre-Stage-1 and was the only thing keeping this CI check red. Local `check-determinism.mjs` run is ✓ green after removal. Workbox install is the natural follow-up (still pending — see 2026-05-12 LOG entry; surfaces in priority 4 subsection B as part of the Stage-1 PWA work).
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

**Reference:** `docs/architecture/architecture-review.html` is the canonical rendering; `_generated/PWA/handoff-2026-04-23.md` is the orientation document for the next session.

### 5. EPUB 3.3 & Accessibility 1.1 — compliance and wikilink strategy
*From W3C spec review 2026-04-22. Full findings: `website/src/posts/notes/2026-04-22-epub-a11y-w3c-review.md`*

EPUB Accessibility 1.1 is now a W3C Recommendation and mandatory for all EPUB 3.3 publications. Several gaps identified in the `tl` toolset and in how wikilinks are handled in distributed EPUBs.

**Tasks:**

- [ ] **Audit `tl create-draft` templates** against EPUB A11y 1.1 mandatory metadata checklist — `accessMode`, `accessibilityFeature`, `accessibilityHazard`, `accessibilitySummary`
- [ ] **Add schema.org accessibility metadata defaults** to `content.opf` template (pre-populated with sensible values + clear placeholders for per-book overrides)
- [ ] **Add `<nav epub:type="page-list">` support** to `tl build-toc` — required for print-replica ebooks (Birukoff biography and similar scan-based projects); enables `printPageNumbers` accessibilityFeature declaration
- [ ] **Define wikilink strategy for distributed EPUBs** — choose between: (a) in-EPUB condensed wiki/glossary spine document linked via `doc-glossref`, or (b) strip wikilinks from distributed EPUBs and replace with endnotes. Decision needed before Birukoff epub goes to distribution.
- [ ] **Update chapter XHTML templates** to use `epub:type` + `role` pairs on all interactive reference elements — never `epub:type` alone. Key pairs: `noteref`/`doc-noteref`, `glossref`/`doc-glossref`, `footnote`/`doc-footnote`
- [ ] **Document `doc-glossref` as canonical wikilink representation** in the Manual of Style skill (`skills/manual/`) — the pattern for how wikilinks appear in EPUB output vs. in the PWA

### 6. timelinegraph — execute the implementation plan
*Spec: `website/src/posts/notes/2026-04-29-timelinegraph-design.md` (`6ba0eec3`). Plan: `website/src/posts/notes/2026-04-29-timelinegraph-plan.md` (`7e987467`).*

A 2D knowledge-graph + timeline visualisation of Tolstoy's universe (`/graph/`), shipping privately first, surfaced on the landing page once the corpus passes ~200 nodes. Brainstormed, specced, and planned 2026-04-29; execution parked for a dedicated session.

**To resume:** invoke `superpowers:subagent-driven-development` against the plan. 35 tasks across 5 tracks (~15+ hours of subagent activity).

**Hard gate:** Task 21 (deuteranopia validation — Johan eyes-on the red↔green period transition at 1851) must pass before Track 3 starts.

**v1 launch criterion:** internal-tool gate per `projects/timelinegraph/QA.md` (planned, will live in the timelinegraph workspace). Public landing-page placement is gated separately on corpus density (~200 nodes) + designer pass on cloud-type palette + Lighthouse / axe-core CI.

### 7. docs/ → dev-blog migration ("Notes" on eleventy)
*Plan + decisions: `website/src/posts/notes/2026-05-11-docs-to-blog-migration.md` (the plan was itself ported in Phase 3 step 2). Started 2026-05-11.*

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

### 8. Biryukov Vol III — recapture from az.lib.ru and patch the ~4.5% gap
*Surfaced 2026-05-28 at end of Vol IV session 5b. Background: when the Vol IV capture was set up, `az.lib.ru` was chosen over `tolstoy-lit.ru` because the latter "silently dropped text" via hex-encoded JS interpolations (already decoded for Vol III) AND carries ~4.5% less material — concentrated in author asterisk footnotes and embedded primary documents. The existing Vol III English translation is sound for the 95.5% that's there, but the gap (≈8,000 RU words) needs closing for the volume to match Vol IV's source standard.*

Re-translating the whole volume is wrong (waste — the matching 95.5% would re-produce identically). The right tool is recapture + targeted patches.

**Three-step plan:**

**Source URL (resolved 2026-05-28):** `http://az.lib.ru/b/birjukow_p_i/text_1905_tolstoy05.shtml` — single HTML file, windows-1251, 1173k. The `text_1905_` filename prefix is an az.lib.ru cataloguing artifact; the file is **Biryukov's 1915 first edition of Vol III** (closes with the "28 октября 1915 г." dateline). The current `vol3/ru/` capture from `tolstoy-lit.ru` is also the 1915 first edition (same closing dateline), so the RU↔RU diff will attribute cleanly to the known hex-JS dropout, not to edition variance. Open follow-up: whether 1915 is the edition Biryukov himself would have preferred (vs a possible later Berlin reissue) — surfaced 2026-05-28, verdict pending; if it moves, step 2 source decision reopens.

- [ ] **Step 1 — probe the actual delta** (1 short session). Recapture **ch18** from the URL above, decode + clean it in the Vol IV style, diff RU↔RU against the current `ru/chapter-18.md`, and report concretely: footnotes missing, embedded documents missing (if any), inline text gaps. ch18 is the best probe candidate: approved quality sample, currently shows 0 Biryukov footnotes, and covers Tolstoy's first Doukhobor-movement appeals (likely embedded-document territory).
- [ ] **Step 2 — full RU recapture from `az.lib.ru`** (1 session if probe confirms the gap). Capture all 22 chapters in the Vol IV style (single-file decode, windows-1251 → UTF-8, footnotes preserved as `(*)` / `(* … *)`, part-dividers + embedded-document H2s). Preserve the current `ru/` capture as record-of-translated-from until step 3 settles.
- [ ] **Step 3 — targeted EN patches** (1–2 sessions, depending on gap size). Per chapter: diff old RU vs new RU; translate only the missing fragments via the proven per-chapter `executor` + `verifier` workflow; slot patches into the existing EN at the right paragraphs; append `## Vol III, Chapter N — patches from az.lib.ru recapture` blocks to the editorial ledger documenting what was added and where.

**Total cost:** ~3–4 sessions vs the **~5–6 sessions** a full re-translation would take (Vol III's documented budget is ≈30k RU words ≈ 4 chapters/session × 22 chapters). The cost ratio is thin enough that the case rests less on cost than on not re-rolling ≈240k words of sound English and ~50 documented editorial decisions, plus register continuity with Vol IV.

**Chapters that currently show 0 Biryukov footnotes** (likeliest sites of the gap): ch08, ch10, ch13, ch17, ch18, ch19, ch22.

**Reference:** the Vol IV [index](docs/research/doukhobors/biryukov-vol4/index.md) documents the `az.lib.ru` advantage; the editorial ledger (`docs/research/doukhobors/biryukov-vol3/en/translation-notes.md`, the `# Volume IV` section) documents what `az.lib.ru`-captured material looks like in practice; the `vol3/en/README.md` carries the public Known-limitation note.

---

### 9. Vol I and Vol II — audit source-completeness against `az.lib.ru`
*Surfaced 2026-05-28 while sizing §8. Both Vol I and Vol II were captured from `tolstoy-lit.ru` — the same source whose hex-encoded-JS interpolations silently drop Biryukov's asterisk footnotes and embedded primary documents in Vol III. The §8 audit method (footnote-pair count per chapter to find zero-footnote chapters as likely gap sites, then RU↔RU diff against an `az.lib.ru` recapture) applies directly.*

Pre-condition: §8 Step 1 (the ch18 probe) completes first, so the recapture-and-patch method is proven on one volume before scaling to two more.

Action once §8's Step 1 lands: count current footnote pairs per chapter in Vol I and Vol II, identify zero-footnote chapters as likely gap sites, and verify which `az.lib.ru` edition matches each volume's existing `tolstoy-lit.ru` capture (the edition match is what makes the diff signal clean — see §8 for the reasoning). az.lib.ru's Birjukov page hosts the whole series sequentially: Vol 1 at `text_1905_tolstoy01.shtml` + `tolstoy02.shtml` (1905 edition, two parts), Vol 2 at `tolstoy03.shtml` + `tolstoy04.shtml` (1905 edition, two parts), Vol 3 at `tolstoy05.shtml` (1915 first edition), Vol 4 at `text_1922_tolstoy06.shtml` (1922 Berlin). So Vols 1–2 are 4 HTML files on az.lib.ru, not 2. If the gap is real on either volume, repeat §8's three-step plan per volume.

Not sized — sizing waits on §8's outcome and the Vol I/II URL check.

---

## Open questions (from log)

### Editorial — Tolstoy on property and copyright (2026-04-26)
Find a direct Tolstoy source linking his religious position to the renunciation of literary property. Needed to strengthen paragraph 2 in `docs/editorial/editorial.md` (marked with an inline `<!-- JE: -->`). Candidate sources: *The Kingdom of God Is Within You*; the 1891 letter to *Russkie Vedomosti*; diary entries from the late 1880s onward. Once the quote is found: bring it into editorial.md and remove the hedge wording.

### Concept pages (2026-04-10)
- The "Tolstoyism" rejection letter: which volume in the Jubilee Edition? Recipient? Year?
- *On Anarchy* (1900): Jubilee Edition vol. 34 or elsewhere? Find the Russian full text.
- Which specific 1894 reviews coined "Christian anarchism"? Check Christoyannopoulos.
- Should Aylmer Maude get his own person page? Referenced in both concept pages but has no wiki entry.

### Bethink Yourselves (2026-04-07)
- First Russian publication date unknown — circulated via Chertkov's London channels.
- Wikidata QID missing.
- Co-translator "I. F. M." unidentified — Isabel F. Mayo?

### TEI ingestion (2026-04-06–07)
- Tatyana Tolstaya: married name Sukhotin — which name form should be the primary title? Should be consistent with citations.
- Yasnaya Polyana: TEI gives "1847" for when Tolstoy inherited the estate — double-check against Birukoff.
- TEI person descriptions are Russian-only — English prose synthesised but unverified. All pages have `recordStatus: draft`.

---

## Brainstorming

### Institutional review — stress-test the project
Go through the project from the perspective of a critical academic institution. Identify weak points before they're found from outside. Focus areas:

- **Source criticism:** Is every factual claim in the wiki traceable to a named primary source? Are there pages with unsupported claims?
- **Copyright:** Is there material in the project that could be challenged legally? Images, texts, scans — what is public domain and what is unclear?
- **Academic credibility:** How does the project look to a researcher reviewing it? What weaknesses would they point to?
- **Tone:** Are there formulations in the wiki that could be read as ideological rather than factual?

See docs/editorial/editorial.md for the project's stance on these questions.


---

## Completed

- ~~Byproduct-capture convention (proposal)~~ — Accepted 2026-05-13. Proposal at `_generated/research/research-practices.md` (status: `accepted`); all four §7 questions resolved on the recommended defaults. Mechanical change committed: the next research-style task session creates its scratchpad at `_generated/research/<topic>/`, not `projects/<topic>/`. No tooling built — convention only.
- ~~`tl` commands for the ebook-production pipeline~~ — Shipped 2026-04-22 (`tools` commit `d47cbf08`): `convert-scans`, `lint-ocr`, `detect-italics`, and `ocr-confidence-report`, auto-registered via `se/commands/`. Completes Phase A–C of `tools/_scratch/johan-workflow.md`. `convert-scans`: JP2 → JPEG + a standalone `index.html` scan browser for split-screen proofreading. `lint-ocr`: detects and auto-fixes OCR artefacts (missing apostrophes, hyphenation, misreads, running headers); supports a book-specific `.tl-lint-ocr.yaml`. `detect-italics`: italic recognition in two modes (`--mode phrase-list` for known titles/phrases, `--mode hocr` for Tesseract hOCR confidence). The Birukoff biography is the intended first test. Ref: `projects/birukoff-biography/`.
- ~~Test the end-of-day skill~~ — Tested 2026-04-14. Triggers correctly, the flow works.
- ~~Korrektur app: pipeline design~~ — Pipeline workflow (typogrify → clean → semanticate as a batch) designed and tested 2026-04-15. 30 Playwright tests green. App development was folded into the `tl` ebook pipeline (now completed, above).
- ~~Scalability report~~ — Done 2026-04-15. Conclusion: Obsidian as the editing tool, LightRAG + Ollama as the necessary query layer. LightRAG setup now an active priority (priority 1).
- ~~PRINCIPLES.md~~ — Created 2026-04-16. Editorial stance, tone, posture toward institutions, readiness for criticism. *(2026-04-26: restructured into `docs/editorial/editorial.md` — public-statement parts moved to MANIFEST.md, tactical parts to `_generated/editorial/institutional-strategy.md`.)*
- ~~LightRAG base installation~~ — 2026-04-18. Qwen2.5:7b (14B doesn't fit 24 GB). First ingestion OK. Performance report in `_generated/`.
- ~~Korrektur Slice 1.C~~ — 2026-04-18. Autosave, git checkpoint, search & replace. 19+59 tests green.
- ~~Korrektur app~~ — Put on ice 2026-04-22. Replaced by macOS split-screen + git as the checkpoint system (see johan-workflow.md).

---

## Deferred (low priority)

- 15 works lack `.data.yaml` sidecar files (created once deep metadata is available)
- Most works pages have minimal prose — wikilink density increases as prose is written
- Switch to a PR workflow (phase 6 in the implementation plan — not relevant during the R&D phase)
