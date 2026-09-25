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
        self.assertEqual(
            self.report["seed_roots"],
            [1, 3, 6, 7, 12, 21, 24, 30, 42, 60, 84, 120, 168, 210, 420, 840],
        )

    def test_closure_nodes(self):
        self.assertEqual(
            self.report["nodes"],
            [1, 3, 6, 7, 12, 21, 24, 30, 42, 60, 84, 120, 168, 210, 420, 840],
        )
        self.assertTrue(self.report["identity_rank_verified"])

    def test_is_true_gcd_lcm_lattice(self):
        self.assertTrue(self.report["closed_under_gcd"])
        self.assertTrue(self.report["closed_under_lcm"])

    def test_hasse_edges(self):
        edges = {tuple(edge) for edge in self.report["hasse_edges"]}
        expected = {
            (1,3),(1,7),(3,6),(3,21),(6,12),(6,30),(6,42),(7,21),
            (12,24),(12,60),(12,84),(21,42),(24,120),(24,168),
            (30,60),(30,210),(42,84),(42,210),(60,120),(60,420),
            (84,168),(84,420),(120,840),(168,840),(210,420),(420,840),
        }
        self.assertEqual(edges, expected)

    def test_key_joins(self):
        joins = {(row["a"], row["b"], row["join"]) for row in self.report["nontrivial_joins"]}
        for triple in ((3,7,21),(6,7,42),(7,30,210),(12,30,60),(24,42,168),(30,42,210)):
            self.assertIn(triple, joins)

    def test_every_lattice_node_is_inhabited(self):
        self.assertTrue(all(not row["structural_only"] for row in self.report["node_records"]))

    def test_square_rank_members(self):
        by_root = {row["root"]: row for row in self.report["node_records"]}
        expected = {
            1:1,3:197,6:73,7:293,12:7081,21:57721,24:18761,30:10877,
            42:3529,60:12752881,84:24988849,120:33788561,168:66207569,
            210:198477,420:1405415637,840:3723626997,
        }
        for root, member in expected.items():
            self.assertIn(member, by_root[root]["stored_members"])

if __name__ == "__main__":
    unittest.main()
