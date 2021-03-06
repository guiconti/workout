#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    dictionary = {}
    dictionary['('] = ')'
    dictionary['['] = ']'
    dictionary['{'] = '}'
    stack = []

    for c in s:
        if c in dictionary:
            stack.append(dictionary[c])
        else:
            if len(stack) == 0 or stack.pop() != c:
                return 'NO'
    
    if len(stack) != 0:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
