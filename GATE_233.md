# Brutus–Pell Gate 233

`233` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{233^2=54289}.$$

## Direct-search history

A Python congruence-filtered scan over

$$1\le k\le200000$$

tested **4,466 admissible prime candidates** and found no witness.

The generic C/OpenMP scanner then covered

$$200001\le k\le10^{10}$$

with

$$\boxed{246\,891\,343}$$

small-prime-sieve survivors subjected to exact Pell-divisibility testing. It produced zero Pell-divisibility hits.

These are bounded negative observations only.

## Primitive part

The exact primitive quotient

$$Q_{233}=\frac{P_{54289}}{P_{233}}$$

has **20,692 decimal digits**.

SHA-256:

`489074e56744d22df377a0ce0c634d02ccfe7e89d015b0a9b0ef2eb22f873d3e`.

A FactorDB check on 2026-09-26 returned status `U` and no nontrivial factor at the time of the check.

## P-1 discovery

A GMP-ECM P-1 run with the known order factor `54289` preloaded,

`B1 = 50,000`, `B2 = 10,000,000`,

returned the factor

$$\boxed{p=179\,216\,201\,898\,552\,121}.$$

The factor divides $Q_{233}$ exactly.

## Prime witness and exact rank

The witness satisfies

$$p=54\,289\cdot3\,301\,151\,281\,080+1,$$

with $k\equiv0\pmod8$.

The repository's deterministic 64-bit primality checker verifies the witness as prime. Independent rank checks give

$$\boxed{z_P(p)=54289=233^2}.$$

- fast exact-target modular verification: PASS;
- original iterative Pell-rank engine: returns `54289`.

## Frontier role

Gate `233` occurs in the preview root

$$4\,209\,500\,564\,058=2\cdot3\cdot233\cdot3\,011\,087\,671.$$

Support `233` is now resolved, but gate `3,011,087,671` remains unresolved. The root is therefore not promotion-ready.

## Status

$$\boxed{\text{RESOLVED / VERIFIED COMPUTATION}}.$$

Level 3 remains simulation-only.

## Reproduce

```bash
python -m calculation.gate_233
```

Machine-readable report: `reports/gate_233.json`.
