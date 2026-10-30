import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.post_frontier_probe import verify_prime_controls


class PostFrontierProbeTests(unittest.TestCase):
    def test_first_post_frontier_prime_controls_are_prime_but_not_witnesses(self):
        rows = verify_prime_controls()
        self.assertEqual(len(rows), 3)
        self.assertEqual([row["root"] for row in rows], [47, 71, 83])
        self.assertTrue(all(row["prime"] for row in rows))
        self.assertTrue(all(row["pell_target_residue"] != 0 for row in rows))
        self.assertTrue(all(not row["exact_rank"] for row in rows))

    def test_exact_recorded_residues(self):
        rows = verify_prime_controls()
        residues = {row["root"]: row["pell_target_residue"] for row in rows}
        self.assertEqual(residues[47], 6_785_485_971_658)
        self.assertEqual(residues[71], 15_070_090_373_130)
        self.assertEqual(residues[83], 45_244_365_050_142)


if __name__ == "__main__":
    unittest.main()
