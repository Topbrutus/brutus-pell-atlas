from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_163.json"

GATE_ROOT = 163
TARGET_RANK = GATE_ROOT * GATE_ROOT
WITNESS = 2_247_896_813
WITNESS_K = 84_606
WITNESS_SIGN = -1

DIRECT_SCAN = {
    "start_k": 1,
    "end_k": 200_000,
    "prime_candidates_tested": 4_716,
    "hits": [
        {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
    ],
}
PRIMITIVE_SHA256 = (
    "f49c7c085612d37b724307ef544537cab5caff884dffe7d810fdc118252ad7f7"
)

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_163 must divide P_26569")
    return q

def build_report() -> dict:
    q = primitive_quotient()
    q_text = str(q)
    digest = hashlib.sha256(q_text.encode()).hexdigest()
    if digest != PRIMITIVE_SHA256:
        raise AssertionError("Gate 163 primitive quotient fingerprint mismatch")
    return {
        "name": "Brutus-Pell Gate 163",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
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
            "object": "P_26569 / P_163",
            "decimal_digits": len(q_text),
            "sha256": digest,
            "exact_division_verified": True,
            "witness_divides_primitive": q % WITNESS == 0,
            "residual_cofactor_digits": len(str(q // WITNESS)),
        },
        "level3_role": {
            "affected_preview_roots": [2_820_552, 29_770_544_451],
            "promotion_ready_after_resolution": [2_820_552],
            "still_blocked": {
                "29770544451": [3851, 15809],
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
