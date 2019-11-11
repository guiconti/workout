#!/bin/python3

import math
import os
import random
import re
import sys

staircaseDictionary = {}
staircaseDictionary[0] = 1

# Complete the stepPerms function below.
def stepPerms(n):
    if n < 0:
        return 0

    if n in staircaseDictionary:
        return staircaseDictionary[n]

    ways = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3);
    staircaseDictionary[n] = ways
    return ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
