#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    visited = [False] * len(arr)

    for i in range(len(arr)):
        j = i
        cycles = 0

        while not visited[j]:
            visited[j] = True
            j = arr[j] - 1
            cycles += 1
        
        if (cycles != 0):
            swaps += cycles - 1
    
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
