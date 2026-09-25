# Brutus–Pell Bridge Finder

The bridge finder searches the curated Atlas for exact arithmetic connections that have not yet been promoted into named atlas objects.

## What it scans

- same-rank clusters;
- coprime pairs whose rank LCM is a perfect square;
- verified rank-preserving products;
- 13/31 mirror-host compatibility;
- verified products that are not yet stored as atlas records.

Run:

```bash
python -m calculation.bridge_finder
```

The machine-readable result is written to `reports/bridge_report.json`.

## Current verified examples

Among the automatically recovered products are:

$$13\cdot293=3809,\qquad z_P(3809)=49=7^2,$$

$$31\cdot10877=337187,\qquad z_P(337187)=900=30^2,$$

$$130\cdot3529=458770,\qquad z_P(458770)=1764=42^2.$$

These are exact computations inside the current curated search space. They are not, by themselves, novelty claims.

## Interpretation rule

A bridge can be:

- already catalogued;
- verified but not yet catalogued;
- a repeated representation of an existing fiber;
- or a candidate for a higher-level classification.

The finder never upgrades a numerical bridge to a theorem or a physical interpretation.
