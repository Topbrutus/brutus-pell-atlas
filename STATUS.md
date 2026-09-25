# Scientific Status

| Object | Status |
|---|---|
| Pell sequence recurrence | standard mathematics |
| Rank of apparition definition | standard mathematics |
| Stored anchor ranks | verified computation |
| Square-Rank Fiber notation | project definition |
| Rank Collision classification | project classification |
| Brutus–Pell Mirror Structure | project classification built from verified ranks |
| 13 / 31 silent-square behavior | verified computation; literature context separate |
| 198477 mirror host | verified computation |
| General mirror-host classification | research program |
| General square-rank generator theorem | requires explicit hypotheses/proof |
| Pell → elliptic bridge for this atlas | research direction only |

## Rule

A visually or numerically striking relation is not upgraded to a theorem or physical claim without a proof or an appropriate external validation.

## Mirror/lattice expansion

- Fixed-width decimal mirror: project representation convention.
- Signed mirror: project representation convention; sign does not alter divisibility after absolute-value projection.
- Roots 3, 12, 21, 24: verified square-rank fibers added.
- All 16 current gcd/lcm lattice nodes: at least one verified Pell square-rank witness.
- Mirror coincidence with verified fibers: exact computational observation; no universal mirror theorem claimed.

## Mirror frontier status

- Root 48: exact verified square-rank witness; direct witness 28,320,769 is prime.
- Root 861: exact verified square-rank witness constructed as `197 * 293 * P_1681`.
- Fiber non-emptiness: universal elementary fact via `z_P(P_m)=m`; not a novelty claim.
- Roots 48 and 861: frontier-only, not yet promoted into the 16-node core Rank Lattice.
- Decimal mirror relation: project representation layer; no universal Pell-mirror theorem claimed.

## Frontier Level 2 status

- Five Level-2 mirror roots: exact representation-level classification.
- Prime-support set before Level 2: `{2,3,5,7,41}`.
- Root 107 support: prime witness `82,318,309`, exact rank `107^2`, verified computation.
- Prime gates 211, 757, 1481: unresolved compact-witness targets.
- No-hit statements for `k <= 200,000`: bounded search observations only, never nonexistence claims.
- Level 2 is not promoted into the core Rank Lattice.

## Gate 211 status

- Target rank: `44521 = 211^2`.
- Existence of a prime with exact Pell rank 44521: `KNOWN_THEORY` via primitive prime divisors of Pell numbers.
- Congruence restriction `p ? (8/p) mod z_P(p)`: `KNOWN_THEORY` for Lucas sequences.
- Explicit compact prime witness: not yet found.
- Deep bounded scan: 200,010 admissible prime candidates tested through `k = 5,000,000`; zero hits.
- Interpretation: `NO_EXPLICIT_PRIME_WITNESS_IN_SCANNED_WINDOW`, not nonexistence.

## Gate 757 status

- Target rank: `573049 = 757^2`.
- Explicit prime witness: `21,855,419,538,769`.
- First hit: `k = 38,138,832` in `p = k*573049 + 1`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Level-2 root `2271`: explicit witness `4,305,517,649,137,493`, exact rank `2271^2`.
- Gate `757`: resolved; core-lattice promotion remains a separate decision.
- Remaining unresolved Level-2 prime gates: `211` and `1481`.
