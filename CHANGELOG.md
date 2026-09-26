# Changelog

## Unreleased

- Checkpoints Level-3 preview Gate 157 as `ACTIVE_UNRESOLVED` after exact scanning through `k = 10^10` with zero Pell-divisibility hits.
- Records the exact 9,375-digit primitive quotient `P_24649 / P_157`, its SHA-256 fingerprint, FactorDB status `U`, and light P-1/P+1 no-factor attempts.
- Adds the `active_unresolved_preview_gates` state and advances the next never-worked Level-3 gate to 163.

- Resolves Level-3 preview Gate 149 with prime witness 5,328,241 at k = 240; records a second verified witness and the 8,441-digit primitive quotient.
- Updates preview root 8,443,383 so that only gate 1453 remains unresolved.

- Resolves Level-3 preview Gate 139 with prime witness 12,635,933 at k = 654.
- Adds an explicit verified square-rank witness for preview root 2,989,473 and marks that root promotion-ready inside the simulation-only preview.

- Resolves Level-3 preview Gate 137 with prime witness 3,415,957 at k = 182.
- Advances the next never-worked Level-3 preview gate to 139.

- Audits Gate 113 factorization metadata from persistent reruns: P-1 and P+1 both use effective `B2=9,714,820` at `B1=50,000`, with exit status 0 and no factor; records audit paths and ECM exit statuses.

- Resolves Level-3 preview Gate 131 with prime witness 2,745,761 at k = 160.
- Records a second Gate-131 prime witness, 576,609,601.
- Advances the next never-worked Level-3 preview gate to 137.

- Checkpoints Level-3 preview Gate 113 as hard-unresolved after a compiled scan through k = 10^10 and recorded P-1/P+1/ECM campaigns.
- Advances the next never-worked Level-3 preview gate to 131.

- Adds the exact odd-rank Pell filter `p ? 1 (mod 4)` before future prime-support scans.
- Refines the Gate 47 C/OpenMP scanner to the only surviving `k mod 8` branches for odd square ranks.

- Adds a reusable generic C/OpenMP prime-support scanner with exact Pell-rank verification.
- Resolves Level-3 preview Gate 109 with prime witness 12,203,170,399,877 at k = 1,027,116,438.
- Advances the next never-worked Level-3 preview gate to 113.

- Resolves Level-3 preview Gate 103 with direct prime witness 403,141 at k = 38.
- Verifies exact rank `z_P(403,141)=10,609=103^2` and exact divisibility into the 4,022-digit primitive quotient `P_10609 / P_103`.
- Records three verified direct hits in the full `k <= 200,000` window; `109` becomes the next never-worked Level-3 gate.

- Adds a hard-unresolved checkpoint for Level-3 preview Gate 101.
- Records compiled Pell-divisibility scanning through `k = 10^10` with 496,754,167 sieve survivors and zero Pell hits.
- Records the 3,867-digit primitive quotient `P_10201 / P_101` and 12 P-1 plus 12 P+1 runs at `B1=10^6`, `B2=10^8`, with no factor.
- Distinguishes hard-unresolved Level-3 gates (`47, 71, 83, 101`) from never-worked gates; `103` is now the next never-worked gate.

- Adds a hard-unresolved checkpoint for Level-3 preview Gate 83.
- Records compiled Pell-divisibility scanning through k = 10^10 with 497,549,028 sieve survivors and zero Pell hits.
- Records the 2,606-digit primitive quotient `P_6889 / P_83` and P-1/P+1 campaigns through `B1=250,000`, `B2=40,000,000`, with no factor.

- Resolves Level-3 preview Gate 79 with primitive-part P-1 prime witness 2,266,870,750,557,409.
- Verifies exact rank `z_P(p)=6241=79^2` and exact divisibility into the 2,359-digit primitive quotient `P_6241 / P_79`.
- Adds per-door resolved/unresolved prime-support state to the Level-3 preview; root 711474 becomes promotion-ready while root 4276191 remains blocked by gate 18043.

- Resolves Level-3 preview Gate 73 with direct prime witness 159,869 at k = 30.
- Verifies exact rank `z_P(159,869)=5329=73^2` and exact divisibility into the 2,012-digit primitive quotient `P_5329 / P_73`.
- Records 3 admissible prime candidates to the first hit and 10,250 across the full k <= 200,000 window.

- Adds an ACTIVE_UNRESOLVED checkpoint for Level-3 preview Gate 71.
- Records direct scanning through k = 100,000,000 with 3,917,148 admissible prime candidates and four P-1/P+1 campaigns on the 1,903-digit primitive quotient.
- Deepens Gate 71 with an independent C/OpenMP scan through k = 10^10 and 493,447,289 sieve survivors, with zero Pell-divisibility hits.
- Extends Gate 71 P-1/P+1 campaigns through B1 = 1,000,000 and classifies it as a deep hard-unresolved frontier.

- Resolves Level-3 preview Gate 67 with direct prime witness 454,134,173 at k = 101,166.
- Verifies exact rank `z_P(454,134,173)=4489=67^2` and primitive-quotient divisibility.

- Resolves Level-3 preview Gate 59 with direct prime witness 31,217,609 at k = 8,968.
- Verifies exact rank `z_P(31,217,609)=3481=59^2` and divisibility into `P_3481 / P_59`.

- Resolves Level-3 preview Gate 53 with prime witness 13,747,841,783,933,689 from the primitive quotient `P_2809 / P_53`.
- Records the GMP-ECM P-1 stage-2 discovery and independent exact-rank verification `z_P(p)=2809=53^2`.

- Adds a formal Gate 47 hard-unresolved checkpoint.
- Extends deterministic Gate 47 direct scanning through k = 1,000,000,000 with 37,316,974 admissible prime candidates tested and zero hits.
- Records the 828-digit primitive quotient `P_2209 / P_47` and audits 1,224 archived factor-run outputs with no nontrivial factor recorded.
- Extends Gate 47 bounded Pell-divisibility scanning through `k = 10^10` with the reproducible C/OpenMP scanner; the `10^9..10^10` extension yields zero Pell-divisibility hits among 451,314,038 sieve survivors.
- Adds audited Gate 47 P-1/P+1 campaigns at `B1=10^7, B2=10^9` (12 runs each) and 12 ECM curves at `B1=3*10^6, B2=3*10^8`, all without a factor.
- Classifies Gate 47 as a `DEEP_COMPUTATIONAL_FRONTIER` while retaining `HARD_UNRESOLVED` and the explicit nonexistence boundary.

- Adds a simulation-only Frontier Level 3 preview: 326 closure nodes, 160 new mirror roots, and 210 novel prime-support gates.
- Adds verified preview witnesses for gates 13, 17, 19, 23, 29, 31, 37, and 43.
- Identifies 47 as the next unresolved Level-3 preview gate.

- Adds the Signed Mirror Layer with fixed-width decimal reversal and independent sign operation.
- Adds verified mirror-root fibers for roots 3, 12, 21, and 24.
- Expands the Rank Lattice to 16 verified nodes and gives every node at least one Pell square-rank witness.
- Refreshes bridge discovery to 230 square-LCM products, 169 rank-preserving products, and 3 mirror hosts within the current curated dataset.
- Expands regression coverage to 161 automated tests.
- Adds a Mirror Frontier for roots 48 and 861 without auto-promoting them into the core lattice.
- Verifies a prime witness for root 48 and a structured 648-digit witness for root 861.
- Documents universal Pell-term witnesses `z_P(P_m)=m` and the fast exact-target verifier.
- Adds Frontier Level 2 with exact mirror-root classification for 633, 2271, 4443, 8886, and 67731.
- Adds the Prime-Support Gate and compresses five mirror doors to three unresolved gates: 211, 757, and 1481.
- Verifies a prime witness for root 107: 82,318,309 with Pell rank 11,449 = 107^2.
- Adds a reproducible deterministic 64-bit prime-witness search engine and bounded-search semantics.
- Adds Gate 211 deep-scan tooling and report.
- Separates known primitive-divisor existence from the unresolved task of finding a compact explicit rank-44521 prime witness.
- Extends the Gate 211 congruence-filtered scan through k = 1,000,000,000: 33,061,422 admissible prime candidates tested, zero hits.
- Refactors prime-support searching into the generic `calculation/gate_scan.py` engine.
- Resolves Gate 757 with prime witness 21,855,419,538,769 at k = 38,138,832.
- Adds an explicit verified root-2271 witness 4,305,517,649,137,493.
- Reduces unresolved Level-2 prime-support gates from three to two: 211 and 1481.
- Resolves Gate 1481 with prime witness 13,169,009,631,553 at k = 6,004,032.
- Adds explicit verified frontier witnesses for roots 4443 and 8886.
- Reduces unresolved Level-2 prime-support gates to one: 211.
- Computes and fingerprints the exact 16,961-digit primitive part `P_44521 / P_211` for the Gate 211 factorization pivot.
- Records that the primitive quotient is coprime to `P_211` and pivots Gate 211 to dedicated factorization tooling.
- Resolves Gate 211 with verified primitive-part prime factor `172,757,248,399,252,109`; verifies a second prime factor `496,863,004,681,392,313`.
- Adds explicit verified Level-2 witnesses for roots 633 and 67731.
- Closes all four Level-2 prime-support gates while keeping Level 2 outside the core Rank Lattice.
- Records the primitive quotient as partially factored, with a 16,926-digit residual cofactor.
- Adds a validated optional OpenMP Gate 211 scanner that reproduces the Python reference window and canonical witness.

## v1.0.0 â€” 2026-09-25

- Creates the integrated Brutusâ€“Pell Atlas.
- Defines Square-Rank Fiber notation.
- Adds verified F_30, F_42, and F_210 anchor records.
- Adds verified rank-collision records.
- Adds the 13/31 mirror-host four-state structure.
- Adds the verified 1,203,930 rank-preserving example.
- Adds an exact modular Pell-rank engine.
- Adds automated regression tests and validation labels.
- Separates verified computation from known theory and open research candidates.
