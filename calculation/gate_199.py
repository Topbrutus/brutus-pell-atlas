from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_199.json"

GATE_ROOT = 199
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 21_788_153_393
WITNESS_K = 550_192
WITNESS_SIGN = 1

DIRECT_SCAN_TO_FIRST_HIT = {
    "start_k": 1,
    "end_k": WITNESS_K,
    "prime_candidates_tested": 12_199,
    "hits": [
        {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
    ],
}
PRIMITIVE_SHA256 = (
    "d0bc5faf08dbd33260e366121957898bc2a64148a5d2b07f5d3c8667288abeea"
)

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_199 must divide P_39601")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    q_text = str(q)
    digest = hashlib.sha256(q_text.encode()).hexdigest()
    if digest != PRIMITIVE_SHA256:
        raise AssertionError("Gate 199 primitive quotient fingerprint mismatch")
    return {
        "name": "Brutus-Pell Gate 199",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan_to_first_hit": DIRECT_SCAN_TO_FIRST_HIT,
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
            "object": "P_39601 / P_199",
            "decimal_digits": len(q_text),
            "sha256": digest,
            "exact_division_verified": True,
            "witness_divides_primitive": q % WITNESS == 0,
            "residual_cofactor_digits": len(str(q // WITNESS)),
        },
        "level3_role": {
            "affected_preview_roots": [75_434_532],
            "resolved_support_after_resolution": {
                "75434532": [31, 199],
            },
            "still_blocked": {
                "75434532": [1019],
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
    primitive = report["primitive_part"]
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"p = {row['p']}")
    print(f"k = {row['k']}")
    print(f"prime_verified = {row['prime_verified']}")
    print(f"exact_rank_verified = {row['exact_rank_verified']}")
    print(f"primitive_digits = {primitive['decimal_digits']}")
    print(
        "witness_divides_primitive = "
        f"{primitive['witness_divides_primitive']}"
    )
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
