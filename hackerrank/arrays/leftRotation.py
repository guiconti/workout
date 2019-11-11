#!/bin/python3

import math
import os
import random
import re
import sys
  
def rotLeftByOne(arr): 
    temp = arr[0] 
    for i in range(len(arr) - 1): 
        arr[i] = arr[i + 1] 
    arr[len(arr) - 1] = temp 
    return arr

def rotRightByOne(arr): 
    temp = arr[len(arr) - 1] 
    for i in range(len(arr) - 1, 0, -1): 
        arr[i] = arr[i - 1] 
    arr[0] = temp 
    return arr

# Complete the rotLeft function below.
def rotLeft(a, d):
    if (len(a) // 2 > d):
        for i in range(d):
            a = rotLeftByOne(a)
    else:
        for i in range(len(a) - d):
            a = rotRightByOne(a)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
