from HurdleRace import hurdleRace
from ddt import ddt, data, unpack
import unittest



class test_AppendAndDelete3(unittest.TestCase):

    def test_hurdleRace(self):
        height = [1, 6, 3, 5, 2]
        k = 4
        sum_too_high = hurdleRace(k, height)
        self.assertEqual(2, sum_too_high)


