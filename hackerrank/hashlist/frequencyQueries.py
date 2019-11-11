#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    valuesDictionary = {}
    frequenciesDictionary = {}
    answer = []

    for query in queries:
        if query[0] == 1:
            if query[1] in valuesDictionary:
                valuesDictionary[query[1]] += 1
                if valuesDictionary[query[1]] in frequenciesDictionary:
                    frequenciesDictionary[valuesDictionary[query[1]]] += 1
                else:
                    frequenciesDictionary[valuesDictionary[query[1]]] = 1
                if (valuesDictionary[query[1]] - 1) in frequenciesDictionary:
                    frequenciesDictionary[valuesDictionary[query[1]] - 1] -= 1
            else:
                valuesDictionary[query[1]] = 1
                if valuesDictionary[query[1]] in frequenciesDictionary:
                    frequenciesDictionary[valuesDictionary[query[1]]] += 1
                else:
                    frequenciesDictionary[valuesDictionary[query[1]]] = 1
        elif query[0] == 2:
            if query[1] in valuesDictionary:
                valuesDictionary[query[1]] -= 1
                frequenciesDictionary[valuesDictionary[query[1]] + 1] -= 1
                if valuesDictionary[query[1]] > 0:
                    frequenciesDictionary[valuesDictionary[query[1]]] += 1
        else:
            if query[1] in frequenciesDictionary:
                if frequenciesDictionary[query[1]] > 0:
                    answer.append(1)
                else:
                    answer.append(0)
            else:
                answer.append(0)
    
    return answer



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
