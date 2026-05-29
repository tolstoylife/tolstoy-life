# docs/research/lib — shared research tooling

Canonical tooling for `corpus-dive` and the `docs/research/` thematic sweeps.

- **`extract_tei.py`** — resolves tolstoydigital-TEI editorial markup into grep-able Russian
  prose. Usage: `python3 extract_tei.py <path-to-xml> [substring]`. Requires `lxml`.
  This is the canonical copy; dives reference it rather than forking it.
- **`corpus-dive-queue.sh`** — overnight queue runner for `corpus-dive`. Spawns a fresh `claude -p` session per theme; skips blank lines and `#` comments; writes a batch summary to `docs/research/_batch-YYYY-MM-DD.md`. Pass `--skip-permissions` to append `--dangerously-skip-permissions` to each invocation (opt-in, OFF by default; required for truly unattended runs). Use `--dry-run` to print commands without executing. Usage: `corpus-dive-queue.sh --themes <file> [--model <tier>] [--skip-permissions] [--dry-run]`.
  Headless invocation probe (2026-05-29): `claude -p "/corpus-dive <theme> --auto" --model haiku` — skill IS found and triggered, arg-parsing works (EXIT=0, stub OK line printed), but the run pauses for interactive write-permission confirmation before creating any file. Without `--skip-permissions` (or a `.claude/settings.json` allow-list), real runs will stall.

## Forked copies to reconcile later (not done here)

Four dives carry their own `extract_tei.py` predating this canonical copy:
`copyright-renunciation/`, `christian-communism-socialism/`, `doukhobors/`,
`tolstoyanism-christian-anarchism/`. Reconciling them against this copy is a separate
cleanup task (see `docs/superpowers/specs/2026-05-29-corpus-dive-design.md`, §17).
