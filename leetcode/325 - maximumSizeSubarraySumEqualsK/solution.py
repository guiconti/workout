# 325. Maximum Size Subarray Sum Equals k
# Medium

# 749

# 28

# Add to List

# Share
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:

# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?

class Solution:
  def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    hashmap = dict()
    totalSum = maxLength = 0
    
    for i in range(len(nums)):
      totalSum += nums[i]
      if totalSum == k:
        maxLength = i + 1
      elif totalSum - k in hashmap:
        maxLength = max(maxLength, i - hashmap[totalSum - k])
        
      if totalSum not in hashmap:
        hashmap[totalSum] = i
    
    return maxLength