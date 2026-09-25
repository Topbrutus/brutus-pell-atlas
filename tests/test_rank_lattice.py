import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.rank_lattice import build_lattice

class RankLatticeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_lattice()

    def test_seed_roots(self):
        self.assertEqual(self.report["seed_roots"], [6, 7, 30, 42, 210])

    def test_closure_adds_identity(self):
        self.assertEqual(self.report["nodes"], [1, 6, 7, 30, 42, 210])
        self.assertTrue(self.report["identity_rank_verified"])

    def test_is_true_gcd_lcm_lattice(self):
        self.assertTrue(self.report["closed_under_gcd"])
        self.assertTrue(self.report["closed_under_lcm"])

    def test_hasse_edges(self):
        edges = {tuple(edge) for edge in self.report["hasse_edges"]}
        expected = {(1, 6), (1, 7), (6, 30), (6, 42), (7, 42), (30, 210), (42, 210)}
        self.assertEqual(edges, expected)

    def test_join_6_7_is_42(self):
        self.assertIn({"a": 6, "b": 7, "join": 42}, self.report["nontrivial_joins"])

    def test_join_7_30_is_210(self):
        self.assertIn({"a": 7, "b": 30, "join": 210}, self.report["nontrivial_joins"])

    def test_join_30_42_is_210(self):
        self.assertIn({"a": 30, "b": 42, "join": 210}, self.report["nontrivial_joins"])

    def test_square_rank_members(self):
        by_root = {row["root"]: row for row in self.report["node_records"]}
        self.assertIn(73, by_root[6]["stored_members"])
        self.assertIn(293, by_root[7]["stored_members"])
        self.assertIn(10877, by_root[30]["stored_members"])
        self.assertIn(3529, by_root[42]["stored_members"])
        self.assertIn(198477, by_root[210]["stored_members"])

if __name__ == "__main__":
    unittest.main()
