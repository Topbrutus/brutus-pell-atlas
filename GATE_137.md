# Brutus–Pell Gate 137

`137` is a resolved prime-support gate in the simulation-only Frontier Level 3 preview.

## Target

$$\boxed{137^2=18769}.$$

The first direct witness is

$$\boxed{p=3\,415\,957},$$

with

$$p=182\cdot18769-1.$$

Exact verification gives

$$\boxed{z_P(3\,415\,957)=18769=137^2}.$$

The witness is prime by the repository's deterministic 64-bit Miller–Rabin test and independently by SymPy.

## Search

In the recorded `k <= 200000` window, 4,780 admissible prime candidates were tested.

The first hit occurs after only 5 admissible prime candidates.
## Primitive part

The exact primitive quotient

$$\frac{P_{18769}}{P_{137}}$$

has 7,132 decimal digits, and the witness divides it exactly.

## Frontier role

Gate `137` affects the Level-3 preview root

$$\boxed{80\,860\,962}.$$

Gate `137` is now resolved, but this preview root still requires the hard-unresolved Gate `47`.

Therefore the root is not promotion-ready and Level 3 remains simulation-only.

Machine-readable report: `reports/gate_137.json`.
