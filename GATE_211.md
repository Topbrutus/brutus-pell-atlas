# Brutus–Pell Gate 211

`211` is the first unresolved prime-support gate of Frontier Level 2.

## Target

$$\boxed{211^2=44521}.$$

The computational target is an explicit prime $p$ satisfying

$$\boxed{z_P(p)=44521}.$$

Such a prime would immediately provide explicit support for the Level-2 mirror roots `633` and `67731`.

## Existence is known theory

Carmichael's primitive-divisor theorem for Pell numbers implies that every Pell number $P_n$ with $n>1$ has a prime divisor that divides no earlier positive Pell term.

For $n=44521$, any such primitive prime divisor $p$ has

$$z_P(p)=44521.$$

Therefore the existence of a prime witness for the 211 gate is not an open question inside this project. The remaining task is computational: exhibit a sufficiently compact explicit witness.

References:

- R. D. Carmichael (1913), *On the numerical factors of the arithmetic forms α^n ± β^n*.
- M. Yabuta (2001), *A simple proof of Carmichael's theorem on primitive divisors*.
- Bilu, Hanrot, Voutier et al. (2001), work on primitive divisors of Lucas and Lehmer numbers.
## Lucas/Pell congruence filter

For a prime $p$ away from the discriminant, the rank of appearance in a Lucas sequence satisfies

$$p\equiv\left(\frac{D}{p}\right)\pmod{z_P(p)}.$$

For Pell numbers the discriminant is $D=8$. Thus a prime with rank $44521$ must satisfy

$$p=44521k\pm1$$

with the sign matching the Legendre symbol $(8/p)$.

This known-theory filter is applied before primality and exact-rank testing.

## Deep scan

Two verified scan segments together cover

$$1\le k\le5\,000\,000.$$

Results:

- `k = 1..200000`: 9,177 admissible prime candidates tested;
- `k = 200001..5000000`: 190,833 admissible prime candidates tested;
- total exact-rank prime candidates tested: **200,010**;
- explicit rank-$44521$ hits: **0**.

The largest candidate bound reached is

$$5\,000\,000\cdot44521+1=222\,605\,000\,001.$$

Therefore the correct status is:

$$\boxed{\text{NO EXPLICIT PRIME WITNESS IN THE SCANNED WINDOW}}.$$

This is not a nonexistence statement.

## Reproduce

```bash
python -m calculation.gate_211
```

Machine-readable report: `reports/gate_211_scan.json`.
