import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.query_atlas import (
    describe_number, inverse_square_rank, members_in_fiber,
    mirror_13_31_compatibility,
)

class AtlasQueryTests(unittest.TestCase):
    def test_describe_known_collision_member(self):
        out = describe_number(3529, 1764)
        self.assertEqual(out["rank"], 1764)
        self.assertEqual(out["square_rank_root"], 42)
        self.assertTrue(out["stored"])

    def test_fiber_42_query(self):
        members = {int(r["n"]) for r in members_in_fiber(42)}
        self.assertTrue({3529, 9261, 21389, 1203930}.issubset(members))

    def test_inverse_210(self):
        out = inverse_square_rank(210)
        self.assertEqual(out["rank"], 44100)
        self.assertTrue(out["absorbs_13_31_mirror"])
        self.assertIn(198477, out["stored_members"])

    def test_mirror_host_198477(self):
        out = mirror_13_31_compatibility(198477, 44100)
        self.assertTrue(out["mirror_compatible"])
        self.assertTrue(out["verified_invariant"])
        self.assertEqual(out["state_ranks"], [44100, 44100, 44100, 44100])

    def test_non_mirror_host_3529(self):
        out = mirror_13_31_compatibility(3529, 1764)
        self.assertFalse(out["mirror_compatible"])

if __name__ == "__main__":
    unittest.main()
