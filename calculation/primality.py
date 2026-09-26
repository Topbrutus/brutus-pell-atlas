from __future__ import annotations

from math import gcd, isqrt

from calculation.frontier_levels import is_prime_64

def verify_pocklington_certificate(
    n: int,
    factors: list[tuple[int, int]] | tuple[tuple[int, int], ...],
    base: int,
) -> bool:
    """Verify a Pocklington-style primality certificate.

    `factors` gives a known prime factorization of a divisor F of n-1.
    The certificate is accepted only when F > sqrt(n).
    Every listed prime factor must itself fit the repository's
    deterministic 64-bit primality checker.
    """
    if n < 2 or base <= 1 or base >= n:
        return False

    known_factor = 1
    distinct_primes: list[int] = []
    for q, exponent in factors:
        if q < 2 or exponent < 1:
            return False
        if q >= 1 << 64:
            return False
        if not is_prime_64(q):
            return False
        known_factor *= q ** exponent
        distinct_primes.append(q)

    if (n - 1) % known_factor != 0:
        return False
    if known_factor <= isqrt(n):
        return False
    if pow(base, n - 1, n) != 1:
        return False

    for q in distinct_primes:
        residue = pow(base, (n - 1) // q, n)
        if gcd(residue - 1, n) != 1:
            return False

    return True
