from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.mirror_frontier import exact_rank_target, pell_number
from calculation.primality import verify_pocklington_certificate

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_157_status.json"

GATE_ROOT = 157
TARGET_RANK = GATE_ROOT * GATE_ROOT

WITNESS = 42_720_756_963_545_450_051_849
WITNESS_K = 1_733_163_899_693_514_952
WITNESS_SIGN = 1
POCKLINGTON_BASE = 3
P_MINUS_ONE_FACTORS = (
    (2, 3),
    (31, 1),
    (157, 2),
    (335_957, 1),
    (20_801_960_107, 1),
)

DIRECT_SCAN = {
    "start_k": 1,
    "end_k": 200_000,
    "prime_candidates_tested": 4_725,
    "hits": [],
}

COMPILED_SCAN = {
    "implementation": "calculation/gate_scan_compiled.c",
    "start_k": 200_001,
    "end_k": 10_000_000_000,
    "small_prime_sieve_survivors": 247_573_895,
    "pell_divisibility_hits": 0,
    "prime_hits": 0,
}

FACTORIZATION_ATTEMPTS = [
    {
        "method": "P-1",
        "B1": 100_000,
        "B2": 10_000_000,
        "runs": 8,
        "factor_found": False,
        "audit_directory": "~/tools/gmp-ecm-local/gate157-pm1pp1",
        "exit_status": 0,
    },
    {
        "method": "P+1",
        "B1": 100_000,
        "B2": 10_000_000,
        "runs": 8,
        "factor_found": False,
        "audit_directory": "~/tools/gmp-ecm-local/gate157-pm1pp1",
        "exit_status": 0,
    },
    {
        "method": "ECM",
        "profile": "checkpoint-250k",
        "B1": 250_000,
        "B2": 40_000_000,
        "curves": 12,
        "factor_found": False,
        "output_check": (
            "all 12 normalized outputs equal the input primitive quotient"
        ),
        "audit_directory": "~/tools/gmp-ecm-local/gate157-ecm250k",
        "exit_statuses": [0] * 12,
    },
    {
        "method": "ECM",
        "profile": "factor-discovery-100k",
        "B1": 100_000,
        "B2": 10_000_000,
        "curves": 12,
        "factor_found": True,
        "factor_curve": 3,
        "factor": WITNESS,
        "sigma": 15_700_003,
        "audit_directory": "~/tools/gmp-ecm-local/gate157-ecm-light",
        "exit_statuses": [0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    },
]

ABORTED_ATTEMPTS = [
    {
        "method": "ECM",
        "B1": 1_000_000,
        "B2": 100_000_000,
        "curves_started": 12,
        "completed_curves": 0,
        "exit_statuses": [143] * 12,
        "status": "ABORTED_INCOMPLETE",
        "interpretation": "not counted as a negative factorization result",
        "audit_directory": "~/tools/gmp-ecm-local/gate157-ecm",
    },
]

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_157 must divide P_24649")
    return q

def primitive_sha256() -> str:
    return hashlib.sha256(str(primitive_quotient()).encode("ascii")).hexdigest()

def verify_witness_primality() -> bool:
    return verify_pocklington_certificate(
        WITNESS,
        P_MINUS_ONE_FACTORS,
        POCKLINGTON_BASE,
    )

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 157",
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
            "object": "P_24649 / P_157",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
            "sha256": primitive_sha256(),
            "witness_divides": q % WITNESS == 0,
            "factordb_observation": {
                "checked_date": "2026-09-26",
                "status": "C",
                "nontrivial_factor_returned_at_check": False,
            },
        },
        "factorization_attempts": FACTORIZATION_ATTEMPTS,
        "aborted_attempts": ABORTED_ATTEMPTS,
        "explicit_prime_witness": {
            "p": WITNESS,
            "k": WITNESS_K,
            "sign": WITNESS_SIGN,
            "identity_verified": (
                WITNESS == WITNESS_K * TARGET_RANK + WITNESS_SIGN
            ),
            "prime_verified": verify_witness_primality(),
            "prime_proof": {
                "method": "Pocklington",
                "base": POCKLINGTON_BASE,
                "p_minus_1_factors": [list(row) for row in P_MINUS_ONE_FACTORS],
                "fully_factored_p_minus_1": (
                    WITNESS - 1
                    == __import__("math").prod(
                        q ** e for q, e in P_MINUS_ONE_FACTORS
                    )
                ),
            },
            "exact_rank_verified": exact_rank_target(WITNESS, TARGET_RANK),
        },
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [432_849],
            "remaining_other_gate_support": {"432849": [919]},
            "promotion_effect": (
                "prime support 157 resolved; preview root 432849 still requires gate 919"
            ),
        },
        "observation": (
            "Gate 157 is an exact computational result inside the simulation-only "
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
    witness = report["explicit_prime_witness"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"witness = {witness['p']}")
    print(f"k = {witness['k']}")
    print(f"prime_verified = {witness['prime_verified']}")
    print(f"exact_rank_verified = {witness['exact_rank_verified']}")
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
