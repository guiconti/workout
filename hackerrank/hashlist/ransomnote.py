#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dictionaryA = {}
    for word in magazine:
        if word in dictionaryA:
            dictionaryA[word] += 1
        else:
            dictionaryA[word] = 1
    
    for word in note:
        if word in dictionaryA:
            if dictionaryA[word] > 0:
                dictionaryA[word] -= 1
            else:
                return 'No'
        else:
            return 'No'
    
    return 'Yes'

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
