# Methods

## Pell rank computation

The implementation computes the Pell sequence modulo $m$:

$$P_{k+2}\equiv2P_{k+1}+P_k\pmod m.$$

The first positive index whose residue is zero is returned as $z_P(m)$.

This avoids constructing the enormous integer Pell numbers themselves.

## Exactness

All rank checks in the reference dataset use integer modular arithmetic only.

No floating-point arithmetic is used for the rank engine.

## Regression strategy

Every anchor record is checked against its stored expected rank.

Mirror-host invariance and selected collision equalities are tested separately.

## Scope

The implementation is designed to verify the curated anchor atlas.

It is not yet optimized as a large-scale exhaustive rank-search engine.


## Fast exact-target verification

For large target ranks the frontier module computes `P_t mod n` by binary matrix exponentiation of the Pell companion matrix. This takes logarithmic time in the index `t` and uses exact integer modular arithmetic.

To certify a proposed exact target `t`, the verifier checks:

1. `P_t = 0 (mod n)`;
2. for every distinct prime divisor `q` of `t`, `P_(t/q) != 0 (mod n)`.

For a divisibility sequence such as the Pell sequence, the rank of apparition of a divisor of `P_t` divides `t`. Therefore, if a proper rank existed, it would divide `t/q` for at least one prime divisor `q` of `t`; the second check excludes all such proper ranks.

The fast matrix implementation is regression-tested against the original iterative modular recurrence on multiple moduli and indices. The 48 frontier witness is additionally checked by both engines independently.

## Universal Pell-term witness

For every positive `m`, `P_m` itself has rank exactly `m`: it divides `P_m`, while strict increase of the positive Pell sequence makes divisibility by any earlier positive term impossible. Thus the Atlas studies structured witnesses rather than mere fiber non-emptiness.

## Prime-Support Gate

For a simulated mirror expansion, each new root is factored and compared with the prime support already present in the current closure. Any newly introduced prime factor is treated as a gate.

A gate can be marked supported only after an exact square-rank witness for that prime root has been verified. Direct-prime searches use candidates `p = k*q^2 +/- 1`, deterministic Miller?Rabin primality for 64-bit candidates, and exact modular Pell-rank testing.

A failed bounded search records only `NO_HIT_IN_WINDOW`; it never establishes nonexistence.

## Gate 211 congruence-filtered scan

For Pell numbers, viewed as the Lucas sequence `U_n(2,-1)`, the discriminant is `D = 8`. For odd primes away from the discriminant, standard Lucas theory gives `p ? (D/p) (mod rho(p))`, where `rho(p)` is the rank of appearance.

For target rank `rho(p) = 44521`, candidate primes are therefore restricted to `p = 44521*k +/- 1`, with the sign required to equal the Legendre symbol `(8/p)`. The implementation applies this arithmetic filter first, then deterministic 64-bit Miller?Rabin primality, then exact modular Pell-rank verification.

The stored deep-scan report records the performed windows and their tested-prime counts; regression tests verify the filter mechanics but intentionally do not rerun the entire one-billion-`k` scan on every test suite invocation.

## Generic prime-support gate scanner

`calculation/gate_scan.py` factors the common Lucas/Pell congruence filter and exact-rank scan logic out of gate-specific modules. Gate-specific files now store only the target root, verified scan history, witness data, and structural consequences.

The 757 search used the same rule as Gate 211 and was parallelized only as an execution optimization; the candidate definition, primality test, and exact-rank criterion were unchanged.

## Primitive-part factorization pivot

For Gate 211, the congruential scan reached `k = 1,000,000,000` without an explicit rank-44521 prime witness. The next stage therefore works with the Pell primitive part directly.

For `n = 44521 = 211^2`, OEIS A008555 gives the Sylvester?Pell cyclotomic/primitive-part construction; because 211 is prime, the relevant exact quotient is `P_44521 / P_211`. The repository computes this quotient exactly, records its decimal length and SHA-256 fingerprint, and verifies that it is coprime to `P_211`.

The quotient has 16,961 decimal digits. General-purpose pure-Python Pollard p-1 is not treated as a completed factorization stage at this size; a dedicated ECM/PARI/NTL-class factorization engine is the appropriate next computational tool.
