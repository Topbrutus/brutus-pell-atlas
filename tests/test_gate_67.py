import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_67 import TARGET_RANK, WITNESS, WITNESS_K, build_report, primitive_quotient
from calculation.pell_atlas import pell_rank

class Gate67Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 4_489)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK - 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 1_693)
        self.assertEqual(q % WITNESS, 0)

    def test_level3_role(self):
        self.assertEqual(
            self.report["level3_role"]["affected_preview_roots"],
            [2_989_473, 7_624_533, 85_683_303_492],
        )

if __name__ == "__main__":
    unittest.main()
