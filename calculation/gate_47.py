from __future__ import annotations

import json
from pathlib import Path

from calculation.gate_scan import scan_window
from calculation.mirror_frontier import pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_47_status.json"

GATE_ROOT = 47
TARGET_RANK = GATE_ROOT * GATE_ROOT

DIRECT_SCAN_WINDOWS = [
    {"start_k": 1, "end_k": 200_000, "prime_candidates_tested": 10_857},
    {"start_k": 200_001, "end_k": 100_000_000, "prime_candidates_tested": 4_065_326},
    {"start_k": 100_000_001, "end_k": 500_000_000, "prime_candidates_tested": 15_066_870},
    {"start_k": 500_000_001, "end_k": 1_000_000_000, "prime_candidates_tested": 18_173_921},
]

ARCHIVED_FACTOR_RUNS = {
    "ecm47_parallel": 48,
    "ecm47_parallel_strong": 96,
    "gate47-ecm-1m": 120,
    "gate47-ecm250k": 240,
    "gate47-pm1-1m": 120,
    "gate47-pm1-250k": 240,
    "gate47-pp1-1m": 120,
    "gate47-pp1-250k": 240,
}

def primitive_quotient() -> int:
    p47 = pell_number(GATE_ROOT)
    p2209 = pell_number(TARGET_RANK)
    q, r = divmod(p2209, p47)
    if r:
        raise AssertionError("P_47 must divide P_2209")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    direct_total = sum(w["prime_candidates_tested"] for w in DIRECT_SCAN_WINDOWS)
    archived_total = sum(ARCHIVED_FACTOR_RUNS.values())
    return {
        "name": "Brutus-Pell Gate 47 Status",
        "status": "HARD_UNRESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "windows": DIRECT_SCAN_WINDOWS,
            "max_k": 1_000_000_000,
            "largest_candidate_bound": 1_000_000_000 * TARGET_RANK + 1,
            "prime_candidates_tested": direct_total,
            "hits": [],
            "interpretation": "NO_EXPLICIT_PRIME_WITNESS_IN_SCANNED_WINDOW",
        },
        "primitive_part": {
            "object": "P_2209 / P_47",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
            "archived_factor_run_outputs": archived_total,
            "archived_output_counts": ARCHIVED_FACTOR_RUNS,
            "archived_outputs_different_from_input": 0,
            "interpretation": "NO_FACTOR_FOUND_IN_ARCHIVED_CAMPAIGNS",
        },
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": "At least one prime p with z_P(p)=2209 exists.",
            "classification": "KNOWN_THEORY",
        },
        "boundary": (
            "Negative bounded searches and failed factorization campaigns do not establish "
            "nonexistence. Gate 47 remains unresolved only at the explicit-witness level."
        ),
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    scan = report["direct_scan"]
    primitive = report["primitive_part"]
    print(f"status = {report['status']}")
    print(f"target_rank = {report['target_rank']}")
    print(f"direct_scan_max_k = {scan['max_k']}")
    print(f"direct_scan_prime_candidates = {scan['prime_candidates_tested']}")
    print(f"primitive_digits = {primitive['decimal_digits']}")
    print(f"archived_factor_outputs = {primitive['archived_factor_run_outputs']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
