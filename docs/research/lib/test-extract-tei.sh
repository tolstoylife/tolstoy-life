#!/usr/bin/env bash
# Test extract_tei.py note-encoded-body recovery + no-pollution guarantee.
#
# Regression target: v82_305 (1910 Explanatory Note to Tolstoy's will, PSS Tom 82
# pp.227-231). Its body is encoded entirely inside <note type="comments"> apparatus
# rather than <p> body elements, so the extractor used to return only the opener.
# The fix must recover that note-encoded primary text WITHOUT pulling genuine
# footnotes into normal extractions.
set -euo pipefail
export PYTHONUTF8=1   # force UTF-8 I/O; a C locale silently drops Cyrillic (see README)

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../../.." && pwd)"
EXTRACT="$HERE/extract_tei.py"
CORPUS="$REPO/primary-sources/tolstoydigital-TEI/texts/letters"

NOTE_DOC="$CORPUS/v82_305_Obyasnitelnayazapiskakzaveshhaniyu.xml"   # note-encoded body
NORMAL_DOC="$CORPUS/v78_170_N_A_SHejermanu.xml"                    # normal body + comments noteGrp

# --- 1. Note-encoded body IS recovered: the operative will provision must appear ---
OUT="$(python3 "$EXTRACT" "$NOTE_DOC")"
printf '%s\n' "$OUT" | grep -q 'Все его сочинения, литературные произведения' \
  || { echo "FAIL: v82_305 operative provision not recovered"; exit 1; }

# --- 2. Recovery is announced, not silent (banner names the apparatus source) ---
printf '%s\n' "$OUT" | grep -qi 'recovered' \
  || { echo "FAIL: v82_305 missing note-body recovery banner"; exit 1; }
printf '%s\n' "$OUT" | grep -q 'noteGrp' \
  || { echo "FAIL: recovery banner should name the noteGrp apparatus source"; exit 1; }

# --- 3. Genuine nested footnote (volume_editor note1, the 1927 committee) stays stripped ---
if printf '%s\n' "$OUT" | grep -q 'Комитет по исполнению воли'; then
  echo "FAIL: v82_305 leaked the nested volume_editor footnote into the body"; exit 1
fi

# --- 4. No pollution: a NORMAL letter's editorial apparatus must NOT leak ---
OUT2="$(python3 "$EXTRACT" "$NORMAL_DOC")"
if printf '%s\n' "$OUT2" | grep -q 'копировальной книге'; then
  echo "FAIL: normal extraction polluted with editorial commentary (noteGrp leaked)"; exit 1
fi

# --- 5. The normal letter's real <p> body is still extracted intact ---
printf '%s\n' "$OUT2" | grep -q 'Давно уже получил ваше письмо' \
  || { echo "FAIL: normal letter body went missing"; exit 1; }

echo "PASS"
