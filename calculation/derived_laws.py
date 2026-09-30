from __future__ import annotations

from functools import reduce
from math import gcd, isqrt, lcm

from calculation.pell_atlas import pell_rank


def pell_number(n: int) -> int:
    """Return the exact Pell number P_n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    p_prev, p_curr = 0, 1
    if n == 0:
        return 0
    for _ in range(1, n):
        p_prev, p_curr = p_curr, 2 * p_curr + p_prev
    return p_curr


def p_valuation(value: int, p: int) -> int:
    """Return v_p(value) for non-zero value."""
    if p < 2:
        raise ValueError("p must be >= 2")
    if value == 0:
        raise ValueError("valuation of zero is not finite")
    value = abs(value)
    exponent = 0
    while value % p == 0:
        value //= p
        exponent += 1
    return exponent


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def odd_primes_below(limit: int) -> list[int]:
    return [p for p in range(3, limit) if is_prime_trial(p)]


def prime_rank_and_lift_depth(p: int) -> tuple[int, int]:
    """
    Return (z_P(p), a_p) where a_p = v_p(P_{z_P(p)}).

    Intended for odd primes in the Pell sequence U_n(2,-1).
    The finite search bound is deliberately generous for the verified
    ranges used by the repository tests.
    """
    if p == 2 or not is_prime_trial(p):
        raise ValueError("p must be an odd prime")
    z = pell_rank(p, 2 * (p + 1))
    depth = p_valuation(pell_number(z), p)
    return z, depth


def predicted_prime_power_rank(p: int, exponent: int) -> int:
    """
    Pell-specialized prime-power lift prediction:

        z_P(p^e) = z_P(p) * p^max(0, e-a_p),

    with a_p = v_p(P_{z_P(p)}).

    This is used as a derived/known-theory relation and then independently
    checked against exact modular rank computation in the tests.
    """
    if exponent < 1:
        raise ValueError("exponent must be >= 1")
    z, depth = prime_rank_and_lift_depth(p)
    return z * p ** max(0, exponent - depth)


def rank_lcm(ranks: list[int] | tuple[int, ...]) -> int:
    if not ranks or any(r < 1 for r in ranks):
        raise ValueError("ranks must be positive and non-empty")
    return reduce(lcm, ranks, 1)


def square_cover_root(ranks: list[int] | tuple[int, ...]) -> int | None:
    combined = rank_lcm(ranks)
    root = isqrt(combined)
    return root if root * root == combined else None


def pairwise_coprime(values: list[int] | tuple[int, ...]) -> bool:
    for i, left in enumerate(values):
        for right in values[i + 1 :]:
            if gcd(left, right) != 1:
                return False
    return True


def absorbed_rank(host_rank: int, added_rank: int) -> bool:
    """True exactly when lcm(host_rank, added_rank) = host_rank."""
    if host_rank < 1 or added_rank < 1:
        raise ValueError("ranks must be positive")
    return lcm(host_rank, added_rank) == host_rank
