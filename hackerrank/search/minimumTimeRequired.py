#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    lower = goal * min(machines) // len(machines)
    higher = goal * max(machines) // len(machines) + 1
 
    while lower < higher:
        days = (lower + higher) // 2
        produced = sum([days // machine for machine in machines])
        if produced >= goal:
            higher = days
        else:
            lower = days + 1
     
    return lower

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
