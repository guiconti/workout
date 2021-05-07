# 360. Sort Transformed Array
# Medium

# 272

# 81

# Add to List

# Share
# Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example 1:

# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:

# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]

class Solution:
  def binarySearch(self, arr, val, start, end):
    if start == end: 
      if arr[start] > val: 
        return start 
      else: 
        return start+1    
    if start > end: 
      return start 
    mid = int((start+end) / 2)
    if arr[mid] < val: 
      return self.binarySearch(arr, val, mid + 1, end) 
    elif arr[mid] > val: 
      return self.binarySearch(arr, val, start, mid - 1) 
    else: 
      return mid  

  def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
    answer = []
    for i in range(len(nums)):
      quadraticNum = (a * (nums[i] ** 2)) + (b * nums[i]) + (c)
      index = self.binarySearch(answer, quadraticNum, 0, len(answer) - 1)
      answer = answer[:index] + [quadraticNum] + answer[index:]
    return answer