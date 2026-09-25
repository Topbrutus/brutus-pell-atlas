import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.bridge_finder import build_report

class BridgeFinderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_collision_cluster_1764_found(self):
        clusters = [x for x in self.report["collision_clusters"] if x["rank"] == 1764]
        self.assertTrue(clusters)
        members = set(clusters[0]["members"])
        self.assertTrue({3529, 9261, 21389, 1203930}.issubset(members))

    def test_mirror_host_found(self):
        hosts = [x for x in self.report["mirror_hosts_13_31"] if x["host"] == 198477]
        self.assertTrue(hosts)
        self.assertEqual(hosts[0]["state_ranks"], [44100] * 4)

    def test_rank_preserving_130_times_9261_found(self):
        bridges = self.report["rank_preserving_products"]
        self.assertTrue(any(
            x["multiplier"] == 130 and x["host"] == 9261 and x["product"] == 1203930
            for x in bridges
        ))

    def test_square_lcm_73_149_found(self):
        bridges = self.report["square_lcm_products"]
        self.assertTrue(any(
            set(x["inputs"]) == {73, 149} and x["rank"] == 900
            for x in bridges
        ))

    def test_report_has_discovery_counts(self):
        counts = self.report["counts"]
        self.assertGreater(counts["collision_clusters"], 0)
        self.assertGreater(counts["square_lcm_products"], 0)
        self.assertGreater(counts["rank_preserving_products"], 0)

    def test_verified_unstored_products(self):
        products = set(self.report["verified_unstored_products"])
        self.assertIn(3809, products)
        self.assertIn(337187, products)
        self.assertGreater(self.report["counts"]["verified_unstored_products"], 0)
if __name__ == "__main__":
    unittest.main()
