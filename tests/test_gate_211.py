import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_211 import (
    TARGET_RANK,
    build_report,
    legendre_8_for_odd_prime_candidate,
    lucas_rank_congruence_admissible,
    scan_window,
)

class Gate211Tests(unittest.TestCase):
    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 44_521)

    def test_legendre_8_residues(self):
        self.assertEqual(legendre_8_for_odd_prime_candidate(17), 1)
        self.assertEqual(legendre_8_for_odd_prime_candidate(23), 1)
        self.assertEqual(legendre_8_for_odd_prime_candidate(11), -1)
        self.assertEqual(legendre_8_for_odd_prime_candidate(13), -1)

    def test_filter_matches_candidate_sign(self):
        for k in range(1, 80):
            for sign in (-1, 1):
                p = k * TARGET_RANK + sign
                expected = p > 2 and p % 2 == 1 and legendre_8_for_odd_prime_candidate(p) == sign
                self.assertEqual(lucas_rank_congruence_admissible(k, sign), expected)

    def test_small_scan_reproducible(self):
        result = scan_window(1, 200, stop_after=1)
        self.assertEqual(result["start_k"], 1)
        self.assertEqual(result["end_k"], 200)
        self.assertEqual(result["hits"], [])

    def test_report_records_deep_scan(self):
        report = build_report()
        self.assertEqual(report["combined"]["max_k"], 1_000_000_000)
        self.assertEqual(report["combined"]["prime_candidates_tested"], 33_061_422)
        self.assertEqual(report["combined"]["hits"], [])
        self.assertEqual(report["combined"]["largest_candidate_bound"], 44_521_000_000_001)
        self.assertEqual(len(report["computed_windows"]), 5)
        self.assertTrue(report["known_theory"]["primitive_prime_divisor_existence"])

if __name__ == "__main__":
    unittest.main()
