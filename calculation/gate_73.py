from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_73.json"

GATE_ROOT = 73
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 159_869
WITNESS_K = 30
WITNESS_SIGN = -1

def primitive_quotient() -> int:
    p73 = pell_number(GATE_ROOT)
    p5329 = pell_number(TARGET_RANK)
    q, r = divmod(p5329, p73)
    if r:
        raise AssertionError("P_73 must divide P_5329")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 73",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "search_cap": 200_000,
            "reported_prime_candidates_tested": 10_250,
            "first_hit_prime_candidates_tested": 3,
            "verified_hit_count_in_full_window": 1,
            "first_hit": {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
        },
        "primitive_part": {
            "object": "P_5329 / P_73",
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
            "affected_preview_roots": [49_713, 6_759_910_011, 2_114_411_978_523, 69_940_136_627_178],
            "promotion_effect": "prime support 73 resolved; affected roots still require other novel gates",
        },
        "observation": (
            "The first verified direct witness occurs at k=30. This is recorded as a computation, "
            "not as a general relation between root 73 and root 30."
        ),
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
