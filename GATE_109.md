# Brutus–Pell Gate 109

`109` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{109^2=11881}.$$

A direct compiled scan found the prime witness

$$\boxed{p=12\,203\,170\,399\,877}.$$

It satisfies

$$p=1\,027\,116\,438\cdot11881-1,$$

and independent verification gives

$$\boxed{z_P(p)=11881=109^2}.$$

Primality was verified by the repository's deterministic 64-bit Miller–Rabin implementation and independently by SymPy.

## First-hit scan

The C/OpenMP scanner checked the full bounded interval

$$1\le k\le1\,027\,116\,438$$

and the witness above is the first exact Pell-rank hit in that recorded interval.
The scan reached the first hit after

$$\boxed{50\,631\,383}$$

small-prime-sieve survivors had been subjected to the exact Pell divisibility test.

The scan produced exactly one Pell hit and that hit is prime.

## Primitive part

The exact primitive quotient

$$\frac{P_{11881}}{P_{109}}$$

has 4,507 decimal digits. The witness divides it exactly. The residual cofactor has 4,493 decimal digits.

## Frontier role

Gate `109` appears in the Level-3 preview root

$$\boxed{23\,467\,643\,211}.$$

Resolving `109` does not make that root promotion-ready because it still requires the novel prime gate

$$\boxed{71\,766\,493}.$$

Level 3 remains simulation-only; no core-lattice promotion is implied.

## Reproduce

```bash
python -m calculation.gate_109
```

Machine-readable report: `reports/gate_109.json`.
