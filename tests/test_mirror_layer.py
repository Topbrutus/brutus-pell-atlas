import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.mirror_layer import build_report, reverse_fixed_width, signed_mirror_orbit

class MirrorLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_30_mirrors_to_03(self):
        out = reverse_fixed_width(30, 2)
        self.assertEqual(out["mirror_token"], "03")
        self.assertEqual(out["mirror_value"], 3)

    def test_210_mirrors_to_012(self):
        out = reverse_fixed_width(210, 3)
        self.assertEqual(out["mirror_token"], "012")
        self.assertEqual(out["mirror_value"], 12)

    def test_signed_orbit_keeps_representation(self):
        out = signed_mirror_orbit(30, 2)
        self.assertEqual(out["orbit_tokens"], ["30", "03", "-30", "-03"])

    def test_all_reference_mirrors_supported(self):
        self.assertTrue(all(row["root_supported"] and row["mirror_supported"] for row in self.report["mirror_cases"]))

    def test_12_21_pair(self):
        rows = {(row["root"], row["mirror_root"]): row for row in self.report["mirror_cases"]}
        self.assertIn((12, 21), rows)
        self.assertIn((21, 12), rows)

    def test_24_42_pair(self):
        rows = {(row["root"], row["mirror_root"]): row for row in self.report["mirror_cases"]}
        self.assertIn((24, 42), rows)
        self.assertIn((42, 24), rows)

if __name__ == "__main__":
    unittest.main()
