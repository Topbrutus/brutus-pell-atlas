import sys
import unittest
from math import gcd, lcm
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.derived_laws import (
    absorbed_rank,
    odd_primes_below,
    pairwise_coprime,
    pell_number,
    p_valuation,
    predicted_prime_power_rank,
    prime_rank_and_lift_depth,
    rank_lcm,
    square_cover_root,
    odd_square_gate_coordinates,
    odd_square_gate_rail_ok,
    divides_primitive_square_quotient,
)
from calculation.pell_atlas import pell_rank
from calculation.frontier_level_3 import KNOWN_LEVEL3_GATE_WITNESSES


class BrutusPellDerivedLawTests(unittest.TestCase):
    def test_13_delayed_prime_power_lift_through_fifth_power(self):
        expected = [7, 7, 91, 1183, 15379]
        z, depth = prime_rank_and_lift_depth(13)
        self.assertEqual((z, depth), (7, 2))
        for exponent, target in enumerate(expected, start=1):
            self.assertEqual(predicted_prime_power_rank(13, exponent), target)
            self.assertEqual(pell_rank(13**exponent, target), target)

    def test_31_delayed_prime_power_lift_through_fifth_power(self):
        expected = [30, 30, 930, 28830, 893730]
        z, depth = prime_rank_and_lift_depth(31)
        self.assertEqual((z, depth), (30, 2))
        for exponent, target in enumerate(expected, start=1):
            self.assertEqual(predicted_prime_power_rank(31, exponent), target)
            self.assertEqual(pell_rank(31**exponent, target), target)

    def test_finite_prime_scan_below_500_finds_only_13_and_31_with_depth_above_one(self):
        exceptional = []
        for p in odd_primes_below(500):
            _, depth = prime_rank_and_lift_depth(p)
            if depth > 1:
                exceptional.append((p, depth))
        self.assertEqual(exceptional, [(13, 2), (31, 2)])

    def test_prime_power_prediction_for_all_odd_primes_below_100_through_cube(self):
        checks = 0
        for p in odd_primes_below(100):
            for exponent in (1, 2, 3):
                target = predicted_prime_power_rank(p, exponent)
                self.assertEqual(pell_rank(p**exponent, target), target)
                checks += 1
        self.assertEqual(checks, 72)

    def test_coprime_rank_lcm_examples(self):
        examples = [
            (73, 97, 36, 48, 144),
            (73, 257, 36, 64, 576),
            (73, 149, 36, 75, 900),
            (73, 293, 36, 49, 1764),
            (197, 293, 9, 49, 441),
        ]
        for a, b, rank_a, rank_b, expected in examples:
            self.assertEqual(gcd(a, b), 1)
            self.assertEqual(pell_rank(a, rank_a), rank_a)
            self.assertEqual(pell_rank(b, rank_b), rank_b)
            self.assertEqual(lcm(rank_a, rank_b), expected)
            self.assertEqual(pell_rank(a * b, expected), expected)

    def test_square_cover_roots_from_rank_lcm(self):
        self.assertEqual(square_cover_root([36, 48]), 12)
        self.assertEqual(square_cover_root([36, 64]), 24)
        self.assertEqual(square_cover_root([36, 75]), 30)
        self.assertEqual(square_cover_root([36, 49]), 42)
        self.assertEqual(square_cover_root([9, 49]), 21)
        self.assertIsNone(square_cover_root([7, 30]))

    def test_rank_absorption_examples(self):
        cases = [
            (293, 13**2, 49, 7),
            (10877, 31**2, 900, 30),
            (198477, 13**2, 44100, 7),
            (198477, 31**2, 44100, 30),
        ]
        for host, added, host_rank, added_rank in cases:
            self.assertTrue(pairwise_coprime([host, added]))
            self.assertTrue(absorbed_rank(host_rank, added_rank))
            self.assertEqual(pell_rank(host * added, host_rank), host_rank)

    def test_full_13_31_mirror_host_absorption(self):
        host = 198477
        host_rank = 44100
        self.assertTrue(absorbed_rank(host_rank, 7))
        self.assertTrue(absorbed_rank(host_rank, 30))
        self.assertEqual(
            pell_rank(host * 13**2 * 31**2, host_rank),
            host_rank,
        )

    def test_exact_anchor_valuations(self):
        self.assertEqual(p_valuation(pell_number(7), 13), 2)
        self.assertEqual(pell_number(7), 169)
        z31 = pell_rank(31, 30)
        self.assertEqual(z31, 30)
        self.assertEqual(p_valuation(pell_number(z31), 31), 2)


    def test_all_known_level3_prime_witnesses_follow_gate8_rails(self):
        checked = 0
        for root, data in sorted(KNOWN_LEVEL3_GATE_WITNESSES.items()):
            witness = int(data["witness"])
            k, sign = odd_square_gate_coordinates(root, witness)
            self.assertEqual(witness, k * root * root + sign)
            self.assertTrue(odd_square_gate_rail_ok(root, witness))
            if sign == 1:
                self.assertEqual(k % 8, 0)
                self.assertEqual(witness % 8, 1)
            else:
                self.assertEqual(k % 8, 6)
                self.assertEqual(witness % 8, 5)
            checked += 1
        self.assertEqual(checked, 25)

    def test_selected_gate_witnesses_divide_primitive_square_quotients(self):
        for root in (13, 17, 23, 29, 37, 43, 73):
            witness = int(KNOWN_LEVEL3_GATE_WITNESSES[root]["witness"])
            self.assertTrue(divides_primitive_square_quotient(root, witness))


if __name__ == "__main__":
    unittest.main()
