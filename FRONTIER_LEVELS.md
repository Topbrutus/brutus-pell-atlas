# Brutus–Pell Frontier Levels

The frontier is expanded level by level. A mirror root is not promoted automatically into the core Rank Lattice.

## Level 2 source

Promoting the verified Level-1 mirror roots 48 and 861 would close the gcd/lcm lattice from 16 to 29 nodes.

Mirroring those 29 simulated nodes produces exactly five roots outside that promoted set:

$$\boxed{633,\ 2271,\ 4443,\ 8886,\ 67731}.$$

Their exact decimal factorizations are

$$633=3\cdot211,$$
$$2271=3\cdot757,$$
$$4443=3\cdot1481,$$
$$8886=2\cdot3\cdot1481,$$
$$67731=3\cdot107\cdot211.$$

## Prime-Support Gate

The 29-node simulated closure has prime support

$$\boxed{\{2,3,5,7,41\}}.$$

Therefore Level 2 introduces four new primes:

$$\boxed{107,\ 211,\ 757,\ 1481}.$$

A mirror root that introduces unresolved prime support remains at the frontier.
## Resolved new support: 107

A direct prime witness was found for the square-rank root 107:

$$\boxed{82\,318\,309}$$

and exact modular verification gives

$$\boxed{z_P(82\,318\,309)=11449=107^2}.$$

The witness is also verified prime by the repository's deterministic 64-bit Miller–Rabin implementation.

## Level 2 closure

All four new prime-support gates are now resolved:

| gate | verified prime witness | affected mirror roots |
|---:|---:|---|
| 107 | 82,318,309 | 67731 |
| 211 | 172,757,248,399,252,109 | 633, 67731 |
| 757 | 21,855,419,538,769 | 2271 |
| 1481 | 13,169,009,631,553 | 4443, 8886 |

Thus every Level-2 mirror root has all newly introduced prime support resolved. This closes the prime-support frontier at Level 2 without promoting those roots into the core Rank Lattice.

## Bounded searches

During gate resolution, direct-prime searches were performed over candidates

$$p=kq^2\pm1,$$

with $1\le k\le200000$. No exact-rank witness was found in the original `k <= 200,000` windows for 211, 757, or 1481. Deeper scans resolved 757 at `k = 38,138,832` and 1481 at `k = 6,004,032`. Gate 211 resisted direct scanning through `k = 1,000,000,000` and was then resolved by factoring the exact Pell primitive quotient `P_44521 / P_211`.

Each no-hit statement is strictly a bounded computational observation. Gate 211 was ultimately resolved by primitive-part factorization rather than by extending the direct scan to its much larger witness index.

## Reproduce the structural classification

```bash
python -m calculation.frontier_levels
```

The machine-readable report is `reports/frontier_level_2.json`.

## Policy

Level 2 stays outside the core lattice until an explicit promotion decision. This prevents mirror expansion from silently changing the mathematical object under study.
