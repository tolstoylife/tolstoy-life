# Research förstudie folder-move Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganise `docs/research/` into `works/` + `themes/` + `wiki/` (+ `_meta/`) so it mirrors the live site, without breaking any link that points at the current flat dive paths.

**Architecture:** Move each dive folder into its new home with `git mv` (history preserved), driven by an explicit move-map. Then repair the references: three index **generators** (point their globs at the new tree), one serve.py routing glob, hard-coded links in prose docs and the reader bundle (parent repo), and ~30 published blog posts (the `website` submodule). The two index pages regenerate themselves once the generators are fixed — never hand-edit `research/index.html` or `reader/index.html`.

**Tech Stack:** Python 3 (the generators + serve.py + small move/rewrite scripts), `git mv`, ripgrep for verification. No new dependencies.

## Global Constraints

- **Design spec:** [`docs/superpowers/specs/2026-07-13-research-forstudie-architecture-design.md`](../specs/2026-07-13-research-forstudie-architecture-design.md). Every decision here derives from it.
- **Two repos.** `docs/**` is the **parent** repo; `website/**` is a **submodule**. Blog-post link edits (Task 6) are a **separate submodule commit**, pushed submodule-first (memory `reference_push_command_sequence`). Never mix parent and submodule changes in one commit.
- **Do NOT touch** `primary-sources/**`, the TEXT zone in `website/src/works/**/text/*.md`, or `website/src/_staging/**`.
- **Nothing graduates in this move.** `wiki/` is created **empty** — populating shared entity pages is the ongoing workflow, not this move. No writes to `website/src/wiki/`.
- **Naming:** `works/<genre>/<subcat>/<date-slug>/` (keep the date prefix), `themes/<slug>/` (bare), `wiki/<Entity>.md` (Title Case). Keep every existing folder's own name — only its location changes.
- **Filename case:** lowercase inside `docs/` subdirs (`move-map.tsv`, `_meta/`), except `INDEX.html`/`README.md`.
- **Commit freely; never push** — Johan pushes (memory / `~/.claude/CLAUDE.md`).

---

## Pre-flight: classification (confirmed with Johan 2026-07-13)

The move-map below is the plan's core. Most rows are unambiguous or confirmed against an existing live `works/` page (✓). The editorial calls were **settled with Johan on 2026-07-13** and are already baked into the move-map and TSV — no further sign-off needed:

| Dive | Home (confirmed) | Note |
|---|---|---|
| `1896-1904-hadji-murat` | `works/fiction/novels/` | Johan's call: a short **novel**, not a novella. |
| `1894-1896-the-christian-teaching` | `works/non-fiction/treatises/` | Systematic religious teaching. |
| `1901-1902-what-is-religion` | `works/non-fiction/essays-and-criticism/` | Essay. |
| `1900-1910-against-the-death-penalty` | `themes/against-the-death-penalty/` | Cluster of death-penalty essays → `themes/`, date dropped. |
| `1901-1902-the-break-with-the-church` | `themes/break-with-the-church/` | Excommunication cluster → `themes/`, date dropped. |
| `1903-folk-tales` | `themes/folk-tales/` | 5-tale cluster → `themes/`, date dropped. |
| `1905-1906-krug-chtenija-tales` | `themes/krug-chtenija-tales/` | Tales cluster → `themes/`, date dropped. |
| `art-aesthetics-satellites` | `themes/` | Satellite essays around *What Is Art?*. |
| `late-voice-encryption-compression` | `themes/` | Methodology/analysis. |
| `biryukov-biography-editions` | `_meta/` | Source-editions reference (methodology). |

The four cluster-dives are the only **renames** (they drop their date prefix into `themes/`); the bare slugs above are the recommended names — adjust in the TSV if a different slug reads better.

---

## The move-map

**Work-dives → `works/<genre>/<subcat>/` (keep folder name).** ✓ = confirmed against an existing live `works/` page.

| Current `research/<slug>/` | New home |
|---|---|
| `1879-1880-examination-of-dogmatic-theology` | `works/non-fiction/treatises/` |
| `1879-1882-a-confession` | `works/non-fiction/personal-papers/` ✓ |
| `1882-1884-what-i-believe` | `works/non-fiction/treatises/` |
| `1882-1886-what-then-must-we-do` | `works/non-fiction/treatises/` |
| `1884-1886-the-death-of-ivan-ilyich` | `works/fiction/novellas/` |
| `1886-1887-on-life` | `works/non-fiction/treatises/` |
| `1886-1890-the-fruits-of-enlightenment` | `works/plays/comedy/` ✓ |
| `1886-the-power-of-darkness` | `works/plays/drama/` ✓ |
| `1887-1889-the-kreutzer-sonata` | `works/fiction/novellas/` |
| `1889-1899-resurrection` | `works/fiction/novels/` |
| `1889-1904-the-forged-coupon` | `works/fiction/novellas/` |
| `1889-1909-the-devil` | `works/fiction/novellas/` |
| `1890-1893-the-kingdom-of-god-is-within-you` | `works/non-fiction/treatises/` ✓ |
| `1890-1898-father-sergius` | `works/fiction/novellas/` |
| `1893-1894-christianity-and-patriotism` | `works/non-fiction/essays-and-criticism/` |
| `1894-1895-master-and-man` | `works/fiction/novellas/` ✓ |
| `1894-1896-the-christian-teaching` | `works/non-fiction/treatises/` *(JC)* |
| `1896-1904-hadji-murat` | `works/fiction/novels/` |
| `1897-1898-what-is-art` | `works/non-fiction/essays-and-criticism/` ✓ |
| `1900-the-slavery-of-our-times` | `works/non-fiction/treatises/` |
| `1900-the-living-corpse` | `works/plays/drama/` |
| `1901-1902-what-is-religion` | `works/non-fiction/essays-and-criticism/` *(JC)* |
| `1903-1906-on-shakespeare-and-the-drama` | `works/non-fiction/essays-and-criticism/` |
| `1903-after-the-ball` | `works/fiction/short-stories/` |
| `1904-bethink-yourselves` | `works/non-fiction/essays-and-criticism/` ✓ |
| `1908-a-letter-to-a-hindu` | `works/non-fiction/essays-and-criticism/` |
| `1908-i-cannot-be-silent` | `works/non-fiction/essays-and-criticism/` |
| `1908-the-law-of-violence-and-the-law-of-love` | `works/non-fiction/treatises/` |

**Theme-dives → `themes/` (keep folder name).**
`biryukov-sofia-relationship`, `christian`, `christian-anarchism`, `christian-communism-socialism`, `copyright-renunciation`, `crisis`, `doukhobors`, `fire-metaphor`, `free-age-press`, `gospel-translation`, `lords-prayer`, `stories-for-the-people`, `tolstoyanism`, `tolstoyanism-christian-anarchism`, `art-aesthetics-satellites`, and `late-voice-encryption-compression`.
Plus the four cluster-dives, which **rename** (drop their date) into `themes/`: `1900-1910-against-the-death-penalty → against-the-death-penalty`, `1901-1902-the-break-with-the-church → break-with-the-church`, `1903-folk-tales → folk-tales`, `1905-1906-krug-chtenija-tales → krug-chtenija-tales`.

**Reference/planning → `_meta/`.**
`jubilee-edition-tei-corpus`, `tolstoy-in-art`, `tolstoy-in-photographs`, `biryukov-biography-editions` *(JC)*, and the loose files: `pss-volume-mapping.{md,html}`, `tolstoydigital-tei-reference.{md,html}`, every `_*.md` / `_*.html` (the `_grounding-*`, `_handoff-*`, `_interactive-edition-*`, `_prophet-period-*`, `_research-index-plan` plans).

**Stays at `research/` root (build machinery — do NOT move).** `lib/`, `visualizations/`, `evidence-index/`, `.omc/`, and `index.html` (the generated research door).
> **Spec refinement (flag for Johan):** the spec put `lib/` + `visualizations/` under `_meta/`. Keeping them at the root is the safer call — they're referenced by stable path in serve.py and the generators skip them for free once the globs target `works/`+`themes/`. This avoids rewriting ~6 serve.py path constants and the public `/research/visualizations/` URL. Net effect: serve.py needs a **one-line** change, not six.

---

### Task 1: Author and commit the move-map

**Files:**
- Create: `docs/research/_meta/move-map.tsv`

The map is a two-column TSV: current path → **full** destination path (dir **plus** final folder name), both relative to `docs/research/`. Using the full path makes the four cluster-dive **renames** explicit (they drop their date prefix into `themes/`). The mover and the link-rewriter both read it, so it is the single source of truth.

- [ ] **Step 1: Create `_meta/` and write the map**

```bash
mkdir -p docs/research/_meta
```

Write `docs/research/_meta/move-map.tsv` with one line per folder from the move-map above, e.g.:

```
1879-1882-a-confession	works/non-fiction/personal-papers/1879-1882-a-confession
1886-the-power-of-darkness	works/plays/drama/1886-the-power-of-darkness
1889-1899-resurrection	works/fiction/novels/1889-1899-resurrection
1896-1904-hadji-murat	works/fiction/novels/1896-1904-hadji-murat
doukhobors	themes/doukhobors
tolstoyanism	themes/tolstoyanism
1900-1910-against-the-death-penalty	themes/against-the-death-penalty
1901-1902-the-break-with-the-church	themes/break-with-the-church
1903-folk-tales	themes/folk-tales
1905-1906-krug-chtenija-tales	themes/krug-chtenija-tales
jubilee-edition-tei-corpus	_meta/jubilee-edition-tei-corpus
pss-volume-mapping.md	_meta/pss-volume-mapping.md
_prophet-period-nonfiction-dives.md	_meta/_prophet-period-nonfiction-dives.md
```

(Full list = every row of the move-map. Keep-name rows repeat the folder name in the destination; the four cluster rows are the only renames. Infra that stays at root is NOT listed.)

- [ ] **Step 2: Sanity-check the map covers everything moveable**

```bash
python3 - <<'PY'
import os
root="docs/research"
stay={"lib","visualizations","evidence-index",".omc","index.html","_meta"}
mapped=set()
for ln in open(f"{root}/_meta/move-map.tsv"):
    ln=ln.strip()
    if ln: mapped.add(ln.split("\t")[0])
present={d for d in os.listdir(root) if d not in stay}
missing=present-mapped
print("UNMAPPED (should be empty):", sorted(missing))
PY
```

Expected: `UNMAPPED (should be empty): []`. If not, add the missing rows.

- [ ] **Step 3: Commit**

```bash
git add docs/research/_meta/move-map.tsv
git commit -m "research move: authoritative folder move-map"
```

---

### Task 2: Move the folders

**Files:**
- Create: `docs/research/{works,themes,wiki}/…` (destination tree)
- Move: every folder named in the move-map

**Interfaces:**
- Consumes: `docs/research/_meta/move-map.tsv` (Task 1)
- Produces: the new tree. Every dive now lives at `research/<dest>/<name>/`.

- [ ] **Step 1: Create the empty `wiki/` home (with a keep-file so git tracks it)**

```bash
mkdir -p docs/research/wiki
printf '# research/wiki/\n\nShared, accreting entity pages (one per person/concept). Populated during the ingestion workflow, not the move. See the design spec.\n' > docs/research/wiki/README.md
```

- [ ] **Step 2: Run the mover (git mv each mapped folder into its dest)**

```bash
python3 - <<'PY'
import os, subprocess
root="docs/research"
for ln in open(f"{root}/_meta/move-map.tsv"):
    ln=ln.strip()
    if not ln: continue
    src, dest = ln.split("\t")          # dest = full new path incl. final name
    os.makedirs(os.path.dirname(f"{root}/{dest}"), exist_ok=True)
    subprocess.run(["git","mv",f"{root}/{src}",f"{root}/{dest}"], check=True)
    print(f"moved {src} -> {dest}")
PY
```

- [ ] **Step 3: Verify the tree shape and that no dive is left at the root**

```bash
python3 -c "import os; r='docs/research'; print(sorted(d for d in os.listdir(r) if os.path.isdir(f'{r}/{d}')))"
# Expected top-level dirs: _meta, evidence-index, lib, themes, visualizations, wiki, works (+ .omc)
find docs/research/works -mindepth 3 -maxdepth 3 -type d | wc -l   # ~28 work-dives
```

Expected: no `NNNN-*` or bare theme folders remain directly under `docs/research/`.

- [ ] **Step 4: Commit**

```bash
git add -A docs/research
git commit -m "research move: relocate dives into works/ themes/ wiki/ _meta/"
```

---

### Task 3: Fix the three index generators

All three walk `RESEARCH.glob("*/dossier.yaml")` (one level) and build `research/<slug>/index.html` hrefs. Point the walk at `works/` + `themes/` and compute the href from the file's real location. `_meta/`, `lib/`, `visualizations/`, `evidence-index/` are then excluded automatically.

**Files:**
- Modify: `docs/research/lib/build_research_index.py` (globs ~175, 177; href ~200)
- Modify: `docs/reader/lib/build_works_tracker.py` (globs ~273, 572; `diveHref` ~97)
- Modify: `docs/research/lib/build_evidence_index.py` (its `<slug>/dossier.yaml` walk)

**Interfaces:**
- Consumes: the moved tree (Task 2)
- Produces: regenerated `docs/research/index.html`, `docs/reader/index.html`, `docs/research/evidence-index/*` with correct nested links.

- [ ] **Step 1: Add a shared dive-discovery helper to each generator**

Replace each `research_dir.glob("*/dossier.yaml")` (and the matching `*/index.md`) with a nested walk. In `build_research_index.py`, where it currently does:

```python
for p in research_dir.glob("*/dossier.yaml"):
    ...
```

use:

```python
def _dive_dossiers(research_dir):
    yield from research_dir.glob("works/*/*/*/dossier.yaml")
    yield from research_dir.glob("themes/*/dossier.yaml")

for p in _dive_dossiers(research_dir):
    ...
```

- [ ] **Step 2: Compute href from the dossier's real location, not the bare slug**

Where it builds the link (currently `href = f"{slug}/index.html"`), use the path relative to the research root:

```python
rel = p.parent.relative_to(research_dir)          # e.g. works/fiction/novels/1889-1899-resurrection
href = f"{rel}/index.html" if (p.parent / "index.html").exists() else None
```

Apply the same two changes in `build_works_tracker.py` (`diveHref = f"research/{rel}/index.html"`, and drop the `slug = dossier.parent.name` assumption — use `rel` for the href, keep `dossier.parent.name` only where a display name is wanted) and in `build_evidence_index.py`.

- [ ] **Step 3: Regenerate all three and check the emitted links are nested**

```bash
python3 docs/research/lib/build_research_index.py
python3 docs/reader/lib/build_works_tracker.py
python3 docs/research/lib/build_evidence_index.py
rg -c 'href="research/(works|themes)/' docs/reader/index.html   # > 0
rg -n 'href="research/[0-9]{4}-' docs/reader/index.html docs/research/index.html   # expected: NO matches
```

Expected: reader/research index links now read `research/works/…` / `research/themes/…`; zero old flat `research/NNNN-…` links.

- [ ] **Step 4: Commit**

```bash
git add docs/research/lib docs/reader/lib docs/research/index.html docs/reader/index.html docs/research/evidence-index
git commit -m "research move: point index generators at works/ + themes/ tree"
```

---

### Task 4: Fix serve.py dive-routing

**Files:**
- Modify: `docs/serve.py:364`

serve.py finds a work's dive for the reader breadcrumb with a one-level glob that now misses the nested dives.

**Interfaces:**
- Consumes: the moved tree (Task 2)
- Produces: working "up" breadcrumb from a reader edition to its dive.

- [ ] **Step 1: Make the routing glob recurse**

Change:

```python
dive = next(ROOT.glob(f"research/*-{work}/index.md"), None)
```

to:

```python
dive = next(ROOT.glob(f"research/works/**/*-{work}/index.md"), None)
```

(Work-dives live under `works/`; `**` spans the genre/subcat levels.)

- [ ] **Step 2: Verify a reader breadcrumb resolves**

Start serve.py (via the `docs` launch proxy, memory `reference_docs_preview_proxy`) and load the Great Sin reader page; confirm the top-bar "up" link points at the dive's new `research/works/non-fiction/essays-and-criticism/1905-the-great-sin/index.html` (or the overview, which takes precedence). No 404 in `preview_logs`.

- [ ] **Step 3: Commit**

```bash
git add docs/serve.py
git commit -m "research move: recurse serve.py dive-routing glob into works/"
```

---

### Task 5: Rewrite hard-coded links in parent-repo prose + the reader bundle

**Files:**
- Modify: `AGENTS.md`, `TODO.md`, `MANIFEST.md` (current-structure references)
- Modify: `docs/reader/non-fiction/essays-and-criticism/the-great-sin/alignment-notes.md`
- Leave as-is: `LOG.md` and everything under `docs/superpowers/specs|plans/` **except this plan** — those are dated records of past state; rewriting them would falsify history.

**Interfaces:**
- Consumes: `move-map.tsv` (Task 1) for the old→new path mapping.

- [ ] **Step 1: Rewrite `docs/research/<oldslug>` → `docs/research/<dest>/<oldslug>` across the target files**

```bash
python3 - <<'PY'
import re
pairs=[]
for ln in open("docs/research/_meta/move-map.tsv"):
    ln=ln.strip()
    if not ln: continue
    src,dest=ln.split("\t")
    if "." in src.split("/")[-1]:  # a loose file, not a dive dir
        continue
    pairs.append((src, dest))          # dest = full new path (handles renames)
pairs.sort(key=lambda p: -len(p[0]))   # longest-first so no partial clobber
targets=["AGENTS.md","TODO.md","MANIFEST.md",
         "docs/reader/non-fiction/essays-and-criticism/the-great-sin/alignment-notes.md"]
for t in targets:
    s=open(t).read(); o=s
    for old,new in pairs:
        s=s.replace(f"research/{old}", f"research/{new}")
    if s!=o:
        open(t,"w").write(s); print("rewrote", t)
PY
```

- [ ] **Step 2: Verify no stale flat path remains in the targets**

```bash
rg -n 'research/(1[89][0-9]{2}|christian|doukhobors|tolstoyanism|free-age-press|crisis|fire-metaphor|copyright-renunciation|gospel-translation|lords-prayer|stories-for-the-people)' AGENTS.md TODO.md MANIFEST.md docs/reader/non-fiction/essays-and-criticism/the-great-sin/alignment-notes.md
```

Expected: no matches (every hit now carries a `works/`/`themes/`/`_meta/` segment).

- [ ] **Step 3: Commit**

```bash
git add AGENTS.md TODO.md MANIFEST.md docs/reader
git commit -m "research move: update parent-repo prose + reader-bundle links"
```

---

### Task 6: Rewrite blog-post links (website submodule — separate repo)

**Files:**
- Modify: ~30 files under `website/src/posts/notes/*.md` that link to `docs/research/<slug>/`

Two link forms appear: a GitHub blob URL (`…/blob/main/docs/research/doukhobors/index.md`) and a relative repo path (`../../../../docs/research/1905-the-great-sin/index.md`). Both embed the flat slug.

**Interfaces:**
- Consumes: `move-map.tsv` (parent repo) for the mapping.

- [ ] **Step 1: Rewrite `docs/research/<oldslug>` → `docs/research/<dest>/<oldslug>` in the blog posts**

```bash
python3 - <<'PY'
import re, glob
pairs=[]
for ln in open("docs/research/_meta/move-map.tsv"):
    ln=ln.strip()
    if not ln: continue
    src,dest=ln.split("\t")
    if "." in src.split("/")[-1]: continue
    pairs.append((src, dest))          # dest = full new path (handles renames)
pairs.sort(key=lambda p: -len(p[0]))
for t in glob.glob("website/src/posts/notes/*.md"):
    s=open(t).read(); o=s
    for old,new in pairs:
        s=s.replace(f"docs/research/{old}", f"docs/research/{new}")
    if s!=o:
        open(t,"w").write(s); print("rewrote", t)
PY
```

- [ ] **Step 2: Verify no stale flat path remains in the posts**

```bash
rg -n 'docs/research/(1[89][0-9]{2}|christian|doukhobors|tolstoyanism|free-age-press|crisis|fire-metaphor|copyright-renunciation|gospel-translation|lords-prayer|stories-for-the-people|art-aesthetics-satellites|biryukov)' website/src/posts/notes/
```

Expected: no matches.

- [ ] **Step 3: Commit inside the submodule (submodule-first push discipline)**

```bash
git -C website add src/posts/notes
git -C website commit -m "research move: update dev-blog links to new research tree paths"
```

> The parent repo will now show `M website` (new submodule pointer). That is committed in Task 7 after the whole move verifies, and pushed submodule-first per `reference_push_command_sequence`.

---

### Task 7: Full verification pass

**Files:**
- Modify: parent-repo submodule pointer (`website`) — final commit only.

- [ ] **Step 1: No dangling flat dive-path anywhere active**

```bash
rg -n 'research/(1[89][0-9]{2}-[a-z]|christian/|doukhobors/|tolstoyanism/|free-age-press/|crisis/|fire-metaphor/|gospel-translation/|lords-prayer/|stories-for-the-people/)' \
  --glob '!docs/research/**' --glob '!LOG.md' --glob '!docs/superpowers/specs/**' --glob '!docs/superpowers/plans/**'
```

Expected: no matches (historical records and the moved tree itself are excluded).

- [ ] **Step 2: The reader test suite passes**

```bash
python3 -m pytest docs/tests/test_reader.py -q
```

Expected: PASS. If it asserts on dive paths, update the fixtures to the new tree and re-run.

- [ ] **Step 3: serve.py boots and the three doors render**

Start serve.py via the `docs` proxy; load `/research/index.html`, `/reader/index.html`, and one moved dive (`/research/works/fiction/novels/1889-1899-resurrection/index.html`). Check `preview_logs` for zero 404s and that index links resolve.

- [ ] **Step 4: Final commit (parent repo, incl. submodule pointer)**

```bash
git add -A
git commit -m "research move: bump website submodule pointer + regenerated indexes"
```

- [ ] **Step 5: Hand Johan the push sequence** (submodule first, then parent — memory `reference_push_command_sequence`). Do not push.

---

## Self-review

- **Spec coverage:** works/themes/wiki/_meta tree (Tasks 1–2); one-entity-one-page `wiki/` created empty, populated later (Task 2 step 1, per spec scope boundary); naming convention (Global Constraints + move-map); the flagged migration cost — reader links, INDEX.html, serve.py routing — all covered (Tasks 3–6). The `_meta` refinement (lib/visualizations stay at root) is called out for Johan.
- **Placeholder scan:** none — every generator change shows the before/after; every verification is a runnable command with an expected result. The `(JC)` rows are deliberate editorial confirmations, resolved in Pre-flight, not plan gaps.
- **Consistency:** `move-map.tsv` is the one source both the mover (Task 2) and both rewriters (Tasks 5–6) read; hrefs are always computed from a dossier's real location (Task 3), never a bare slug.
- **INDEX.html:** regenerated by serve.py's build on next run (it walks the docs tree, not the flat dive list) — no manual edit; expect it to re-dirty its timestamp as usual.
