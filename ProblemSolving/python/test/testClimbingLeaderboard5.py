from ClimbingLeaderboard5 import get_positions
from ddt import ddt, data, unpack
import unittest
from collections import OrderedDict


class test_AppendAndDelete3(unittest.TestCase):

    def test_get_positions(self):
        scores = [100, 50, 25, 25, 15, 10]
        scores = sorted(list(set(scores)))[::-1]
        scores_alice = [0, 12, 25, 55, 120]
        positions = get_positions(scores, scores_alice)
        self.assertEqual([6, 5, 3, 2, 1], positions)


