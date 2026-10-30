from __future__ import annotations

import json

from calculation.frontier_levels import is_prime_64
from calculation.gate_scan import scan_window
from calculation.mirror_frontier import exact_rank_target, pell_mod_fast

ROOTS = (47, 71, 83)
START_K = 10_000_000_001
END_K = 10_000_100_000

FIRST_POST_FRONTIER_PRIME_CONTROLS = (
    {"root": 47, "sign": 1, "k": 10_000_000_072, "p": 22_090_000_159_049},
    {"root": 71, "sign": -1, "k": 10_000_000_038, "p": 50_410_000_191_557},
    {"root": 83, "sign": -1, "k": 10_000_000_038, "p": 68_890_000_261_781},
)


def verify_prime_controls() -> list[dict]:
    rows = []
    for row in FIRST_POST_FRONTIER_PRIME_CONTROLS:
        root = row["root"]
        target = root * root
        p = row["p"]
        rows.append({
            **row,
            "target_rank": target,
            "prime": is_prime_64(p),
            "pell_target_residue": pell_mod_fast(target, p),
            "exact_rank": exact_rank_target(p, target),
        })
    return rows


def run_probe() -> list[dict]:
    return [
        scan_window(root, START_K, END_K, stop_after=1)
        for root in ROOTS
    ]


def main() -> None:
    payload = {
        "prime_controls": verify_prime_controls(),
        "window_probe": run_probe(),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
