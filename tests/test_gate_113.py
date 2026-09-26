import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_113 import (
    COMPILED_SCAN,
    DIRECT_SCAN,
    FACTORIZATION_ATTEMPTS,
    TARGET_RANK,
    build_report,
    primitive_quotient,
)

class Gate113Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 12_769)

    def test_status_boundary(self):
        self.assertEqual(self.report["status"], "HARD_UNRESOLVED")
        self.assertEqual(
            self.report["frontier_class"],
            "DEEP_COMPUTATIONAL_FRONTIER",
        )
        self.assertTrue(
            self.report["known_theory"][
                "primitive_prime_divisor_existence"
            ]
        )
        self.assertIn("nonexistence", self.report["boundary"])

    def test_direct_scan(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(
            DIRECT_SCAN["prime_candidates_tested"],
            9_828,
        )
        self.assertEqual(DIRECT_SCAN["hits"], [])

    def test_compiled_scan(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["end_k"], 10_000_000_000)
        self.assertEqual(
            scan["small_prime_sieve_survivors"],
            496_329_793,
        )
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)
        self.assertEqual(scan["implementation"], COMPILED_SCAN["implementation"])

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 4_845)
        self.assertEqual(
            self.report["primitive_part"]["decimal_digits"],
            4_845,
        )

    def test_factorization_attempts(self):
        attempts = FACTORIZATION_ATTEMPTS
        self.assertEqual(len(attempts), 3)
        self.assertTrue(all(not row["factor_found"] for row in attempts))
        self.assertEqual(
            [row["method"] for row in attempts],
            ["P-1", "P+1", "ECM"],
        )
        self.assertEqual(attempts[2]["curves"], 12)
        self.assertEqual(attempts[2]["B1"], 250_000)
        self.assertEqual(attempts[2]["B2"], 40_000_000)

    def test_level3_role(self):
        self.assertEqual(
            self.report["level3_role"]["affected_preview_roots"],
            [4_743_650_391, 8_019_668_082, 72_557_343_957],
        )

if __name__ == "__main__":
    unittest.main()
