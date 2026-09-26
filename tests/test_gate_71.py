import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_71 import TARGET_RANK, build_report, primitive_quotient

class Gate71Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 5_041)

    def test_status_boundary(self):
        self.assertEqual(self.report["status"], "HARD_UNRESOLVED")
        self.assertTrue(self.report["known_theory"]["primitive_prime_divisor_existence"])
        self.assertIn("nonexistence", self.report["boundary"])

    def test_direct_scan_accounting(self):
        scan = self.report["direct_scan"]
        self.assertEqual(scan["max_k"], 100_000_000)
        self.assertEqual(scan["prime_candidates_tested"], 3_917_148)
        self.assertEqual(scan["largest_candidate_bound"], 504_100_000_001)
        self.assertEqual(scan["hits"], [])

    def test_compiled_scan_checkpoint(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["end_k"], 10_000_000_000)
        self.assertEqual(scan["small_prime_sieve_survivors"], 493_447_289)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 1_903)
        self.assertEqual(self.report["primitive_part"]["decimal_digits"], 1_903)

    def test_factorization_attempts(self):
        attempts = self.report["factorization_attempts"]
        self.assertEqual(len(attempts), 6)
        self.assertTrue(all(not row["factor_found"] for row in attempts))
        self.assertEqual([row["B1"] for row in attempts], [50_000, 50_000, 250_000, 250_000, 1_000_000, 1_000_000])

if __name__ == "__main__":
    unittest.main()
