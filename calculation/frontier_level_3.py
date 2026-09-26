from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from calculation.frontier_levels import is_prime_64, mirror_value, prime_factorization, prime_support
from calculation.mirror_frontier import build_frontier, exact_rank_target
from calculation.rank_lattice import closure_under_gcd_lcm

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "frontier_level_3_preview.json"

LEVEL2_ROOTS = [633, 2271, 4443, 8886, 67731]
HARD_UNRESOLVED_LEVEL3_GATES = {47, 71, 83, 101, 113}

KNOWN_LEVEL3_GATE_WITNESSES = {
    13: {"witness": 1013, "kind": "preexisting-prime-direct"},
    17: {"witness": 1733, "kind": "prime-direct"},
    19: {"witness": 1_050_509, "kind": "prime-direct"},
    23: {"witness": 20_101, "kind": "prime-direct"},
    29: {"witness": 45_413, "kind": "prime-direct"},
    31: {"witness": 14_213_189, "kind": "prime-direct"},
    37: {"witness": 1_566_137, "kind": "prime-direct"},
    43: {
        "witness": 938_887_039_417,
        "kind": "primitive-part-pminus1-prime",
        "primitive_quotient": "P_1849 / P_43",
    },
    53: {
        "witness": 13_747_841_783_933_689,
        "kind": "primitive-part-pminus1-prime",
        "primitive_quotient": "P_2809 / P_53",
    },
    59: {
        "witness": 31_217_609,
        "kind": "prime-direct",
    },
    67: {
        "witness": 454_134_173,
        "kind": "prime-direct",
    },
    73: {
        "witness": 159_869,
        "kind": "prime-direct",
    },
    79: {
        "witness": 2_266_870_750_557_409,
        "kind": "primitive-part-pminus1-prime",
        "primitive_quotient": "P_6241 / P_79",
    },
    103: {
        "witness": 403_141,
        "kind": "prime-direct",
    },
    109: {
        "witness": 12_203_170_399_877,
        "kind": "compiled-prime-direct",
    },
    131: {
        "witness": 2_745_761,
        "kind": "prime-direct",
    },
    137: {
        "witness": 3_415_957,
        "kind": "prime-direct",
    },
    139: {
        "witness": 12_635_933,
        "kind": "prime-direct",
    },
}

def build_level_3_preview() -> dict:
    level1_promoted = build_frontier()["promotion_effect"]["promoted_nodes"]
    simulated_nodes = closure_under_gcd_lcm(level1_promoted + LEVEL2_ROOTS)
    node_set = set(simulated_nodes)
    support_before = prime_support(simulated_nodes)

    sources_by_target: dict[int, list[dict]] = defaultdict(list)
    for source in simulated_nodes:
        token, target = mirror_value(source)
        if target not in node_set:
            sources_by_target[target].append({
                "source_root": source,
                "mirror_token": token,
            })

    novel_gates: set[int] = set()
    doors = []
    for target in sorted(sources_by_target):
        factors = prime_factorization(target)
        novel = sorted(set(factors) - support_before)
        novel_gates.update(novel)
        resolved_support = sorted(p for p in novel if p in KNOWN_LEVEL3_GATE_WITNESSES)
        unresolved_support = sorted(p for p in novel if p not in KNOWN_LEVEL3_GATE_WITNESSES)
        doors.append({
            "root": target,
            "factorization": {str(p): e for p, e in factors.items()},
            "sources": sources_by_target[target],
            "novel_prime_support": novel,
            "resolved_novel_support": resolved_support,
            "unresolved_prime_gates": unresolved_support,
            "promotion_ready": len(unresolved_support) == 0,
        })

    witness_checks = {}
    for gate, data in KNOWN_LEVEL3_GATE_WITNESSES.items():
        witness = int(data["witness"])
        target_rank = gate * gate
        witness_checks[str(gate)] = {
            **data,
            "rank": target_rank,
            "prime_verified": is_prime_64(witness),
            "exact_rank_verified": exact_rank_target(witness, target_rank),
        }

    resolved = sorted(set(novel_gates) & set(KNOWN_LEVEL3_GATE_WITNESSES))
    unresolved = sorted(set(novel_gates) - set(KNOWN_LEVEL3_GATE_WITNESSES))
    hard_unresolved = sorted(set(unresolved) & HARD_UNRESOLVED_LEVEL3_GATES)
    unworked = sorted(set(unresolved) - HARD_UNRESOLVED_LEVEL3_GATES)
    ready_roots = sorted(d["root"] for d in doors if d["promotion_ready"])
    return {
        "name": "Brutus-Pell Frontier Level 3 Preview",
        "status": "SIMULATION_ONLY_NOT_PROMOTED",
        "source_level_2_roots": LEVEL2_ROOTS,
        "simulated_closure_count": len(simulated_nodes),
        "simulated_closure_max_node": max(simulated_nodes),
        "prime_support_before_mirror": sorted(support_before),
        "new_mirror_root_count": len(sources_by_target),
        "new_mirror_roots": sorted(sources_by_target),
        "doors": doors,
        "novel_prime_gate_count": len(novel_gates),
        "novel_prime_gates": sorted(novel_gates),
        "verified_gate_witnesses": witness_checks,
        "resolved_preview_gates": resolved,
        "unresolved_preview_gates": unresolved,
        "hard_unresolved_preview_gates": hard_unresolved,
        "unworked_preview_gates": unworked,
        "next_unresolved_gate": unresolved[0] if unresolved else None,
        "next_unworked_gate": unworked[0] if unworked else None,
        "promotion_ready_root_count": len(ready_roots),
        "promotion_ready_roots": ready_roots,
        "policy": (
            "Level 3 is a preview only. No Level-2 root or Level-3 mirror root is promoted "
            "into the core lattice by this report."
        ),
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_level_3_preview()
    save_report(report)
    print(f"simulated_closure_count = {report['simulated_closure_count']}")
    print(f"new_mirror_root_count = {report['new_mirror_root_count']}")
    print(f"novel_prime_gate_count = {report['novel_prime_gate_count']}")
    print(f"resolved_preview_gates = {report['resolved_preview_gates']}")
    print(f"next_unresolved_gate = {report['next_unresolved_gate']}")
    print(f"next_unworked_gate = {report['next_unworked_gate']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
