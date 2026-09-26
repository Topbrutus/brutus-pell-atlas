# Brutus–Pell Gate 113

`113` is a hard-unresolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{113^2=12769}.$$

Known primitive-divisor theory guarantees that at least one prime witness of exact Pell rank `12769` exists. The unresolved task is to exhibit one explicitly.

## Direct searches

A Python congruence-filtered scan over

$$1\le k\le200000$$

tested 9,828 admissible prime candidates and found no witness.

The generic C/OpenMP scanner then covered

$$1\le k\le10^{10}$$

with

$$\boxed{496\,329\,793}$$

small-prime-sieve survivors subjected to exact Pell-rank testing. It produced zero Pell-divisibility hits and zero prime hits.
## Primitive part

The exact primitive quotient

$$\frac{P_{12769}}{P_{113}}$$

has 4,845 decimal digits.

Recorded factorization attempts:

- P-1: 10 runs, `B1 = 50,000`, effective `B2 = 14,856,276`; no factor;
- P+1: 10 runs, `B1 = 50,000`, effective `B2 = 19,411,780`; no factor;
- ECM: 12 curves, `B1 = 250,000`, `B2 = 40,000,000`; no factor.

For the ECM campaign, all 12 normalized outputs were exactly equal to the input primitive quotient.

## Frontier role

Gate `113` affects the Level-3 preview roots:

- `4,743,650,391`;
- `8,019,668,082`;
- `72,557,343,957`.

All three still require other novel prime support even if Gate 113 is eventually resolved.

## Status

$$\boxed{\text{HARD\_UNRESOLVED / DEEP\_COMPUTATIONAL\_FRONTIER}}.$$

This means only that no explicit witness was found in the recorded bounded searches and factorization campaigns. It is not a nonexistence statement.

Machine-readable report: `reports/gate_113_status.json`.
