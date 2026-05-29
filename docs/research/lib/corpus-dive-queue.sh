#!/usr/bin/env bash
# corpus-dive overnight queue runner.
# Spawns a FRESH `claude -p` session per theme (clean context per dive), continues on failure,
# writes a combined batch summary. See .claude/skills/corpus-dive/SKILL.md and design spec §13.
#
# Usage:
#   corpus-dive-queue.sh --themes <file> [--model <tier>] [--skip-permissions] [--dry-run]
#
# themes file: one theme per line; blank lines and lines starting with # are ignored.
#
# --skip-permissions appends Claude's `--dangerously-skip-permissions` to each invocation so the
#   run does not stall on write-permission prompts. REQUIRED for true unattended/overnight use
#   (or configure a .claude/settings.json allow-list instead). It disables ALL permission prompts
#   for that headless process — use deliberately.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
THEMES="" ; MODEL="" ; DRY_RUN=0 ; SKIP_PERMS=0
DATE="$(date +%F)"

while [ $# -gt 0 ]; do
  case "$1" in
    --themes) THEMES="$2"; shift 2 ;;
    --model)  MODEL="$2";  shift 2 ;;
    --skip-permissions) SKIP_PERMS=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) tail -n +2 "$0" | grep '^#' | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [ -z "$THEMES" ] || [ ! -f "$THEMES" ]; then
  echo "Need --themes <existing file>" >&2; exit 2
fi

if [ "$DRY_RUN" -eq 0 ] && [ "$SKIP_PERMS" -eq 0 ]; then
  echo "WARNING: running for real without --skip-permissions; dives will stall on permission prompts unless a .claude/settings.json allow-list covers them." >&2
fi

SUMMARY="$REPO_ROOT/docs/research/_batch-$DATE.md"
if [ "$DRY_RUN" -eq 0 ]; then printf '# corpus-dive batch — %s\n\n' "$DATE" > "$SUMMARY"; fi

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

while IFS= read -r line || [ -n "$line" ]; do
  case "$line" in ''|\#*) continue ;; esac
  theme="$line"

  cmd_args=(-p "/corpus-dive $theme --auto")
  if [ -n "$MODEL" ]; then cmd_args+=(--model "$MODEL"); fi
  if [ "$SKIP_PERMS" -eq 1 ]; then cmd_args+=(--dangerously-skip-permissions); fi

  if [ "$DRY_RUN" -eq 1 ]; then
    printf 'claude'; printf ' %q' "${cmd_args[@]}"; printf '\n'
    continue
  fi

  slug="$(slugify "$theme")"
  [ -n "$slug" ] || slug="untitled"
  echo ">>> $(date +%T) dive: $theme"
  if claude "${cmd_args[@]}"; then status="ok"; else status="FAILED"; fi
  printf -- '- **%s** — %s — [run-report](%s)\n' \
    "$theme" "$status" "docs/research/$slug/run-report.md" >> "$SUMMARY"
done < "$THEMES"

if [ "$DRY_RUN" -eq 0 ]; then echo "Batch summary: $SUMMARY"; fi
