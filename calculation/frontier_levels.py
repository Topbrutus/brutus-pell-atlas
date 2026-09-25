from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from calculation.mirror_frontier import build_frontier, exact_rank_target

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "frontier_level_2.json"

PRIME_SUPPORT_WITNESSES = {
    107: {
        "witness": 82_318_309,
        "rank": 107 * 107,
        "kind": "prime-direct",
        "status": "VERIFIED_COMPUTATION",
    },
}

BOUNDED_SEARCH_OBSERVATIONS = {
    211: {"max_k": 200_000, "hits": [], "status": "NO_HIT_IN_WINDOW"},
    757: {"max_k": 200_000, "hits": [], "status": "NO_HIT_IN_WINDOW"},
    1481: {"max_k": 200_000, "hits": [], "status": "NO_HIT_IN_WINDOW"},
}

MR_BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    if n in small:
        return True
    if any(n % p == 0 for p in small):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in MR_BASES_64:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def search_prime_square_rank_witness(root: int, max_k: int, stop_after: int = 1) -> list[dict]:
    target = root * root
    hits: list[dict] = []
    for k in range(1, max_k + 1):
        for candidate in (k * target - 1, k * target + 1):
            if candidate <= 2 or not is_prime_64(candidate):
                continue
            if exact_rank_target(candidate, target):
                hits.append({"witness": candidate, "k": k, "rank": target})
                if len(hits) >= stop_after:
                    return hits
    return hits

def prime_factorization(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    factors: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            factors[p] = factors.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        factors[x] = factors.get(x, 0) + 1
    return factors

def prime_support(values: list[int]) -> set[int]:
    support: set[int] = set()
    for value in values:
        support.update(prime_factorization(value))
    return support

def mirror_value(n: int) -> tuple[str, int]:
    token = str(n)[::-1]
    return token, int(token)

def build_level_2() -> dict:
    frontier = build_frontier()
    promoted_nodes = frontier["promotion_effect"]["promoted_nodes"]
    promoted_set = set(promoted_nodes)
    support_before = prime_support(promoted_nodes)

    sources_by_target: dict[int, list[dict]] = defaultdict(list)
    for source in promoted_nodes:
        mirror_token, target = mirror_value(source)
        if target not in promoted_set:
            sources_by_target[target].append({
                "source_root": source,
                "mirror_token": mirror_token,
            })

    doors = []
    unresolved_gate_to_doors: dict[int, list[int]] = defaultdict(list)
    for target in sorted(sources_by_target):
        factors = prime_factorization(target)
        novel_support = sorted(set(factors) - support_before)
        resolved_support = sorted(p for p in novel_support if p in PRIME_SUPPORT_WITNESSES)
        unresolved_support = sorted(p for p in novel_support if p not in PRIME_SUPPORT_WITNESSES)
        for p in unresolved_support:
            unresolved_gate_to_doors[p].append(target)
        doors.append({
            "root": target,
            "factorization": {str(p): e for p, e in factors.items()},
            "sources": sources_by_target[target],
            "novel_prime_support": novel_support,
            "resolved_novel_support": resolved_support,
            "unresolved_prime_gates": unresolved_support,
            "promotion_ready": len(unresolved_support) == 0,
        })

    witness_checks = {}
    for p, data in PRIME_SUPPORT_WITNESSES.items():
        witness = int(data["witness"])
        target_rank = int(data["rank"])
        witness_checks[str(p)] = {
            **data,
            "prime_verified": is_prime_64(witness),
            "exact_rank_verified": exact_rank_target(witness, target_rank),
        }

    return {
        "name": "Brutus-Pell Frontier Level 2",
        "source": "mirror of the 29-node simulated promotion closure",
        "promoted_node_count": len(promoted_nodes),
        "promoted_nodes": promoted_nodes,
        "prime_support_before": sorted(support_before),
        "new_mirror_roots": sorted(sources_by_target),
        "doors": doors,
        "prime_support_witnesses": witness_checks,
        "bounded_search_method": {
            "candidate_form": "p = k*q^2 +/- 1",
            "primality": "deterministic Miller-Rabin for 64-bit candidates",
            "rank_test": "exact modular Pell target verification",
            "interpretation": "NO_HIT_IN_WINDOW is not a nonexistence claim",
        },
        "bounded_search_observations": {str(k): v for k, v in BOUNDED_SEARCH_OBSERVATIONS.items()},
        "unresolved_gate_count": len(unresolved_gate_to_doors),
        "unresolved_gate_to_doors": {
            str(k): sorted(v) for k, v in sorted(unresolved_gate_to_doors.items())
        },
        "policy": (
            "Do not promote a mirror root that introduces unresolved prime support; "
            "keep it at the frontier until a compact or structurally justified witness is verified."
        ),
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_level_2()
    save_report(report)
    print(f"new_mirror_roots = {report['new_mirror_roots']}")
    print(f"prime_support_before = {report['prime_support_before']}")
    print(f"unresolved_gate_count = {report['unresolved_gate_count']}")
    print(f"unresolved_gate_to_doors = {report['unresolved_gate_to_doors']}")
    for door in report["doors"]:
        print(
            f"root={door['root']} factors={door['factorization']} "
            f"unresolved={door['unresolved_prime_gates']}"
        )
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
