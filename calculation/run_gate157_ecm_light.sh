#!/usr/bin/env bash
set -euo pipefail

BASE="$HOME/tools/gmp-ecm-local"
BIN="$BASE/usr/bin/ecm"
LIB="$BASE/usr/lib/x86_64-linux-gnu"
IN="$BASE/P24649_primitive.txt"
OUTDIR="$BASE/gate157-ecm-light"

rm -rf "$OUTDIR"
mkdir -p "$OUTDIR"
export LD_LIBRARY_PATH="$LIB"
export BIN IN OUTDIR

seq 1 12 | xargs -P12 -I{} bash -c '
  id={}
  set +e
  "$BIN" -q -sigma "$((15700000 + id))" 100000 10000000 < "$IN" > "$OUTDIR/$id.out" 2> "$OUTDIR/$id.err"
  code=$?
  echo "$code" > "$OUTDIR/$id.status"
  exit 0
'

python3 - <<'PY'
from pathlib import Path
base=Path.home()/"tools/gmp-ecm-local"
q=(base/"P24649_primitive.txt").read_text().strip()
d=base/"gate157-ecm-light"
different=[]
statuses=[]
for p in sorted(d.glob("*.out"), key=lambda p:int(p.stem)):
    s=p.read_text().strip()
    code=(p.with_suffix(".status")).read_text().strip()
    statuses.append(code)
    print(p.stem,"status",code,"sameQ",s==q,"len",len(s))
    if s and s!=q:
        different.append((p.stem,s))
        print("CANDIDATE_OUTPUT",s[:1000])
print("STATUS_SUMMARY",statuses)
print("DIFFERENT_COUNT",len(different))
PY
