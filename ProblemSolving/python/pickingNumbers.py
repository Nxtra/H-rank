#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    a.sort()
    max_array_size = 0
    i = 0
    while i < len(a):
        index_plus = 0
        while i + index_plus < len(a):
            if a[i + index_plus] <= a[i] + 1:
                index_plus += 1
            else:
                break
        if index_plus > max_array_size:
            max_array_size = index_plus
        i += 1
    return max_array_size


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
