#!/bin/python3

import math
import os
import random
import re
import sys

HOURGLASS_WIDTH = 3
HOURGLASS_HEIGHT = 3

# Complete the hourglassSum function below.
def hourglassSum(arr):
    biggestHourglassSum = -10000
    for i in range(len(arr) - HOURGLASS_HEIGHT + 1):
        for j in range(len(arr[i]) - HOURGLASS_WIDTH + 1):
            hourglassSum = 0
            hourglassSum += arr[i][j]
            hourglassSum += arr[i][j + 1]
            hourglassSum += arr[i][j + 2]
            hourglassSum += arr[i + 1][j + 1]
            hourglassSum += arr[i + 2][j]
            hourglassSum += arr[i + 2][j + 1]
            hourglassSum += arr[i + 2][j + 2]
            if (hourglassSum > biggestHourglassSum):
                biggestHourglassSum = hourglassSum
    return biggestHourglassSum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
