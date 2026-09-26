#!/usr/bin/env bash
set -euo pipefail
BASE="$HOME/tools/gmp-ecm-local"
BIN="$BASE/usr/bin/ecm"
LIB="$BASE/usr/lib/x86_64-linux-gnu"
IN="$BASE/P72361_primitive.txt"
OUT="$BASE/gate269-pm1pp1"
rm -rf "$OUT"
mkdir -p "$OUT"
export LD_LIBRARY_PATH="$LIB"
export BIN IN OUT

for method in pm1 pp1; do
  (
    flag="-${method}"
    set +e
    "$BIN" -q "$flag" -go 72361 -c 4 20000 2000000 < "$IN" > "$OUT/${method}.out" 2> "$OUT/${method}.err"
    code=$?
    set -e
    echo "$code" > "$OUT/${method}.status"
  ) &
done
wait

python3 - <<'PY'
from pathlib import Path
base=Path.home()/"tools/gmp-ecm-local"
q=(base/"P72361_primitive.txt").read_text().strip()
d=base/"gate269-pm1pp1"
for tag in ("pm1","pp1"):
    out=(d/f"{tag}.out").read_text().strip()
    code=(d/f"{tag}.status").read_text().strip()
    print(tag,"status",code,"sameQ",out==q,"len",len(out))
    if out and out!=q:
        print("CANDIDATE",out[:1200])
PY
