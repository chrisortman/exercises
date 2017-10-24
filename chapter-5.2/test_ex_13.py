import unittest
from ex_5_13 import falling_distance

class TestDistanceCalculation(unittest.TestCase):
    def test_one_second(self):
        self.assertEqual( falling_distance(1), 4.9 )

unittest.main()
