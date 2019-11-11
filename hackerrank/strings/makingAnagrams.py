#!/bin/python3

import math
import os
import random
import re
import sys

CHARS = 26

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dictionaryA = [0] * CHARS
    dictionaryB = [0] * CHARS

    for i in range(len(a)):
        dictionaryA[ord(a[i]) - ord('a')] += 1

    for i in range(len(b)):
        dictionaryB[ord(b[i]) - ord('a')] += 1

    result = 0
    for i in range(CHARS): 
        result += abs(dictionaryA[i] - dictionaryB[i]) 
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
