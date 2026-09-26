import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_163 import (
    DIRECT_SCAN,
    PRIMITIVE_SHA256,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate163Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 26_569)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK - 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_direct_scan(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_716)
        self.assertEqual(len(DIRECT_SCAN["hits"]), 1)

    def test_primitive_quotient(self):
        q = primitive_quotient()
        primitive = self.report["primitive_part"]
        self.assertEqual(len(str(q)), 10_108)
        self.assertEqual(primitive["sha256"], PRIMITIVE_SHA256)
        self.assertTrue(primitive["witness_divides_primitive"])

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(
            role["affected_preview_roots"],
            [2_820_552, 29_770_544_451],
        )
        self.assertEqual(
            role["promotion_ready_after_resolution"],
            [2_820_552],
        )
        self.assertEqual(
            role["still_blocked"],
            {"29770544451": [3851, 15809]},
        )

if __name__ == "__main__":
    unittest.main()
