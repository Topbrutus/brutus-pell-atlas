import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.mirror_frontier import (
    build_frontier,
    exact_rank_target,
    is_prime_trial,
    pell_mod_fast,
    pell_number,
)
from calculation.pell_atlas import pell_rank

class MirrorFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_frontier()
        cls.by_root = {row["root"]: row for row in cls.report["frontier"]}

    def test_fast_mod_matches_iterative_small_cases(self):
        for modulus in (7, 13, 31, 73, 293):
            a, b = 0, 1 % modulus
            for index in range(1, 40):
                a, b = b, (2 * b + a) % modulus
                self.assertEqual(pell_mod_fast(index, modulus), a)

    def test_48_witness_is_prime(self):
        n = int(self.by_root[48]["witness"])
        self.assertTrue(is_prime_trial(n))
        self.assertTrue(self.by_root[48]["witness_prime_verified"])

    def test_48_rank_by_two_independent_paths(self):
        n = int(self.by_root[48]["witness"])
        self.assertEqual(pell_rank(n, 48 * 48), 48 * 48)
        self.assertTrue(exact_rank_target(n, 48 * 48))

    def test_861_structured_witness(self):
        row = self.by_root[861]
        self.assertEqual(row["target_rank"], 861 * 861)
        self.assertEqual(row["component_rank_roots"], [3, 7, 41])
        self.assertEqual(row["gcd_P1681_197"], 1)
        self.assertEqual(row["gcd_P1681_293"], 1)
        self.assertTrue(row["P_1681_exact_rank_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_P1681_has_expected_exact_rank(self):
        p1681 = pell_number(1681)
        self.assertTrue(exact_rank_target(p1681, 1681))

    def test_frontier_is_not_promoted_automatically(self):
        effect = self.report["promotion_effect"]
        self.assertEqual(effect["current_lattice_nodes"], 16)
        self.assertEqual(effect["nodes_if_both_promoted"], 29)
        self.assertIn(48, effect["promoted_nodes"])
        self.assertIn(861, effect["promoted_nodes"])

if __name__ == "__main__":
    unittest.main()
