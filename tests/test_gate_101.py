import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_101 import TARGET_RANK, build_report, primitive_quotient

class Gate101Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 10_201)

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
    def test_compiled_scan(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["max_k"], 10_000_000_000)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)
        self.assertEqual(
            scan["small_prime_sieve_survivors"],
            496_754_167,
        )

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 3_867)
        self.assertEqual(
            self.report["primitive_part"]["decimal_digits"],
            3_867,
        )

    def test_strong_factorization_attempts(self):
        attempts = self.report["strong_factorization_attempts"]
        self.assertEqual(len(attempts), 2)
        self.assertEqual(
            [row["method"] for row in attempts],
            ["P-1", "P+1"],
        )
        self.assertTrue(
            all(row["B1"] == 1_000_000 for row in attempts)
        )
        self.assertTrue(
            all(row["B2"] == 100_000_000 for row in attempts)
        )
        self.assertTrue(
            all(row["completed_runs"] == 12 for row in attempts)
        )
        self.assertTrue(
            all(not row["factor_found"] for row in attempts)
        )
        self.assertTrue(
            all(
                row["outputs_equal_to_primitive_input"] == 12
                for row in attempts
            )
        )

    def test_level3_role(self):
        self.assertEqual(
            self.report["level3_role"]["affected_preview_roots"],
            [76_327_215, 299_902_623_543_471],
        )

if __name__ == "__main__":
    unittest.main()
