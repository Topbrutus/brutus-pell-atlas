import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.frontier_levels import (
    build_level_2,
    is_prime_64,
    prime_factorization,
    search_prime_square_rank_witness,
)

class FrontierLevel2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_level_2()

    def test_new_mirror_roots_exact(self):
        self.assertEqual(
            self.report["new_mirror_roots"],
            [633, 2271, 4443, 8886, 67731],
        )

    def test_prime_support_before(self):
        self.assertEqual(self.report["prime_support_before"], [2, 3, 5, 7, 41])

    def test_factorizations(self):
        expected = {
            633: {3: 1, 211: 1},
            2271: {3: 1, 757: 1},
            4443: {3: 1, 1481: 1},
            8886: {2: 1, 3: 1, 1481: 1},
            67731: {3: 1, 107: 1, 211: 1},
        }
        for n, factors in expected.items():
            self.assertEqual(prime_factorization(n), factors)

    def test_unresolved_gate_compression(self):
        self.assertEqual(self.report["unresolved_gate_count"], 1)
        self.assertEqual(
            self.report["unresolved_gate_to_doors"],
            {"211": [633, 67731]},
        )

    def test_107_prime_support_witness(self):
        row = self.report["prime_support_witnesses"]["107"]
        self.assertEqual(row["witness"], 82_318_309)
        self.assertEqual(row["rank"], 11_449)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_757_prime_support_witness(self):
        row = self.report["prime_support_witnesses"]["757"]
        self.assertEqual(row["witness"], 21_855_419_538_769)
        self.assertEqual(row["rank"], 573_049)
        self.assertEqual(row["k"], 38_138_832)
        self.assertEqual(row["sign"], 1)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_2271_door_is_ready(self):
        by_root = {door["root"]: door for door in self.report["doors"]}
        self.assertTrue(by_root[2271]["promotion_ready"])
        self.assertEqual(by_root[2271]["unresolved_prime_gates"], [])

    def test_1481_prime_support_witness(self):
        row = self.report["prime_support_witnesses"]["1481"]
        self.assertEqual(row["witness"], 13_169_009_631_553)
        self.assertEqual(row["rank"], 2_193_361)
        self.assertEqual(row["k"], 6_004_032)
        self.assertEqual(row["sign"], 1)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_4443_and_8886_doors_are_ready(self):
        by_root = {door["root"]: door for door in self.report["doors"]}
        for root in (4443, 8886):
            self.assertTrue(by_root[root]["promotion_ready"])
            self.assertEqual(by_root[root]["unresolved_prime_gates"], [])

    def test_107_search_reproduces_first_hit(self):
        hits = search_prime_square_rank_witness(107, 7190, stop_after=1)
        self.assertEqual(hits, [{"witness": 82_318_309, "k": 7190, "rank": 11_449}])

    def test_prime_checker(self):
        self.assertTrue(is_prime_64(82_318_309))
        self.assertFalse(is_prime_64(82_318_309 * 3))

    def test_sources_are_preserved(self):
        by_root = {door["root"]: door for door in self.report["doors"]}
        self.assertEqual([s["source_root"] for s in by_root[633]["sources"]], [336])
        self.assertEqual([s["source_root"] for s in by_root[2271]["sources"]], [1722, 17220])
        self.assertEqual([s["source_root"] for s in by_root[4443]["sources"]], [3444, 34440])
        self.assertEqual([s["source_root"] for s in by_root[8886]["sources"]], [6888, 68880])
        self.assertEqual([s["source_root"] for s in by_root[67731]["sources"]], [13776])

if __name__ == "__main__":
    unittest.main()
