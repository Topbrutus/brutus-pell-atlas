# Brutus–Pell Signed Mirror Layer

The mirror layer is a representation layer placed above the arithmetic Atlas.

## Fixed-width decimal mirror

A mirror operation reverses a fixed-width decimal token. Leading zeroes are preserved as representation:

$$30\leftrightarrow03,$$

$$42\leftrightarrow24,$$

$$210\leftrightarrow012.$$

After projection back to integers:

$$03\mapsto3,\qquad012\mapsto12.$$

This distinction matters: the representation `03` is not the same token as `3`, even though both project to the integer 3.

## Verified Pell support

The mirrored roots are supported by exact square-rank fibers:

$$z_P(197)=9=3^2,$$

$$z_P(7081)=144=12^2,$$

$$z_P(57721)=441=21^2,$$

$$z_P(18761)=576=24^2.$$

Thus the currently verified mirror relations include

$$30\leftrightarrow03,$$
$$12\leftrightarrow21,$$
$$24\leftrightarrow42,$$
$$210\leftrightarrow012.$$
## Signed mirror

Sign is treated as a separate involution from decimal reversal.

For a fixed-width token $x$, the four representation states are

$$x,\quad R(x),\quad -x,\quad -R(x).$$

For example:

$$\boxed{30,\ 03,\ -30,\ -03}.$$

At the divisibility level, sign does not create a new Pell rank because

$$(-n)\mid P_k\iff n\mid P_k.$$

So the signed layer can encode orientation/state while the Pell rank depends on the magnitude after integer projection.

## Reproduce

```bash
python -m calculation.mirror_layer
```

Machine-readable output: `reports/mirror_layer.json`.

## Boundary

Decimal reversal and sign operations are representation conventions. Their occurrence alongside verified Pell fibers is an exact observation in this Atlas, not by itself a claim of a new universal number-theoretic law.
