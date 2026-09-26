#!/usr/bin/env bash
set -euo pipefail
BASE="$HOME/tools/gmp-ecm-local"
LIB="$BASE/usr/lib/x86_64-linux-gnu"
BIN="$BASE/usr/bin/ecm"
IN="$BASE/P24649_primitive.txt"
OUT="$BASE/gate157_pm1.log"

set +e
LD_LIBRARY_PATH="$LIB" "$BIN" -pm1 -go 24649 50000 10000000 < "$IN" > "$OUT" 2>&1
code=$?
set -e
echo "$code" > "$BASE/gate157_pm1.status"
echo "EXIT=$code" >> "$OUT"
tail -40 "$OUT"
