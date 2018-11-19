#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    counter = collections.Counter(a)
    my_set = set(a)
    max_length = 0;
    for i in my_set:
        current_length = counter[i] + counter[i + 1]
        max_length = current_length if current_length > max_length else max_length
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
