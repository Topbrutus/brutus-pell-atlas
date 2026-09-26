import sys
import unittest
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_157 import (
    ABORTED_ATTEMPTS,
    COMPILED_SCAN,
    DIRECT_SCAN,
    FACTORIZATION_ATTEMPTS,
    P_MINUS_ONE_FACTORS,
    POCKLINGTON_BASE,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    WITNESS_SIGN,
    build_report,
    primitive_quotient,
    primitive_sha256,
    verify_witness_primality,
)
from calculation.mirror_frontier import exact_rank_target
from calculation.pell_atlas import pell_rank

class Gate157Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 24_649)

    def test_status_resolved(self):
        self.assertEqual(self.report["status"], "RESOLVED")
        self.assertTrue(self.report["known_theory"]["primitive_prime_divisor_existence"])

    def test_direct_scan_history(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_725)
        self.assertEqual(DIRECT_SCAN["hits"], [])

    def test_compiled_scan_history(self):
        scan = self.report["compiled_pell_scan"]
        self.assertEqual(scan["end_k"], 10_000_000_000)
        self.assertEqual(scan["small_prime_sieve_survivors"], 247_573_895)
        self.assertEqual(scan["pell_divisibility_hits"], 0)
        self.assertEqual(scan["prime_hits"], 0)
        self.assertEqual(scan["implementation"], COMPILED_SCAN["implementation"])

    def test_primitive_quotient(self):
        q = primitive_quotient()
        self.assertEqual(len(str(q)), 9_375)
        self.assertEqual(
            primitive_sha256(),
            "af8f60fea2efe11b26aa3d863d7bf2aac31b7e587830b539f3b572819d113621",
        )
        self.assertEqual(q % WITNESS, 0)
        self.assertTrue(self.report["primitive_part"]["witness_divides"])

    def test_witness_identity(self):
        self.assertEqual(WITNESS_SIGN, 1)
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + WITNESS_SIGN)
        self.assertEqual(WITNESS_K % 8, 0)

    def test_pocklington_certificate(self):
        self.assertEqual(POCKLINGTON_BASE, 3)
        self.assertEqual(
            prod(q ** e for q, e in P_MINUS_ONE_FACTORS),
            WITNESS - 1,
        )
        self.assertTrue(verify_witness_primality())
        self.assertTrue(self.report["explicit_prime_witness"]["prime_verified"])

    def test_exact_rank_two_paths(self):
        self.assertTrue(exact_rank_target(WITNESS, TARGET_RANK))
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_factorization_history(self):
        attempts = FACTORIZATION_ATTEMPTS
        self.assertEqual([row["method"] for row in attempts], ["P-1", "P+1", "ECM", "ECM"])
        self.assertFalse(attempts[0]["factor_found"])
        self.assertFalse(attempts[1]["factor_found"])
        self.assertFalse(attempts[2]["factor_found"])
        self.assertTrue(attempts[3]["factor_found"])
        self.assertEqual(attempts[3]["factor_curve"], 3)
        self.assertEqual(attempts[3]["factor"], WITNESS)
        self.assertEqual(attempts[3]["exit_statuses"][2], 6)

    def test_aborted_heavy_campaign_not_negative_evidence(self):
        self.assertEqual(len(ABORTED_ATTEMPTS), 1)
        row = ABORTED_ATTEMPTS[0]
        self.assertEqual(row["status"], "ABORTED_INCOMPLETE")
        self.assertEqual(row["completed_curves"], 0)
        self.assertEqual(row["exit_statuses"], [143] * 12)
        self.assertIn("not counted", row["interpretation"])

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [432_849])
        self.assertEqual(role["remaining_other_gate_support"], {"432849": [919]})
        self.assertIn("919", role["promotion_effect"])

if __name__ == "__main__":
    unittest.main()
