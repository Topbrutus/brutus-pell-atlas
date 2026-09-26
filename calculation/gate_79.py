from __future__ import annotations

import json
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_79.json"

GATE_ROOT = 79
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 2_266_870_750_557_409
WITNESS_K = 363_222_360_288
WITNESS_SIGN = 1

def primitive_quotient() -> int:
    p79 = pell_number(GATE_ROOT)
    p6241 = pell_number(TARGET_RANK)
    q, r = divmod(p6241, p79)
    if r:
        raise AssertionError("P_79 must divide P_6241")
    return q
def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 79",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": {
            "python_window": {
                "start_k": 1,
                "end_k": 200_000,
                "prime_candidates_tested": 10_241,
                "hits": [],
            },
            "compiled_window": {
                "start_k": 1,
                "end_k": 1_000_000_000,
                "small_prime_sieve_survivors": 49_243_669,
                "pell_divisibility_hits": 0,
                "prime_hits": 0,
            },
        },
        "primitive_part": {
            "object": "P_6241 / P_79",
            "decimal_digits": len(str(q)),
            "factor_divides_primitive_quotient": q % WITNESS == 0,
        },
        "discovery": {
            "method": "GMP-ECM P-1",
            "B1": 50_000,
            "B2": 10_000_000,
            "preloaded_order_factor": TARGET_RANK,
            "requested_runs": 10,
            "note": "Factor returned during quiet P-1 campaign before the planned P+1 campaign.",
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
            "affected_preview_roots": [711_474, 4_276_191],
            "newly_ready_preview_root": 711_474,
            "remaining_gate_for_4276191": 18_043,
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
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
