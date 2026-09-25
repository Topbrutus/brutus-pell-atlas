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
