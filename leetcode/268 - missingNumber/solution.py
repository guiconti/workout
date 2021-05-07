# 268. Missing Number
# Easy

# 1288

# 1693

# Add to List

# Share
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    numsSet = set(nums)
    for i in range(len(nums) + 1):
      if i not in numsSet:
        return i
    return -1