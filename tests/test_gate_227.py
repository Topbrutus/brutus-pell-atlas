import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_227 import (
    CANONICAL_K,
    CANONICAL_WITNESS,
    FIRST_HIT_SCAN,
    FULL_SCAN,
    PRIMITIVE_SHA256,
    SECONDARY_K,
    SECONDARY_WITNESS,
    TARGET_RANK,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate227Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 51_529)

    def test_canonical_witness(self):
        row = self.report["verified_prime_witnesses"][0]
        self.assertEqual(CANONICAL_WITNESS, CANONICAL_K * TARGET_RANK - 1)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertTrue(row["divides_primitive"])
        self.assertEqual(pell_rank(CANONICAL_WITNESS, TARGET_RANK), TARGET_RANK)

    def test_secondary_witness(self):
        row = self.report["verified_prime_witnesses"][1]
        self.assertEqual(SECONDARY_WITNESS, SECONDARY_K * TARGET_RANK - 1)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertTrue(row["divides_primitive"])
        self.assertEqual(pell_rank(SECONDARY_WITNESS, TARGET_RANK), TARGET_RANK)

    def test_first_hit_accounting(self):
        self.assertEqual(FIRST_HIT_SCAN["prime_candidates_tested"], 1)
        self.assertEqual(FIRST_HIT_SCAN["end_k"], 6)

    def test_full_scan(self):
        self.assertEqual(FULL_SCAN["end_k"], 200_000)
        self.assertEqual(FULL_SCAN["prime_candidates_tested"], 4_629)
        self.assertEqual(len(FULL_SCAN["hits"]), 2)

    def test_primitive_quotient(self):
        q = primitive_quotient()
        primitive = self.report["primitive_part"]
        self.assertEqual(len(str(q)), 19_638)
        self.assertEqual(primitive["sha256"], PRIMITIVE_SHA256)

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(
            role["affected_preview_roots"],
            [49_713, 61_455_314_793],
        )
        self.assertEqual(role["promotion_ready_after_resolution"], [49_713])
        self.assertEqual(
            role["still_blocked"],
            {"61455314793": [90_242_753]},
        )

if __name__ == "__main__":
    unittest.main()
