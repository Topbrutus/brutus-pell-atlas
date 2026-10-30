# Zenodo Draft — Brutus–Pell Gate Laws and Post-Frontier Attacks

Author: **Gabriel St-Pierre**
Date: 2026-09-30
Status: DRAFT / NOT YET PUBLISHED

## Proposed title

**Brutus–Pell Gate Laws: Prime-Power Lifts, Square-Cover Construction, and Primitive-Quotient Witnesses**

## Abstract

This note organizes a set of exact relations and bounded computations for the Pell sequence P_0=0, P_1=1, P_(n+2)=2P_(n+1)+P_n, with emphasis on the rank of apparition z_P(m). The work separates standard Lucas/Pell theory from project-specific derived relations and finite computational observations. The main operational results are: a prime-power lift law with delayed lifting at the observed primes 13 and 31; an LCM construction principle for coprime moduli; rank absorption; a square-cover criterion; two Gate-8 congruence rails for odd square target ranks; primitive-quotient containment; a post-scan witness lower bound; and, for odd prime roots q, an equivalence showing that every prime factor of P_(q^2)/P_q has exact Pell rank q^2. A bounded continuation beyond k=10^10 is reported for gates 47, 71, and 83, with 4,853 additional prime candidates tested and no exact-rank hit.

## Definitions

- `z_P(m)` = least positive n such that m divides P_n.
- `F_C = {m : z_P(m)=C^2}` = square-rank fiber.
- For odd root q, a square gate targets rank q^2.
- `Q_q = P_(q^2)/P_q` = primitive square quotient used in gate factorization.

## Result L1 — Prime-Power Lift

For an odd prime p, write rho_p=z_P(p) and a_p=v_p(P_(rho_p)). Then the Pell specialization of the Lucas prime-power lifting relation is

`z_P(p^e)=rho_p * p^max(0,e-a_p)`.

Observed delayed-lift anchors:

- p=13: rho=7, a_13=2, ranks 7,7,91,1183,15379 through e=5.
- p=31: rho=30, a_31=2, ranks 30,30,930,28830,893730 through e=5.

Finite scan: among the 94 odd primes below 500, only 13 and 31 have a_p>1; both have depth 2. This is a bounded observation, not a uniqueness theorem.

Status: **KNOWN_THEORY / DERIVED_RELATION + VERIFIED_COMPUTATION**.

## Result L2 — Coprime Rank-LCM

For coprime Pell moduli m,n:

`z_P(mn)=lcm(z_P(m),z_P(n))`.

Status: **KNOWN_THEORY / DERIVED_RELATION**.

## Result L3 — Rank Absorption

If gcd(m,n)=1 and z_P(n) divides z_P(m), then

`z_P(mn)=z_P(m)`.

This explains rank-preserving extensions, including the verified 13^2 / 31^2 mirror-host behavior.

Status: **DERIVED_RELATION**.

## Result L4 — Square-Cover Criterion

For pairwise coprime n_i with r_i=z_P(n_i):

`z_P(product n_i)=lcm(r_i)`.

Therefore the product has square rank iff the LCM is a perfect square. Equivalently, every prime-exponent coordinate in the LCM must be even.

Example:

`lcm(36,75)=900=30^2`.

Status: **DERIVED_RELATION**.

## Result L5 — Odd Square Gate-8 Rails

For odd q and a prime p with z_P(p)=q^2, the admissible rails reduce to:

`p=kq^2+1,  k=0 (mod 8)`

or

`p=kq^2-1,  k=6 (mod 8)`.

All 25 stored resolved Level-3 prime witnesses obey one of these rails.

Status: **KNOWN_THEORY / DERIVED_RELATION + VERIFIED_COMPUTATION**.

## Result L6 — Primitive-Quotient Containment

If z_P(p)=q^2, then

`p | P_(q^2)/P_q`.

This provides a factorization route complementary to direct Gate-8 scanning.

Status: **KNOWN_THEORY / DERIVED_RELATION**.

## Result L7 — Post-Scan Gate-8 Lower Bound

If a Gate-8 search has been completed with no witness through k<=K, then the first possible future witness lies on the first admissible rail strictly above K.

For K=10^10, the next admissible coefficients are:

- minus rail: k=10,000,000,006;
- plus rail: k=10,000,000,008.

Thus any future witness must satisfy

`p >= min((K_minus)q^2-1,(K_plus)q^2+1)`.

For q=47 this gives p>=22,090,000,013,253; analogous exact bounds are recorded for 71,83,101,113,251,269.

Status: **DERIVED_FROM_BOUNDED_SEARCH**.

## Result L8 — Prime-Square Quotient Witness Equivalence

For odd prime q define

`Q_q=P_(q^2)/P_q`.

The Pell/Lucas quotient congruence gives

`Q_q ≡ (-1)^((q-1)/2) q (mod P_q)`.

Together with the prime-index Pell congruence `P_q ≡ (2/q) (mod q)`, this yields

`gcd(P_q,Q_q)=1`.

Hence if p is any prime divisor of Q_q, then p divides P_(q^2) but not P_q. Since z_P(p) divides q^2 and cannot divide q, and q is prime,

`z_P(p)=q^2`.

Therefore **every prime factor of Q_q is an exact q^2 witness**.

Regression anchors include q=3 (197), q=5 (1549,29201), q=7 (293,40710764977973), and q=13 (1013).

Status: **KNOWN_THEORY / DERIVED_RELATION**.

## Attack A1 — continuation beyond k=10^10

Search interval for q in {47,71,83}:

`10,000,000,001 <= k <= 10,000,100,000`.

Exact results:

| q | target q^2 | prime candidates tested | exact-rank hits |
|---:|---:|---:|---:|
| 47 | 2209 | 1673 | 0 |
| 71 | 5041 | 1590 | 0 |
| 83 | 6889 | 1590 | 0 |

Total additional prime candidates: **4,853**.
Total hits: **0**.

This extends the recorded no-hit boundary for these three gates to k<=10,000,100,000. It does not establish nonexistence.

## First post-frontier prime controls

| q | p | P_(q^2) mod p | exact q^2 witness |
|---:|---:|---:|---|
| 47 | 22,090,000,159,049 | 6,785,485,971,658 | no |
| 71 | 50,410,000,191,557 | 15,070,090,373,130 | no |
| 83 | 68,890,000,261,781 | 45,244,365,050,142 | no |

These are deterministic prime negative controls immediately beyond the previous frontier.

## ZELSTÉRÉOS machine trace

The visible/audible machine was used as a participatory trace layer.

Successful control salve:

`47 -> 71 -> 83`

Each returned PASS / RESISTE with 1,413 Z transformations, 16,956 active Zenodo evaluations, 5,301 F006 checks, 1,296/1,296 inverse reconstruction, and 23,670 total calculation events.

A subsequent salve with ~10^13 post-frontier prime controls exposed a machine scalability stall before sonification. That engineering anomaly is tracked separately and is not used as mathematical evidence.

## Literature boundary

General Lucas-sequence rank, divisibility, p-adic lifting, and primitive-divisor theory are established in the literature. This draft does not claim those general theorems as new.

Starting references:

- P. K. Ray, N. Irmak, B. K. Patel, *The rank of apparition of powers of Lucas sequence*, Turkish Journal of Mathematics 42 (2018), DOI 10.3906/mat-1705-116.
- C. Sanna, *The p-Adic Valuation of Lucas Sequences*, Fibonacci Quarterly 54(2) (2016), DOI 10.1080/00150517.2016.12427821.
- Y. Bilu, G. Hanrot, P. M. Voutier, *Existence of primitive divisors of Lucas and Lehmer numbers*, J. Reine Angew. Math. 539 (2001), DOI 10.1515/crll.2001.080.

## Publication boundary

- No bounded negative scan is a nonexistence proof.
- No ZELSTÉRÉOS PASS is a proof of a Pell theorem.
- Novelty claims require a dedicated literature review.
- Exact computations, source code, commit hashes, and machine traces should accompany the release.
