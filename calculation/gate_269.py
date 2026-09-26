from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.mirror_frontier import pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_269_status.json"

GATE_ROOT = 269
TARGET_RANK = GATE_ROOT * GATE_ROOT

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
    "small_prime_sieve_survivors": 246_634_988,
    "pell_divisibility_hits": 0,
    "prime_hits": 0,
}

FACTORIZATION_ATTEMPTS = [
    {
        "method": "P-1",
        "B1": 20_000,
        "B2": 2_000_000,
        "runs": 4,
        "factor_found": False,
        "output_check": "normalized output equals the input primitive quotient",
        "audit_directory": "~/tools/gmp-ecm-local/gate269-pm1pp1",
        "exit_status": 0,
    },
    {
        "method": "P+1",
        "B1": 20_000,
        "B2": 2_000_000,
        "runs": 4,
        "factor_found": False,
        "output_check": "normalized output equals the input primitive quotient",
        "audit_directory": "~/tools/gmp-ecm-local/gate269-pm1pp1",
        "exit_status": 0,
    },
]

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_269 must divide P_72361")
    return q

def primitive_sha256() -> str:
    return hashlib.sha256(str(primitive_quotient()).encode("ascii")).hexdigest()

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 269 Status",
        "status": "HARD_UNRESOLVED",
        "frontier_class": "DEEP_COMPUTATIONAL_FRONTIER",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "compiled_pell_scan": {
            **COMPILED_SCAN,
            "largest_candidate_bound": COMPILED_SCAN["end_k"] * TARGET_RANK + 1,
            "interpretation": "NO_PELL_DIVISIBILITY_HIT_THROUGH_K_1E10",
        },
        "primitive_part": {
            "object": "P_72361 / P_269",
            "decimal_digits": len(str(q)),
            "exact_division_verified": True,
            "sha256": primitive_sha256(),
        },
        "factorization_attempts": FACTORIZATION_ATTEMPTS,
        "known_theory": {
            "primitive_prime_divisor_existence": True,
            "consequence": "At least one prime p with z_P(p)=72361 exists.",
            "classification": "KNOWN_THEORY",
        },
        "level3_role": {
            "affected_preview_roots": [42_771],
            "already_resolved_other_support": {"42771": [53]},
            "would_make_promotion_ready": [42_771],
        },
        "boundary": (
            "No hit in bounded scans and no factor in recorded P-1/P+1 campaigns "
            "do not establish nonexistence."
        ),
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"compiled_scan_max_k = {report['compiled_pell_scan']['end_k']}")
    print(f"compiled_sieve_survivors = {report['compiled_pell_scan']['small_prime_sieve_survivors']}")
    print(f"compiled_pell_hits = {report['compiled_pell_scan']['pell_divisibility_hits']}")
    print(f"primitive_digits = {report['primitive_part']['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
