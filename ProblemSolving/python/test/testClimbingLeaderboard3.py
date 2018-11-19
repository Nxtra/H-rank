from ClimbingLeaderboard3 import find_insert_index
from ClimbingLeaderboard3 import climbingLeaderboard
from ddt import ddt, data, unpack
import unittest
from collections import OrderedDict


class test_AppendAndDelete3(unittest.TestCase):


    def test_climbingLeaderboard(self):
        scores = [100, 50, 25, 25, 15, 10]
        scores_alice = [0, 12, 25, 55]
        positions = climbingLeaderboard(scores, scores_alice)
        self.assertEqual([6, 5, 3, 2], positions)


