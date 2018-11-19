#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right
from collections import OrderedDict

def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


# Complete the climbingLeaderboard function below.
def find_positions_in_desc_order(scores, scores_alice_in_desc_order):
    positions = []
    index_scores = 0
    index_alice_scores = 0
    scores.append(0)
    len_scores = len(scores)
    len_scores_alice = len(scores_alice_in_desc_order)
    while index_scores < len_scores and index_alice_scores < len_scores_alice:
        score_alice = scores_alice_in_desc_order[index_alice_scores]
        if score_alice >= scores[index_scores]:
            current_position = index_scores + 1
            positions.append(current_position)
            index_alice_scores += 1
        else:
            index_scores += 1
    return positions


def climbingLeaderboard(scores, scores_alice):
    scores = list(unique_everseen(scores))
    scores_alice.reverse()
    positions_desc = find_positions_in_desc_order(scores, scores_alice)
    positions = positions_desc[::-1]

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
