# Brutus–Pell Gate 53

`53` is a resolved prime-support gate in the Frontier Level 3 preview.

## Target

$$\boxed{53^2=2809}.$$

A direct congruence scan through `k = 200,000` tested 10,593 admissible prime candidates and found no witness.

The exact primitive target is

$$Q_{53}=\frac{P_{2809}}{P_{53}},$$

an integer with **1,055 decimal digits**.

## Discovery

GMP-ECM 7.0.6, using Pollard P−1 with `2809` preloaded, found in stage 2:

$$\boxed{p_{53}=13\,747\,841\,783\,933\,689}.$$

The recorded discovery profile used

- `B1 = 50,000`;
- effective `B2 = 6,303,568`;
- preloaded order factor `2809`;
- exit status `14` (factor found).

Independent verification confirms:

$$p_{53}\mid Q_{53},$$

$$p_{53}=4\,894\,212\,098\,232\cdot2809+1,$$

and

$$\boxed{z_P(p_{53})=2809=53^2}.$$
## Level-3 role

Gate `53` appears in five current preview roots:

- `42,771`;
- `8,633,541`;
- `116,903,001`;
- `639,871,014`;
- `679,699,401`.

Resolving `53` removes that prime-support requirement, but none of those roots is automatically promoted because each still contains other novel prime support.

## Status

$$\boxed{\text{RESOLVED}}.$$

Core Rank Lattice promotion is not performed.

## Reproduce

```bash
python -m calculation.gate_53
```

Machine-readable report: `reports/gate_53.json`.
