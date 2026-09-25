# Brutus–Pell Gate 757

`757` is the second prime-support gate of Frontier Level 2.

## Target

$$\boxed{757^2=573049}.$$

A direct explicit prime witness was found:

$$\boxed{p=21\,855\,419\,538\,769}.$$

It satisfies

$$p=38\,138\,832\cdot573049+1,$$

and independent exact checks give

$$\boxed{z_P(p)=573049=757^2}.$$

Primality is verified by the repository's deterministic 64-bit Miller–Rabin test and independently by SymPy during discovery.

## Search depth

The first hit occurred at

$$\boxed{k=38\,138\,832}.$$

Chronological admissible-prime accounting to that first hit:

- `k = 1..200000`: 8,205 candidates;
- `k = 200001..5000000`: 172,511 candidates;
- `k = 5000001..38138832`: 1,105,892 candidates;
- total: **1,286,608** admissible prime candidates tested.
## Mirror door unlocked

The Level-2 mirror root is

$$2271=3\cdot757.$$

Using the previously verified rank-$3^2$ witness

$$z_P(197)=9,$$

and the new 757 witness, define

$$N_{2271}=197\cdot21\,855\,419\,538\,769$$

$$\boxed{N_{2271}=4\,305\,517\,649\,137\,493}.$$

The factors are coprime and exact verification gives

$$\boxed{z_P(N_{2271})=5\,157\,441=2271^2}.$$

Thus the prime-support gate `757` is resolved and the mirror root `2271` has an explicit verified witness.

## Status

- gate `757`: **RESOLVED**;
- mirror root `2271`: **VERIFIED FRONTIER WITNESS**;
- automatic promotion into the core Rank Lattice: **not performed**.

## Reproduce

```bash
python -m calculation.gate_757
```

Machine-readable report: `reports/gate_757_scan.json`.
