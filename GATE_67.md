# Brutus–Pell Gate 67

`67` is a resolved prime-support gate in the Frontier Level 3 preview.

## Target

$$\boxed{67^2=4489}.$$

The direct congruence search found

$$\boxed{p_{67}=454\,134\,173}$$

at

$$\boxed{k=101\,166},$$

with

$$p_{67}=101\,166\cdot4489-1.$$

Independent verification confirms primality and

$$\boxed{z_P(p_{67})=4489=67^2}.$$

The witness divides the exact primitive quotient

$$\frac{P_{4489}}{P_{67}},$$

which has 1,693 decimal digits.

## Level-3 role

Gate `67` appears in preview roots `2,989,473`, `7,624,533`, and `85,683,303,492`. Those roots retain other novel prime-support requirements.

## Status

$$\boxed{\text{RESOLVED}}.$$

No core-lattice promotion is performed.

## Reproduce

```bash
python -m calculation.gate_67
```

Machine-readable report: `reports/gate_67.json`.
