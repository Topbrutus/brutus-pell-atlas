import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_1481 import (
    GATE_ROOT,
    ROOT_4443,
    ROOT_8886,
    TARGET_4443,
    TARGET_8886,
    TARGET_RANK,
    WITNESS,
    WITNESS_4443,
    WITNESS_8886,
    WITNESS_K,
    build_report,
)
from calculation.gate_scan import lucas_rank_congruence_admissible
from calculation.pell_atlas import pell_rank

class Gate1481Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_constants(self):
        self.assertEqual(GATE_ROOT, 1481)
        self.assertEqual(TARGET_RANK, 2_193_361)
        self.assertEqual(ROOT_4443, 4_443)
        self.assertEqual(ROOT_8886, 8_886)

    def test_prime_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_iterative_rank_of_prime_witness(self):
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_congruence_filter_accepts_witness(self):
        self.assertTrue(lucas_rank_congruence_admissible(1481, WITNESS_K, 1))

    def test_scan_accounting_to_first_hit(self):
        self.assertEqual(self.report["combined"]["first_hit_k"], 6_004_032)
        self.assertEqual(self.report["combined"]["prime_candidates_tested_to_first_hit"], 205_702)

    def test_secondary_parallel_hit(self):
        row = self.report["secondary_parallel_hit"]
        self.assertEqual(row["k"], 15_422_416)
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_unlocked_4443(self):
        rows = {row["root"]: row for row in self.report["unlocked_mirror_roots"]}
        self.assertEqual(rows[4443]["witness"], WITNESS_4443)
        self.assertEqual(rows[4443]["target_rank"], TARGET_4443)
        self.assertEqual(rows[4443]["gcd_components"], 1)
        self.assertTrue(rows[4443]["exact_rank_verified"])

    def test_unlocked_8886(self):
        rows = {row["root"]: row for row in self.report["unlocked_mirror_roots"]}
        self.assertEqual(rows[8886]["witness"], WITNESS_8886)
        self.assertEqual(rows[8886]["target_rank"], TARGET_8886)
        self.assertEqual(rows[8886]["gcd_components"], [1, 1, 1])
        self.assertTrue(rows[8886]["exact_rank_verified"])

if __name__ == "__main__":
    unittest.main()
