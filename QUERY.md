# Brutus–Pell Atlas Query Engine

The atlas can now be queried in both directions.

## Number → rank → fiber

```bash
python -m calculation.query_atlas --n 3529 --max-steps 1764
```

Returns the Pell rank, square-rank root when applicable, and stored atlas roles.

## Rank → stored inputs

```bash
python -m calculation.query_atlas --rank 1764
```

## Square-Rank Fiber → stored members

```bash
python -m calculation.query_atlas --fiber 42
```

## Inverse Square-Rank query

```bash
python -m calculation.query_atlas --inverse 210
```

This reports the target rank $210^2=44100$, curated atlas members, and whether the rank can absorb the verified 13/31 mirror pair under the current mirror-host criterion.

## 13/31 Mirror Host test

```bash
python -m calculation.query_atlas --mirror-host 198477 --max-steps 44100
```

The engine checks the host and then recomputes all four states:

$$n,\quad13^2n,\quad31^2n,\quad13^231^2n.$$

For the reference host 198477, all four return rank 44100.

## Boundary

The query engine answers from exact modular computation plus the curated atlas dataset. A stored classification is not automatically a novelty claim or a physical interpretation.
