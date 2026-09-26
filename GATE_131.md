# Brutus–Pell Gate 131

`131` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{131^2=17161}.$$

The first direct witness is

$$\boxed{p=2\,745\,761}$$

with

$$p=160\cdot17161+1.$$

Exact verification gives

$$\boxed{z_P(2\,745\,761)=17161=131^2}.$$

The witness is prime by the repository's deterministic 64-bit Miller–Rabin test and independently by SymPy.

## Direct-search window

In the recorded window

$$1\le k\le200000,$$

4,832 admissible prime candidates were tested.
The first hit occurred after only 6 admissible prime candidates.

A second verified prime witness also occurs in the same window:

$$\boxed{576\,609\,601}$$

at

$$k=33600,$$

with the same exact Pell rank `17161`.

## Primitive part

The exact primitive quotient

$$\frac{P_{17161}}{P_{131}}$$

has 6,519 decimal digits, and the canonical witness `2,745,761` divides it exactly.

## Frontier role

Gate `131` appears in the Level-3 preview root

$$\boxed{80\,777\,607\,891}.$$

Resolving `131` does not make that root promotion-ready because it still requires the novel prime gates

$$\boxed{389\quad\text{and}\quad528383}.$$

Level 3 remains simulation-only.

Machine-readable report: `reports/gate_131.json`.
