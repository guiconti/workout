#!/bin/python3

import math
import os
import random
import re
import sys


def getMedian(countingSortList, days, medianPosition):
    counter, left = 0, 0

    while counter < medianPosition:
        counter += countingSortList[left]
        left += 1
    right = left
    left -= 1

    if counter > medianPosition or days % 2 != 0:
        return left
    else:
        while countingSortList[right] == 0:
            right += 1
        return (left + right) / 2

# Complete the activityNotifications function below.

def activityNotifications(expenditure, d):
    countingSortList = [0] * 201
    for i in range(d):
        countingSortList[expenditure[i]] += 1

    current = 0
    end = d
    notifications = 0
    medianPosition = 0
    if (d % 2 != 0):
        medianPosition = int(d / 2) + 1
    else:
        medianPosition = int(d / 2)

    while end < len(expenditure):
        median = getMedian(countingSortList, d, medianPosition)
        if expenditure[end] >= median * 2:
            notifications += 1
        countingSortList[expenditure[current]] -= 1
        countingSortList[expenditure[end]] += 1
        current += 1
        end += 1
    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
