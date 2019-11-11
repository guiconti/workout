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
    if right[right_index][1] == 0:
        result.append(right[right_index])
        right_index += 1
    elif left[left_index][1] == 0:
        result.append(left[left_index])
        left_index += 1
    elif left[left_index][0] > right[right_index][0]:
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

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests = merge_sort(contests)
    luckSaved = 0
    for i in range(len(contests)):
        if (contests[i][1] == 1):
            if (k > 0):
                luckSaved += contests[i][0]
                k -= 1
            else:
                luckSaved -= contests[i][0]
        else:
            luckSaved += contests[i][0]
    
    return luckSaved

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
