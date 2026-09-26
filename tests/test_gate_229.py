import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_229 import (
    COMPILED_SCAN,
    DIRECT_SCAN,
    PRIMITIVE_SHA256,
    TARGET_RANK,
    WITNESS,
    WITNESS_K,
    build_report,
    primitive_quotient,
)
from calculation.pell_atlas import pell_rank

class Gate229Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_target_rank(self):
        self.assertEqual(TARGET_RANK, 52_441)

    def test_witness(self):
        row = self.report["explicit_prime_witness"]
        self.assertEqual(WITNESS, WITNESS_K * TARGET_RANK + 1)
        self.assertTrue(row["identity_verified"])
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])
        self.assertEqual(pell_rank(WITNESS, TARGET_RANK), TARGET_RANK)

    def test_direct_scan(self):
        self.assertEqual(DIRECT_SCAN["end_k"], 200_000)
        self.assertEqual(DIRECT_SCAN["prime_candidates_tested"], 4_529)
        self.assertEqual(DIRECT_SCAN["hits"], [])

    def test_compiled_scan(self):
        self.assertEqual(COMPILED_SCAN["end_k"], 10_000_000_000)
        self.assertEqual(COMPILED_SCAN["small_prime_sieve_survivors"], 246_915_578)
        self.assertEqual(COMPILED_SCAN["pell_divisibility_hits"], 1)
        self.assertEqual(COMPILED_SCAN["prime_hits"], 1)
        self.assertEqual(COMPILED_SCAN["best_p"], WITNESS)
        self.assertEqual(COMPILED_SCAN["best_k"], WITNESS_K)

    def test_primitive_quotient(self):
        q = primitive_quotient()
        primitive = self.report["primitive_part"]
        self.assertEqual(len(str(q)), 19_986)
        self.assertEqual(primitive["sha256"], PRIMITIVE_SHA256)
        self.assertTrue(primitive["witness_divides_primitive"])

    def test_level3_role(self):
        role = self.report["level3_role"]
        self.assertEqual(role["affected_preview_roots"], [4_809, 8_008_342_512])
        self.assertEqual(role["promotion_ready_after_resolution"], [4_809])
        self.assertEqual(role["still_blocked"], {"8008342512": [728_561]})

if __name__ == "__main__":
    unittest.main()
