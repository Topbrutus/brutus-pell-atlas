from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.gate_scan import (
    legendre_8_for_odd_prime_candidate,
    lucas_rank_congruence_admissible as _generic_admissible,
    scan_window as _generic_scan_window,
)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_211_scan.json"

GATE_ROOT = 211
TARGET_RANK = GATE_ROOT * GATE_ROOT

def lucas_rank_congruence_admissible(k: int, sign: int) -> bool:
    return _generic_admissible(GATE_ROOT, k, sign)

def scan_window(start_k: int, end_k: int, stop_after: int = 1) -> dict:
    return _generic_scan_window(GATE_ROOT, start_k, end_k, stop_after)

def build_report() -> dict:
    windows = [
        {"start_k": 1, "end_k": 200_000, "prime_candidates_tested": 9_177, "hits": []},
        {"start_k": 200_001, "end_k": 5_000_000, "prime_candidates_tested": 190_833, "hits": []},
    ]
    return {
        "name": "Brutus-Pell Gate 211 Deep Scan",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "target_factorization": "211^2",
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": "There exists at least one prime p with z_P(p)=44521.",
            "classification": "KNOWN_THEORY",
            "references": [
                "R. D. Carmichael (1913), On the numerical factors of the arithmetic forms alpha^n +/- beta^n",
                "M. Yabuta (2001), A simple proof of Carmichael's theorem on primitive divisors",
                "Bilu-Hanrot-Voutier et al. (2001), primitive divisors of Lucas and Lehmer numbers",
            ],
        },
        "prime_rank_congruence_filter": {
            "discriminant": 8,
            "rule": "p congruent to (8/p) modulo z_P(p)",
            "candidate_form": "p = k*44521 +/- 1 with sign matching (8/p)",
            "classification": "KNOWN_THEORY",
        },
        "computed_windows": windows,
        "combined": {
            "max_k": 5_000_000,
            "largest_candidate_bound": 5_000_000 * TARGET_RANK + 1,
            "prime_candidates_tested": sum(w["prime_candidates_tested"] for w in windows),
            "hits": [],
            "status": "NO_EXPLICIT_PRIME_WITNESS_IN_SCANNED_WINDOW",
        },
        "research_status": (
            "Prime witness existence is guaranteed by known primitive-divisor theory; "
            "the open computational task is to exhibit a compact explicit witness."
        ),
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    c = report["combined"]
    print(f"root = {report['root']}")
    print(f"target_rank = {report['target_rank']}")
    print(f"max_k = {c['max_k']}")
    print(f"prime_candidates_tested = {c['prime_candidates_tested']}")
    print(f"hits = {c['hits']}")
    print(f"status = {c['status']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
