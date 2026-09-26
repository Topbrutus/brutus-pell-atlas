# Brutus–Pell Atlas

**An integrated, reproducible map of Pell ranks, square-rank fibers, collisions, mirror structures, lifts, and rank-preserving constructions.**

Author: **Gabriel St-Pierre**

## Core definition

Let the Pell sequence be

$$P_0=0,\qquad P_1=1,\qquad P_{n+2}=2P_{n+1}+P_n.$$

For an integer $m\ge1$, define its Pell rank of apparition

$$\boxed{z_P(m)=\min\{k\ge1:m\mid P_k\}.}$$

The atlas uses this rank as the central coordinate.

## Square-Rank Fiber

For a positive integer $C$, define

$$\boxed{\mathcal F_C=\{m\ge1:z_P(m)=C^2\}.}$$

This lets the same square rank be studied from the output side rather than only from the input side.
## Atlas coordinates

Each verified record may be connected through:

```text
INPUT n
  ↓
PELL RANK z_P(n)
  ↓
SQUARE-RANK FIBER F_C
  ↙          ↓          ↘
COLLISION   MIRROR      LIFT
  ↓          ↓          ↓
RANK-PRESERVING / INVERSE CONSTRUCTIONS
```

## Verified anchor records

| n | factorization / role | z_P(n) | atlas role |
|---:|---|---:|---|
| 13 | mirror prime | 7 | silent-square anchor |
| 169 | $13^2$ | 7 | silent-square anchor |
| 31 | mirror prime | 30 | silent-square anchor |
| 961 | $31^2$ | 30 | silent-square anchor |
| 73 | prime | 36 | square-rank generator component |
| 149 | prime | 75 | square-rank generator component |
| 10877 | $73\cdot149$ | 900 | $\mathcal F_{30}$ |
| 293 | prime | 49 | square-rank generator component |
| 21389 | $73\cdot293$ | 1764 | $\mathcal F_{42}$ |
| 3529 | prime | 1764 | $\mathcal F_{42}$ |
| 9261 | $21^3$ | 1764 | $\mathcal F_{42}$ |
| 130 | $2\cdot5\cdot13$ | 42 | rank-preserving component |
| 1203930 | $130\cdot21^3$ | 1764 | $\mathcal F_{42}$ |
| 198477 | $3^3\cdot7351$ | 44100 | mirror host, $\mathcal F_{210}$ |
| 33542613 | $13^2\cdot198477$ | 44100 | mirror-host state |
| 190736397 | $31^2\cdot198477$ | 44100 | mirror-host state |
| 32234451093 | $13^2\cdot31^2\cdot198477$ | 44100 | full mirror-host state |

All anchor ranks above are recomputed by the included modular Pell recurrence tests.

## Scientific boundary

The atlas organizes and tests arithmetic structures. It does **not** claim that standard Pell-sequence theory is new, and it does not infer physical meaning from numerical structure.

Names beginning with `Brutus–Pell` are nomenclature for the organization, search strategies, and candidate classifications used in this project.
## Reproduce

Python 3.10+; no third-party packages:

```bash
python calculation/pell_atlas.py
python -m unittest discover -s tests -v
```

## Contents

- `ATLAS.md` — integrated research map.
- `SCHEMA.md` — record and relation schema.
- `METHODS.md` — exact modular computation method.
- `STATUS.md` — claim boundaries and validation levels.
- `atlas/records.json` — verified anchor records.
- `calculation/pell_atlas.py` — rank engine and atlas verifier.
- `tests/test_atlas.py` — automated regression tests.
- `figures/brutus-pell-atlas.svg` — visual map.
- `.zenodo.json` / `CITATION.cff` — archival metadata.

## Existing Brutus series

This atlas is intended to connect, not replace, independently archived Brutus objects and future Pell-specific candidate relations.

## License

MIT License. See `LICENSE`.

## Query the atlas

The repository now includes a bidirectional query engine:

```bash
python -m calculation.query_atlas --n 3529 --max-steps 1764
python -m calculation.query_atlas --rank 1764
python -m calculation.query_atlas --fiber 42
python -m calculation.query_atlas --inverse 210
python -m calculation.query_atlas --mirror-host 198477 --max-steps 44100
```

See `QUERY.md` for the supported query modes and scientific boundaries.

## Find missing bridges

The Atlas can scan its verified records for additional exact connections:

```bash
python -m calculation.bridge_finder
```

See `BRIDGES.md` and `reports/bridge_report.json`.

## Rank Lattice

The verified Square-Rank Fiber roots are also organized as a strict gcd/lcm lattice:

```bash
python -m calculation.rank_lattice
```

See `LATTICE.md` and `reports/rank_lattice.json`.

## Signed Mirror Layer

Fixed-width decimal reversal is tracked separately from integer value and Pell rank. Verified mirror projections now include:

```text
30  <-> 03  -> root 3
42  <-> 24  -> root 24
210 <-> 012 -> root 12
12  <-> 21  -> root 21
```

See `MIRROR_LAYER.md` and `reports/mirror_layer.json`.

## Fully inhabited lattice

Every node in the current 16-node gcd/lcm Rank Lattice now has at least one stored exact Pell square-rank witness.

## Mirror Frontier

The first unpromoted mirror continuation is tracked separately from the 16-node core lattice:

- `84 -> 48`, with prime witness `28,320,769` and exact rank `48^2 = 2304`;
- `168 -> 861`, with structured witness `197 * 293 * P_1681` and exact rank `861^2 = 741321`.

These roots are verified but remain frontier-only because automatic gcd/lcm closure would expand the lattice from 16 to 29 nodes.

See `MIRROR_FRONTIER.md` and `reports/mirror_frontier.json`.

## Frontier Level 2

The mirror expansion is controlled by a Prime-Support Gate. The five Level-2 mirror roots are `633`, `2271`, `4443`, `8886`, and `67731`; the new prime support is `107`, `211`, `757`, and `1481`. All four gates now have explicit verified prime witnesses, so Level 2 is closed at the prime-support layer while remaining outside the core Rank Lattice.

See `FRONTIER_LEVELS.md` and `reports/frontier_level_2.json`.

## Gate 211

Gate `211` is resolved. A congruence-filtered scan tested 33,061,422 admissible prime candidates through `k = 1,000,000,000` without a hit; the search then pivoted to the exact 16,961-digit primitive quotient `P_44521 / P_211`. GMP-ECM 7.0.6 in P+1 mode exposed prime factor `172,757,248,399,252,109`, whose exact Pell rank is `44,521 = 211^2`. A second verified prime factor, `496,863,004,681,392,313`, has the same exact rank. These witnesses unlock explicit Level-2 witnesses for roots `633` and `67731`.

See `GATE_211.md`, `reports/gate_211_scan.json`, and `reports/gate_211_primitive.json`.

An optional validated OpenMP accelerator is available at `calculation/pell_gate211_native.cpp`; it reproduces the Python reference scan on the regression window and recovers the canonical witness in a local neighborhood test.

## Gate 757

Gate `757` is resolved by the explicit prime witness `21,855,419,538,769`, with exact Pell rank `573,049 = 757^2`. Combining it with the verified root-3 witness `197` gives an explicit Level-2 mirror witness for root `2271`:

`4,305,517,649,137,493`, with exact Pell rank `5,157,441 = 2271^2`.

See `GATE_757.md` and `reports/gate_757_scan.json`.

## Gate 1481

Gate `1481` is resolved by the explicit prime witness `13,169,009,631,553`, with exact Pell rank `2,193,361 = 1481^2`. It unlocks explicit Level-2 witnesses for roots `4443` and `8886`.

All Level-2 prime-support gates are now resolved; promotion into the core lattice remains a separate decision.

See `GATE_1481.md` and `reports/gate_1481_scan.json`.

## Frontier Level 3 preview

After closing Frontier Level 2, the next mirror expansion is kept as a simulation-only preview. The simulated gcd/lcm closure contains 326 nodes; mirroring it produces 160 roots outside that closure and 210 novel prime-support gates.

Twelve preview gates now have verified witnesses: `13, 17, 19, 23, 29, 31, 37, 43, 53, 59, 67, 73`. Gate `47` remains the earliest hard-unresolved gate; Gate `71` is tracked separately as active-unresolved.

See `reports/frontier_level_3_preview.json`.

## Gate 47

Gate `47` is the first hard unresolved gate in the Level-3 preview. The original Python prime-candidate scan covers `k <= 1,000,000,000` with 37,316,974 admissible prime candidates exactly tested and no hit. A separate C/OpenMP exact Pell-divisibility scan extends bounded no-hit coverage through `k = 10,000,000,000`; the extension from `10^9` to `10^10` tested 451,314,038 small-prime-sieve survivors and produced zero Pell-divisibility hits. The primitive quotient `P_2209 / P_47` has 828 digits; archived and newer P-1/P+1/ECM campaigns still record no nontrivial factor.

Status: `HARD_UNRESOLVED` / `DEEP_COMPUTATIONAL_FRONTIER`, not a nonexistence claim. See `GATE_47.md` and `reports/gate_47_status.json`.

## Gate 53

Gate `53` is resolved by the prime witness `13,747,841,783,933,689`, extracted from the exact primitive quotient `P_2809 / P_53` by GMP-ECM P-1. Its exact Pell rank is `2809 = 53^2`.

Gate `47` remains hard-unresolved; Level 3 remains simulation-only. See `GATE_53.md` and `reports/gate_53.json`.

## Gate 59

Gate `59` is resolved by the direct prime witness `31,217,609`, found at `k = 8,968` and independently verified to have exact Pell rank `3481 = 59^2`.

Level 3 remains simulation-only. See `GATE_59.md` and `reports/gate_59.json`.

## Gate 67

Gate `67` is resolved by direct prime witness `454,134,173` at `k = 101,166`, with exact Pell rank `4489 = 67^2`.

See `GATE_67.md` and `reports/gate_67.json`.

## Gate 71

Gate `71` is currently `ACTIVE_UNRESOLVED`: direct scanning through `k = 100,000,000` tested 3,917,148 admissible prime candidates with no hit, and four recorded P-1/P+1 campaigns on `P_5041 / P_71` found no factor.

This is a bounded-search status, not a nonexistence claim. See `GATE_71.md` and `reports/gate_71_status.json`.

## Gate 73

Gate `73` is resolved by direct prime witness `159,869` at `k = 30`, with exact Pell rank `5329 = 73^2`. The full `k <= 200,000` window contains 10,250 admissible prime candidates and exactly one verified hit. The witness divides the exact 2,012-digit primitive quotient `P_5329 / P_73`.

See `GATE_73.md` and `reports/gate_73.json`.
