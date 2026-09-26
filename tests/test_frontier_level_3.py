import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.frontier_level_3 import (
    ACTIVE_UNRESOLVED_LEVEL3_GATES,
    HARD_UNRESOLVED_LEVEL3_GATES,
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
            [13, 17, 19, 23, 29, 31, 37, 43, 53, 59, 67, 73, 79, 103, 109, 131, 137, 139, 149, 157, 163, 199, 227, 229, 233],
        )
        self.assertEqual(self.report["next_unresolved_gate"], 47)

    def test_hard_unresolved_vs_unworked(self):
        self.assertEqual(HARD_UNRESOLVED_LEVEL3_GATES, {47, 71, 83, 101, 113, 251, 269})
        self.assertEqual(
            self.report["hard_unresolved_preview_gates"],
            [47, 71, 83, 101, 113, 251, 269],
        )
        self.assertEqual(ACTIVE_UNRESOLVED_LEVEL3_GATES, set())
        self.assertEqual(
            self.report["active_unresolved_preview_gates"],
            [],
        )
        self.assertNotIn(157, self.report["unworked_preview_gates"])
        self.assertEqual(self.report["next_unworked_gate"], 277)
        self.assertEqual(self.report["unworked_preview_gates"][0], 277)

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

    def test_gate_137_direct_method(self):
        row = self.report["verified_gate_witnesses"]["137"]
        self.assertEqual(row["witness"], 3_415_957)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_139_direct_method(self):
        row = self.report["verified_gate_witnesses"]["139"]
        self.assertEqual(row["witness"], 12_635_933)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_229_compiled_direct_method(self):
        row = self.report["verified_gate_witnesses"]["229"]
        self.assertEqual(row["witness"], 257_753_713_526_201)
        self.assertEqual(row["kind"], "compiled-prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_233_primitive_pminus1_method(self):
        row = self.report["verified_gate_witnesses"]["233"]
        self.assertEqual(row["witness"], 179_216_201_898_552_121)
        self.assertEqual(row["kind"], "primitive-part-pminus1-prime")
        self.assertEqual(row["primitive_quotient"], "P_54289 / P_233")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_227_direct_method(self):
        row = self.report["verified_gate_witnesses"]["227"]
        self.assertEqual(row["witness"], 309_173)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_199_direct_method(self):
        row = self.report["verified_gate_witnesses"]["199"]
        self.assertEqual(row["witness"], 21_788_153_393)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_163_direct_method(self):
        row = self.report["verified_gate_witnesses"]["163"]
        self.assertEqual(row["witness"], 2_247_896_813)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_157_ecm_pocklington_method(self):
        row = self.report["verified_gate_witnesses"]["157"]
        self.assertEqual(row["witness"], 42_720_756_963_545_450_051_849)
        self.assertEqual(row["kind"], "primitive-part-ecm-prime")
        self.assertEqual(row["primitive_quotient"], "P_24649 / P_157")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_149_direct_method(self):
        row = self.report["verified_gate_witnesses"]["149"]
        self.assertEqual(row["witness"], 5_328_241)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_131_direct_method(self):
        row = self.report["verified_gate_witnesses"]["131"]
        self.assertEqual(row["witness"], 2_745_761)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_109_compiled_direct_method(self):
        row = self.report["verified_gate_witnesses"]["109"]
        self.assertEqual(row["witness"], 12_203_170_399_877)
        self.assertEqual(row["kind"], "compiled-prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_103_direct_method(self):
        row = self.report["verified_gate_witnesses"]["103"]
        self.assertEqual(row["witness"], 403_141)
        self.assertEqual(row["kind"], "prime-direct")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_gate_79_primitive_method(self):
        row = self.report["verified_gate_witnesses"]["79"]
        self.assertEqual(row["witness"], 2_266_870_750_557_409)
        self.assertEqual(row["primitive_quotient"], "P_6241 / P_79")
        self.assertTrue(row["prime_verified"])
        self.assertTrue(row["exact_rank_verified"])

    def test_promotion_ready_roots(self):
        self.assertEqual(self.report["promotion_ready_root_count"], 9)
        self.assertIn(711_474, self.report["promotion_ready_roots"])
        by_root = {door["root"]: door for door in self.report["doors"]}
        self.assertTrue(by_root[711_474]["promotion_ready"])
        self.assertEqual(by_root[711_474]["unresolved_prime_gates"], [])
        self.assertTrue(by_root[2_989_473]["promotion_ready"])
        self.assertEqual(by_root[2_989_473]["unresolved_prime_gates"], [])
        self.assertTrue(by_root[2_820_552]["promotion_ready"])
        self.assertEqual(by_root[2_820_552]["unresolved_prime_gates"], [])
        self.assertEqual(by_root[29_770_544_451]["unresolved_prime_gates"], [3851, 15809])
        self.assertEqual(by_root[75_434_532]["resolved_novel_support"], [31, 199])
        self.assertEqual(by_root[75_434_532]["unresolved_prime_gates"], [1019])
        self.assertTrue(by_root[49_713]["promotion_ready"])
        self.assertEqual(by_root[49_713]["unresolved_prime_gates"], [])
        self.assertEqual(by_root[61_455_314_793]["resolved_novel_support"], [227])
        self.assertEqual(by_root[61_455_314_793]["unresolved_prime_gates"], [90_242_753])
        self.assertTrue(by_root[4_809]["promotion_ready"])
        self.assertEqual(by_root[4_809]["unresolved_prime_gates"], [])
        self.assertEqual(by_root[8_008_342_512]["resolved_novel_support"], [229])
        self.assertEqual(by_root[8_008_342_512]["unresolved_prime_gates"], [728_561])
        self.assertFalse(by_root[4_209_500_564_058]["promotion_ready"])
        self.assertEqual(by_root[4_209_500_564_058]["resolved_novel_support"], [233])
        self.assertEqual(by_root[4_209_500_564_058]["unresolved_prime_gates"], [3_011_087_671])
        self.assertFalse(by_root[4_276_191]["promotion_ready"])
        self.assertEqual(by_root[4_276_191]["unresolved_prime_gates"], [18_043])
        self.assertFalse(by_root[8_443_383]["promotion_ready"])
        self.assertEqual(by_root[8_443_383]["unresolved_prime_gates"], [1_453])
        self.assertFalse(by_root[432_849]["promotion_ready"])
        self.assertEqual(by_root[432_849]["resolved_novel_support"], [157])
        self.assertEqual(by_root[432_849]["unresolved_prime_gates"], [919])

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
