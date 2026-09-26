from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.mirror_frontier import pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_157_status.json"

GATE_ROOT = 157
TARGET_RANK = GATE_ROOT * GATE_ROOT

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
        "B1": 50_000,
        "effective_B2": 14_856_276,
        "runs": 1,
        "factor_found": False,
        "audit_log": "~/tools/gmp-ecm-local/gate157_pm1.log",
        "exit_status": 0,
    },
    {
        "method": "P+1",
        "B1": 50_000,
        "effective_B2": 19_411_780,
        "runs": 1,
        "factor_found": False,
        "audit_log": "~/tools/gmp-ecm-local/gate157_pp1.log",
        "exit_status": 0,
    },
]

PRIMITIVE_SHA256 = (
    "af8f60fea2efe11b26aa3d863d7bf2aac31b7e587830b539f3b572819d113621"
)

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_157 must divide P_24649")
    return q
def build_report() -> dict:
    q = primitive_quotient()
    q_text = str(q)
    digest = hashlib.sha256(q_text.encode()).hexdigest()
    if digest != PRIMITIVE_SHA256:
        raise AssertionError("Gate 157 primitive quotient fingerprint mismatch")
    return {
        "name": "Brutus-Pell Gate 157 Status",
        "status": "ACTIVE_UNRESOLVED",
        "frontier_class": "ACTIVE_COMPUTATIONAL_FRONTIER",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "compiled_pell_scan": {
            **COMPILED_SCAN,
            "largest_candidate_bound": (
                COMPILED_SCAN["end_k"] * TARGET_RANK + 1
            ),
            "interpretation": "NO_PELL_DIVISIBILITY_HIT_THROUGH_K_1E10",
        },
        "primitive_part": {
            "object": "P_24649 / P_157",
            "decimal_digits": len(q_text),
            "sha256": digest,
            "exact_division_verified": True,
            "factordb_observation": {
                "checked_date": "2026-09-25",
                "status": "U",
                "nontrivial_factor_returned": False,
            },
        },
        "factorization_attempts": FACTORIZATION_ATTEMPTS,
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": (
                "At least one prime p with z_P(p)=24649 exists."
            ),
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [432_849],
            "other_unresolved_support": {"432849": [919]},
        },
        "boundary": (
            "No hit in bounded scans and no factor in the recorded light "
            "P-1/P+1 attempts do not establish nonexistence. Gate 157 is "
            "worked but not yet classified as a hard computational frontier."
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
    scan = report["compiled_pell_scan"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"compiled_scan_max_k = {scan['end_k']}")
    print(
        "compiled_sieve_survivors = "
        f"{scan['small_prime_sieve_survivors']}"
    )
    print(f"compiled_pell_hits = {scan['pell_divisibility_hits']}")
    print(
        "primitive_digits = "
        f"{report['primitive_part']['decimal_digits']}"
    )
    print(f"primitive_sha256 = {report['primitive_part']['sha256']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
