# Brutus–Pell Gate 227

`227` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{227^2=51529}.$$

The canonical direct witness is

$$\boxed{p=309\,173}$$

with

$$\boxed{k=6}$$

in

$$p=k\cdot51529-1.$$

Exact verification gives

$$\boxed{z_P(309\,173)=51\,529=227^2}.$$
A second verified prime witness is

$$\boxed{105\,428\,333}$$

at

$$k=2046,$$

also on the `-1` branch.

## Direct search

The first hit occurs after exactly **one admissible prime candidate**.

The full recorded window

$$1\le k\le200000$$

tests **4,629 admissible prime candidates** and contains exactly two verified hits.

## Primitive part

The exact primitive quotient

$$Q_{227}=\frac{P_{51529}}{P_{227}}$$

has **19,638 decimal digits**.
Its SHA-256 fingerprint is

`ae347e0dc8e9224d442ebcc22234e48cba2e680a831a5e36c051b9c038c794d5`.

Both verified prime witnesses divide this primitive quotient exactly.

## Level-3 consequences

### Root 49,713

$$49\,713=3\cdot73\cdot227.$$

Gate `73` was already resolved, so Gate `227` removes the final unresolved novel support.

Therefore:

$$\boxed{49\,713\text{ is promotion-ready inside the preview}}.$$

### Root 61,455,314,793

After resolving `227`, this root remains blocked only by

$$\boxed{90\,242\,753}.$$
## Status

- gate `227`: **RESOLVED**;
- canonical witness: `309,173`;
- secondary witness: `105,428,333`;
- preview root `49,713`: **promotion-ready**;
- preview root `61,455,314,793`: still blocked by `90,242,753`;
- next never-worked Level-3 gate: **229**;
- Level 3 remains simulation-only.

## Reproduce

```bash
python -m calculation.gate_227
python -m calculation.frontier_level_3
```

Machine-readable report: `reports/gate_227.json`.
