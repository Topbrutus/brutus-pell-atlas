import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_269 import (
    COMPILED_SCAN,
    DIRECT_SCAN,
    FACTORIZATION_ATTEMPTS,
    TARGET_RANK,
    build_report,
    primitive_quotient,
    primitive_sha256,
)

class Gate269Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 72_361)

    def test_status_boundary(self):
        self.assertEqual(self.report["status"], "HARD_UNRESOLVED")
        self.assertEqual(
            self.report["frontier_class"],
            "DEEP_COMPUTATIONAL_FRONTIER",
        )
        self.assertTrue(
            self.report["known_theory"]["primitive_prime_divisor_existence"]
        )
        self.assertIn("nonexistence", self.report["boundary"])

    def test_direct_scan(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_529)
        self.assertEqual(DIRECT_SCAN["hits"], [])

    def test_compiled_scan(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["end_k"], 10_000_000_000)
        self.assertEqual(scan["small_prime_sieve_survivors"], 246_634_988)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)
        self.assertEqual(scan["implementation"], COMPILED_SCAN["implementation"])

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 27_596)
        self.assertEqual(
            primitive_sha256(),
            "964ba924f1bc564d5435449b31dd3d7c0a2f8086343fdf95b872662d9642cefb",
        )

    def test_factorization_attempts(self):
        self.assertEqual([r["method"] for r in FACTORIZATION_ATTEMPTS], ["P-1", "P+1"])
        self.assertTrue(all(not r["factor_found"] for r in FACTORIZATION_ATTEMPTS))
        self.assertEqual([r["runs"] for r in FACTORIZATION_ATTEMPTS], [4, 4])

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [42_771])
        self.assertEqual(role["already_resolved_other_support"], {"42771": [53]})
        self.assertEqual(role["would_make_promotion_ready"], [42_771])

if __name__ == "__main__":
    unittest.main()
