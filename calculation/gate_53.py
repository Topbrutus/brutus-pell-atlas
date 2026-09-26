from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_53.json"

GATE_ROOT = 53
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 13_747_841_783_933_689
WITNESS_K = 4_894_212_098_232
WITNESS_SIGN = 1

def primitive_quotient() -> int:
    p53 = pell_number(GATE_ROOT)
    p2809 = pell_number(TARGET_RANK)
    q, r = divmod(p2809, p53)
    if r:
        raise AssertionError("P_53 must divide P_2809")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 53",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "max_k": 200_000,
            "prime_candidates_tested": 10_593,
            "hits": [],
            "status": "NO_HIT_IN_WINDOW",
        },
        "primitive_part": {
            "object": "P_2809 / P_53",
            "decimal_digits": len(str(q)),
            "factor_divides_primitive_quotient": q % WITNESS == 0,
        },
        "discovery": {
            "engine": "GMP-ECM 7.0.6",
            "method": "P-1",
            "stage": 2,
            "B1": 50_000,
            "effective_B2": 6_303_568,
            "preloaded_order_factor": TARGET_RANK,
            "exit_status": 14,
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
            "affected_preview_roots": [42_771, 8_633_541, 116_903_001, 639_871_014, 679_699_401],
            "promotion_effect": "prime support 53 resolved; affected roots still require other novel gates",
        },
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
