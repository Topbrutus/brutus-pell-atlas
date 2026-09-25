# Brutus–Pell Gate 211

`211` was the last unresolved prime-support gate of Frontier Level 2. It is now resolved.

## Target

$$\boxed{211^2=44521}.$$

The target is an explicit prime $p$ satisfying

$$\boxed{z_P(p)=44521}.$$

## Known-theory existence

Primitive-divisor theory for Lucas sequences guarantees primitive prime divisors at this index; $44521$ is far beyond the exceptional small indices. Thus existence was not the unresolved question. The computational problem was to exhibit explicit compact factors and verify their exact Pell ranks.

References used by the project:

- R. D. Carmichael (1913), work on primitive divisors of Lucas sequences;
- M. Yabuta (2001), a proof of Carmichael's primitive-divisor theorem;
- Bilu, Hanrot, Voutier et al. (2001), primitive divisors of Lucas and Lehmer numbers.

## Congruence-filtered scan

For Pell numbers, viewed as $U_n(2,-1)$ with discriminant $D=8$, a prime rank witness satisfies

$$p\equiv\left(\frac{8}{p}\right)\pmod{z_P(p)}.$$

Hence a rank-$44521$ prime must have the form

$$p=44521k\pm1$$

with the sign matching $(8/p)$.

The bounded scan covered

$$1\le k\le1\,000\,000\,000$$

and tested **33,061,422** admissible prime candidates by exact Pell-rank verification, with zero hits in that window. The largest candidate bound was

$$44\,521\,000\,000\,001.$$

This remains a bounded negative search result only.

## Primitive-part pivot

Because

$$44521=211^2$$

the exact primitive Pell quotient used here is

$$\boxed{Q=\frac{P_{44521}}{P_{211}}}.$$

Exact computation gives:

- `P_211`: 81 decimal digits;
- `P_44521`: 17,042 decimal digits;
- `Q`: 16,961 decimal digits;
- exact division remainder: `0`;
- `gcd(Q,P_211)=1`;
- SHA-256 of the decimal expansion of `Q`:

`d516a24aaa5abcf58f1a232596db70b390174e74bab44b20ae0682896703321e`.

## Resolution

Using GMP-ECM 7.0.6 in P+1 mode on the exact primitive quotient, the project recovered the prime factor

$$\boxed{q_1=172\,757\,248\,399\,252\,109}.$$

It satisfies

$$q_1=3\,880\,354\,178\,910\cdot44521-1,$$

is verified prime by two independent primality implementations, divides $Q$ exactly, and has

$$\boxed{z_P(q_1)=44521}.$$

A second verified prime factor of the same primitive quotient is

$$\boxed{q_2=496\,863\,004\,681\,392\,313}.$$

It satisfies

$$q_2=11\,160\,194\,170\,872\cdot44521+1,$$

divides $Q$ exactly, is verified prime, and also has

$$\boxed{z_P(q_2)=44521}.$$

After removing both known prime factors, the remaining cofactor of $Q$ has **16,926 decimal digits**. The primitive part is therefore only partially factored; complete factorization is not claimed.

## Mirror doors unlocked

Using the canonical witness $q_1$:

$$N_{633}=197\cdot q_1$$

$$\boxed{N_{633}=34\,033\,177\,934\,652\,665\,473},$$

with

$$\boxed{z_P(N_{633})=633^2=400689}.$$

For the second affected root, using the verified root-$107$ witness $82\,318\,309$:

$$N_{67731}=197\cdot82\,318\,309\cdot q_1$$

$$\boxed{N_{67731}=2\,801\,553\,657\,476\,719\,924\,080\,045\,157},$$

with exact fast modular verification

$$\boxed{z_P(N_{67731})=67731^2=4\,587\,488\,361}.$$

## Status

- Gate `211`: **RESOLVED**.
- Level-2 roots `633` and `67731`: **VERIFIED FRONTIER WITNESSES**.
- Primitive quotient: **PARTIALLY FACTORED**, not fully factored.
- Core Rank Lattice promotion: **not performed**.

## Reproduce

```bash
python -m calculation.gate_211
python -m calculation.gate_211_primitive
```

Machine-readable reports: `reports/gate_211_scan.json` and `reports/gate_211_primitive.json`.
