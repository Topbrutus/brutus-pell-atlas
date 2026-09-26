from __future__ import annotations

import json
from pathlib import Path

from calculation.mirror_frontier import pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_83_status.json"

GATE_ROOT = 83
TARGET_RANK = GATE_ROOT * GATE_ROOT

def primitive_quotient() -> int:
    p83 = pell_number(GATE_ROOT)
    p6889 = pell_number(TARGET_RANK)
    q, r = divmod(p6889, p83)
    if r:
        raise AssertionError("P_83 must divide P_6889")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 83 Status",
        "status": "HARD_UNRESOLVED",
        "frontier_class": "DEEP_COMPUTATIONAL_FRONTIER",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "start_k": 1,
            "end_k": 200_000,
            "prime_candidates_tested": 10_113,
            "hits": [],
        },
        "compiled_pell_scan": {
            "implementation": "C/OpenMP exact modular Pell scanner derived from calculation/gate_47_scan.c",
            "windows": [
                {
                    "start_k": 1,
                    "end_k": 1_000_000_000,
                    "small_prime_sieve_survivors": 49_255_590,
                    "pell_divisibility_hits": 0,
                },
                {
                    "start_k": 1_000_000_001,
                    "end_k": 10_000_000_000,
                    "small_prime_sieve_survivors": 448_293_438,
                    "pell_divisibility_hits": 0,
                },
            ],
            "max_k": 10_000_000_000,
            "pell_divisibility_hits": 0,
        },
        "primitive_part": {
            "object": "P_6889 / P_83",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
        },
        "factorization_attempts": [
            {"method": "P-1", "B1": 50_000, "B2": 10_000_000, "runs": 10, "factor_found": False},
            {"method": "P+1", "B1": 50_000, "B2": 10_000_000, "runs": 10, "factor_found": False},
            {"method": "P-1", "B1": 250_000, "B2": 40_000_000, "runs": 12, "factor_found": False},
            {"method": "P+1", "B1": 250_000, "B2": 40_000_000, "runs": 12, "factor_found": False},
        ],
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": "At least one prime p with z_P(p)=6889 exists.",
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [76_327_215, 205_901_835, 6_773_594_061],
        },
        "boundary": (
            "No hit in bounded scans and no factor in recorded P-1/P+1 campaigns "
            "do not establish nonexistence."
        ),
    }
def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    print(f"status = {report['status']}")
    print(f"target_rank = {report['target_rank']}")
    print(f"compiled_scan_max_k = {report['compiled_pell_scan']['max_k']}")
    print(f"compiled_pell_hits = {report['compiled_pell_scan']['pell_divisibility_hits']}")
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
