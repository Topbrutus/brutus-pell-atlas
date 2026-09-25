from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_211_primitive.json"

INDEX = 211 * 211
DIVISOR_INDEX = 211

def pell_number(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, 2 * b + a
    return a

def build_report() -> dict:
    sys.set_int_max_str_digits(0)
    p211 = pell_number(DIVISOR_INDEX)
    p44521 = pell_number(INDEX)
    primitive, remainder = divmod(p44521, p211)
    primitive_text = str(primitive)
    return {
        "name": "Gate 211 Pell primitive part",
        "index": INDEX,
        "divisor_index": DIVISOR_INDEX,
        "identity": "primitive_part = P_44521 / P_211",
        "division_exact": remainder == 0,
        "P_211_digits": len(str(p211)),
        "P_44521_digits": len(str(p44521)),
        "primitive_digits": len(primitive_text),
        "primitive_sha256": hashlib.sha256(primitive_text.encode()).hexdigest(),
        "primitive_prefix_80": primitive_text[:80],
        "primitive_suffix_80": primitive_text[-80:],
        "gcd_primitive_P_211": math.gcd(primitive, p211),
        "primitive_mod_211": primitive % 211,
        "P_211_mod_211": p211 % 211,
        "classification": "EXACT_COMPUTATION",
        "factorization_status": "UNFACTORED_PRIMITIVE_PART",
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    print(f"index = {report['index']}")
    print(f"primitive_digits = {report['primitive_digits']}")
    print(f"division_exact = {report['division_exact']}")
    print(f"gcd_primitive_P_211 = {report['gcd_primitive_P_211']}")
    print(f"sha256 = {report['primitive_sha256']}")
    print(f"status = {report['factorization_status']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
