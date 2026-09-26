# Brutus–Pell Gate 71

`71` is an active unresolved prime-support gate in the Frontier Level 3 preview.

## Target

$$\boxed{71^2=5041}.$$

Primitive-divisor theory guarantees at least one prime witness of exact Pell rank 5041. The open task is to exhibit one explicitly.

## Direct scan

The congruence-filtered direct search covers

$$1\le k\le100\,000\,000$$

for candidates $p=5041k\pm1$ with the Lucas/Pell sign restriction.

A total of **3,917,148 admissible prime candidates** have received exact-rank testing, with zero hits.

The largest candidate bound is

$$\boxed{504\,100\,000\,001}.$$

## Primitive part

The exact primitive target is

$$Q_{71}=\frac{P_{5041}}{P_{71}},$$

an integer with **1,903 decimal digits**.

Recorded factorization attempts:

- P−1, `B1=50,000`, 10 runs — no factor;
- P+1, `B1=50,000`, 10 runs — no factor;
- P−1, `B1=250,000`, 20 runs — no factor;
- P+1, `B1=250,000`, 20 runs — no factor.

## Status

$$\boxed{\text{ACTIVE\_UNRESOLVED}}.$$

This is a bounded computational status, never a nonexistence claim.

Gate `71` currently occurs in preview roots `222,916,002`, `498,940,572`, and `679,699,401`.

## Reproduce

```bash
python -m calculation.gate_71
```

Machine-readable report: `reports/gate_71_status.json`.
