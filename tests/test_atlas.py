import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.pell_atlas import (
    fiber_members, load_atlas, pell_rank, square_root_if_square, verify_atlas
)

class BrutusPellAtlasTests(unittest.TestCase):
    def test_rank_13(self):
        self.assertEqual(pell_rank(13, 7), 7)

    def test_rank_13_squared_is_silent(self):
        self.assertEqual(pell_rank(13**2, 7), 7)

    def test_rank_31(self):
        self.assertEqual(pell_rank(31, 30), 30)

    def test_rank_31_squared_is_silent(self):
        self.assertEqual(pell_rank(31**2, 30), 30)

    def test_73_149_square_rank(self):
        self.assertEqual(pell_rank(73 * 149, 900), 900)
        self.assertEqual(square_root_if_square(900), 30)
    def test_fiber_42_collision(self):
        for n in (73 * 293, 3529, 21**3):
            self.assertEqual(pell_rank(n, 1764), 1764)

    def test_1203930_rank(self):
        self.assertEqual(pell_rank(1203930, 1764), 1764)

    def test_mirror_host(self):
        self.assertEqual(pell_rank(198477, 44100), 44100)

    def test_all_mirror_host_states(self):
        host = 198477
        states = (host, 13**2 * host, 31**2 * host, 13**2 * 31**2 * host)
        for n in states:
            self.assertEqual(pell_rank(n, 44100), 44100)

    def test_stored_fiber_42(self):
        members = set(fiber_members(42))
        self.assertTrue({21389, 3529, 9261, 1203930}.issubset(members))

    def test_every_stored_record_recomputes(self):
        checks = verify_atlas()
        self.assertTrue(checks)
        self.assertTrue(all(check.passed for check in checks))

    def test_atlas_has_relations(self):
        atlas = load_atlas()
        self.assertGreaterEqual(len(atlas["relations"]), 3)

if __name__ == "__main__":
    unittest.main()
