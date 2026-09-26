from __future__ import annotations

import json
import sys
from pathlib import Path

from calculation.mirror_frontier import pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_113_status.json"

GATE_ROOT = 113
TARGET_RANK = GATE_ROOT * GATE_ROOT

DIRECT_SCAN = {
    "start_k": 1,
    "end_k": 200_000,
    "prime_candidates_tested": 9_828,
    "hits": [],
}

COMPILED_SCAN = {
    "implementation": "calculation/gate_scan_compiled.c",
    "start_k": 1,
    "end_k": 10_000_000_000,
    "small_prime_sieve_survivors": 496_329_793,
    "pell_divisibility_hits": 0,
    "prime_hits": 0,
}
FACTORIZATION_ATTEMPTS = [
    {
        "method": "P-1",
        "B1": 50_000,
        "effective_B2": 14_856_276,
        "runs": 10,
        "factor_found": False,
    },
    {
        "method": "P+1",
        "B1": 50_000,
        "effective_B2": 19_411_780,
        "runs": 10,
        "factor_found": False,
    },
    {
        "method": "ECM",
        "B1": 250_000,
        "B2": 40_000_000,
        "curves": 12,
        "factor_found": False,
        "output_check": (
            "all 12 normalized outputs equal the input primitive quotient"
        ),
    },
]

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_113 must divide P_12769")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 113 Status",
        "status": "HARD_UNRESOLVED",
        "frontier_class": "DEEP_COMPUTATIONAL_FRONTIER",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "compiled_pell_scan": {
            **COMPILED_SCAN,
            "largest_candidate_bound": (
                COMPILED_SCAN["end_k"] * TARGET_RANK + 1
            ),
            "interpretation": (
                "NO_PELL_DIVISIBILITY_HIT_THROUGH_K_1E10"
            ),
        },
        "primitive_part": {
            "object": "P_12769 / P_113",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
        },
        "factorization_attempts": FACTORIZATION_ATTEMPTS,
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": (
                "At least one prime p with z_P(p)=12769 exists."
            ),
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [
                4_743_650_391,
                8_019_668_082,
                72_557_343_957,
            ],
        },
        "boundary": (
            "No hit in bounded scans and no factor in recorded "
            "P-1/P+1/ECM campaigns do not establish nonexistence."
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
    scan = report["compiled_pell_scan"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"compiled_scan_max_k = {scan['end_k']}")
    print(
        "compiled_sieve_survivors = "
        f"{scan['small_prime_sieve_survivors']}"
    )
    print(
        "compiled_pell_hits = "
        f"{scan['pell_divisibility_hits']}"
    )
    print(
        "primitive_digits = "
        f"{report['primitive_part']['decimal_digits']}"
    )
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
