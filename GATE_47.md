# Brutus–Pell Gate 47

`47` is the first hard unresolved prime-support gate in the Frontier Level 3 preview.

## Target

$$\boxed{47^2=2209}.$$

The explicit-witness target is a prime $p$ satisfying

$$\boxed{z_P(p)=2209}.$$

Primitive-divisor theory guarantees existence of such a prime. The unresolved task is to exhibit one explicitly.

## Direct congruence scan

For Pell numbers the Lucas rank congruence restricts a prime witness to

$$p=2209k\pm1,$$

with the sign compatible with the Legendre symbol $(8/p)$.

The verified bounded scan now covers

$$\boxed{1\le k\le1\,000\,000\,000}.$$

Across that range, **37,316,974 admissible prime candidates** received the exact Pell-rank test.

Result:

$$\boxed{\text{NO EXPLICIT PRIME WITNESS IN THE SCANNED WINDOW}}.$$

The largest direct candidate bound is

$$\boxed{2\,209\,000\,000\,001}.$$

## Compiled Pell-divisibility extension

A separate C/OpenMP scanner (`calculation/gate_47_scan.c`) uses the same Lucas congruence restriction, a small-prime sieve, and exact `unsigned __int128` modular Pell arithmetic. It checks Pell divisibility before primality.

The compiled scan independently cross-checks the Python-scanned region and extends the search through

$$\boxed{k=10^{10}}.$$

The new extension `1,000,000,001 <= k <= 10,000,000,000` sent **451,314,038** small-prime-sieve survivors to the exact Pell test. None satisfied the target Pell divisibility condition, so no prime witness can occur in that extension.

The resulting candidate bound is

$$\boxed{22\,090\,000\,000\,001}.$$

The compiled no-hit statement is a bounded computation, not a nonexistence theorem.
## Primitive-part attack

Because $2209=47^2$, the exact primitive target used for factorization is

$$Q_{47}=\frac{P_{2209}}{P_{47}}.$$

The division is exact and $Q_{47}$ has **828 decimal digits**.

Archived local factorization campaigns contain **1,224 silent-run outputs** distributed across ECM, P−1, and P+1 campaigns. Every archived output equals the original primitive quotient, so none records a nontrivial factor.

Additional explicit logs include light and strong P−1/P+1 campaigns and ECM campaigns; no verified factor has been produced.

## Current status

$$\boxed{\text{HARD\_UNRESOLVED}}\qquad\text{(DEEP COMPUTATIONAL FRONTIER)}.$$

This status means only that no explicit compact prime witness has been found by the recorded searches. It does **not** mean that a witness does not exist.

## Level-3 consequences

Gate `47` occurs in at least these preview roots:

- `4,553,031 = 3 × 7² × 47 × 659`;
- `80,860,962 = 2 × 3 × 7 × 13 × 23 × 47 × 137`.

Resolving `47` alone would not completely resolve either door because both contain additional novel prime support.

## Reproduce status report

```bash
python -m calculation.gate_47
```

Machine-readable report: `reports/gate_47_status.json`.
