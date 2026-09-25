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

Five verified scan segments together cover

$$1\le k\le1\,000\,000\,000.$$

Results:

- `k = 1..200000`: 9,177 admissible prime candidates tested;
- `k = 200001..5000000`: 190,833 tested;
- `k = 5000001..100000000`: 3,374,781 tested;
- `k = 100000001..500000000`: 13,342,466 tested;
- `k = 500000001..1000000000`: 16,144,165 tested;
- total exact-rank prime candidates tested: **33,061,422**;
- explicit rank-$44521$ hits: **0**.

The largest candidate bound reached is

$$1\,000\,000\,000\cdot44521+1=44\,521\,000\,000\,001.$$

The later windows used a segmented small-prime sieve as an execution optimization. Surviving integers were still subjected to deterministic 64-bit primality testing followed by the same exact Pell-rank criterion.

Therefore the correct status remains

$$\boxed{\text{NO EXPLICIT PRIME WITNESS IN THE SCANNED WINDOW}}.$$

This is not a nonexistence statement.

## Primitive-part pivot

The OEIS primitive-part sequence for Pell numbers (A008555) defines the Sylvester?Pell cyclotomic part by removing the primitive parts attached to proper divisor indices. Since

$$44521=211^2$$

and `211` is prime, the relevant primitive part reduces here to

$$\boxed{\Phi^{(P)}_{44521}=\frac{P_{44521}}{P_{211}}}.$$

Exact computation gives:

- `P_211`: 81 decimal digits;
- `P_44521`: 17,042 decimal digits;
- primitive quotient: **16,961 decimal digits**;
- division remainder: `0`;
- `gcd(primitive quotient, P_211) = 1`;
- SHA-256 of the decimal primitive quotient:

`d516a24aaa5abcf58f1a232596db70b390174e74bab44b20ae0682896703321e`.

The primitive quotient is currently **unfactored** in this project. A direct SymPy Pollard p-1 attempt is operationally unsuitable at this size; the next factorization stage calls for a dedicated ECM/PARI/NTL-class engine rather than simply extending the congruential brute-force window.

## Reproduce

```bash
python -m calculation.gate_211
```

Machine-readable reports: `reports/gate_211_scan.json` and `reports/gate_211_primitive.json`.

Primitive-part fingerprint: `python -m calculation.gate_211_primitive`.
