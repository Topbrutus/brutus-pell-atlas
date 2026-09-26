import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_103 import (
    FULL_WINDOW_HITS,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate103Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 10_609)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, 403_141)
        self.assertEqual(WITNESS_K, 38)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK - 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_direct_scan_accounting(self):
        scan = self.report["direct_scan"]
        self.assertEqual(scan["search_cap"], 200_000)
        self.assertEqual(scan["reported_prime_candidates_tested"], 9_898)
        self.assertEqual(scan["first_hit_prime_candidates_tested"], 2)
        self.assertEqual(scan["verified_hit_count_in_full_window"], 3)
        self.assertEqual(scan["verified_hits"], FULL_WINDOW_HITS)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 4_022)
        self.assertEqual(q % WITNESS, 0)

    def test_level3_role(self):
        self.assertEqual(
            self.report["level3_role"]["affected_preview_roots"],
            [2_820_552, 40_435_431, 79_783_491, 6_726_265_341],
        )

    def test_observation_is_bounded(self):
        self.assertIn("bounded computation", self.report["observation"])

if __name__ == "__main__":
    unittest.main()
