import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_139 import (
    AFFECTED_ROOT,
    AFFECTED_TARGET_RANK,
    AFFECTED_WITNESS,
    DIRECT_SCAN,
    SECONDARY_WITNESS,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate139Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 19_321)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, 12_635_933)
        self.assertEqual(WITNESS_K, 654)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK - 1)
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
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_830)
        self.assertEqual(DIRECT_SCAN["first_hit_prime_candidates_tested"], 24)
        self.assertEqual(len(DIRECT_SCAN["hits"]), 2)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 7_343)
        self.assertEqual(q % WITNESS, 0)
    def test_affected_preview_root(self):
        row = self.report["affected_preview_root"]
        self.assertEqual(row["root"], AFFECTED_ROOT)
        self.assertEqual(row["target_rank"], AFFECTED_TARGET_RANK)
        self.assertEqual(row["witness"], AFFECTED_WITNESS)
        self.assertEqual(AFFECTED_WITNESS, 93_058_096_395_323_907_653_285_057)
        self.assertTrue(row["exact_rank_verified"])
        self.assertTrue(row["promotion_ready"])
        self.assertTrue(all(gcd_row[2] == 1 for gcd_row in row["pairwise_gcds"]))

if __name__ == "__main__":
    unittest.main()
