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

For Gate 211, the congruential scan reached `k = 1,000,000,000` without an explicit rank-44521 prime witness. The computation therefore pivoted from candidate enumeration to the exact Pell primitive part.

For `n = 44521 = 211^2`, the relevant exact quotient is

`Q = P_44521 / P_211`.

The repository computes `Q` exactly, verifies exact division, records its 16,961-digit decimal length and SHA-256 fingerprint, and verifies `gcd(Q, P_211) = 1`.

A local copy of GMP-ECM 7.0.6 was extracted without system installation. A Pollard P-1 profile with the known factor `44521` preloaded into the group-order condition produced no non-trivial factor. A Williams P+1 profile on the same exact quotient produced the prime factor `172,757,248,399,252,109`.

That factor is then verified independently by deterministic 64-bit Miller?Rabin, SymPy primality, direct divisibility of `Q`, the fast exact-target Pell verifier, and the original iterative Pell-rank engine. Its exact rank is `44521`.

A second verified prime divisor of `Q`, `496,863,004,681,392,313`, is likewise checked for primality, exact divisibility, and exact Pell rank `44521`.

The primitive quotient is only partially factored. After removing both known prime factors, the residual cofactor has 16,926 decimal digits; no complete factorization is claimed.

## Optional native Gate 211 scanner

`calculation/pell_gate211_native.cpp` is an optional OpenMP accelerator for the Gate 211 congruence scan. It implements all four admissible `(k mod 8, sign)` classes, deterministic 64-bit Miller?Rabin, and exact Pell-rank testing by modular matrix exponentiation.

Validation under WSL with `g++ -O3 -march=native -fopenmp` reproduces the Python reference count exactly on `k = 1..200000`: 9,177 admissible prime candidates, zero hits. On `k = 3,880,354,178,905..3,880,354,178,915`, it recovers the canonical Gate 211 witness at `k = 3,880,354,178,910`, sign `-1`.

The native scanner is an execution accelerator only; the Python exact-rank verifier remains the reference validation path.
