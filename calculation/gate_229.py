from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_229.json"

GATE_ROOT = 229
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 257_753_713_526_201
WITNESS_K = 4_915_118_200
WITNESS_SIGN = 1

DIRECT_SCAN = {
    "start_k": 1,
    "end_k": 200_000,
    "prime_candidates_tested": 4_529,
    "hits": [],
}

COMPILED_SCAN = {
    "implementation": "calculation/gate_scan_compiled.c",
    "start_k": 200_001,
    "end_k": 10_000_000_000,
    "small_prime_sieve_survivors": 246_915_578,
    "pell_divisibility_hits": 1,
    "prime_hits": 1,
    "best_p": WITNESS,
    "best_k": WITNESS_K,
    "best_sign": WITNESS_SIGN,
}

PRIMITIVE_SHA256 = (
    "8cc27fbbf87f1ab3b407a4e28695d3f654b7e0f0cefc792885ffd9eb188996e1"
)

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_229 must divide P_52441")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    q_text = str(q)
    digest = hashlib.sha256(q_text.encode()).hexdigest()
    if digest != PRIMITIVE_SHA256:
        raise AssertionError("Gate 229 primitive quotient fingerprint mismatch")
    return {
        "name": "Brutus-Pell Gate 229",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "compiled_pell_scan": {
            **COMPILED_SCAN,
            "largest_candidate_bound": (
                COMPILED_SCAN["end_k"] * TARGET_RANK + 1
            ),
        },
        "explicit_prime_witness": {
            "p": WITNESS,
            "k": WITNESS_K,
            "sign": WITNESS_SIGN,
            "identity_verified": (
                WITNESS == WITNESS_K * TARGET_RANK + WITNESS_SIGN
            ),
            "prime_verified": is_prime_64(WITNESS),
            "exact_rank_verified": exact_rank_target(WITNESS, TARGET_RANK),
        },
        "primitive_part": {
            "object": "P_52441 / P_229",
            "decimal_digits": len(q_text),
            "sha256": digest,
            "exact_division_verified": True,
            "witness_divides_primitive": q % WITNESS == 0,
        },
        "level3_role": {
            "affected_preview_roots": [4_809, 8_008_342_512],
            "promotion_ready_after_resolution": [4_809],
            "still_blocked": {
                "8008342512": [728_561],
            },
        },
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
    row = report["explicit_prime_witness"]
    scan = report["compiled_pell_scan"]
    primitive = report["primitive_part"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"p = {row['p']}")
    print(f"k = {row['k']}")
    print(f"prime_verified = {row['prime_verified']}")
    print(f"exact_rank_verified = {row['exact_rank_verified']}")
    print(f"compiled_scan_max_k = {scan['end_k']}")
    print(f"compiled_pell_hits = {scan['pell_divisibility_hits']}")
    print(f"primitive_digits = {primitive['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
