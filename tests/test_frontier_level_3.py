import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.frontier_level_3 import (
    KNOWN_LEVEL3_GATE_WITNESSES,
    build_level_3_preview,
)
from calculation.pell_atlas import pell_rank

class FrontierLevel3PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_level_3_preview()

    def test_preview_counts(self):
        self.assertEqual(self.report["simulated_closure_count"], 326)
        self.assertEqual(self.report["new_mirror_root_count"], 160)
        self.assertEqual(self.report["novel_prime_gate_count"], 210)

    def test_preview_not_promoted(self):
        self.assertEqual(self.report["status"], "SIMULATION_ONLY_NOT_PROMOTED")

    def test_resolved_gate_prefix(self):
        self.assertEqual(
            self.report["resolved_preview_gates"],
            [13, 17, 19, 23, 29, 31, 37, 43, 53, 59, 67, 73],
        )
        self.assertEqual(self.report["next_unresolved_gate"], 47)

    def test_known_gate_witnesses(self):
        checks = self.report["verified_gate_witnesses"]
        for gate, data in KNOWN_LEVEL3_GATE_WITNESSES.items():
            row = checks[str(gate)]
            self.assertEqual(row["witness"], data["witness"])
            self.assertEqual(row["rank"], gate * gate)
            self.assertTrue(row["prime_verified"])
            self.assertTrue(row["exact_rank_verified"])

    def test_iterative_ranks_for_small_gate_witnesses(self):
        for gate, data in KNOWN_LEVEL3_GATE_WITNESSES.items():
            self.assertEqual(pell_rank(data["witness"], gate * gate), gate * gate)

    def test_gate_73_direct_method(self):
        row = self.report["verified_gate_witnesses"]["73"]
        self.assertEqual(row["witness"], 159_869)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_67_direct_method(self):
        row = self.report["verified_gate_witnesses"]["67"]
        self.assertEqual(row["witness"], 454_134_173)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_59_direct_method(self):
        row = self.report["verified_gate_witnesses"]["59"]
        self.assertEqual(row["witness"], 31_217_609)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_53_primitive_method(self):
        row = self.report["verified_gate_witnesses"]["53"]
        self.assertEqual(row["witness"], 13_747_841_783_933_689)
        self.assertEqual(row["primitive_quotient"], "P_2809 / P_53")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_43_primitive_method(self):
        row = self.report["verified_gate_witnesses"]["43"]
        self.assertEqual(row["witness"], 938_887_039_417)
        self.assertEqual(row["primitive_quotient"], "P_1849 / P_43")

if __name__ == "__main__":
    unittest.main()
