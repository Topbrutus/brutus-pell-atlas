# Brutus–Pell Gate 163

`163` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{163^2=26569}.$$

A direct prime witness was found in the first bounded search:

$$\boxed{p=2\,247\,896\,813}.$$

It satisfies

$$p=84\,606\cdot26\,569-1.$$

Exact verification gives

$$\boxed{z_P(p)=26\,569=163^2}.$$

Primality is independently confirmed by the repository's deterministic 64-bit Miller–Rabin test and SymPy.
## Direct scan

The full recorded window

$$1\le k\le200000$$

tested **4,716 admissible prime candidates** and found one exact-rank hit, at

$$\boxed{k=84\,606}.$$

## Primitive part

The exact primitive quotient

$$Q_{163}=\frac{P_{26569}}{P_{163}}$$

has **10,108 decimal digits**.

Its SHA-256 fingerprint is

`f49c7c085612d37b724307ef544537cab5caff884dffe7d810fdc118252ad7f7`.

The explicit prime witness divides this primitive quotient exactly.
## Level-3 consequences

Gate `163` occurs in two preview roots.

### Root 2,820,552

$$2\,820\,552=2^3\cdot3\cdot7\cdot103\cdot163.$$

Gate `103` was already resolved, so resolving `163` removes the last unresolved novel support.

Therefore:

$$\boxed{2\,820\,552\text{ is promotion-ready inside the preview}}.$$

### Root 29,770,544,451

This root contains novel support

$$\{163,3851,15809\}.$$

After Gate 163 is resolved, it remains blocked by

$$\boxed{3851\text{ and }15809}.$$
## Status

- gate `163`: **RESOLVED**;
- witness kind: **prime-direct**;
- root `2,820,552`: **promotion-ready in the simulation-only preview**;
- root `29,770,544,451`: still unresolved;
- next never-worked Level-3 gate: **199**.

No Level-3 root is promoted into the core Rank Lattice by this result.

## Reproduce

```bash
python -m calculation.gate_163
python -m calculation.frontier_level_3
```

Machine-readable report: `reports/gate_163.json`.
