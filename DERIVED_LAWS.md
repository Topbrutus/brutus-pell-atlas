# Brutus–Pell Derived Laws — next research layer

Author: **Gabriel St-Pierre**

Status: research note on branch `astra/derived-laws-next`.

This note records relations that are **derived from known Lucas/Pell divisibility theory and independently checked by exact computation in this repository**. It does not claim that the general theorems are new.

Scientific labels used here:

- `KNOWN_THEORY` — standard Lucas/Pell theory; literature attribution required.
- `DERIVED_RELATION` — consequence specialized to the Pell sequence.
- `VERIFIED_COMPUTATION` — finite exact computation performed by this repository.
- `RESEARCH_CANDIDATE` — project-level classification or naming, not a theorem claim.

---

## L1 — Prime-Power Lift

For an odd prime `p`, let

`rho_p = z_P(p)`

and define the lift depth

`a_p = v_p(P_{rho_p})`.

The Pell specialization of the Lucas prime-power rank law is

`z_P(p^e) = rho_p * p^max(0, e-a_p)`.

**Status:** `KNOWN_THEORY / DERIVED_RELATION`.

### Silent-square anchors

For `p=13`:

- `z_P(13)=7`
- `P_7=169=13^2`
- `a_13=2`

Therefore:

`z_P(13^e) = 7 * 13^max(0,e-2)`.

Exact ranks through the fifth power:

`7, 7, 91, 1183, 15379`.

For `p=31`:

- `z_P(31)=30`
- `v_31(P_30)=2`
- `a_31=2`

Therefore:

`z_P(31^e) = 30 * 31^max(0,e-2)`.

Exact ranks through the fifth power:

`30, 30, 930, 28830, 893730`.

This explains the project term **silent square**: the first square does not raise the rank, but the next powers resume the ordinary multiplicative lift.

### Finite scan

The repository test scans all **94 odd primes below 500** and computes `a_p` exactly. In this bounded range, the only primes with `a_p>1` are:

`13, 31`

and both have `a_p=2`.

This is a **finite computational observation**, not a universal uniqueness claim.

---

## L2 — Coprime Rank-LCM Law

For coprime Pell moduli `m,n`, the rank behaves by

`z_P(mn) = lcm(z_P(m), z_P(n))`.

**Status:** `KNOWN_THEORY / DERIVED_RELATION`.

The Atlas already contains exact examples:

- `73 * 97 = 7081`: `lcm(36,48)=144=12^2`
- `73 * 257 = 18761`: `lcm(36,64)=576=24^2`
- `73 * 149 = 10877`: `lcm(36,75)=900=30^2`
- `73 * 293 = 21389`: `lcm(36,49)=1764=42^2`
- `197 * 293 = 57721`: `lcm(9,49)=441=21^2`

The tests recompute every listed product rank directly.

---

## L3 — Rank Absorption

If `gcd(m,n)=1` and

`z_P(n) | z_P(m)`,

then L2 immediately gives

`z_P(mn)=z_P(m)`.

**Status:** `DERIVED_RELATION`.

This is the exact mechanism behind rank-preserving extensions and the 13/31 mirror host.

Examples:

- `z_P(293)=49` absorbs `z_P(13^2)=7`.
- `z_P(10877)=900` absorbs `z_P(31^2)=30`.
- `z_P(198477)=44100` absorbs both `7` and `30`.

Hence the four states

`n, 13^2 n, 31^2 n, 13^2 31^2 n`

all have rank `44100=210^2` for the verified host `n=198477`.

### Project classification

**Silent-Square Absorption** is useful project nomenclature for the special case where the absorbed factor is a silent square such as `13^2` or `31^2`.

The nomenclature is project-specific; the underlying rank identity is not claimed as new.

---

## L4 — Square-Cover Criterion

For pairwise coprime moduli `n_i`, let

`r_i = z_P(n_i)`.

By repeated use of L2,

`z_P(product n_i) = lcm(r_i)`.

Therefore the product has square Pell rank exactly when

`lcm(r_i)`

is a perfect square.

Equivalently, for every prime `q`, the coordinatewise maximum

`max_i v_q(r_i)`

must be even.

**Status:** `DERIVED_RELATION`.

This gives a direct construction/search rule for Square-Rank Fibers: search for component ranks whose prime-exponent maxima complete an even vector.

Example:

`z_P(73)=36=2^2*3^2`

and

`z_P(149)=75=3*5^2`.

The coordinatewise maxima are

`2^2 * 3^2 * 5^2 = 900 = 30^2`.

So `73*149` lands in `F_30` even though `75` itself is not a square.

This is a stronger construction principle than requiring every component rank to be square.

---

## Machine checks added

File:

`tests/test_derived_laws.py`

The test layer includes:

- 13 and 31 prime-power ranks through exponent 5;
- all odd primes below 100 through exponent 3: **72 prime-power checks**;
- finite lift-depth scan of all odd primes below 500;
- coprime LCM examples from the Atlas;
- square-cover roots `12, 21, 24, 30, 42`;
- rank-absorption examples;
- full `13^2 / 31^2` mirror-host state.

No finite scan is promoted to a universal theorem.

---

## Literature boundary

The p-adic Lucas-sequence framework underlying L1 is standard. Relevant starting references include:

- Carlo Sanna, *The p-Adic Valuation of Lucas Sequences*, Fibonacci Quarterly 54(2), DOI: `10.1080/00150517.2016.12427821`.
- P. K. Ray, N. Irmak, B. K. Patel, *The rank of apparition of powers of Lucas sequence*, Turkish Journal of Mathematics 42 (2018), DOI: `10.3906/mat-1705-116`.

A dedicated bibliography review is still required before any novelty statement or formal publication of this layer.
