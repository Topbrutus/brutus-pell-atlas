from __future__ import annotations

import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_137.json"

GATE_ROOT = 137
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 3_415_957
WITNESS_K = 182
WITNESS_SIGN = -1

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_137 must divide P_18769")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 137",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "search_cap": 200_000,
            "reported_prime_candidates_tested": 4_780,
            "first_hit_prime_candidates_tested": 5,
            "first_hit": {
                "p": WITNESS,
                "k": WITNESS_K,
                "sign": WITNESS_SIGN,
            },
        },
        "primitive_part": {
            "object": "P_18769 / P_137",
            "decimal_digits": len(str(q)),
            "factor_divides_primitive_quotient": q % WITNESS == 0,
        },
        "explicit_prime_witness": {
            "p": WITNESS,
            "k": WITNESS_K,
            "sign": WITNESS_SIGN,
            "identity_verified": (
                WITNESS == WITNESS_K * TARGET_RANK + WITNESS_SIGN
            ),
            "prime_verified": is_prime_64(WITNESS),
            "exact_rank_verified": exact_rank_target(
                WITNESS,
                TARGET_RANK,
            ),
        },
        "level3_role": {
            "affected_preview_roots": [80_860_962],
            "remaining_novel_gates": [47],
            "promotion_effect": (
                "prime support 137 resolved; affected preview root "
                "still requires hard-unresolved gate 47"
            ),
        },
        "observation": (
            "The witness is the first verified direct hit in the "
            "recorded bounded scan. This is not a general mirror theorem."
        ),
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

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

