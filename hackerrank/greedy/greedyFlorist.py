#!/bin/python3

import math
import os
import random
import re
import sys

def merge(left, right):
  """Merge sort merging function."""

  left_index, right_index = 0, 0
  result = []
  while left_index < len(left) and right_index < len(right):
    if left[left_index] > right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1

  result += left[left_index:]
  result += right[right_index:]
  return result


def merge_sort(array):
  """Merge sort algorithm implementation."""

  if len(array) <= 1:  # base case
      return array

  # divide array in half and merge sort recursively
  half = len(array) // 2
  left = merge_sort(array[:half])
  right = merge_sort(array[half:])

  return merge(left, right)

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    multiplyFactor = 0
    iterationsUntilIncrementMultiplyFactor = k
    result = 0
    sortedFlowersArray = merge_sort(c)
    for flower in sortedFlowersArray:
        result += (multiplyFactor + 1) * flower
        iterationsUntilIncrementMultiplyFactor -= 1
        if (iterationsUntilIncrementMultiplyFactor == 0):
            iterationsUntilIncrementMultiplyFactor = k
            multiplyFactor += 1
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
