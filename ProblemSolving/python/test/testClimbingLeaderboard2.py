from ClimbingLeaderboard2 import do_bisect
from ClimbingLeaderboard2 import climbingLeaderboard
from ddt import ddt, data, unpack
import unittest
from collections import OrderedDict


@ddt
class test_AppendAndDelete2(unittest.TestCase):

    @data((20, 4),
          (10, 4),
          (5, 5),
          (40, 3))
    @unpack
    def test_do_bisect_one(self, value1, value2):
        scores = [100, 50, 40, 40, 10]
        scores.sort()
        sorted_set_scores = list(OrderedDict.fromkeys(scores))
        score_alice = value1
        insert_position = do_bisect(sorted_set_scores, score_alice)
        self.assertEqual(value2, insert_position, "Tested with score alice: {} and expected position {} but got {}"
                         .format(score_alice, value2, insert_position))

    def test_climbingLeaderboard(self):
        scores = [100, 50, 25, 25, 15, 10]
        scores_alice = [0, 12]
        positions = climbingLeaderboard(scores, scores_alice)
        self.assertEqual([6, 5], positions)


