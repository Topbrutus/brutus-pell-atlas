import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_157 import (
    COMPILED_SCAN,
    DIRECT_SCAN,
    FACTORIZATION_ATTEMPTS,
    PRIMITIVE_SHA256,
    TARGET_RANK,
    build_report,
    primitive_quotient,
)

class Gate157Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 24_649)

    def test_status_boundary(self):
        self.assertEqual(self.report["status"], "ACTIVE_UNRESOLVED")
        self.assertEqual(
            self.report["frontier_class"],
            "ACTIVE_COMPUTATIONAL_FRONTIER",
        )
        self.assertIn("nonexistence", self.report["boundary"])

    def test_direct_scan(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_725)
        self.assertEqual(DIRECT_SCAN["hits"], [])

    def test_compiled_scan(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["start_k"], 200_001)
        self.assertEqual(scan["end_k"], 10_000_000_000)
        self.assertEqual(scan["small_prime_sieve_survivors"], 247_573_895)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 9_375)
        self.assertEqual(self.report["primitive_part"]["sha256"], PRIMITIVE_SHA256)
        self.assertEqual(self.report["primitive_part"]["factordb_observation"]["status"], "U")

    def test_factorization_attempts(self):
        self.assertEqual(
            [row["method"] for row in FACTORIZATION_ATTEMPTS],
            ["P-1", "P+1"],
        )
        self.assertTrue(all(not row["factor_found"] for row in FACTORIZATION_ATTEMPTS))
        self.assertEqual(FACTORIZATION_ATTEMPTS[0]["exit_status"], 0)
        self.assertEqual(FACTORIZATION_ATTEMPTS[1]["exit_status"], 0)

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [432_849])
        self.assertEqual(role["other_unresolved_support"], {"432849": [919]})

if __name__ == "__main__":
    unittest.main()
