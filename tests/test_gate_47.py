import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_47 import (
    ARCHIVED_FACTOR_RUNS,
    COMPILED_PELL_SCAN_WINDOWS,
    DIRECT_SCAN_WINDOWS,
    RECENT_FACTOR_CAMPAIGNS,
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

    def test_compiled_scan_extension(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["max_k"], 10_000_000_000)
        self.assertEqual(scan["largest_candidate_bound"], 22_090_000_000_001)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)
        self.assertEqual(len(COMPILED_PELL_SCAN_WINDOWS), 3)
        self.assertEqual(COMPILED_PELL_SCAN_WINDOWS[-1]["small_prime_sieve_survivors"], 451_314_038)

    def test_recent_factor_campaigns_are_negative_only(self):
        self.assertEqual(len(RECENT_FACTOR_CAMPAIGNS), 3)
        self.assertTrue(all(not row["factor_found"] for row in RECENT_FACTOR_CAMPAIGNS))
        self.assertEqual(RECENT_FACTOR_CAMPAIGNS[0]["B1"], 10_000_000)
        self.assertEqual(RECENT_FACTOR_CAMPAIGNS[1]["B1"], 10_000_000)
        self.assertEqual(RECENT_FACTOR_CAMPAIGNS[2]["completed_runs"], 12)
        self.assertEqual(self.report["frontier_class"], "DEEP_COMPUTATIONAL_FRONTIER")

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
