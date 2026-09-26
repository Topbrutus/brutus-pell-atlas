import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_47 import (
    ARCHIVED_FACTOR_RUNS,
    DIRECT_SCAN_WINDOWS,
    TARGET_RANK,
    build_report,
    primitive_quotient,
)
from calculation.gate_scan import scan_window

class Gate47Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 2_209)

    def test_status_is_unresolved_not_nonexistent(self):
        self.assertEqual(self.report["status"], "HARD_UNRESOLVED")
        self.assertTrue(self.report["known_theory"]["primitive_prime_divisor_existence"])
        self.assertIn("nonexistence", self.report["boundary"])

    def test_direct_scan_accounting(self):
        scan = self.report["direct_scan"]
        self.assertEqual(scan["max_k"], 1_000_000_000)
        self.assertEqual(scan["prime_candidates_tested"], 37_316_974)
        self.assertEqual(scan["largest_candidate_bound"], 2_209_000_000_001)
        self.assertEqual(scan["hits"], [])
        self.assertEqual(len(DIRECT_SCAN_WINDOWS), 4)

    def test_primitive_quotient_metadata(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 828)
        self.assertEqual(self.report["primitive_part"]["decimal_digits"], 828)
        self.assertEqual(self.report["primitive_part"]["archived_factor_run_outputs"], 1_224)
        self.assertEqual(sum(ARCHIVED_FACTOR_RUNS.values()), 1_224)
        self.assertEqual(self.report["primitive_part"]["archived_outputs_different_from_input"], 0)

    def test_small_direct_scan_reproducible(self):
        row = scan_window(47, 1, 200, stop_after=1)
        self.assertEqual(row["hits"], [])

if __name__ == "__main__":
    unittest.main()
