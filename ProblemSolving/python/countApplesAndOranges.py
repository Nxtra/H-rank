#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    number_of_apples = 0
    number_of_oranges = 0
    for apple in apples:
        if s <= a + apple <= t:
            number_of_apples += 1
    for orange in oranges:
        if s <= b + orange <= t:
            number_of_oranges += 1
    print(number_of_apples)
    print(number_of_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
