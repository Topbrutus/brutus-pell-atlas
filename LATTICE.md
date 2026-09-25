# Brutus–Pell Rank Lattice

The Rank Lattice organizes verified Square-Rank Fibers by divisibility of their roots $C$ where

$$z_P(n)=C^2.$$

## Fully inhabited verified lattice

The current verified root set is

$$\boxed{\{1,3,6,7,12,21,24,30,42,60,84,120,168,210,420,840\}}.$$

This set is closed under

$$C_1\wedge C_2=\gcd(C_1,C_2)$$

and

$$C_1\vee C_2=\operatorname{lcm}(C_1,C_2).$$

Every node now has at least one stored integer witness whose Pell rank is exactly the node squared.

## Selected witnesses

| root C | rank C² | verified witness n |
|---:|---:|---:|
| 1 | 1 | 1 |
| 3 | 9 | 197 |
| 6 | 36 | 73 |
| 7 | 49 | 293 |
| 12 | 144 | 7081 |
| 21 | 441 | 57721 |
| 24 | 576 | 18761 |
| 30 | 900 | 10877 / 1801 |
| 42 | 1764 | 3529 |
| 60 | 3600 | 12752881 |
| 84 | 7056 | 24988849 |
| 120 | 14400 | 33788561 |
| 168 | 28224 | 66207569 |
| 210 | 44100 | 198477 |
| 420 | 176400 | 1405415637 |
| 840 | 705600 | 3723626997 |
## Selected joins

$$3\vee7=21,$$
$$6\vee7=42,$$
$$7\vee30=210,$$
$$12\vee30=60,$$
$$24\vee42=168,$$
$$30\vee42=210,$$
$$24\vee210=840.$$

## Mirror projection into the lattice

The representation layer lands on verified nodes:

$$30\to03\mapsto3,$$
$$42\to24,$$
$$210\to012\mapsto12,$$
$$12\leftrightarrow21.$$

That is why the mirror layer now changes the structure of the Atlas rather than remaining only a visual annotation.

## Reproduce

```bash
python -m calculation.rank_lattice
```

Machine-readable output: `reports/rank_lattice.json`.

Static diagram: `figures/rank-lattice.svg`.

## Boundary

The gcd/lcm lattice of positive integers is standard mathematics. `Brutus–Pell Rank Lattice` is the project classification obtained by attaching verified Pell square-rank fibers to that structure.
