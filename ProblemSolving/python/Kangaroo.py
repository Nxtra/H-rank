#!/bin/python3

import os

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 is 0 and v2 is 0:
        return "NO"
    while 1:
        if x1 is x2:
            return "YES"
        elif v1 - v2 is 0:
            return "NO"
        x1_prev = x1
        x2_prev = x2
        x1 += v1
        x2 += v2
        diff = abs(x1_prev - x2_prev)
        closing = abs(v1 - v2)
        if abs(x1 - x2) > abs(x1_prev - x2_prev):
            return "NO"
        if diff % closing is 0:
            return "YES"


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
