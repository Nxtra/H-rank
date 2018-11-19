#!/bin/python3

import os


def get_positions(scores, scores_alice):
    positions = []
    index_scores = len(scores) - 1
    for a in scores_alice:
        while index_scores >= 0 and a > scores[index_scores]:
            index_scores -= 1
        if scores[index_scores] == a:
            positions.append(index_scores + 1)
        else:
            positions.append(index_scores + 2)
    return positions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
    m = int(input().strip())
    scores_alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

    scores = sorted(list(set(scores)))[::-1]
    positions = get_positions(scores, scores_alice)

    fptr.write('\n'.join(map(str, positions)))
    fptr.write('\n')

    fptr.close()
