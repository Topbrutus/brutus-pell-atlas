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

## Frontier Level 3 preview status

- Level 3 is `SIMULATION_ONLY_NOT_PROMOTED`.
- Simulated closure: 326 nodes.
- New mirror roots: 160.
- Novel prime-support gates: 210.
- Verified preview gates: `13, 17, 19, 23, 29, 31, 37, 43, 53, 59, 67, 73, 79, 103`.
- Next unresolved preview gate: `47`.
- Hard-unresolved preview gates: `47, 71, 83, 101, 113`.
- Next never-worked preview gate: `137`.
- No Level-2 or Level-3 root is promoted into the core lattice by this preview.

## Gate 47 status

- Target rank: `2209 = 47^2`.
- Known theory: a primitive prime divisor, hence an exact rank-2209 prime witness, exists.
- Explicit witness: not yet found.
- Direct Python scan: `k <= 1,000,000,000`; 37,316,974 admissible prime candidates tested; zero hits.
- Future odd-rank scans now also enforce the exact quadratic-residue filter `p ? 1 (mod 4)`; historical counts above remain unchanged.
- Independent C/OpenMP Pell-divisibility scan: bounded coverage through `k = 10,000,000,000`; the `10^9..10^10` extension tested 451,314,038 small-prime-sieve survivors and produced zero Pell-divisibility hits.
- Primitive quotient: `P_2209 / P_47`, 828 decimal digits.
- Archived factor-run outputs checked: 1,224; none differs from the input quotient.
- New audited campaigns: 12 P+1 runs at `B1=10^7, B2=10^9`; 12 P-1 runs at the same bounds; 12 ECM curves at `B1=3*10^6, B2=3*10^8`; no factor.
- Dated FactorDB observation (2026-09-25): status `C`, no nontrivial factor returned.
- Status: `HARD_UNRESOLVED` / `DEEP_COMPUTATIONAL_FRONTIER`.
- No Level-3 promotion is implied.

## Gate 53 status

- Target rank: `2809 = 53^2`.
- Explicit prime witness: `13,747,841,783,933,689`.
- Primitive quotient: `P_2809 / P_53`, 1,055 digits.
- Discovery: GMP-ECM P-1, stage 2, `B1=50,000`, effective `B2=6,303,568`, preloaded order factor `2809`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Gate `53`: resolved; affected Level-3 preview roots still require other novel prime support.

## Gate 59 status

- Target rank: `3481 = 59^2`.
- Explicit prime witness: `31,217,609`.
- Direct-search hit: `k = 8,968` in `p = k*3481 + 1`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient `P_3481 / P_59`: 1,310 digits; witness divides it exactly.
- Gate `59`: resolved; affected preview roots still require other novel prime support.

## Gate 67 status

- Target rank: `4489 = 67^2`.
- Explicit prime witness: `454,134,173`.
- Direct-search hit: `k = 101,166` in `p = k*4489 - 1`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient `P_4489 / P_67`: 1,693 digits; witness divides it exactly.
- Gate `67`: resolved; affected Level-3 preview roots still require other novel prime support.

## Gate 71 status

- Target rank: `5041 = 71^2`.
- Explicit prime witness: not yet found.
- Direct Python scan: `k <= 100,000,000`; 3,917,148 admissible prime candidates; zero hits.
- Independent C/OpenMP scan: `100,000,001 <= k <= 10,000,000,000`; 493,447,289 small-prime-sieve survivors; zero Pell-divisibility hits.
- Primitive quotient: `P_5041 / P_71`, 1,903 decimal digits.
- P-1/P+1 campaigns extended through `B1=1,000,000`, `B2=100,000,000`; no factor.
- Status: `HARD_UNRESOLVED` / `DEEP_COMPUTATIONAL_FRONTIER`, never a nonexistence claim.

## Gate 83 status

- Target rank: `6889 = 83^2`.
- Explicit prime witness: not yet found.
- Direct Python scan: `k <= 200,000`; 10,113 admissible prime candidates; zero hits.
- Independent C/OpenMP scan: `k <= 10,000,000,000`; 497,549,028 small-prime-sieve survivors across recorded windows; zero Pell-divisibility hits.
- Primitive quotient: `P_6889 / P_83`, 2,606 decimal digits.
- P-1/P+1 campaigns through `B1=250,000`, `B2=40,000,000`; no factor.
- Status: `HARD_UNRESOLVED` / `DEEP_COMPUTATIONAL_FRONTIER`, never a nonexistence claim.

## Gate 79 status

- Target rank: `6241 = 79^2`.
- Explicit prime witness: `2,266,870,750,557,409`.
- Witness identity: `p = 363,222,360,288 * 6241 + 1`.
- Primitive quotient: `P_6241 / P_79`, 2,359 decimal digits; witness divides it exactly.
- Discovery: GMP-ECM P-1 with `B1=50,000`, `B2=10,000,000`, preloaded order factor `6241`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Level-3 preview root `711474` is now promotion-ready; `4276191` still requires gate `18043`.
- Gate `79`: resolved; Level 3 remains simulation-only.

## Gate 73 status

- Target rank: `5329 = 73^2`.
- Explicit prime witness: `159,869`.
- First hit: `k = 30` in `p = k*5329 - 1`; 3 admissible prime candidates tested to the first hit.
- Full recorded window: `k <= 200,000`; 10,250 admissible prime candidates; exactly one verified hit.
- Exact rank: verified by fast target testing and the original iterative Pell-rank engine.
- Primitive quotient `P_5329 / P_73`: 2,012 digits; witness divides it exactly.
- Gate `73`: resolved; Level 3 remains simulation-only.

## Gate 101 status

- Target rank: `10201 = 101^2`.
- Explicit prime witness: not yet found.
- C/OpenMP exact Pell-divisibility scan: `k <= 10,000,000,000`; 496,754,167 small-prime-sieve survivors; zero Pell-divisibility hits.
- Primitive quotient: `P_10201 / P_101`, 3,867 decimal digits.
- Archived light P-1/P+1 attempts found no factor.
- Strong campaigns: 12 P-1 and 12 P+1 runs at `B1=1,000,000`, `B2=100,000,000`; all outputs equal the unchanged primitive quotient.
- Affected Level-3 preview roots: `76,327,215` and `299,902,623,543,471`.
- Status: `HARD_UNRESOLVED` / `DEEP_COMPUTATIONAL_FRONTIER`, never a nonexistence claim.
- Next never-worked Level-3 gate: `109`.

## Gate 103 status

- Target rank: `10,609 = 103^2`.
- Explicit prime witness: `403,141`.
- First hit: `k = 38` in `p = k*10,609 - 1`; 2 admissible prime candidates tested to the first hit.
- Full recorded window: `k <= 200,000`; 9,898 admissible prime candidates; 3 verified hits.
- Exact rank: verified by fast target testing and the original iterative Pell-rank engine.
- Primitive quotient `P_10609 / P_103`: 4,022 digits; witness divides it exactly.
- Affected preview roots remain blocked by other novel prime gates.
- Gate `103`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `109`.

## Gate 109 status

- Target rank: `11,881 = 109^2`.
- Explicit prime witness: `12,203,170,399,877`.
- First recorded compiled hit: `k = 1,027,116,438` in `p = k*11,881 - 1`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient `P_11881 / P_109`: 4,507 digits; witness divides it exactly.
- Level-3 preview root `23,467,643,211` still requires gate `71,766,493`.
- Gate `109`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `113`.


## Gate 113 status

- Target rank: `12,769 = 113^2`.
- Explicit prime witness: not yet found.
- Direct Python scan: `k <= 200,000`; 9,828 admissible prime candidates; zero hits.
- Generic C/OpenMP exact Pell scan: `k <= 10,000,000,000`; 496,329,793 small-prime-sieve survivors; zero Pell-divisibility hits.
- Primitive quotient: `P_12769 / P_113`, 4,845 decimal digits.
- P-1: 10 runs at `B1=50,000`, effective `B2=14,856,276`; no factor.
- P+1: 10 runs at `B1=50,000`, effective `B2=19,411,780`; no factor.
- ECM: 12 curves at `B1=250,000`, `B2=40,000,000`; all normalized outputs equal the input quotient.
- Status: `HARD_UNRESOLVED` / `DEEP_COMPUTATIONAL_FRONTIER`, never a nonexistence claim.
- Next never-worked Level-3 gate: `131`.


## Gate 131 status

- Target rank: `17,161 = 131^2`.
- Canonical prime witness: `2,745,761`.
- First hit: `k = 160` in `p = k*17,161 + 1`; 6 admissible prime candidates tested to the first hit.
- Second verified prime witness: `576,609,601` at `k = 33,600`.
- Primitive quotient `P_17161 / P_131`: 6,519 digits; canonical witness divides it exactly.
- Affected Level-3 preview root `80,777,607,891` still requires gates `389` and `528,383`.
- Gate `131`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `137`.
