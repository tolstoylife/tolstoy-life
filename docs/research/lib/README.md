# docs/research/lib — shared research tooling

Canonical tooling for `corpus-dive` and the `docs/research/` thematic sweeps.

- **`extract_tei.py`** — resolves tolstoydigital-TEI editorial markup into grep-able Russian
  prose. Usage: `python3 extract_tei.py <path-to-xml> [substring] [--notes=auto|off|force]`.
  Requires `lxml`. This is the canonical copy; dives reference it rather than forking it.
  - **Note-encoded body recovery.** Most documents carry their text in `<p>` body elements,
    with `<note>`/`<noteGrp>` holding footnotes that are stripped. A handful of PSS documents
    instead encode the document's *own* text inside `<noteGrp type="comments">` (the body has
    no `<p>` at all) — e.g. the 1910 Explanatory Note to Tolstoy's will (`v82_305`, PSS Tom 82
    pp. 227–231), which otherwise extracted to the opener alone. `--notes=auto` (the default)
    recovers that text **only when the body has no real `<p>`/`<closer>` prose**, so a normal
    extraction can never be polluted with its footnotes; corpus-wide, `auto` changes the output
    of exactly 3 files (`v82_305`, `v78_174`, `v78_177`). Genuine nested footnotes (e.g.
    `<note resp="volume_editor" xml:id="…">`) are still stripped. Recovered paragraphs are
    tagged `[note]` and announced by a `# note-body:` banner — they mix the document's own text
    with editorial commentary, so verify against the source PDF. `--notes=off` forces the legacy
    strip-everything behaviour; `--notes=force` additionally dumps the comments apparatus after a
    normal body (for reading the editorial commentary).
- **`verify_quotes.py`** — mechanical byte-fidelity gate for a dive's dossier. Loads every
  `evidence[].quoteRu`, opens the named `extract` file, and asserts the (whitespace-normalised)
  quote appears **verbatim** in it — turning Phase 5's core credibility check into one deterministic
  command instead of an LLM judgement call. Also checks declared `facsimile:` files exist and warns
  (soft) when a `quoteEn` lacks the `(working English)` label. Honours author elision marks:
  leading/trailing ellipsis (mid-sentence excerpt, bare or bracketed) is stripped before matching;
  an internal `[…]`/`[...]` splits the quote into fragments that must each appear, in order — but a
  bare internal `…` stays literal (it can be Tolstoy's own). A mismatch report names the exact
  diverging word. Requires `PyYAML`. Usage: `python3 docs/research/lib/verify_quotes.py
  docs/research/<slug>/dossier.yaml [--quiet]`. Exit 0 = PASS, 1 = FAIL (mismatch or missing
  facsimile), 2 = usage/parse error.
- **`build_evidence_index.py`** — cross-dive aggregator. Walks every `docs/research/*/dossier.yaml`
  and emits an entity-keyed evidence index so wiki ingestion reuses verified research instead of
  re-collating it across dives (the same entity recurs in many dives — Chertkov in all five). For
  each entity (keyed by the slug of `wikilinkTarget`, == the eventual wiki/works slug) it resolves
  that dive's `evidenceRefs` to full evidence rows qualified by dive, collates and de-dupes visuals
  (by `url`, so the same image cached under different per-dive paths merges with an `alsoInDives`
  list), unions sources, and **re-derives `vaultStatus` live** against `website/src/wiki/` and
  `website/src/works/` (stub = prose body < 60 words, or a `draft` < 120). Writes
  `docs/research/evidence-index/evidence-index.yaml` (machine) + `index.md` (human; renders to
  `index.html` via `serve.py --build-only`). A `lint` block flags unresolved `evidenceRefs`,
  name/`wikiType` conflicts (e.g. Birukoff/Biryukov, Maude person/translator), works-routed-not-wiki,
  vaultStatus drift, and zero-evidence research gaps. Output is deterministic (byte-identical on
  rebuild). Requires `PyYAML`. Usage: `python3 docs/research/lib/build_evidence_index.py [--check]
  [--quiet] [--research-dir PATH]`. Exit 0 = built (or `--check` clean), 1 = `--check` found broken
  links (unresolved refs), 2 = usage/parse error.
- **`test-verify-quotes.sh`** — regression check for the above: asserts a clean quote passes, a
  tampered body fails, a boundary-ellipsis excerpt passes, a valid internal `[...]` elision passes,
  and a corruption hidden behind an elision still fails. Run: `bash test-verify-quotes.sh` (prints `PASS`).
- **`test-extract-tei.sh`** — regression check for the above: asserts `v82_305` recovers the
  operative will provision and the recovery banner, that its nested volume-editor footnote stays
  stripped, and that a normal letter (`v78_170`) keeps its body while its editorial apparatus is
  not leaked. Run: `bash test-extract-tei.sh` (prints `PASS`).
- **`test-corpus-dive-queue.sh`** — `--dry-run` command-generation check for the queue runner.
- **`corpus-dive-queue.sh`** — overnight queue runner for `corpus-dive`. Spawns a fresh `claude -p` session per theme; skips blank lines and `#` comments; writes a batch summary to `docs/research/_batch-YYYY-MM-DD.md`. Pass `--skip-permissions` to append `--dangerously-skip-permissions` to each invocation (opt-in, OFF by default; required for truly unattended runs). Use `--dry-run` to print commands without executing. Usage: `corpus-dive-queue.sh --themes <file> [--model <tier>] [--skip-permissions] [--dry-run]`.
  Headless permission behaviour (re-probed 2026-05-29): the skill is found, triggered, and arg-parsing works (EXIT=0). In `claude -p`, a tool that needs permission and isn't allowlisted is **cleanly denied** — the run continues/exits, it does **not** hang — *when the session runs with a controlled posture* (`--setting-sources project` + an `--allowedTools`/settings allow-list); read-only "safe" commands are auto-approved. This script sets no such posture (it inherits your user settings), so for truly unattended batches still pass `--skip-permissions` or supply a `.claude/settings.json` allow-list — otherwise a run may deny the writes the dive needs, or behave per whatever your user permission posture auto-approves.

## Single source of truth (forks removed)

This is the **only** copy of `extract_tei.py`. Four dives
(`copyright-renunciation/`, `christian-communism-socialism/`, `doukhobors/`,
`tolstoyanism-christian-anarchism/`) used to carry byte-identical forks that had to be
re-synced by hand on every change; those forks were deleted and each dive's `index.md`
now links to this copy via a relative path (`../lib/extract_tei.py`). New dives should
reference this file rather than copying it. (Resolves the §17 cleanup in
`docs/superpowers/specs/2026-05-29-corpus-dive-design.md`.)
