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
- Prime gates 107, 211, 757, and 1481: all resolved with explicit verified prime witnesses.
- All five Level-2 mirror roots have resolved new prime support.
- Level 2 remains frontier-only and is not promoted into the core Rank Lattice.

## Gate 211 status

- Target rank: `44521 = 211^2`.
- Congruence-filtered scan: 33,061,422 admissible prime candidates tested through `k = 1,000,000,000`; zero hits in that bounded window.
- Exact primitive quotient `P_44521 / P_211`: 16,961 digits, SHA-256 `d516a24aaa5abcf58f1a232596db70b390174e74bab44b20ae0682896703321e`.
- Canonical prime witness: `172,757,248,399,252,109`, exact rank `44521`.
- Secondary verified prime witness: `496,863,004,681,392,313`, exact rank `44521`.
- Both primes divide the exact primitive quotient.
- Primitive quotient status: partially factored; residual cofactor has 16,926 digits.
- Level-2 root `633`: verified witness `34,033,177,934,652,665,473`, exact rank `633^2`.
- Level-2 root `67731`: verified witness `2,801,553,657,476,719,924,080,045,157`, exact rank `67731^2`.
- Gate `211`: **resolved**.

## Gate 757 status

- Target rank: `573049 = 757^2`.
- Explicit prime witness: `21,855,419,538,769`.
- First hit: `k = 38,138,832` in `p = k*573049 + 1`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Level-2 root `2271`: explicit witness `4,305,517,649,137,493`, exact rank `2271^2`.
- Gate `757`: resolved; core-lattice promotion remains a separate decision.
- All Level-2 prime gates are resolved.

## Gate 1481 status

- Target rank: `2,193,361 = 1481^2`.
- Explicit prime witness: `13,169,009,631,553`.
- First hit in scanned windows: `k = 6,004,032` in `p = k*2,193,361 + 1`.
- Exact prime-witness rank: verified by fast target testing and the original iterative Pell-rank engine.
- Level-2 root `4443`: explicit verified witness `2,594,294,897,415,941`.
- Level-2 root `8886`: explicit verified witness `7,782,884,692,247,823`.
- Gate `1481`: resolved; core-lattice promotion remains a separate decision.
- All Level-2 prime gates are resolved.
