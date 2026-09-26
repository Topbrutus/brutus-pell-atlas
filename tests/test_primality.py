import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculation.primality import verify_pocklington_certificate

class PocklingtonCertificateTests(unittest.TestCase):
    def test_gate_157_certificate(self):
        n = 42_720_756_963_545_450_051_849
        factors = [
            (2, 3),
            (31, 1),
            (157, 2),
            (335_957, 1),
            (20_801_960_107, 1),
        ]
        self.assertTrue(verify_pocklington_certificate(n, factors, 3))

    def test_rejects_wrong_factorization(self):
        n = 42_720_756_963_545_450_051_849
        factors = [(2, 3), (31, 1), (157, 2)]
        self.assertFalse(verify_pocklington_certificate(n, factors, 3))

    def test_rejects_composite(self):
        self.assertFalse(
            verify_pocklington_certificate(
                91,
                [(2, 1), (3, 2)],
                3,
            )
        )

if __name__ == "__main__":
    unittest.main()
