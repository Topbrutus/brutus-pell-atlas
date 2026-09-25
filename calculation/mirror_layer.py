from __future__ import annotations

import json
from pathlib import Path

from calculation.pell_atlas import load_atlas

ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "mirror_layer.json"

def reverse_fixed_width(value: int, width: int | None = None) -> dict:
    if value < 0:
        raise ValueError("value must be nonnegative; sign is handled separately")
    token = str(value) if width is None else f"{value:0{width}d}"
    if width is not None and len(token) > width:
        raise ValueError("value does not fit requested width")
    mirrored = token[::-1]
    return {
        "input_token": token,
        "mirror_token": mirrored,
        "mirror_value": int(mirrored),
        "width": len(token),
    }

def signed_mirror_orbit(value: int, width: int | None = None) -> dict:
    base = reverse_fixed_width(value, width)
    token = base["input_token"]
    mirror = base["mirror_token"]
    return {
        **base,
        "orbit_tokens": [token, mirror, "-" + token, "-" + mirror],
        "orbit_values": [int(token), int(mirror), -int(token), -int(mirror)],
    }

def verified_square_roots() -> set[int]:
    return {
        int(r["square_rank_root"])
        for r in load_atlas()["records"]
        if r.get("square_rank_root") is not None
    }

def members_for_root(root: int) -> list[int]:
    target = root * root
    return sorted(
        int(r["n"])
        for r in load_atlas()["records"]
        if int(r["rank"]) == target
    )

def build_report() -> dict:
    roots = verified_square_roots()
    cases = [
        (30, 2),
        (42, 2),
        (210, 3),
        (12, 2),
        (24, 2),
        (21, 2),
    ]
    rows = []
    for root, width in cases:
        orbit = signed_mirror_orbit(root, width)
        mirror_root = orbit["mirror_value"]
        rows.append({
            "root": root,
            "rank": root * root,
            "width": width,
            "mirror_token": orbit["mirror_token"],
            "mirror_root": mirror_root,
            "mirror_rank": mirror_root * mirror_root,
            "root_supported": root in roots,
            "mirror_supported": mirror_root in roots,
            "root_members": members_for_root(root),
            "mirror_members": members_for_root(mirror_root),
            "signed_orbit_tokens": orbit["orbit_tokens"],
            "signed_orbit_values": orbit["orbit_values"],
            "sign_invariant_at_root_magnitude": True,
        })
    return {
        "name": "Brutus-Pell Signed Mirror Layer",
        "representation_rule": "reverse fixed-width decimal tokens; sign is a separate involution",
        "arithmetic_rule": "negative sign does not change divisibility by Pell terms after absolute-value projection",
        "verified_square_roots": sorted(roots),
        "mirror_cases": rows,
    }

def save_report(report: dict, path: Path = REPORT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    report = build_report()
    save_report(report)
    for row in report["mirror_cases"]:
        print(
            f"{row['root']:>3} -> {row['mirror_token']} = {row['mirror_root']:<3} "
            f"supported={row['root_supported']} mirror_supported={row['mirror_supported']}"
        )
    print(f"report = {REPORT_PATH}")

if __name__ == "__main__":
    main()
