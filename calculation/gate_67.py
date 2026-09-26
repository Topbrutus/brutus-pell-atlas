from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_67.json"

GATE_ROOT = 67
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 454_134_173
WITNESS_K = 101_166
WITNESS_SIGN = -1

def primitive_quotient() -> int:
    p67 = pell_number(GATE_ROOT)
    p4489 = pell_number(TARGET_RANK)
    q, r = divmod(p4489, p67)
    if r:
        raise AssertionError("P_67 must divide P_4489")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 67",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "search_cap": 200_000,
            "reported_prime_candidates_tested": 10_302,
            "first_hit": {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
        },
        "primitive_part": {
            "object": "P_4489 / P_67",
            "decimal_digits": len(str(q)),
            "factor_divides_primitive_quotient": q % WITNESS == 0,
        },
        "explicit_prime_witness": {
            "p": WITNESS,
            "k": WITNESS_K,
            "sign": WITNESS_SIGN,
            "identity_verified": WITNESS == WITNESS_K * TARGET_RANK + WITNESS_SIGN,
            "prime_verified": is_prime_64(WITNESS),
            "exact_rank_verified": exact_rank_target(WITNESS, TARGET_RANK),
        },
        "level3_role": {
            "affected_preview_roots": [2_989_473, 7_624_533, 85_683_303_492],
            "promotion_effect": "prime support 67 resolved; affected roots still require other novel gates",
        },
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    w = report["explicit_prime_witness"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"witness = {WITNESS}")
    print(f"k = {WITNESS_K}")
    print(f"prime_verified = {w['prime_verified']}")
    print(f"exact_rank_verified = {w['exact_rank_verified']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
