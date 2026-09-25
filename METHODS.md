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
