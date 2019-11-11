#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    dictionary = {}
    count = 0

    for i in range(len(arr)):
        if arr[i] in dictionary:
            dictionary[arr[i]] += 1
        else:
            dictionary[arr[i]] = 1

    for i in range(len(arr)):
        if int(arr[i] / r) in dictionary:
            if arr[i] * r in dictionary:
                smallerAmount = dictionary[int(arr[i] / r)]
                biggerAmount = dictionary[arr[i] * r]
                count += max([smallerAmount, biggerAmount])
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
