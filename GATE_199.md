# Brutus–Pell Gate 199

`199` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{199^2=39601}.$$

The first verified direct witness is

$$\boxed{p=21\,788\,153\,393}.$$

with

$$\boxed{k=550\,192}$$

in

$$p=k\cdot39601+1.$$

Exact verification gives

$$\boxed{z_P(p)=39601=199^2}.$$
## Direct search

The strengthened congruence scan tested

$$1\le k\le550\,192$$

until the first hit.

Exactly **12,199 admissible prime candidates** were tested before the witness was reached.

No hit occurs in the preceding range.

## Primitive part

The exact primitive quotient

$$Q_{199}=\frac{P_{39601}}{P_{199}}$$

has **15,083 decimal digits**.

Its SHA-256 fingerprint is

`d0bc5faf08dbd33260e366121957898bc2a64148a5d2b07f5d3c8667288abeea`.

The witness divides this primitive quotient exactly.
## Level-3 consequence

Gate `199` occurs in preview root

$$75\,434\,532
=2^2\cdot3\cdot31\cdot199\cdot1019.$$

Gate `31` was already resolved.

After resolving `199`, the only unresolved novel support for this door is

$$\boxed{1019}.$$

Therefore the root is not promotion-ready yet.

## Status

- gate `199`: **RESOLVED**;
- witness kind: **prime-direct**;
- preview root `75,434,532`: still blocked by `1019`;
- next never-worked Level-3 gate: **227**;
- Level 3 remains simulation-only.
## Reproduce

```bash
python -m calculation.gate_199
python -m calculation.frontier_level_3
```

Machine-readable report: `reports/gate_199.json`.
