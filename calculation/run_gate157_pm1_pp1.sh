#!/usr/bin/env bash
set -euo pipefail

BASE="$HOME/tools/gmp-ecm-local"
BIN="$BASE/usr/bin/ecm"
LIB="$BASE/usr/lib/x86_64-linux-gnu"
IN="$BASE/P24649_primitive.txt"
OUTDIR="$BASE/gate157-pm1pp1"

mkdir -p "$OUTDIR"
export LD_LIBRARY_PATH="$LIB"

run_method() {
  method="$1"
  tag="$2"
  echo "--- $tag ---"
  set +e
  "$BIN" -q "$method" -go 24649 -c 8 100000 10000000 < "$IN" > "$OUTDIR/$tag.out" 2> "$OUTDIR/$tag.err"
  code=$?
  set -e
  echo "$code" > "$OUTDIR/$tag.status"
  echo "$tag exit=$code"
}

run_method -pm1 pm1
run_method -pp1 pp1

python3 - <<'PY'
from pathlib import Path
base=Path.home()/"tools/gmp-ecm-local"
q=(base/"P24649_primitive.txt").read_text().strip()
d=base/"gate157-pm1pp1"
for tag in ("pm1","pp1"):
    out=(d/f"{tag}.out").read_text().strip()
    code=(d/f"{tag}.status").read_text().strip()
    print(tag,"status",code,"sameQ",out==q,"len",len(out))
    if out and out!=q:
        print("CANDIDATE_OUTPUT",out[:1000])
PY
