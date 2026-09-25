from __future__ import annotations

import argparse
import json
from math import gcd

from calculation.pell_atlas import load_atlas, pell_rank, square_root_if_square

MIRROR_LEFT = 13
MIRROR_RIGHT = 31
MIRROR_BASE_LCM = 210

def stored_record(n: int) -> dict | None:
    atlas = load_atlas()
    for record in atlas["records"]:
        if int(record["n"]) == n:
            return record
    return None

def describe_number(n: int, max_steps: int) -> dict:
    rank = pell_rank(n, max_steps)
    root = square_root_if_square(rank)
    record = stored_record(n)
    return {
        "n": n,
        "rank": rank,
        "square_rank_root": root,
        "stored": record is not None,
        "roles": [] if record is None else record.get("role", []),
    }

def members_with_rank(rank: int) -> list[dict]:
    atlas = load_atlas()
    return [r for r in atlas["records"] if int(r["rank"]) == rank]

def members_in_fiber(root: int) -> list[dict]:
    return members_with_rank(root * root)

def mirror_13_31_compatibility(n: int, max_steps: int) -> dict:
    rank = pell_rank(n, max_steps)
    coprime = gcd(n, MIRROR_LEFT * MIRROR_RIGHT) == 1
    absorbs_both = coprime and rank % MIRROR_BASE_LCM == 0
    result = {
        "n": n,
        "rank": rank,
        "coprime_to_13x31": coprime,
        "rank_divisible_by_210": rank % MIRROR_BASE_LCM == 0,
        "mirror_compatible": absorbs_both,
    }
    if absorbs_both:
        states = [n, 13**2 * n, 31**2 * n, 13**2 * 31**2 * n]
        state_ranks = [pell_rank(value, rank) for value in states]
        result["states"] = states
        result["state_ranks"] = state_ranks
        result["verified_invariant"] = all(value == rank for value in state_ranks)
    return result

def inverse_square_rank(root: int) -> dict:
    rank = root * root
    members = members_with_rank(rank)
    return {
        "square_rank_root": root,
        "rank": rank,
        "stored_members": [int(r["n"]) for r in members],
        "member_count": len(members),
        "absorbs_13_31_mirror": root % MIRROR_BASE_LCM == 0,
    }

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query the Brutus-Pell Atlas")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--n", type=int, help="describe an input integer")
    group.add_argument("--rank", type=int, help="list stored inputs with this Pell rank")
    group.add_argument("--fiber", type=int, help="list stored inputs in F_C, i.e. rank C^2")
    group.add_argument("--mirror-host", type=int, help="test 13/31 mirror-host compatibility")
    group.add_argument("--inverse", type=int, help="query square-rank root C")
    parser.add_argument("--max-steps", type=int, default=1000000)
    return parser

def main() -> None:
    args = build_parser().parse_args()
    if args.n is not None:
        out = describe_number(args.n, args.max_steps)
    elif args.rank is not None:
        out = {"rank": args.rank, "stored_members": [int(r["n"]) for r in members_with_rank(args.rank)]}
    elif args.fiber is not None:
        out = {"fiber_root": args.fiber, "rank": args.fiber**2, "stored_members": [int(r["n"]) for r in members_in_fiber(args.fiber)]}
    elif args.mirror_host is not None:
        out = mirror_13_31_compatibility(args.mirror_host, args.max_steps)
    else:
        out = inverse_square_rank(args.inverse)
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
