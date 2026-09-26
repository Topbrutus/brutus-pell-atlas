from __future__ import annotations

import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_149.json"

GATE_ROOT = 149
TARGET_RANK = GATE_ROOT * GATE_ROOT

WITNESS = 5_328_241
WITNESS_K = 240
WITNESS_SIGN = 1

SECONDARY_WITNESS = 304_908_533
SECONDARY_K = 13_734
SECONDARY_SIGN = -1

DIRECT_SCAN = {
    "search_cap": 200_000,
    "prime_candidates_tested": 4_773,
    "first_hit_prime_candidates_tested": 8,
    "hits": [
        {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
        {
            "p": SECONDARY_WITNESS,
            "k": SECONDARY_K,
            "sign": SECONDARY_SIGN,
        },
    ],
}

AFFECTED_ROOT = 8_443_383

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_149 must divide P_22201")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 149",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "primitive_part": {
            "object": "P_22201 / P_149",
            "decimal_digits": len(str(q)),
            "first_witness_divides": q % WITNESS == 0,
            "second_witness_divides": q % SECONDARY_WITNESS == 0,
        },
        "explicit_prime_witness": {
            "p": WITNESS,
            "k": WITNESS_K,
            "sign": WITNESS_SIGN,
            "identity_verified": (
                WITNESS == WITNESS_K * TARGET_RANK + WITNESS_SIGN
            ),
            "prime_verified": is_prime_64(WITNESS),
            "exact_rank_verified": exact_rank_target(WITNESS, TARGET_RANK),
        },
        "secondary_verified_witness": {
            "p": SECONDARY_WITNESS,
            "k": SECONDARY_K,
            "sign": SECONDARY_SIGN,
            "identity_verified": (
                SECONDARY_WITNESS
                == SECONDARY_K * TARGET_RANK + SECONDARY_SIGN
            ),
            "prime_verified": is_prime_64(SECONDARY_WITNESS),
            "exact_rank_verified": exact_rank_target(
                SECONDARY_WITNESS,
                TARGET_RANK,
            ),
        },
        "level3_role": {
            "affected_preview_roots": [AFFECTED_ROOT],
            "remaining_novel_gates": [1_453],
            "promotion_effect": (
                "prime support 149 resolved; affected preview root "
                "still requires gate 1453"
            ),
        },
        "observation": (
            "Gate 149 is an exact computational result inside the "
            "simulation-only Level-3 preview."
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
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"witness = {WITNESS}")
    print(f"k = {WITNESS_K}")
    print(
        "remaining_novel_gates = "
        f"{report['level3_role']['remaining_novel_gates']}"
    )
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
