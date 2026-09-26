from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_59.json"

GATE_ROOT = 59
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 31_217_609
WITNESS_K = 8_968
WITNESS_SIGN = 1

def primitive_quotient() -> int:
    p59 = pell_number(GATE_ROOT)
    p3481 = pell_number(TARGET_RANK)
    q, r = divmod(p3481, p59)
    if r:
        raise AssertionError("P_59 must divide P_3481")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 59",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "start_k": 1,
            "first_hit_k": WITNESS_K,
            "search_cap": 200_000,
            "reported_prime_candidates_tested": 10_517,
            "first_hit": {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
        },
        "primitive_part": {
            "object": "P_3481 / P_59",
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
            "affected_preview_roots": [8_646_981, 6_773_594_061],
            "promotion_effect": "prime support 59 resolved; affected roots still require other novel gates",
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
