from __future__ import annotations

import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_109.json"

GATE_ROOT = 109
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 12_203_170_399_877
WITNESS_K = 1_027_116_438
WITNESS_SIGN = -1

COMPILED_SCAN = {
    "start_k": 1,
    "end_k": WITNESS_K,
    "segment": 1_000_000,
    "small_prime_sieve_survivors": 50_631_383,
    "pell_divisibility_hits": 1,
    "prime_hits": 1,
}

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_109 must divide P_11881")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 109",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "discovery": {
            "method": "generic C/OpenMP exact Pell scan",
            "implementation": "calculation/gate_scan_compiled.c",
            "compiled_scan": COMPILED_SCAN,
            "first_hit": {
                "p": WITNESS,
                "k": WITNESS_K,
                "sign": WITNESS_SIGN,
            },
        },
        "primitive_part": {
            "object": "P_11881 / P_109",
            "decimal_digits": len(str(q)),
            "factor_divides_primitive_quotient": q % WITNESS == 0,
            "residual_cofactor_digits": len(str(q // WITNESS)),
        },
        "explicit_prime_witness": {
            "p": WITNESS,
            "k": WITNESS_K,
            "sign": WITNESS_SIGN,
            "identity_verified": (
                WITNESS == WITNESS_K * TARGET_RANK + WITNESS_SIGN
            ),
            "prime_verified": is_prime_64(WITNESS),
            "exact_rank_verified": exact_rank_target(
                WITNESS,
                TARGET_RANK,
            ),
        },
        "level3_role": {
            "affected_preview_roots": [23_467_643_211],
            "remaining_novel_gate_for_affected_root": 71_766_493,
            "promotion_effect": (
                "prime support 109 resolved; affected preview root "
                "still requires gate 71766493"
            ),
        },
        "observation": (
            "The witness is the first exact Pell-rank hit in the "
            "recorded compiled scan through k=1027116438. This is "
            "a bounded computational result, not a general mirror theorem."
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
    w = report["explicit_prime_witness"]
    scan = report["discovery"]["compiled_scan"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"witness = {WITNESS}")
    print(f"k = {WITNESS_K}")
    print(
        "small_prime_sieve_survivors = "
        f"{scan['small_prime_sieve_survivors']}"
    )
    print(f"prime_verified = {w['prime_verified']}")
    print(f"exact_rank_verified = {w['exact_rank_verified']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
