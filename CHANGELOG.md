# Changelog

## Unreleased

- Resolves Level-3 preview Gate 53 with prime witness 13,747,841,783,933,689 from the primitive quotient `P_2809 / P_53`.
- Records the GMP-ECM P-1 stage-2 discovery and independent exact-rank verification `z_P(p)=2809=53^2`.

- Adds a formal Gate 47 hard-unresolved checkpoint.
- Extends deterministic Gate 47 direct scanning through k = 1,000,000,000 with 37,316,974 admissible prime candidates tested and zero hits.
- Records the 828-digit primitive quotient `P_2209 / P_47` and audits 1,224 archived factor-run outputs with no nontrivial factor recorded.

- Adds a simulation-only Frontier Level 3 preview: 326 closure nodes, 160 new mirror roots, and 210 novel prime-support gates.
- Adds verified preview witnesses for gates 13, 17, 19, 23, 29, 31, 37, and 43.
- Identifies 47 as the next unresolved Level-3 preview gate.

- Adds the Signed Mirror Layer with fixed-width decimal reversal and independent sign operation.
- Adds verified mirror-root fibers for roots 3, 12, 21, and 24.
- Expands the Rank Lattice to 16 verified nodes and gives every node at least one Pell square-rank witness.
- Refreshes bridge discovery to 230 square-LCM products, 169 rank-preserving products, and 3 mirror hosts within the current curated dataset.
- Expands regression coverage to 87 automated tests.
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
