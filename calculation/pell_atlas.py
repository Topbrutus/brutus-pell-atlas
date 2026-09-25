from __future__ import annotations

import json
from dataclasses import dataclass
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS_PATH = ROOT / "atlas" / "records.json"

@dataclass(frozen=True)
class RankCheck:
    n: int
    expected_rank: int
    computed_rank: int
    square_rank_root: int | None
    passed: bool

def pell_rank(n: int, max_steps: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    if max_steps < 1:
        raise ValueError("max_steps must be >= 1")
    p_prev, p_curr = 0, 1 % n
    for k in range(1, max_steps + 1):
        if p_curr == 0:
            return k
        p_prev, p_curr = p_curr, (2 * p_curr + p_prev) % n
    raise ValueError(f"no zero residue found for n={n} through step {max_steps}")

def square_root_if_square(value: int) -> int | None:
    root = isqrt(value)
    return root if root * root == value else None
def load_atlas(path: Path = RECORDS_PATH) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)

def verify_record(record: dict) -> RankCheck:
    n = int(record["n"])
    expected = int(record["rank"])
    computed = pell_rank(n, expected)
    root = square_root_if_square(computed)
    stored_root = record.get("square_rank_root")
    passed = computed == expected and root == stored_root
    return RankCheck(
        n=n,
        expected_rank=expected,
        computed_rank=computed,
        square_rank_root=root,
        passed=passed,
    )

def verify_atlas() -> list[RankCheck]:
    atlas = load_atlas()
    return [verify_record(record) for record in atlas["records"]]

def fiber_members(root: int) -> list[int]:
    target = root * root
    atlas = load_atlas()
    return [
        int(record["n"])
        for record in atlas["records"]
        if int(record["rank"]) == target
    ]
def main() -> None:
    checks = verify_atlas()
    failed = [check for check in checks if not check.passed]
    print(f"records = {len(checks)}")
    print(f"passed = {len(checks) - len(failed)}")
    print(f"failed = {len(failed)}")
    print(f"fiber_30 = {fiber_members(30)}")
    print(f"fiber_42 = {fiber_members(42)}")
    print(f"fiber_210 = {fiber_members(210)}")
    if failed:
        for check in failed:
            print(check)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
