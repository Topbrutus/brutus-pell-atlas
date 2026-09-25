from __future__ import annotations

import json
from math import gcd
from pathlib import Path

from calculation.rank_lattice import build_lattice, closure_under_gcd_lcm

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "mirror_frontier.json"

def pell_number(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, 2 * b + a
    return a

def pell_mod_fast(index: int, modulus: int) -> int:
    if index < 0:
        raise ValueError("index must be nonnegative")
    if modulus < 1:
        raise ValueError("modulus must be positive")
    a, b, c, d = 1, 0, 0, 1
    e, f, g, h = 2, 1, 1, 0
    n = index
    while n:
        if n & 1:
            a, b, c, d = (
                (a * e + b * g) % modulus,
                (a * f + b * h) % modulus,
                (c * e + d * g) % modulus,
                (c * f + d * h) % modulus,
            )
        e, f, g, h = (
            (e * e + f * g) % modulus,
            (e * f + f * h) % modulus,
            (g * e + h * g) % modulus,
            (g * f + h * h) % modulus,
        )
        n //= 2
    return b % modulus

def distinct_prime_divisors(n: int) -> list[int]:
    out: list[int] = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out

def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def exact_rank_target(modulus: int, target: int) -> bool:
    if pell_mod_fast(target, modulus) != 0:
        return False
    return all(
        pell_mod_fast(target // q, modulus) != 0
        for q in distinct_prime_divisors(target)
    )

def build_frontier() -> dict:
    root_48 = 48
    target_48 = root_48 * root_48
    witness_48 = 28_320_769

    root_861 = 861
    target_861 = root_861 * root_861
    p_1681 = pell_number(41 * 41)
    witness_861 = 197 * 293 * p_1681

    current_nodes = build_lattice()["nodes"]
    promoted_nodes = closure_under_gcd_lcm(current_nodes + [root_48, root_861])

    return {
        "name": "Brutus-Pell Mirror Frontier",
        "principle": (
            "Fiber non-emptiness is universal because z_P(P_m)=m; "
            "frontier interest is compact or structured witnesses."
        ),
        "frontier": [
            {
                "source_root": 84,
                "mirror_token": "48",
                "root": root_48,
                "target_rank": target_48,
                "witness": str(witness_48),
                "witness_digits": len(str(witness_48)),
                "witness_kind": "prime-direct",
                "witness_prime_verified": is_prime_trial(witness_48),
                "exact_rank_verified": exact_rank_target(witness_48, target_48),
            },
            {
                "source_root": 168,
                "mirror_token": "861",
                "root": root_861,
                "target_rank": target_861,
                "witness": str(witness_861),
                "witness_digits": len(str(witness_861)),
                "witness_kind": "structured-product",
                "construction": "197 * 293 * P_1681",
                "component_rank_roots": [3, 7, 41],
                "P_1681_digits": len(str(p_1681)),
                "gcd_P1681_197": gcd(p_1681, 197),
                "gcd_P1681_293": gcd(p_1681, 293),
                "P_1681_exact_rank_verified": exact_rank_target(p_1681, 1681),
                "exact_rank_verified": exact_rank_target(witness_861, target_861),
            },
        ],
        "promotion_effect": {
            "current_lattice_nodes": len(current_nodes),
            "nodes_if_both_promoted": len(promoted_nodes),
            "promoted_nodes": promoted_nodes,
            "policy": "frontier-only until deliberate promotion",
        },
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_frontier()
    save_report(report)
    for row in report["frontier"]:
        print(
            f"{row['source_root']} -> {row['root']} : "
            f"rank={row['target_rank']} verified={row['exact_rank_verified']} "
            f"digits={row['witness_digits']} kind={row['witness_kind']}"
        )
    print(f"promotion: {report['promotion_effect']['current_lattice_nodes']} -> "
          f"{report['promotion_effect']['nodes_if_both_promoted']} nodes")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
