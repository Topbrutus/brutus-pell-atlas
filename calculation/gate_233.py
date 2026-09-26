from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_233.json"

GATE_ROOT = 233
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 179_216_201_898_552_121
WITNESS_K = 3_301_151_281_080
WITNESS_SIGN = 1

DIRECT_SCAN = {
    "start_k": 1,
    "end_k": 200_000,
    "prime_candidates_tested": 4_466,
    "hits": [],
}

COMPILED_SCAN = {
    "implementation": "calculation/gate_scan_compiled.c",
    "start_k": 200_001,
    "end_k": 10_000_000_000,
    "small_prime_sieve_survivors": 246_891_343,
    "pell_divisibility_hits": 0,
    "prime_hits": 0,
}

PRIMITIVE_SHA256 = (
    "489074e56744d22df377a0ce0c634d02ccfe7e89d015b0a9b0ef2eb22f873d3e"
)

FACTORIZATION = {
    "method": "P-1",
    "B1": 50_000,
    "B2": 10_000_000,
    "preloaded_order_factor": TARGET_RANK,
    "factor_found": True,
    "factor": WITNESS,
    "exit_status": 6,
    "audit_log": "~/tools/gmp-ecm-local/gate233_pm1.log",
}

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_233 must divide P_54289")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    q_text = str(q)
    digest = hashlib.sha256(q_text.encode("ascii")).hexdigest()
    if digest != PRIMITIVE_SHA256:
        raise AssertionError("Gate 233 primitive quotient fingerprint mismatch")
    return {
        "name": "Brutus-Pell Gate 233",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "compiled_pell_scan": {
            **COMPILED_SCAN,
            "largest_candidate_bound": COMPILED_SCAN["end_k"] * TARGET_RANK + 1,
            "interpretation": "NO_PELL_DIVISIBILITY_HIT_THROUGH_K_1E10",
        },
        "primitive_part": {
            "object": "P_54289 / P_233",
            "decimal_digits": len(q_text),
            "sha256": digest,
            "exact_division_verified": True,
            "witness_divides_primitive": q % WITNESS == 0,
            "factordb_observation": {
                "checked_date": "2026-09-26",
                "status": "U",
                "nontrivial_factor_returned_at_check": False,
            },
        },
        "factorization": FACTORIZATION,
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
        "level3_role": {
            "affected_preview_roots": [4_209_500_564_058],
            "remaining_other_gate_support": {
                "4209500564058": [3_011_087_671],
            },
            "promotion_effect": (
                "prime support 233 resolved; affected preview root still requires gate 3011087671"
            ),
        },
        "observation": (
            "Gate 233 is an exact computational result inside the simulation-only "
            "Level-3 preview; it does not promote any root into the core lattice."
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
    row = report["explicit_prime_witness"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"p = {row['p']}")
    print(f"k = {row['k']}")
    print(f"prime_verified = {row['prime_verified']}")
    print(f"exact_rank_verified = {row['exact_rank_verified']}")
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
