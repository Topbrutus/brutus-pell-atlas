# Brutus–Pell Gate 157

`157` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{157^2=24649}.$$

## Bounded direct-search history

A Python congruence-filtered scan over

$$1\le k\le200000$$

tested **4,725 admissible prime candidates** and found no witness.

The generic C/OpenMP scanner then covered

$$200001\le k\le10^{10}$$

with

$$\boxed{247\,573\,895}$$

small-prime-sieve survivors subjected to exact Pell-divisibility testing. It produced zero Pell-divisibility hits.

Those bounded negative scans remain valid historical observations; they are not nonexistence claims.

## Primitive part

The exact primitive quotient

$$Q_{157}=\frac{P_{24649}}{P_{157}}$$

has **9,375 decimal digits**.

SHA-256:

`af8f60fea2efe11b26aa3d863d7bf2aac31b7e587830b539f3b572819d113621`.

A FactorDB check on 2026-09-26 reported status `C` and no nontrivial factor at the time of the check.

## Factorization history

- P-1: 8 runs, `B1 = 100,000`, `B2 = 10,000,000`; no factor.
- P+1: 8 runs, `B1 = 100,000`, `B2 = 10,000,000`; no factor.
- ECM checkpoint: 12 curves, `B1 = 250,000`, `B2 = 40,000,000`; all 12 outputs equal the original primitive quotient.
- A later 12-curve ECM campaign at `B1 = 1,000,000`, `B2 = 100,000,000` was deliberately stopped before any curve completed. It is recorded as `ABORTED_INCOMPLETE` and is not counted as negative evidence.

Finally, a lighter independent 12-curve ECM campaign at

`B1 = 100,000`, `B2 = 10,000,000`

found a nontrivial factor on curve 3 (`sigma = 15,700,003`):

$$\boxed{p=42\,720\,756\,963\,545\,450\,051\,849}.$$

The factor divides $Q_{157}$ exactly.

## Prime certificate

The witness satisfies

$$p=24\,649\cdot1\,733\,163\,899\,693\,514\,952+1,$$

with $k\equiv0\pmod 8$.

Its predecessor is fully factored:

$$p-1=2^3\cdot31\cdot157^2\cdot335957\cdot20801960107.$$

All listed factors are verified prime by the repository's deterministic 64-bit checker. Pocklington verification with base

$$\boxed{a=3}$$

passes for every distinct prime factor of $p-1$, giving an autonomous primality proof for the 23-digit witness.

## Exact Pell rank

Two independent repository paths agree:

$$\boxed{z_P(p)=24649=157^2}.$$

- fast exact-target modular verification: PASS;
- original iterative Pell-rank engine: returns `24649`.

## Frontier role

Gate `157` occurs in

$$432849=3\cdot157\cdot919.$$

Gate `157` is now resolved, but that preview root still requires Gate `919`. Therefore `432849` is **not** promoted or marked promotion-ready.

## Status

$$\boxed{\text{RESOLVED / VERIFIED COMPUTATION}}.$$

Level 3 remains simulation-only.

## Reproduce

```bash
python -m calculation.gate_157
```

Machine-readable report: `reports/gate_157_status.json`.
