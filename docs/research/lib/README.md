# docs/research/lib — shared research tooling

Canonical tooling for `corpus-dive` and the `docs/research/` thematic sweeps.

- **`extract_tei.py`** — resolves tolstoydigital-TEI editorial markup into grep-able Russian
  prose. Usage: `python3 extract_tei.py <path-to-xml> [substring]`. Requires `lxml`.
  This is the canonical copy; dives reference it rather than forking it.
- **`corpus-dive-queue.sh`** — overnight queue runner for `corpus-dive` (not yet created; see the skill and the plan).

## Forked copies to reconcile later (not done here)

Four dives carry their own `extract_tei.py` predating this canonical copy:
`copyright-renunciation/`, `christian-communism-socialism/`, `doukhobors/`,
`tolstoyanism-christian-anarchism/`. Reconciling them against this copy is a separate
cleanup task (see `docs/superpowers/specs/2026-05-29-corpus-dive-design.md`, §17).
