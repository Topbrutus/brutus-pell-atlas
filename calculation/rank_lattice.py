from __future__ import annotations

import json
from itertools import combinations_with_replacement
from math import gcd, lcm
from pathlib import Path

from calculation.pell_atlas import load_atlas, pell_rank

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "rank_lattice.json"

def seed_roots() -> list[int]:
    roots = {
        int(record["square_rank_root"])
        for record in load_atlas()["records"]
        if record.get("square_rank_root") is not None
    }
    return sorted(roots)

def closure_under_gcd_lcm(values: list[int]) -> list[int]:
    nodes = set(values)
    changed = True
    while changed:
        changed = False
        current = sorted(nodes)
        for a, b in combinations_with_replacement(current, 2):
            for value in (gcd(a, b), lcm(a, b)):
                if value not in nodes:
                    nodes.add(value)
                    changed = True
    return sorted(nodes)

def hasse_edges(nodes: list[int]) -> list[list[int]]:
    edges: list[list[int]] = []
    for a in nodes:
        for b in nodes:
            if a >= b or b % a != 0:
                continue
            if any(a < c < b and c % a == 0 and b % c == 0 for c in nodes):
                continue
            edges.append([a, b])
    return edges

def stored_members_for_root(root: int) -> list[int]:
    target = root * root
    return sorted(
        int(record["n"])
        for record in load_atlas()["records"]
        if int(record["rank"]) == target
    )

def pair_operations(nodes: list[int]) -> list[dict]:
    rows: list[dict] = []
    for a, b in combinations_with_replacement(nodes, 2):
        meet = gcd(a, b)
        join = lcm(a, b)
        rows.append({
            "a": a,
            "b": b,
            "meet_gcd": meet,
            "join_lcm": join,
            "meet_in_lattice": meet in nodes,
            "join_in_lattice": join in nodes,
            "nontrivial_join": join not in (a, b),
        })
    return rows

def build_lattice() -> dict:
    seeds = seed_roots()
    nodes = closure_under_gcd_lcm(seeds)
    pairs = pair_operations(nodes)
    node_records = []
    for root in nodes:
        members = stored_members_for_root(root)
        node_records.append({
            "root": root,
            "square_rank": root * root,
            "stored_members": members,
            "stored_member_count": len(members),
            "structural_only": len(members) == 0,
        })
    identity_verified = pell_rank(1, 1) == 1
    return {
        "name": "Brutus-Pell Rank Lattice",
        "order": "divisibility on square-rank roots C",
        "seed_roots": seeds,
        "nodes": nodes,
        "identity_root": 1,
        "identity_rank": 1,
        "identity_rank_verified": identity_verified,
        "hasse_edges": hasse_edges(nodes),
        "pairs": pairs,
        "closed_under_gcd": all(row["meet_in_lattice"] for row in pairs),
        "closed_under_lcm": all(row["join_in_lattice"] for row in pairs),
        "node_records": node_records,
        "nontrivial_joins": [
            {"a": row["a"], "b": row["b"], "join": row["join_lcm"]}
            for row in pairs if row["nontrivial_join"]
        ],
    }

def save_lattice(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_lattice()
    save_lattice(report)
    print(f"seed_roots = {report['seed_roots']}")
    print(f"nodes = {report['nodes']}")
    print(f"hasse_edges = {report['hasse_edges']}")
    print(f"closed_under_gcd = {report['closed_under_gcd']}")
    print(f"closed_under_lcm = {report['closed_under_lcm']}")
    print(f"nontrivial_joins = {report['nontrivial_joins']}")
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
