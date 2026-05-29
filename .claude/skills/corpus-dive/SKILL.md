---
name: corpus-dive
description: "STUB — Primary-source research on one theme across the Tolstoy corpus. Triggers on 'corpus dive', 'corpus-dive', 'research X across the corpus/PSS/TEI'."
argument-hint: "<theme> [--auto] [--confirm-scope] [--model <tier>]"
triggers:
  - "corpus dive"
  - "corpus-dive"
---

# corpus-dive (stub)

Parse `{{ARGUMENTS}}`:
- `theme` = everything that is not a flag.
- `--auto` = unattended; `--confirm-scope` = approve-then-detach; `--model <tier>` = baseline.
- `slug` = kebab-case of the theme.

Then, as a stub, do ONLY this:
1. Create the folder `docs/research/<slug>/`.
2. Write `docs/research/<slug>/run-report.md` containing the parsed `theme`, `slug`, and the
   boolean flags, under a heading `# corpus-dive stub run`.
3. Print: `corpus-dive stub OK — theme="<theme>" auto=<bool> model=<tier>`.

Do nothing else. This stub exists only to verify invocation and arg-parsing.
