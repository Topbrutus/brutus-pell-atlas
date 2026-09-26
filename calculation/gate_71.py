from __future__ import annotations

import json
from pathlib import Path

from calculation.mirror_frontier import pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_71_status.json"

GATE_ROOT = 71
TARGET_RANK = GATE_ROOT * GATE_ROOT

def primitive_quotient() -> int:
    p71 = pell_number(GATE_ROOT)
    p5041 = pell_number(TARGET_RANK)
    q, r = divmod(p5041, p71)
    if r:
        raise AssertionError("P_71 must divide P_5041")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 71 Status",
        "status": "ACTIVE_UNRESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "windows": [
                {"start_k": 1, "end_k": 200_000, "prime_candidates_tested": 10_187},
                {"start_k": 200_001, "end_k": 100_000_000, "prime_candidates_tested": 3_906_961},
            ],
            "max_k": 100_000_000,
            "prime_candidates_tested": 3_917_148,
            "largest_candidate_bound": 100_000_000 * TARGET_RANK + 1,
            "hits": [],
        },
        "primitive_part": {
            "object": "P_5041 / P_71",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
        },
        "factorization_attempts": [
            {"method": "P-1", "B1": 50_000, "effective_B2": 6_303_568, "runs": 10, "factor_found": False},
            {"method": "P+1", "B1": 50_000, "effective_B2": 9_714_820, "runs": 10, "factor_found": False},
            {"method": "P-1", "B1": 250_000, "effective_B2": 39_925_198, "runs": 20, "factor_found": False},
            {"method": "P+1", "B1": 250_000, "effective_B2": 39_925_198, "runs": 20, "factor_found": False},
        ],
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": "At least one prime p with z_P(p)=5041 exists.",
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [222_916_002, 498_940_572, 679_699_401],
        },
        "boundary": (
            "No hit in bounded direct scans and no factor in recorded P-1/P+1 attempts "
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
    print(f"direct_scan_max_k = {report['direct_scan']['max_k']}")
    print(f"direct_scan_prime_candidates = {report['direct_scan']['prime_candidates_tested']}")
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
