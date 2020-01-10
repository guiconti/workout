# 136. Single Number
# Easy

# 3273

# 126

# Add to List

# Share
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    hashmap = {}
    for num in nums:
      if not num in hashmap:
        hashmap[num] = 1
      else:
        del hashmap[num]
    for key in hashmap.keys():
      return key
        