import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_211 import (
    CANONICAL_K,
    CANONICAL_SIGN,
    CANONICAL_WITNESS,
    ROOT_633,
    ROOT_67731,
    SECONDARY_K,
    SECONDARY_SIGN,
    SECONDARY_WITNESS,
    TARGET_633,
    TARGET_67731,
    TARGET_RANK,
    WITNESS_633,
    WITNESS_67731,
    build_report,
    legendre_8_for_odd_prime_candidate,
    lucas_rank_congruence_admissible,
    scan_window,
)
from calculation.pell_atlas import pell_rank

class Gate211Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

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
                expected = (
                    p > 2
                    and p % 2 == 1
                    and p % 4 == 1
                    and legendre_8_for_odd_prime_candidate(p) == sign
                )
                self.assertEqual(lucas_rank_congruence_admissible(k, sign), expected)

    def test_small_scan_reproducible(self):
        result = scan_window(1, 200, stop_after=1)
        self.assertEqual(result["start_k"], 1)
        self.assertEqual(result["end_k"], 200)
        self.assertEqual(result["hits"], [])

    def test_report_records_deep_scan(self):
        scan = self.report["combined_scan"]
        self.assertEqual(scan["max_k"], 1_000_000_000)
        self.assertEqual(scan["prime_candidates_tested"], 33_061_422)
        self.assertEqual(scan["hits"], [])
        self.assertEqual(scan["largest_candidate_bound"], 44_521_000_000_001)
        self.assertEqual(len(self.report["computed_windows"]), 5)

    def test_canonical_discovery_metadata(self):
        row = self.report["ecm_resolution"]["canonical_discovery"]
        self.assertEqual(row["method"], "P+1")
        self.assertEqual(row["B1"], 50_000)
        self.assertEqual(row["B2"], 9_714_820)
        self.assertEqual(row["preloaded_order_factor"], 44_521)
        self.assertEqual(row["exit_status"], 6)

    def test_canonical_prime_witness(self):
        row = self.report["ecm_resolution"]["canonical_witness"]
        self.assertEqual(CANONICAL_WITNESS, CANONICAL_K * TARGET_RANK + CANONICAL_SIGN)
        self.assertEqual(row["p"], CANONICAL_WITNESS)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(CANONICAL_WITNESS, TARGET_RANK), TARGET_RANK)

    def test_secondary_prime_witness(self):
        row = self.report["ecm_resolution"]["secondary_verified_witness"]
        self.assertEqual(SECONDARY_WITNESS, SECONDARY_K * TARGET_RANK + SECONDARY_SIGN)
        self.assertEqual(row["p"], SECONDARY_WITNESS)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(SECONDARY_WITNESS, TARGET_RANK), TARGET_RANK)

    def test_unlocked_633(self):
        rows = {row["root"]: row for row in self.report["unlocked_mirror_roots"]}
        row = rows[ROOT_633]
        self.assertEqual(row["witness"], WITNESS_633)
        self.assertEqual(row["target_rank"], TARGET_633)
        self.assertEqual(row["gcd_components"], 1)
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS_633, TARGET_633), TARGET_633)

    def test_unlocked_67731(self):
        rows = {row["root"]: row for row in self.report["unlocked_mirror_roots"]}
        row = rows[ROOT_67731]
        self.assertEqual(row["witness"], WITNESS_67731)
        self.assertEqual(row["target_rank"], TARGET_67731)
        self.assertEqual(row["gcd_components"], [1, 1, 1])
        self.assertTrue(row["exact_rank_verified"])

if __name__ == "__main__":
    unittest.main()
