#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socksDictionary = {}
    pairs = 0

    for sock in ar:
        if sock in socksDictionary:
            socksDictionary[sock] += 1
        else:
            socksDictionary[sock] = 1

    for sock in socksDictionary:
        pairs += socksDictionary[sock] // 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
