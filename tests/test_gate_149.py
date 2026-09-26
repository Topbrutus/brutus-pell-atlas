import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_149 import (
    AFFECTED_ROOT,
    DIRECT_SCAN,
    SECONDARY_WITNESS,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate149Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 22_201)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, 5_328_241)
        self.assertEqual(WITNESS_K, 240)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_secondary_witness(self):
        row = self.report["secondary_verified_witness"]
        self.assertEqual(row["p"], SECONDARY_WITNESS)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_scan_accounting(self):
        self.assertEqual(DIRECT_SCAN["search_cap"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_773)
        self.assertEqual(DIRECT_SCAN["first_hit_prime_candidates_tested"], 8)
        self.assertEqual(len(DIRECT_SCAN["hits"]), 2)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 8_441)
        self.assertEqual(q % WITNESS, 0)
        self.assertEqual(q % SECONDARY_WITNESS, 0)
    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [AFFECTED_ROOT])
        self.assertEqual(AFFECTED_ROOT, 8_443_383)
        self.assertEqual(role["remaining_novel_gates"], [1_453])

if __name__ == "__main__":
    unittest.main()
