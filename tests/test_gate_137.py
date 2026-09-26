import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_137 import (
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate137Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 18_769)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, 3_415_957)
        self.assertEqual(WITNESS_K, 182)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK - 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_scan_accounting(self):
        scan = self.report["direct_scan"]
        self.assertEqual(scan["search_cap"], 200_000)
        self.assertEqual(scan["reported_prime_candidates_tested"], 4_780)
        self.assertEqual(scan["first_hit_prime_candidates_tested"], 5)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 7_132)
        self.assertEqual(q % WITNESS, 0)

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [80_860_962])
        self.assertEqual(role["remaining_novel_gates"], [47])

if __name__ == "__main__":
    unittest.main()

