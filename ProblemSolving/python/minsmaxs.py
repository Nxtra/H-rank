#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    mins = sum(arr[:-1])
    maxs = sum(arr[1:])
    return str(mins), str(maxs)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))
