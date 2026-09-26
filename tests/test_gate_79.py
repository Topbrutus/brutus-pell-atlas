import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_79 import (
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
)
from calculation.pell_atlas import pell_rank

class Gate79Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 6_241)

    def test_witness_identity(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_iterative_rank(self):
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_primitive_divisibility(self):
        self.assertTrue(self.report["primitive_part"]["factor_divides_primitive_quotient"])
        self.assertEqual(self.report["primitive_part"]["decimal_digits"], 2_359)

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["newly_ready_preview_root"], 711_474)
        self.assertEqual(role["remaining_gate_for_4276191"], 18_043)

if __name__ == "__main__":
    unittest.main()
