import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_131 import (
    FULL_WINDOW_HITS,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate131Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 17_161)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, 2_745_761)
        self.assertEqual(WITNESS_K, 160)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_direct_scan_accounting(self):
        scan = self.report["direct_scan"]
        self.assertEqual(scan["search_cap"], 200_000)
        self.assertEqual(scan["reported_prime_candidates_tested"], 4_832)
        self.assertEqual(scan["first_hit_prime_candidates_tested"], 6)
        self.assertEqual(scan["verified_hit_count_in_full_window"], 2)
        self.assertEqual(scan["verified_hits"], FULL_WINDOW_HITS)

    def test_secondary_witness(self):
        row = self.report["secondary_prime_witness"]
        self.assertEqual(row["p"], 576_609_601)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(
            pell_rank(row["p"], TARGET_RANK),
            TARGET_RANK,
        )

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 6_519)
        self.assertEqual(q % WITNESS, 0)
    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(
            role["affected_preview_roots"],
            [80_777_607_891],
        )
        self.assertEqual(
            role["remaining_novel_gates"],
            [389, 528_383],
        )

    def test_observation_is_bounded(self):
        self.assertIn("bounded computation", self.report["observation"])

if __name__ == "__main__":
    unittest.main()
