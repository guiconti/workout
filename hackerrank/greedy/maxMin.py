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
    if left[left_index] < right[right_index]:
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

# Complete the maxMin function below.
def maxMin(k, arr):
    sortedArray = merge_sort(arr)
    minimumUnfair = 1000000000
    for i in range(len(sortedArray) - (k - 1)):
        currentUnfair = sortedArray[i + (k - 1)] - sortedArray[i]
        if currentUnfair < minimumUnfair:
            minimumUnfair = currentUnfair
    return minimumUnfair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
