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
- Verified preview gates: `13, 17, 19, 23, 29, 31, 37, 43, 53, 59, 67, 73, 79, 103, 109, 131, 137, 139, 149, 157, 163, 199, 227, 229, 233`.
- Hard-unresolved preview gates: `47, 71, 83, 101, 113`.
- Active-unresolved preview gates: none.
- Next unresolved preview gate: `47`.
- Next never-worked preview gate: `251`.
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


## Gate 137 status

- Target rank: `18,769 = 137^2`.
- Explicit prime witness: `3,415,957`.
- First hit: `k = 182` in `p = k*18,769 - 1`; 5 admissible prime candidates tested to the first hit.
- Primitive quotient `P_18769 / P_137`: 7,132 digits; witness divides it exactly.
- Affected preview root `80,860,962` still requires hard-unresolved Gate `47`.
- Gate `137`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `139`.

## Gate 139 status

- Target rank: `19,321 = 139^2`.
- Explicit prime witness: `12,635,933`.
- First hit: `k = 654` in `p = k*19,321 - 1`, after 24 admissible prime candidates.
- Full recorded window: `k <= 200,000`; 4,830 admissible prime candidates; two verified hits.
- Primitive quotient `P_19321 / P_139`: 7,343 decimal digits; first witness divides it exactly.
- Preview root `2,989,473`: explicit verified witness `93,058,096,395,323,907,653,285,057`, exact rank `2,989,473^2`.
- Gate `139`: resolved; preview root `2,989,473` is promotion-ready, but Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `149`.

## Gate 149 status

- Target rank: `22,201 = 149^2`.
- Explicit prime witness: `5,328,241`.
- First hit: `k = 240` in `p = k*22,201 + 1`, after 8 admissible prime candidates.
- Full recorded window: `k <= 200,000`; 4,773 admissible prime candidates; two verified hits.
- Primitive quotient `P_22201 / P_149`: 8,441 decimal digits; both witnesses divide it exactly.
- Preview root `8,443,383`: support `149` resolved, but gate `1453` remains unresolved.
- Gate `149`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `157`.

## Gate 157 status

- Target rank: `24,649 = 157^2`.
- Explicit prime witness: `42,720,756,963,545,450,051,849`.
- Witness identity: `p = 1,733,163,899,693,514,952 * 24,649 + 1`, with `k ? 0 (mod 8)`.
- Python scan: `k <= 200,000`; 4,725 admissible prime candidates; zero hits.
- C/OpenMP scan: `200,001 <= k <= 10^10`; 247,573,895 small-prime-sieve survivors; zero Pell-divisibility hits.
- Primitive quotient: `P_24649 / P_157`, 9,375 digits, SHA-256 `af8f60fea2efe11b26aa3d863d7bf2aac31b7e587830b539f3b572819d113621`; witness divides it exactly.
- Discovery: GMP-ECM curve 3 (`sigma = 15,700,003`), `B1 = 100,000`, `B2 = 10,000,000`.
- Primality: verified by a repository Pocklington certificate using the complete factorization `p-1 = 2^3 * 31 * 157^2 * 335957 * 20801960107` and base `3`.
- Exact rank: verified by fast exact-target testing and the original iterative Pell-rank engine.
- Affected preview root: `432,849 = 3*157*919`; gate `919` remains unresolved.
- Gate `157`: **resolved**; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `233`.

## Gate 163 status

- Target rank: `26,569 = 163^2`.
- Explicit prime witness: `2,247,896,813`.
- Direct-search hit: `k = 84,606` in `p = k*26,569 - 1`.
- Full `k <= 200,000` window: 4,716 admissible prime candidates; exactly one verified hit.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient: `P_26569 / P_163`, 10,108 decimal digits; witness divides it exactly.
- Preview root `2,820,552` is now promotion-ready because gate `103` was already resolved.
- Preview root `29,770,544,451` remains blocked by gates `3,851` and `15,809`.
- Gate `163`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `199`.

## Gate 199 status

- Target rank: `39,601 = 199^2`.
- Explicit prime witness: `21,788,153,393`.
- First hit: `k = 550,192` in `p = k*39,601 + 1`.
- Admissible prime candidates tested to first hit: `12,199`.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient: `P_39601 / P_199`, 15,083 decimal digits; witness divides it exactly.
- Preview root `75,434,532` now has resolved novel support `{31,199}` and remains blocked only by gate `1019`.
- Gate `199`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `227`.

## Gate 227 status

- Target rank: `51,529 = 227^2`.
- Canonical prime witness: `309,173`, first hit at `k = 6` in `p = k*51,529 - 1`.
- Exactly one admissible prime candidate was tested before the first hit.
- Secondary verified prime witness: `105,428,333` at `k = 2,046`.
- Full `k <= 200,000` window: 4,629 admissible prime candidates; exactly two verified hits.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient: `P_51529 / P_227`, 19,638 decimal digits; both witnesses divide it exactly.
- Preview root `49,713` is now promotion-ready because gate `73` was already resolved.
- Preview root `61,455,314,793` remains blocked only by gate `90,242,753`.
- Gate `227`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `229`.

## Gate 229 status

- Target rank: `52,441 = 229^2`.
- Explicit prime witness: `257,753,713,526,201`.
- Compiled-search hit: `k = 4,915,118,200` in `p = k*52,441 + 1`.
- Python pre-scan: `k <= 200,000`; 4,529 admissible prime candidates; zero hits.
- C/OpenMP extension: `200,001 <= k <= 10^10`; 246,915,578 small-prime-sieve survivors; exactly one Pell-divisibility hit and one prime hit.
- Exact rank: verified by fast modular target testing and the original iterative Pell-rank engine.
- Primitive quotient: `P_52441 / P_229`, 19,986 decimal digits; witness divides it exactly.
- Preview root `4,809` is now promotion-ready.
- Preview root `8,008,342,512` remains blocked only by gate `728,561`.
- Gate `229`: resolved; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `233`.

## Gate 233 status

- Target rank: `54,289 = 233^2`.
- Explicit prime witness: `179,216,201,898,552,121`.
- Witness identity: `p = 3,301,151,281,080 * 54,289 + 1`, with `k ? 0 (mod 8)`.
- Python scan: `k <= 200,000`; 4,466 admissible prime candidates; zero hits.
- C/OpenMP scan: `200,001 <= k <= 10^10`; 246,891,343 small-prime-sieve survivors; zero Pell-divisibility hits.
- Primitive quotient: `P_54289 / P_233`, 20,692 digits, SHA-256 `489074e56744d22df377a0ce0c634d02ccfe7e89d015b0a9b0ef2eb22f873d3e`; witness divides it exactly.
- Discovery: GMP-ECM P-1 with `B1=50,000`, `B2=10,000,000`, preloaded order factor `54,289`.
- Exact rank: verified by fast exact-target testing and the original iterative Pell-rank engine.
- Preview root `4,209,500,564,058` remains blocked by gate `3,011,087,671`.
- Gate `233`: **resolved**; Level 3 remains simulation-only.
- Next never-worked Level-3 gate: `251`.

## Gate 251 status

- Target rank: `63,001 = 251^2`.
- Direct Python scan through `k = 200,000`: 4,551 prime candidates, zero hits.
- Compiled scan through `k = 10^10`: 246,749,264 sieve survivors, zero Pell-divisibility hits.
- Primitive quotient `P_63001 / P_251`: 24,020 decimal digits.
- Bounded P-1/P+1 checkpoints: no factor.
- Classification: `HARD_UNRESOLVED / DEEP_COMPUTATIONAL_FRONTIER`.
- Affected Level-3 preview root `4,015,052,475` also requires gate `30,469`.

## Gate 269 status

- Target rank: `72,361 = 269^2`.
- Direct Python scan through `k = 200,000`: 4,529 prime candidates, zero hits.
- Compiled scan through `k = 10^10`: 246,634,988 sieve survivors, zero Pell-divisibility hits.
- Primitive quotient `P_72361 / P_269`: 27,596 decimal digits.
- Bounded P-1/P+1 checkpoints: no factor.
- Classification: `HARD_UNRESOLVED / DEEP_COMPUTATIONAL_FRONTIER`.
- Preview root `42,771` has gate `53` already resolved and is blocked only by gate `269`.
