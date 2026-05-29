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
