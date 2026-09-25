# Brutus–Pell Mirror Frontier

The Mirror Frontier records verified mirror-root continuations without automatically promoting them into the core Rank Lattice.

## Why existence alone is not the question

For every positive index $m$, the Pell number $P_m$ itself has rank exactly $m$:

$$z_P(P_m)=m.$$

Indeed, $P_m$ divides itself and the positive Pell sequence is strictly increasing, so no earlier positive Pell term can be a multiple of $P_m$.

Therefore every square-rank fiber

$$\mathcal F_C=\{n:z_P(n)=C^2\}$$

is nonempty. The useful question for the Atlas is whether a root has a compact, prime, factorized, or otherwise structurally informative witness.

## Frontier A — mirror of 84

Fixed-width reversal gives

$$84\longleftrightarrow48.$$

A direct prime witness was found and verified:

$$\boxed{28\,320\,769}$$

with

$$\boxed{z_P(28\,320\,769)=2304=48^2}.$$

The repository independently checks primality by trial division and checks the Pell rank by both iterative recurrence and fast modular matrix exponentiation.
## Frontier B — mirror of 168

Fixed-width reversal gives

$$168\longleftrightarrow861.$$

Since

$$861=3\cdot7\cdot41,$$

a structured witness was built from verified component roots:

$$N_{861}=197\cdot293\cdot P_{1681}.$$

The component ranks are

$$z_P(197)=3^2,$$

$$z_P(293)=7^2,$$

$$z_P(P_{1681})=1681=41^2.$$

The computed witness has 648 decimal digits, and exact modular verification gives

$$\boxed{z_P(N_{861})=741321=861^2}.$$

The full decimal witness is stored as text in `reports/mirror_frontier.json` so consumers are not forced to parse a 648-digit JSON integer.

## Controlled promotion

The current core Rank Lattice has 16 nodes. Closing the lattice under gcd/lcm after adding roots 48 and 861 would produce 29 nodes.

For that reason, these roots remain `frontier-only` until a deliberate promotion step.

## Reproduce

```bash
python -m calculation.mirror_frontier
```

Machine-readable output: `reports/mirror_frontier.json`.

## Boundary

Decimal reversal is a representation convention. The rank statements above are exact computational statements for the listed witnesses. They are not presented as a universal theorem relating decimal reversal to Pell ranks.
