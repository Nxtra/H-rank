#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.


def find_matching_part_index(string1, string2):
    i = 0
    matching_index = -2
    while i <= len(string1) and i <= len(string2):
        sub1 = string1[:i]
        sub2 = string2[:i]
        if sub2 in sub1:
            matching_index += 1
            i += 1
        else:
            break
    return matching_index


def find_number_of_deletes(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    matching_index = find_matching_part_index(string1, string2)
    number_of_deletes = 0
    if len1 < len2 and matching_index and matching_index is not -2:
        number_of_deletes = 0
    else:
        number_of_deletes = len1 - (matching_index + 1)


    return number_of_deletes


def get_intermediate_string(string1, d):
    if d is not 0:
        return string1[:-d]
    elif d is 0:
        return string1


def find_delete_append_margin(string1):
    return 2*len(string1)


def find_number_of_appends(string1, string2):
    return len(string2) - len(string1)


def get_list_with_options(deletes, appends, margin):
    start_numbers = list(range(deletes + appends, deletes + appends + margin, 2))
    return start_numbers + list(range(deletes + appends + margin, 101))


def appendAndDelete(s, t, k):
    number_of_deletes = find_number_of_deletes(s, t)
    intermediate1 = get_intermediate_string(s, number_of_deletes)
    margin = find_delete_append_margin(intermediate1)
    number_of_appends = find_number_of_appends(intermediate1, t)
    numbers = get_list_with_options(number_of_deletes, number_of_appends, margin)
    if k in numbers:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    print(appendAndDelete(s, t, k))
    #
    # result = appendAndDelete(s, t, k)
    #
    # fptr.write(result + '\n')
    #
    # fptr.close()
