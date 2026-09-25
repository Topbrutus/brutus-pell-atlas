from __future__ import annotations

from calculation.frontier_levels import is_prime_64
from calculation.mirror_frontier import exact_rank_target

def legendre_8_for_odd_prime_candidate(p: int) -> int:
    if p <= 2 or p % 2 == 0:
        raise ValueError("p must be an odd positive candidate")
    residue = p % 8
    if residue in (1, 7):
        return 1
    if residue in (3, 5):
        return -1
    raise AssertionError("odd residue modulo 8 expected")

def lucas_rank_congruence_admissible(root: int, k: int, sign: int) -> bool:
    if root < 1 or k < 1:
        raise ValueError("root and k must be positive")
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    target = root * root
    p = k * target + sign
    if p <= 2 or p % 2 == 0:
        return False
    return legendre_8_for_odd_prime_candidate(p) == sign

def scan_window(root: int, start_k: int, end_k: int, stop_after: int = 1) -> dict:
    if root < 1:
        raise ValueError("root must be positive")
    if start_k < 1 or end_k < start_k:
        raise ValueError("invalid search window")
    target = root * root
    hits: list[dict] = []
    prime_candidates_tested = 0
    for k in range(start_k, end_k + 1):
        for sign in (-1, 1):
            if not lucas_rank_congruence_admissible(root, k, sign):
                continue
            p = k * target + sign
            if not is_prime_64(p):
                continue
            prime_candidates_tested += 1
            if exact_rank_target(p, target):
                hits.append({"p": p, "k": k, "sign": sign})
                if len(hits) >= stop_after:
                    return {
                        "root": root,
                        "target_rank": target,
                        "start_k": start_k,
                        "end_k": k,
                        "prime_candidates_tested": prime_candidates_tested,
                        "hits": hits,
                    }
    return {
        "root": root,
        "target_rank": target,
        "start_k": start_k,
        "end_k": end_k,
        "prime_candidates_tested": prime_candidates_tested,
        "hits": hits,
    }
