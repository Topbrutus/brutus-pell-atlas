# Brutus–Pell Gate 229

`229` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{229^2=52441}.$$

The verified witness is

$$\boxed{p=257\,753\,713\,526\,201}$$

with

$$\boxed{k=4\,915\,118\,200}$$

in

$$p=k\cdot52441+1.$$

Exact verification gives

$$\boxed{z_P(p)=52\,441=229^2}.$$
## Search history

The initial Python scan over

$$1\le k\le200000$$

tested **4,529 admissible prime candidates** and found no hit.

The generic C/OpenMP scanner then covered

$$200001\le k\le10^{10}$$

with **246,915,578** small-prime-sieve survivors subjected to exact Pell-rank testing.

Exactly one Pell-divisibility hit and one prime hit were found:

$$\boxed{k=4\,915\,118\,200}.$$

No smaller hit was found in the scanned range.
## Primitive part

The exact primitive quotient

$$Q_{229}=\frac{P_{52441}}{P_{229}}$$

has **19,986 decimal digits**.

Its SHA-256 fingerprint is

`8cc27fbbf87f1ab3b407a4e28695d3f654b7e0f0cefc792885ffd9eb188996e1`.

The witness divides this primitive quotient exactly.

## Level-3 consequences

### Root 4,809

$$4\,809=3\cdot7\cdot229.$$

Gate `229` is the only novel support, so this root is now

$$\boxed{\text{promotion-ready inside the preview}}.$$
### Root 8,008,342,512

After resolving `229`, this root remains blocked only by

$$\boxed{728\,561}.$$

## Status

- gate `229`: **RESOLVED**;
- witness kind: **compiled-prime-direct**;
- preview root `4,809`: **promotion-ready**;
- preview root `8,008,342,512`: still blocked by `728,561`;
- next never-worked Level-3 gate: **233**;
- Level 3 remains simulation-only.

## Reproduce

```bash
python -m calculation.gate_229
python -m calculation.frontier_level_3
```

Machine-readable report: `reports/gate_229.json`.
