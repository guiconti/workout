#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    outputArray = [0] * (n + 2)
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        outputArray[a] += k
        outputArray[b + 1] -= k
    maxValue = -10000
    sumValue = 0
    for i in range(len(outputArray)):
        sumValue += outputArray[i]
        maxValue = max([maxValue, sumValue])
    return maxValue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
