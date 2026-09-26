from __future__ import annotations

import json
import sys
from math import gcd
from pathlib import Path

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target, pell_number

sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "gate_139.json"

GATE_ROOT = 139
TARGET_RANK = GATE_ROOT * GATE_ROOT

WITNESS = 12_635_933
WITNESS_K = 654
WITNESS_SIGN = -1

SECONDARY_WITNESS = 1_175_141_861
SECONDARY_K = 60_822
SECONDARY_SIGN = -1

DIRECT_SCAN = {
    "search_cap": 200_000,
    "prime_candidates_tested": 4_830,
    "first_hit_prime_candidates_tested": 24,
    "hits": [
        {"p": WITNESS, "k": WITNESS_K, "sign": WITNESS_SIGN},
        {
            "p": SECONDARY_WITNESS,
            "k": SECONDARY_K,
            "sign": SECONDARY_SIGN,
        },
    ],
}

AFFECTED_ROOT = 2_989_473
AFFECTED_TARGET_RANK = AFFECTED_ROOT * AFFECTED_ROOT
COMPONENT_WITNESSES = {
    3: 197,
    67: 454_134_173,
    107: 82_318_309,
    139: WITNESS,
}
AFFECTED_WITNESS = (
    COMPONENT_WITNESSES[3]
    * COMPONENT_WITNESSES[67]
    * COMPONENT_WITNESSES[107]
    * COMPONENT_WITNESSES[139]
)

def primitive_quotient() -> int:
    p_root = pell_number(GATE_ROOT)
    p_target = pell_number(TARGET_RANK)
    q, r = divmod(p_target, p_root)
    if r:
        raise AssertionError("P_139 must divide P_19321")
    return q

def pairwise_component_gcds() -> list[list[int]]:
    items = list(COMPONENT_WITNESSES.items())
    rows: list[list[int]] = []
    for i, (root_a, witness_a) in enumerate(items):
        for root_b, witness_b in items[i + 1:]:
            rows.append([root_a, root_b, gcd(witness_a, witness_b)])
    return rows

def build_report() -> dict:
    q = primitive_quotient()
    return {
        "name": "Brutus-Pell Gate 139",
        "status": "RESOLVED",
        "root": GATE_ROOT,
        "target_rank": TARGET_RANK,
        "direct_scan": DIRECT_SCAN,
        "primitive_part": {
            "object": "P_19321 / P_139",
            "decimal_digits": len(str(q)),
            "factor_divides_primitive_quotient": q % WITNESS == 0,
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
        "secondary_verified_witness": {
            "p": SECONDARY_WITNESS,
            "k": SECONDARY_K,
            "sign": SECONDARY_SIGN,
            "identity_verified": (
                SECONDARY_WITNESS
                == SECONDARY_K * TARGET_RANK + SECONDARY_SIGN
            ),
            "prime_verified": is_prime_64(SECONDARY_WITNESS),
            "exact_rank_verified": exact_rank_target(
                SECONDARY_WITNESS,
                TARGET_RANK,
            ),
        },
        "affected_preview_root": {
            "root": AFFECTED_ROOT,
            "target_rank": AFFECTED_TARGET_RANK,
            "factorization": "3 * 67 * 107 * 139",
            "component_witnesses": {
                str(k): v for k, v in COMPONENT_WITNESSES.items()
            },
            "pairwise_gcds": pairwise_component_gcds(),
            "witness": AFFECTED_WITNESS,
            "exact_rank_verified": exact_rank_target(
                AFFECTED_WITNESS,
                AFFECTED_TARGET_RANK,
            ),
            "promotion_ready": True,
        },
        "observation": (
            "Gate 139 resolves the last novel prime support of preview root "
            "2989473. This remains a simulation-only frontier result."
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
    print(f"status = {report['status']}")
    print(f"target_rank = {TARGET_RANK}")
    print(f"witness = {WITNESS}")
    print(f"k = {WITNESS_K}")
    print("affected_root = " f"{report['affected_preview_root']['root']}")
    print(
        "affected_root_rank_verified = "
        f"{report['affected_preview_root']['exact_rank_verified']}"
    )
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
