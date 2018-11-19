#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right
from collections import OrderedDict


def do_bisect(scores, score_alice):
    insert_position = len(scores) - bisect_right(scores, score_alice) + 1
    return insert_position


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, scores_alice):
    positions = []
    scores = list(set(scores))
    scores.sort()
    for score_alice in scores_alice:
        positions.append(do_bisect(scores, score_alice))
    return positions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
