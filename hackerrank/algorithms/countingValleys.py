#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    stack = []
    valleys = 0

    for step in s:
        print(step)
        if len(stack) == 0:
            stack.append(step)
            if step == 'D':
                valleys += 1
        elif stack[len(stack) - 1] == step:
            stack.append(step)
        else:
            stack.pop()

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
