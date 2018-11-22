#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    index_word = 0
    height_max = 0
    while index_word < len(word):
        height_letter = h[ord(word[index_word]) - 97]
        height_max = height_letter if height_letter > height_max else height_max
        index_word += 1
    return len(word) * height_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
