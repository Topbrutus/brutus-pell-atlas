# Brutus–Pell Gate 59

`59` is a resolved prime-support gate in the Frontier Level 3 preview.

## Target

$$\boxed{59^2=3481}.$$

The direct congruence search found:

$$\boxed{p_{59}=31\,217\,609}$$

at

$$\boxed{k=8968},$$

with

$$p_{59}=8968\cdot3481+1.$$

Independent verification confirms that `p_59` is prime and

$$\boxed{z_P(p_{59})=3481=59^2}.$$

The witness also divides the exact primitive quotient

$$\frac{P_{3481}}{P_{59}},$$

which has 1,310 decimal digits.

## Level-3 role

Gate `59` appears in the preview roots `8,646,981` and `6,773,594,061`. Those roots still contain other novel prime support, so resolving `59` does not promote them.

## Status

$$\boxed{\text{RESOLVED}}.$$

Core Rank Lattice promotion is not performed.

## Reproduce

```bash
python -m calculation.gate_59
```

Machine-readable report: `reports/gate_59.json`.
