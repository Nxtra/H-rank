#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right
from collections import OrderedDict


def find_insert_index(scores, score_alice):
    return bisect_right(scores, score_alice)


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, scores_alice):
    positions = []
    scores = list(set(scores))
    original_len = len(scores)
    scores.sort()
    last_insert_index = 0
    for score_alice in scores_alice:
        insert_index_in_current_score_list = find_insert_index(scores, score_alice)
        last_insert_index = last_insert_index + insert_index_in_current_score_list
        insert_position = original_len - last_insert_index + 1
        positions.append(insert_position)
        scores = scores[insert_index_in_current_score_list:]
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
