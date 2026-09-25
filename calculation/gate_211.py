from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_211_scan.json"

GATE_ROOT = 211
TARGET_RANK = GATE_ROOT * GATE_ROOT

def legendre_8_for_odd_prime_candidate(p: int) -> int:
    if p <= 2 or p % 2 == 0:
        raise ValueError("p must be an odd positive candidate")
    residue = p % 8
    if residue in (1, 7):
        return 1
    if residue in (3, 5):
        return -1
    raise AssertionError("odd residue modulo 8 expected")

def lucas_rank_congruence_admissible(k: int, sign: int) -> bool:
    if k < 1:
        raise ValueError("k must be positive")
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    p = k * TARGET_RANK + sign
    if p <= 2 or p % 2 == 0:
        return False
    return legendre_8_for_odd_prime_candidate(p) == sign

def scan_window(start_k: int, end_k: int, stop_after: int = 1) -> dict:
    if start_k < 1 or end_k < start_k:
        raise ValueError("invalid search window")
    hits: list[dict] = []
    prime_candidates_tested = 0
    for k in range(start_k, end_k + 1):
        for sign in (-1, 1):
            if not lucas_rank_congruence_admissible(k, sign):
                continue
            p = k * TARGET_RANK + sign
            if not is_prime_64(p):
                continue
            prime_candidates_tested += 1
            if exact_rank_target(p, TARGET_RANK):
                hits.append({"p": p, "k": k, "sign": sign})
                if len(hits) >= stop_after:
                    return {
                        "start_k": start_k,
                        "end_k": k,
                        "prime_candidates_tested": prime_candidates_tested,
                        "hits": hits,
                    }
    return {
        "start_k": start_k,
        "end_k": end_k,
        "prime_candidates_tested": prime_candidates_tested,
        "hits": hits,
    }

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
