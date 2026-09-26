# Brutus–Pell Gate 73

`73` is a resolved prime-support gate in the Frontier Level 3 preview.

## Target

$$\boxed{73^2=5329}.$$

A direct prime witness is

$$\boxed{p=159\,869}.$$

It satisfies

$$p=30\cdot5329-1,$$

and exact verification gives

$$\boxed{z_P(159\,869)=5329=73^2}.$$

Primality was verified independently during discovery, and the repository verifies the exact Pell rank with both the fast target test and the iterative rank engine.
## Direct scan

The congruence-filtered search over

$$p=k\cdot5329\pm1$$

found the first witness at

$$\boxed{k=30}.$$

Only **3 admissible prime candidates** had been tested when that first hit appeared.

The full recorded search window

$$1\le k\le200\,000$$

contains **10,250 admissible prime candidates** and exactly one verified rank-$5329$ hit.

## Primitive part

The exact primitive quotient is

$$Q_{73}=\frac{P_{5329}}{P_{73}}.$$

It has **2,012 decimal digits**, and the witness $159\,869$ divides it exactly.
## Level-3 role

Gate `73` supplies verified prime support to the affected preview roots recorded in `reports/gate_73.json`.

This does not promote those roots automatically: each affected root may still require other novel prime-support gates.

The numerical coincidence that the first hit occurs at $k=30$ is recorded only as a bounded computational observation. It is **not** presented as a general relation between roots 73 and 30.

## Status

- gate `73`: **RESOLVED**;
- explicit prime witness: **verified**;
- Level 3: **simulation only, not promoted**.

## Reproduce

```bash
python -m calculation.gate_73
```

Machine-readable report: `reports/gate_73.json`.
