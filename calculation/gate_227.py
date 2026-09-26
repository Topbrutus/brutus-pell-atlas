from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_227.json"

GATE_ROOT = 227
TARGET_RANK = GATE_ROOT * GATE_ROOT

CANONICAL_WITNESS = 309_173
CANONICAL_K = 6
CANONICAL_SIGN = -1

SECONDARY_WITNESS = 105_428_333
SECONDARY_K = 2_046
SECONDARY_SIGN = -1

FULL_SCAN = {
    "start_k": 1,
    "end_k": 200_000,
    "prime_candidates_tested": 4_629,
    "hits": [
        {"p": CANONICAL_WITNESS, "k": CANONICAL_K, "sign": CANONICAL_SIGN},
        {"p": SECONDARY_WITNESS, "k": SECONDARY_K, "sign": SECONDARY_SIGN},
    ],
}
FIRST_HIT_SCAN = {
    "start_k": 1,
    "end_k": CANONICAL_K,
    "prime_candidates_tested": 1,
    "hits": [
        {"p": CANONICAL_WITNESS, "k": CANONICAL_K, "sign": CANONICAL_SIGN},
    ],
}

PRIMITIVE_SHA256 = (
    "ae347e0dc8e9224d442ebcc22234e48cba2e680a831a5e36c051b9c038c794d5"
)

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_227 must divide P_51529")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    q_text = str(q)
    digest = hashlib.sha256(q_text.encode()).hexdigest()
    if digest != PRIMITIVE_SHA256:
        raise AssertionError("Gate 227 primitive quotient fingerprint mismatch")

    witnesses = []
    for p, k, sign, role in (
        (CANONICAL_WITNESS, CANONICAL_K, CANONICAL_SIGN, "canonical"),
        (SECONDARY_WITNESS, SECONDARY_K, SECONDARY_SIGN, "secondary"),
    ):
        witnesses.append({
            "role": role,
            "p": p,
            "k": k,
            "sign": sign,
            "identity_verified": p == k * TARGET_RANK + sign,
            "prime_verified": is_prime_64(p),
            "exact_rank_verified": exact_rank_target(p, TARGET_RANK),
            "divides_primitive": q % p == 0,
        })

    return {
        "name": "Brutus-Pell Gate 227",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "first_hit_scan": FIRST_HIT_SCAN,
        "full_scan": FULL_SCAN,
        "verified_prime_witnesses": witnesses,
        "primitive_part": {
            "object": "P_51529 / P_227",
            "decimal_digits": len(q_text),
            "sha256": digest,
            "exact_division_verified": True,
        },
        "level3_role": {
            "affected_preview_roots": [49_713, 61_455_314_793],
            "promotion_ready_after_resolution": [49_713],
            "still_blocked": {
                "61455314793": [90_242_753],
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
    first = report["verified_prime_witnesses"][0]
    primitive = report["primitive_part"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"p = {first['p']}")
    print(f"k = {first['k']}")
    print(f"prime_verified = {first['prime_verified']}")
    print(f"exact_rank_verified = {first['exact_rank_verified']}")
    print(f"primitive_digits = {primitive['decimal_digits']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
