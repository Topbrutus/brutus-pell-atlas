# Brutus–Pell Gate 139

`139` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{139^2=19321}.$$

The first verified direct witness is

$$\boxed{p=12\,635\,933},$$

with

$$p=654\cdot19321-1.$$

Exact verification gives

$$\boxed{z_P(12\,635\,933)=19321=139^2}.$$

The witness is prime by the repository's deterministic 64-bit Miller–Rabin test and independently by SymPy.

## Search

With the exact odd-rank filter enabled, the recorded `k <= 200000` window contains 4,830 admissible prime candidates and exactly two verified hits.

The first hit occurs at `k = 654`, after 24 admissible prime candidates.
## Primitive part

The exact primitive quotient

$$\frac{P_{19321}}{P_{139}}$$

has 7,343 decimal digits, and the first witness divides it exactly.

## Preview root unlocked

Gate `139` is the last unresolved novel support of

$$\boxed{2\,989\,473=3\cdot67\cdot107\cdot139}.$$

Using the verified component witnesses

- `197` for root `3`;
- `454,134,173` for root `67`;
- `82,318,309` for root `107`;
- `12,635,933` for root `139`;

their pairwise gcds are all 1. Their product is

$$\boxed{93\,058\,096\,395\,323\,907\,653\,285\,057}.$$

Exact modular verification gives this product Pell rank

$$\boxed{2\,989\,473^2}.$$
Therefore preview root `2,989,473` is now `promotion_ready=true`.

This does **not** promote Level 3 into the core Rank Lattice; the Level-3 object remains simulation-only.

Machine-readable report: `reports/gate_139.json`.
