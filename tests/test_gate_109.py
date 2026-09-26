import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_109 import (
    COMPILED_SCAN,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate109Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 11_881)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, 12_203_170_399_877)
        self.assertEqual(WITNESS_K, 1_027_116_438)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK - 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_compiled_scan_accounting(self):
        scan = self.report["discovery"]["compiled_scan"]
        self.assertEqual(scan, COMPILED_SCAN)
        self.assertEqual(scan["small_prime_sieve_survivors"], 50_631_383)
        self.assertEqual(scan["pell_divisibility_hits"], 1)
        self.assertEqual(scan["prime_hits"], 1)

    def test_primitive_part(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 4_507)
        self.assertEqual(q % WITNESS, 0)
        self.assertEqual(
            self.report["primitive_part"]["residual_cofactor_digits"],
            4_493,
        )

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [23_467_643_211])
        self.assertEqual(
            role["remaining_novel_gate_for_affected_root"],
            71_766_493,
        )

    def test_observation_is_bounded(self):
        self.assertIn("bounded computational result", self.report["observation"])

if __name__ == "__main__":
    unittest.main()
