#!/usr/bin/env bash
set -euo pipefail

BASE="$HOME/tools/gmp-ecm-local"
LIB="$BASE/usr/lib/x86_64-linux-gnu"
BIN="$BASE/usr/bin/ecm"
IN="$BASE/P54289_primitive.txt"
OUT="$BASE/gate233_pm1.log"

set +e
LD_LIBRARY_PATH="$LIB" "$BIN" -q -pm1 -go 54289 50000 10000000 < "$IN" > "$OUT" 2>&1
code=$?
set -e

echo "$code" > "$BASE/gate233_pm1.status"
echo "EXIT=$code"
head -c 1000 "$OUT"
echo
