#!/usr/bin/env bash
# Test corpus-dive-queue.sh --dry-run command generation.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
RUNNER="$HERE/corpus-dive-queue.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

cat > "$TMP/themes.txt" <<'EOF'
# a comment line, skipped
capital punishment

non-resistance to evil
EOF

# --- Default: no --skip-permissions ---
OUT="$("$RUNNER" --dry-run --model sonnet --themes "$TMP/themes.txt")"
echo "$OUT"
[ "$(printf '%s\n' "$OUT" | grep -c '^claude -p ')" -eq 2 ] || { echo "FAIL: expected 2 commands"; exit 1; }
printf '%s\n' "$OUT" | grep -- '--model sonnet' | grep -q 'capital' || { echo "FAIL: theme 1 missing"; exit 1; }
printf '%s\n' "$OUT" | grep -q 'non-resistance' || { echo "FAIL: theme 2 missing"; exit 1; }
if printf '%s\n' "$OUT" | grep -q 'dangerously-skip-permissions'; then echo "FAIL: skip-perms leaked without the flag"; exit 1; fi

# --- With --skip-permissions ---
OUT2="$("$RUNNER" --dry-run --model sonnet --skip-permissions --themes "$TMP/themes.txt")"
echo "$OUT2"
[ "$(printf '%s\n' "$OUT2" | grep -c -- '--dangerously-skip-permissions')" -eq 2 ] || { echo "FAIL: expected --dangerously-skip-permissions on both"; exit 1; }

# --- Safety: a theme with shell metacharacters must NOT expand/execute ---
printf '%s\n' 'Tolstoy and $(whoami)' > "$TMP/themes2.txt"
OUT3="$("$RUNNER" --dry-run --themes "$TMP/themes2.txt")"
echo "$OUT3"
printf '%s\n' "$OUT3" | grep -q 'whoami' || { echo "FAIL: metachar theme missing or executed"; exit 1; }

echo "PASS"
