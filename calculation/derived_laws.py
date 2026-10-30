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


def legendre_2_symbol_for_odd_candidate(p: int) -> int:
    """Return (2/p) from the odd prime-candidate residue modulo 8."""
    if p <= 2 or p % 2 == 0:
        raise ValueError("p must be odd and > 2")
    residue = p % 8
    if residue in (1, 7):
        return 1
    if residue in (3, 5):
        return -1
    raise AssertionError("unreachable odd residue")


def odd_square_gate_coordinates(root: int, witness: int) -> tuple[int, int]:
    """
    For odd root q and a prime witness p of target rank q^2, recover
    p = k*q^2 + sign using sign=(2/p).
    """
    if root < 1 or root % 2 == 0:
        raise ValueError("root must be positive and odd")
    if witness <= 2 or witness % 2 == 0:
        raise ValueError("witness must be odd and > 2")
    sign = legendre_2_symbol_for_odd_candidate(witness)
    target = root * root
    numerator = witness - sign
    if numerator % target:
        raise ValueError("witness is not on a q^2 congruence rail")
    return numerator // target, sign


def odd_square_gate_rail_ok(root: int, witness: int) -> bool:
    """
    Exact Gate-8 rail used for odd square target ranks:

      sign=+1 -> k == 0 (mod 8), p == 1 (mod 8)
      sign=-1 -> k == 6 (mod 8), p == 5 (mod 8)
    """
    try:
        k, sign = odd_square_gate_coordinates(root, witness)
    except ValueError:
        return False
    if witness % 4 != 1:
        return False
    if sign == 1:
        return witness % 8 == 1 and k % 8 == 0
    return witness % 8 == 5 and k % 8 == 6


def primitive_square_quotient(root: int) -> int:
    """Return the exact quotient P_(root^2) / P_root."""
    if root < 1:
        raise ValueError("root must be positive")
    numerator = pell_number(root * root)
    denominator = pell_number(root)
    quotient, remainder = divmod(numerator, denominator)
    if remainder:
        raise AssertionError("P_root must divide P_(root^2)")
    return quotient


def divides_primitive_square_quotient(root: int, witness: int) -> bool:
    if witness < 2:
        raise ValueError("witness must be >= 2")
    return primitive_square_quotient(root) % witness == 0


def next_gate8_k_after(bound_k: int, sign: int) -> int:
    """
    Return the first Gate-8-admissible k strictly above bound_k.

    sign=+1 uses k == 0 (mod 8).
    sign=-1 uses k == 6 (mod 8).
    """
    if bound_k < 0:
        raise ValueError("bound_k must be non-negative")
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    residue = 0 if sign == 1 else 6
    candidate = bound_k + 1
    candidate += (residue - candidate) % 8
    return candidate


def bounded_gate8_witness_lower_bound(root: int, scanned_through_k: int) -> int:
    """
    Given a completed no-hit scan through scanned_through_k, return the
    smallest integer p that could lie on either next legal Gate-8 rail.

    This is a computational lower bound, not a universal existence theorem.
    """
    if root < 1 or root % 2 == 0:
        raise ValueError("root must be positive and odd")
    target = root * root
    km = next_gate8_k_after(scanned_through_k, -1)
    kp = next_gate8_k_after(scanned_through_k, 1)
    minus_candidate = km * target - 1
    plus_candidate = kp * target + 1
    return min(minus_candidate, plus_candidate)

def prime_square_quotient_congruence(root: int) -> tuple[int, int, int]:
    """Return (P_q, Q_q mod P_q, expected residue) for odd prime q."""
    if root == 2 or not is_prime_trial(root):
        raise ValueError("root must be an odd prime")
    p_root = pell_number(root)
    quotient = primitive_square_quotient(root)
    sign = -1 if ((root - 1) // 2) % 2 else 1
    expected = (sign * root) % p_root
    return p_root, quotient % p_root, expected

def prime_square_quotient_coprime(root: int) -> bool:
    if root == 2 or not is_prime_trial(root):
        raise ValueError("root must be an odd prime")
    return gcd(pell_number(root), primitive_square_quotient(root)) == 1

def quotient_factor_is_exact_square_rank_witness(root: int, factor: int) -> bool:
    """Verify the L8 consequence for a concrete prime quotient factor."""
    if root == 2 or not is_prime_trial(root):
        raise ValueError("root must be an odd prime")
    if factor < 3 or not is_prime_trial(factor):
        return False
    quotient = primitive_square_quotient(root)
    if quotient % factor != 0:
        return False
    if pell_number(root) % factor == 0:
        return False
    return pell_rank(factor, root * root) == root * root
