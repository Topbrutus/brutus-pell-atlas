from __future__ import annotations

import json
from itertools import combinations
from math import gcd, isqrt, lcm
from pathlib import Path

from calculation.pell_atlas import load_atlas, pell_rank

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "bridge_report.json"
MIRROR_PRODUCT = 13 * 31
MIRROR_RANK_LCM = 210

def is_square(value: int) -> bool:
    root = isqrt(value)
    return root * root == value

def relation_keys() -> set[tuple]:
    atlas = load_atlas()
    keys: set[tuple] = set()
    for rel in atlas.get("relations", []):
        kind = rel.get("kind")
        members = tuple(sorted(int(x) for x in rel.get("members", [])))
        keys.add((kind, members))
    return keys

def stored_records() -> list[dict]:
    return load_atlas()["records"]

def find_collision_bridges(records: list[dict]) -> list[dict]:
    by_rank: dict[int, list[int]] = {}
    for record in records:
        rank = int(record["rank"])
        by_rank.setdefault(rank, []).append(int(record["n"]))
    out: list[dict] = []
    for rank, members in sorted(by_rank.items()):
        if len(members) < 2:
            continue
        members = sorted(members)
        out.append({
            "kind": "same-rank-cluster",
            "rank": rank,
            "square_rank": is_square(rank),
            "members": members,
            "status": "VERIFIED_COMPUTATION",
        })
    return out

def find_square_lcm_bridges(records: list[dict]) -> list[dict]:
    out: list[dict] = []
    for left, right in combinations(records, 2):
        a, b = int(left["n"]), int(right["n"])
        if gcd(a, b) != 1:
            continue
        ra, rb = int(left["rank"]), int(right["rank"])
        target = lcm(ra, rb)
        if not is_square(target):
            continue
        product = a * b
        computed = pell_rank(product, target)
        if computed != target:
            continue
        out.append({
            "kind": "square-lcm-product",
            "inputs": [a, b],
            "input_ranks": [ra, rb],
            "product": product,
            "rank": target,
            "square_rank_root": isqrt(target),
            "status": "VERIFIED_COMPUTATION",
        })
    return out

def find_preserving_bridges(records: list[dict]) -> list[dict]:
    out: list[dict] = []
    for multiplier, host in combinations(records, 2):
        candidates = ((multiplier, host), (host, multiplier))
        for left, right in candidates:
            a, n = int(left["n"]), int(right["n"])
            if gcd(a, n) != 1:
                continue
            ra, rn = int(left["rank"]), int(right["rank"])
            if rn % ra != 0:
                continue
            product = a * n
            computed = pell_rank(product, rn)
            if computed != rn:
                continue
            out.append({
                "kind": "rank-preserving-product",
                "multiplier": a,
                "host": n,
                "multiplier_rank": ra,
                "host_rank": rn,
                "product": product,
                "rank": rn,
                "status": "VERIFIED_COMPUTATION",
            })
    unique = {(x["multiplier"], x["host"], x["product"]): x for x in out}
    return sorted(unique.values(), key=lambda x: (x["rank"], x["host"], x["multiplier"]))

def find_mirror_hosts(records: list[dict]) -> list[dict]:
    out: list[dict] = []
    for record in records:
        n = int(record["n"])
        rank = int(record["rank"])
        if gcd(n, MIRROR_PRODUCT) != 1 or rank % MIRROR_RANK_LCM != 0:
            continue
        states = [n, 13**2 * n, 31**2 * n, 13**2 * 31**2 * n]
        ranks = [pell_rank(value, rank) for value in states]
        if all(value == rank for value in ranks):
            out.append({
                "kind": "mirror-host-13-31",
                "host": n,
                "rank": rank,
                "square_rank": is_square(rank),
                "states": states,
                "state_ranks": ranks,
                "status": "VERIFIED_COMPUTATION",
            })
    return out

def find_missing_declared_bridges(report: dict) -> list[dict]:
    declared = relation_keys()
    missing: list[dict] = []
    for cluster in report["collision_clusters"]:
        key = ("rank-collision", tuple(sorted(cluster["members"])))
        if key not in declared:
            missing.append({
                "kind": "undeclared-collision-cluster",
                "members": cluster["members"],
                "rank": cluster["rank"],
                "status": "DISCOVERED_FROM_VERIFIED_RECORDS",
            })
    return missing

def build_report() -> dict:
    records = stored_records()
    report = {
        "atlas": "Brutus-Pell Atlas",
        "record_count": len(records),
        "collision_clusters": find_collision_bridges(records),
        "square_lcm_products": find_square_lcm_bridges(records),
        "rank_preserving_products": find_preserving_bridges(records),
        "mirror_hosts_13_31": find_mirror_hosts(records),
    }
    report["missing_declared_bridges"] = find_missing_declared_bridges(report)
    stored_n = {int(record["n"]) for record in records}
    new_products = {
        int(item["product"])
        for key in ("square_lcm_products", "rank_preserving_products")
        for item in report[key]
        if int(item["product"]) not in stored_n
    }
    report["verified_unstored_products"] = sorted(new_products)
    report["counts"] = {
        "collision_clusters": len(report["collision_clusters"]),
        "square_lcm_products": len(report["square_lcm_products"]),
        "rank_preserving_products": len(report["rank_preserving_products"]),
        "mirror_hosts_13_31": len(report["mirror_hosts_13_31"]),
        "missing_declared_bridges": len(report["missing_declared_bridges"]),
        "verified_unstored_products": len(report["verified_unstored_products"]),
    }
    return report

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    print(json.dumps(report["counts"], indent=2, sort_keys=True))
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
