import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.frontier_levels import is_prime_64
from calculation.gate_233 import (
    COMPILED_SCAN,
    DIRECT_SCAN,
    FACTORIZATION,
    PRIMITIVE_SHA256,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    WITNESS_SIGN,
    build_report,
    primitive_quotient,
)
from calculation.mirror_frontier import exact_rank_target
from calculation.pell_atlas import pell_rank

class Gate233Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 54_289)

    def test_status_resolved(self):
        self.assertEqual(self.report["status"], "RESOLVED")

    def test_direct_scan_history(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_466)
        self.assertEqual(DIRECT_SCAN["hits"], [])

    def test_compiled_scan_history(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["end_k"], 10_000_000_000)
        self.assertEqual(scan["small_prime_sieve_survivors"], 246_891_343)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)
        self.assertEqual(scan["implementation"], COMPILED_SCAN["implementation"])

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 20_692)
        self.assertEqual(
            self.report["primitive_part"]["sha256"],
            PRIMITIVE_SHA256,
        )
        self.assertEqual(q % WITNESS, 0)
        self.assertTrue(self.report["primitive_part"]["witness_divides_primitive"])

    def test_factorization_discovery(self):
        self.assertEqual(FACTORIZATION["method"], "P-1")
        self.assertEqual(FACTORIZATION["B1"], 50_000)
        self.assertEqual(FACTORIZATION["B2"], 10_000_000)
        self.assertEqual(FACTORIZATION["preloaded_order_factor"], TARGET_RANK)
        self.assertTrue(FACTORIZATION["factor_found"])
        self.assertEqual(FACTORIZATION["factor"], WITNESS)
        self.assertEqual(FACTORIZATION["exit_status"], 6)

    def test_witness_identity_and_prime(self):
        self.assertEqual(WITNESS_SIGN, 1)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + WITNESS_SIGN)
        self.assertEqual(WITNESS_K % 8, 0)
        self.assertTrue(is_prime_64(WITNESS))
        self.assertTrue(self.report["explicit_prime_witness"]["prime_verified"])

    def test_exact_rank_two_paths(self):
        self.assertTrue(exact_rank_target(WITNESS, TARGET_RANK))
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [4_209_500_564_058])
        self.assertEqual(
            role["remaining_other_gate_support"],
            {"4209500564058": [3_011_087_671]},
        )
        self.assertIn("3011087671", role["promotion_effect"])

if __name__ == "__main__":
    unittest.main()
