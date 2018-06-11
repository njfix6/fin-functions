import unittest
from context import finfunctions

class TestNPV(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(float("{0:.5f}".format(finfunctions.npv(10, 0.2, 2, 3, 4))), -3.94907)


if __name__ == '__main__':
    unittest.main()
