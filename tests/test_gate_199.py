import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_199 import (
    DIRECT_SCAN_TO_FIRST_HIT,
    PRIMITIVE_SHA256,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate199Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 39_601)

    def test_direct_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_scan_to_first_hit(self):
        scan = DIRECT_SCAN_TO_FIRST_HIT
        self.assertEqual(scan["end_k"], 550_192)
        self.assertEqual(scan["prime_candidates_tested"], 12_199)
        self.assertEqual(scan["hits"][0]["p"], WITNESS)

    def test_primitive_quotient(self):
        q = primitive_quotient()
        primitive = self.report["primitive_part"]
        self.assertEqual(len(str(q)), 15_083)
        self.assertEqual(primitive["sha256"], PRIMITIVE_SHA256)
        self.assertTrue(primitive["witness_divides_primitive"])

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [75_434_532])
        self.assertEqual(
            role["resolved_support_after_resolution"],
            {"75434532": [31, 199]},
        )
        self.assertEqual(role["still_blocked"], {"75434532": [1019]})

if __name__ == "__main__":
    unittest.main()
