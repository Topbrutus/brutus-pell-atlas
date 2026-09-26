from __future__ import annotations

import json
from pathlib import Path

from calculation.mirror_frontier import pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_101_status.json"

GATE_ROOT = 101
TARGET_RANK = GATE_ROOT * GATE_ROOT

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_101 must divide P_10201")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    windows = [
        {
            "start_k": 1,
            "end_k": 1_000_000_000,
            "small_prime_sieve_survivors": 49_278_561,
            "pell_divisibility_hits": 0,
            "prime_hits": 0,
        },
        {
            "start_k": 1_000_000_001,
            "end_k": 10_000_000_000,
            "small_prime_sieve_survivors": 447_475_606,
            "pell_divisibility_hits": 0,
            "prime_hits": 0,
        },
    ]
    return {
        "name": "Brutus-Pell Gate 101 Status",
        "status": "HARD_UNRESOLVED",
        "frontier_class": "DEEP_COMPUTATIONAL_FRONTIER",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "compiled_pell_scan": {
            "implementation": (
                "C/OpenMP exact modular Pell scanner derived from "
                "calculation/gate_47_scan.c"
            ),
            "windows": windows,
            "max_k": 10_000_000_000,
            "largest_candidate_bound": 10_000_000_000 * TARGET_RANK + 1,
            "small_prime_sieve_survivors": sum(
                row["small_prime_sieve_survivors"] for row in windows
            ),
            "pell_divisibility_hits": 0,
            "prime_hits": 0,
            "interpretation": "NO_PELL_DIVISIBILITY_HIT_THROUGH_K_1E10",
        },
        "primitive_part": {
            "object": "P_10201 / P_101",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
        },
        "archived_light_attempts": [
            {
                "method": "P-1",
                "B1": 50_000,
                "factor_found": False,
                "output_equal_to_primitive_input": True,
                "note": "B2 was not preserved in the archived light-run artifact.",
            },
            {
                "method": "P+1",
                "B1": 50_000,
                "factor_found": False,
                "output_equal_to_primitive_input": True,
                "note": "B2 was not preserved in the archived light-run artifact.",
            },
        ],
        "strong_factorization_attempts": [
            {
                "method": "P-1",
                "B1": 1_000_000,
                "B2": 100_000_000,
                "runs": 12,
                "completed_runs": 12,
                "factor_found": False,
                "outputs_equal_to_primitive_input": 12,
            },
            {
                "method": "P+1",
                "B1": 1_000_000,
                "B2": 100_000_000,
                "runs": 12,
                "completed_runs": 12,
                "factor_found": False,
                "outputs_equal_to_primitive_input": 12,
            },
        ],
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": "At least one prime p with z_P(p)=10201 exists.",
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [
                76_327_215,
                299_902_623_543_471,
            ],
        },
        "boundary": (
            "No hit in bounded compiled scans and no factor in recorded "
            "P-1/P+1 campaigns do not establish nonexistence."
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
    print(f"target_rank = {report['target_rank']}")
    print(f"compiled_scan_max_k = {scan['max_k']}")
    print(f"compiled_pell_hits = {scan['pell_divisibility_hits']}")
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
