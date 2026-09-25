import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_757 import (
    GATE_ROOT,
    MIRROR_ROOT,
    MIRROR_TARGET_RANK,
    MIRROR_WITNESS,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
)
from calculation.gate_scan import lucas_rank_congruence_admissible
from calculation.pell_atlas import pell_rank

class Gate757Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_constants(self):
        self.assertEqual(GATE_ROOT, 757)
        self.assertEqual(TARGET_RANK, 573_049)
        self.assertEqual(MIRROR_ROOT, 2_271)
        self.assertEqual(MIRROR_TARGET_RANK, 5_157_441)

    def test_witness_identity(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_iterative_rank_of_prime_witness(self):
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_unlocked_2271_witness(self):
        row = self.report["unlocked_mirror_root"]
        self.assertEqual(row["witness"], MIRROR_WITNESS)
        self.assertEqual(row["target_rank"], MIRROR_TARGET_RANK)
        self.assertEqual(row["gcd_components"], 1)
        self.assertTrue(row["exact_rank_verified"])

    def test_iterative_rank_of_2271_witness(self):
        self.assertEqual(pell_rank(MIRROR_WITNESS, MIRROR_TARGET_RANK), MIRROR_TARGET_RANK)

    def test_congruence_filter_accepts_witness(self):
        self.assertTrue(lucas_rank_congruence_admissible(757, WITNESS_K, 1))

    def test_scan_accounting_to_first_hit(self):
        self.assertEqual(
            self.report["combined"]["prime_candidates_tested_to_first_hit"],
            1_286_608,
        )
        self.assertEqual(self.report["combined"]["first_hit_k"], WITNESS_K)

if __name__ == "__main__":
    unittest.main()
