import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.gate_211_primitive import build_report

class Gate211PrimitiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_exact_primitive_identity(self):
        self.assertTrue(self.report["division_exact"])
        self.assertEqual(self.report["index"], 44_521)
        self.assertEqual(self.report["divisor_index"], 211)

    def test_sizes(self):
        self.assertEqual(self.report["P_211_digits"], 81)
        self.assertEqual(self.report["P_44521_digits"], 17_042)
        self.assertEqual(self.report["primitive_digits"], 16_961)

    def test_fingerprint(self):
        self.assertEqual(
            self.report["primitive_sha256"],
            "d516a24aaa5abcf58f1a232596db70b390174e74bab44b20ae0682896703321e",
        )

    def test_coprime_to_previous_pell_term(self):
        self.assertEqual(self.report["gcd_primitive_P_211"], 1)
        self.assertEqual(self.report["primitive_mod_211"], 210)

if __name__ == "__main__":
    unittest.main()
