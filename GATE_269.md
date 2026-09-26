# Brutus–Pell Gate 269

`269` is a hard-unresolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{269^2=72361}.$$

Known primitive-divisor theory guarantees that at least one prime witness of exact Pell rank `72361` exists. The unresolved task is to exhibit one explicitly.

## Direct searches

A Python congruence-filtered scan over

$$1\le k\le200000$$

tested **4,529 admissible prime candidates** and found no witness.

The generic C/OpenMP scanner then covered

$$200001\le k\le10^{10}$$

with

$$\boxed{246\,634\,988}$$

small-prime-sieve survivors subjected to exact Pell-divisibility testing. It produced zero Pell-divisibility hits and zero prime hits.

## Primitive part

The exact primitive quotient

$$Q_{269}=\frac{P_{72361}}{P_{269}}$$

has **27,596 decimal digits**.

SHA-256:

`964ba924f1bc564d5435449b31dd3d7c0a2f8086343fdf95b872662d9642cefb`.

Recorded bounded factorization attempts:

- P-1: 4 runs, `B1 = 20,000`, `B2 = 2,000,000`; no factor.
- P+1: 4 runs, `B1 = 20,000`, `B2 = 2,000,000`; no factor.

For both methods, the normalized output was exactly equal to the input primitive quotient.

## Frontier role

Gate `269` is the only unresolved novel support remaining in

$$42\,771=3\cdot53\cdot269.$$

Gate `53` is already resolved. Therefore an explicit Gate-269 witness would make preview root `42,771` promotion-ready.

## Status

$$\boxed{\text{HARD\_UNRESOLVED / DEEP\_COMPUTATIONAL\_FRONTIER}}.$$

This means only that no explicit witness was found in the recorded bounded searches and factorization campaigns. It is **not** a nonexistence statement.

## Reproduce

```bash
python -m calculation.gate_269
```

Machine-readable report: `reports/gate_269_status.json`.
