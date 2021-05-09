# 34. Find First and Last Position of Element in Sorted Array
# Medium

# 2440

# 112

# Add to List

# Share
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    first = 0
    last = len(nums) - 1
    found = False
    answer = [-1, -1]
    while first<=last and not found:
      mid = (first + last) // 2
      if nums[mid] == target:
        minusIndex = 0
        plusIndex = 0
        while mid - minusIndex >= 0 and nums[mid - minusIndex] == target:
          minusIndex += 1
        while mid + plusIndex <= len(nums) - 1 and nums[mid + plusIndex] == target:
          plusIndex += 1
        answer = [mid - minusIndex + 1, mid + plusIndex - 1]
        found = True
      else:
        if target < nums[mid]:
          last = mid - 1
        else:
          first = mid + 1	
    return answer