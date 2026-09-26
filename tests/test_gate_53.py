import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_53 import (
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate53Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 2_809)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 1_055)
        self.assertEqual(q % WITNESS, 0)
        self.assertTrue(self.report["primitive_part"]["factor_divides_primitive_quotient"])

    def test_witness_identity_and_rank(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_discovery_metadata(self):
        row = self.report["discovery"]
        self.assertEqual(row["method"], "P-1")
        self.assertEqual(row["stage"], 2)
        self.assertEqual(row["B1"], 50_000)
        self.assertEqual(row["effective_B2"], 6_303_568)
        self.assertEqual(row["preloaded_order_factor"], 2_809)
        self.assertEqual(row["exit_status"], 14)

    def test_level3_role(self):
        roots = self.report["level3_role"]["affected_preview_roots"]
        self.assertEqual(roots, [42_771, 8_633_541, 116_903_001, 639_871_014, 679_699_401])

if __name__ == "__main__":
    unittest.main()
