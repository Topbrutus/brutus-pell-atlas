# Brutus–Pell Gate 157

`157` is an active-unresolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{157^2=24649}.$$

Known primitive-divisor theory guarantees that at least one prime witness of exact Pell rank `24649` exists. The unresolved task is to exhibit one explicitly.

## Direct searches

A Python congruence-filtered scan over

$$1\le k\le200000$$

tested **4,725 admissible prime candidates** and found no witness.

The generic C/OpenMP scanner then covered

$$200001\le k\le10^{10}$$

with

$$\boxed{247\,573\,895}$$

small-prime-sieve survivors subjected to exact Pell-rank testing.
It produced zero Pell-divisibility hits and zero prime hits.

The resulting direct candidate bound is

$$\boxed{246\,490\,000\,000\,001}.$$

## Primitive part

The exact primitive quotient

$$Q_{157}=\frac{P_{24649}}{P_{157}}$$

has **9,375 decimal digits**.

Its SHA-256 fingerprint is

`af8f60fea2efe11b26aa3d863d7bf2aac31b7e587830b539f3b572819d113621`.

A dated FactorDB check on 2026-09-25 returned status `U` and no nontrivial factor.

Recorded light factorization attempts:

- P-1: one run, `B1 = 50,000`, effective `B2 = 14,856,276`; no factor;
- P+1: one run, `B1 = 50,000`, effective `B2 = 19,411,780`; no factor.
## Frontier role

Gate `157` occurs in the preview root

$$432849=3\cdot157\cdot919.$$

Even if Gate 157 is resolved, that door still requires Gate `919`.

## Status

$$\boxed{\text{ACTIVE\_UNRESOLVED}}.$$

This is deliberately weaker than `HARD_UNRESOLVED`: the bounded scan is deep, but only light P-1/P+1 factorization attempts have been recorded so far.

The negative searches do **not** establish nonexistence.

## Reproduce

```bash
python -m calculation.gate_157
```

Machine-readable report: `reports/gate_157_status.json`.
