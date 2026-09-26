# Brutus–Pell Gate 251

`251` is a hard-unresolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{251^2=63001}.$$

Known primitive-divisor theory guarantees that at least one prime witness of exact Pell rank `63001` exists. The unresolved task is to exhibit one explicitly.

## Direct searches

A Python congruence-filtered scan over

$$1\le k\le200000$$

tested **4,551 admissible prime candidates** and found no witness.

The generic C/OpenMP scanner then covered

$$200001\le k\le10^{10}$$

with

$$\boxed{246\,749\,264}$$

small-prime-sieve survivors subjected to exact Pell-divisibility testing. It produced zero Pell-divisibility hits and zero prime hits.

## Primitive part

The exact primitive quotient

$$Q_{251}=\frac{P_{63001}}{P_{251}}$$

has **24,020 decimal digits**.

SHA-256:

`4b2b8068a367ec812b83cca2c05902a5768f0e36e24c71de6b79c2ffd24067d6`.

Recorded bounded factorization attempts:

- P-1: 4 runs, `B1 = 20,000`, `B2 = 2,000,000`; no factor;
- P+1: 4 runs, `B1 = 20,000`, `B2 = 2,000,000`; no factor.

For both methods, the normalized output was exactly equal to the input primitive quotient.

## Frontier role

Gate `251` occurs in the preview root

$$4\,015\,052\,475.$$

That root also requires novel gate `30469`, so resolving Gate 251 alone would not make it promotion-ready.

## Status

$$\boxed{\text{HARD\_UNRESOLVED / DEEP\_COMPUTATIONAL\_FRONTIER}}.$$

This means only that no explicit witness was found in the recorded bounded searches and factorization campaigns. It is **not** a nonexistence statement.

## Reproduce

```bash
python -m calculation.gate_251
```

Machine-readable report: `reports/gate_251_status.json`.
