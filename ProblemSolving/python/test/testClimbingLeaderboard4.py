from ClimbingLeaderboard4 import find_positions_in_desc_order
from ClimbingLeaderboard4 import climbingLeaderboard
from ClimbingLeaderboard4 import filterfalse
from ClimbingLeaderboard4 import unique_everseen
from ddt import ddt, data, unpack
import unittest
from collections import OrderedDict


class test_AppendAndDelete3(unittest.TestCase):

    def test_find_positions_in_desc_order(self):
        scores = [100, 50, 25, 25, 15, 10]
        scores = list(unique_everseen(scores))
        scores_alice = [0, 12, 25, 55, 120]
        scores_alice.reverse()
        positions = find_positions_in_desc_order(scores, scores_alice)
        self.assertEqual([1, 2, 3, 5, 6], positions)

    def test_climbingLeaderboard(self):
        scores = [100, 50, 25, 25, 15, 10]
        scores_alice = [0, 12, 25, 55, 120]
        positions = climbingLeaderboard(scores, scores_alice)
        self.assertEqual([6, 5, 3, 2, 1], positions)


