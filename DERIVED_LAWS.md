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

---

## L5 — Odd Square Gate-8 Congruence Rails

Let `q` be odd and suppose a prime `p` has exact Pell rank

`z_P(p)=q^2`.

The Lucas rank congruence forces

`q^2 | p-(2/p)`,

where `(2/p)` is the Legendre symbol.

Since `q^2` is odd, the Pell identity at odd index also forces `p=1 (mod 4)`. Combining these conditions with the modulo-8 formula for `(2/p)` leaves exactly two rails:

`p = k q^2 + 1` with `k = 0 (mod 8)`,

or

`p = k q^2 - 1` with `k = 6 (mod 8)`.

Equivalently:

- plus rail: `p = 1 (mod 8)`, `k = 0 (mod 8)`;
- minus rail: `p = 5 (mod 8)`, `k = 6 (mod 8)`.

**Status:** `KNOWN_THEORY / DERIVED_RELATION`.

### Current Atlas verification

All **25** stored resolved Level-3 prime witnesses obey one of the two rails exactly.

Examples:

- gate 13: `1013 = 6*13^2 - 1`;
- gate 37: `1566137 = 1144*37^2 + 1`;
- gate 139: `12635933 = 654*139^2 - 1`;
- gate 227: `309173 = 6*227^2 - 1`.

This is the mathematical reason the direct gate scanner can reject most `(k,sign)` pairs before primality or Pell-divisibility testing.

---

## L6 — Primitive-Quotient Containment

If a prime witness satisfies

`z_P(p)=q^2`

with `q>=1`, then `p` divides `P_(q^2)` but does not divide `P_q`, because its first appearance is at `q^2>q`.

Since the Pell sequence is a divisibility sequence and `q | q^2`,

`P_q | P_(q^2)`.

Therefore

`p | P_(q^2) / P_q`.

**Status:** `KNOWN_THEORY / DERIVED_RELATION`.

The repository adds direct quotient-divisibility checks for selected resolved gates `13,17,23,29,37,43,73`; many deeper gate modules already independently record the same primitive-quotient condition.

### Two-key gate strategy

L5 and L6 give two independent search routes for a square gate `q`:

1. **Congruence route:** search only the Gate-8 rails `p=kq^2 +/- 1`.
2. **Primitive route:** factor the exact quotient `P_(q^2)/P_q`.

A valid prime witness discovered by either route is then sent through exact rank verification.

This formalizes the search pattern already used successfully by the Atlas for direct witnesses and for difficult gates resolved through P-1/P+1/ECM factorization.


---

## L7 — Gate-8 Post-Scan Witness Lower Bound

Suppose an odd square gate `q` has been exhaustively checked with no witness through

`k <= K`

on the Gate-8 rails from L5.

The next legal coefficients are determined exactly by their residue classes:

- minus rail: first `k > K` with `k = 6 (mod 8)`;
- plus rail: first `k > K` with `k = 0 (mod 8)`.

Therefore every future explicit prime witness must satisfy

`p >= min(k_minus*q^2 - 1, k_plus*q^2 + 1)`.

**Status:** `DERIVED_FROM_BOUNDED_SEARCH`.

This is not a universal theorem about where a witness exists. It is an exact lower bound conditional on the recorded finite scan being complete through `K`.

### Specialization to K = 10^10

Since

`10^10 = 0 (mod 8)`,

the next legal coefficients are

`k_minus = 10,000,000,006`

and

`k_plus = 10,000,000,008`.

Thus the first possible post-frontier integer on either legal rail is the minus-rail value

`(10,000,000,006) q^2 - 1`.

For the current hard gates:

| q | target q^2 | exact witness lower bound after k<=10^10 |
|---:|---:|---:|
| 47 | 2209 | 22,090,000,013,253 |
| 71 | 5041 | 50,410,000,030,245 |
| 83 | 6889 | 68,890,000,041,333 |
| 101 | 10201 | 102,010,000,061,205 |
| 113 | 12769 | 127,690,000,076,613 |
| 251 | 63001 | 630,010,000,378,005 |
| 269 | 72361 | 723,610,000,434,165 |

The A1 continuation scan further raises the finite bound for q = 47,71,83 from `K=10^10` to `K=10,000,100,000`; those updated per-gate bounds can be regenerated mechanically with the same formula.

---

## L8 — Prime-Square Quotient Witness Equivalence

Let `q` be an odd prime and define

`Q_q = P_(q^2) / P_q`.

The Pell/Lucas divisibility congruence gives

`Q_q ≡ (-1)^((q-1)/2) q (mod P_q)`.

The prime-index Pell congruence also gives

`P_q ≡ (2/q) (mod q)`,

so `q` does not divide `P_q`. Therefore

`gcd(P_q,Q_q)=1`.

Now let `p` be a prime divisor of `Q_q`. Then `p | P_(q^2)` but `p` does not divide `P_q`. Hence `z_P(p)` divides `q^2` but does not divide `q`. Since q is prime, the only remaining divisor is `q^2`.

Therefore:

**every prime factor of Q_q is an exact Pell-rank q^2 witness.**

**Status:** `KNOWN_THEORY / DERIVED_RELATION`.

Operationally, for hard prime-root gates such as `47,71,83,101,113,251,269`, any prime factor obtained from `P_(q^2)/P_q` is already in the exact target fiber.

Regression anchors:

- q=3: 197 has rank 9;
- q=5: 1549 and 29201 have rank 25;
- q=7: 293 and 40710764977973 have rank 49;
- q=13: 1013 has rank 169.

The repository also verifies the quotient congruence and coprimality for every odd prime q<50.
