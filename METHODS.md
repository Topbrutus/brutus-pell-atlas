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
