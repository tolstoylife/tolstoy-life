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
  Headless invocation probe (2026-05-29): `claude -p "/corpus-dive <theme> --auto" --model haiku` — skill IS found and triggered, arg-parsing works (EXIT=0, stub OK line printed), but the run pauses for interactive write-permission confirmation before creating any file. Without `--skip-permissions` (or a `.claude/settings.json` allow-list), real runs will stall.

## Forked copies (kept byte-identical; structural dedup still pending)

Four dives carry their own `extract_tei.py` predating this canonical copy:
`copyright-renunciation/`, `christian-communism-socialism/`, `doukhobors/`,
`tolstoyanism-christian-anarchism/`. They are byte-identical to this copy and are
re-synced whenever the canonical extractor changes (the note-body recovery above was
copied into all four), so the fix is live wherever the dives actually run.
Replacing the four forks with a reference to this single canonical copy — so there is
nothing left to sync — remains a separate cleanup task
(see `docs/superpowers/specs/2026-05-29-corpus-dive-design.md`, §17).
