# Brutus–Pell Gate 149

`149` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{149^2=22201}.$$

The first verified direct witness is

$$\boxed{p=5\,328\,241},$$

with

$$p=240\cdot22201+1.$$

Exact verification gives

$$\boxed{z_P(5\,328\,241)=22201=149^2}.$$

The witness is prime by the repository's deterministic 64-bit Miller–Rabin test and independently by SymPy.

## Search

With the exact odd-rank filter enabled, the recorded `k <= 200000` window contains 4,773 admissible prime candidates and exactly two verified hits.

The first hit occurs at `k = 240`, after 8 admissible prime candidates.
A second verified witness is

$$\boxed{304\,908\,533},$$

at `k = 13,734` on the `-1` branch.

## Primitive part

The exact primitive quotient

$$\frac{P_{22201}}{P_{149}}$$

has 8,441 decimal digits, and both verified witnesses divide it exactly.

## Frontier role

Gate `149` affects preview root

$$\boxed{8\,443\,383=3\cdot13\cdot149\cdot1453}.$$

The supports `13` and `149` are resolved, but gate `1453` remains unresolved.

Therefore this preview root is **not** promotion-ready yet, and Level 3 remains simulation-only.

Machine-readable report: `reports/gate_149.json`.
