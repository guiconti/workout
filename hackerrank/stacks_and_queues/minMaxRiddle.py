#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    size = 1
    mxwindows = []
    
    # size variation from 1 to s
    while size <= len(arr):
        windows = []
        
        # looping the given array for a specfic size windows
        for i in range(len(arr) - size + 1):
            s = 0
            window = []
            
            # make a list - size of s
            while s < size:
                window.append(arr[i + s])
                s += 1
            # attach a min size to windows list
            windows.append(min(window))
        size += 1
        
        # get max from all mins of windows
        mxwindows.append(max(windows))
    return mxwindows

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
