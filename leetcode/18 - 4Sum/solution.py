# 18. 4Sum
# Medium

# 1449

# 275

# Add to List

# Share
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# **********************************  Solution explanation **********************************
# We now a fast way to find all two sums in the array, starting a pointer at the beginning of the array
# and another at the end of the array we can check if the sum of these two pointers are equal to our target
# in that case we add it to our solution, if it is smaller, in that case we advance the smallest pointer by 1
# or if it is bigger where in that case we reduce the biggest pointer by 1. In order to use this same approach
# for a N sum (in the case of this problem a 4 sum) we check if the current sum is bigger than 2 
# if it is we loop the array from the beginning to the end minus the current size that we are looking for
# we then recursively call of findNSum with a slice of the original array, removing the first elements
# we reduce the size that we are looking in 1 and we reduce the target that we are looking by the current
# value of the array that our loop is.
# An example:
# Let's suppose that we have the array [-1, 1, 2, 3, 4], whe are looking sum of 3 values that matches the target 6
# Our algorithm would go like this:
# - First we check that our current size is bigger than 2 (in our example 3)
# - We then start iterating through our array [-1, 1, 2, 3, 4] from the beginning
# - Then we call our findNSum, but we change the following parameters:
#   - The array is now [1, 2, 3, 4]
#   - The target is now 7 (6 - (-1))
#   - We send our current result (the value that we removed in this case [-1])
#   - The size is now 2
# - Now we start our findNSum again but at this time the size is 2, so we do the two pointer algorithm
# - We find the answer [3, 4] and sum it to our -1 from the parameter call, we end up with [-1, 3, 4]
# - Now that we returned we come back from the for loop where our size was 3
# - We do the same steps with our second value (1), now sending the array [2, 3, 4]
# - We find the answer [1, 2, 3]
# - We come back once again and to the same starting at 2 and sending [3, 4] as our array
# - This time no answer was found
# - We return our found answer [[-1, 3, 4], [1, 2, 3]
# Using this method we could apply any N sum that we wanted, we just need to always sort our array before starting
class Solution:
  def findNsum(self, nums, target, size, result, results):
    if len(nums) < size or size < 2 or target < nums[0] * size or target > nums[-1] * size:
      return
    if size == 2: # two pointers solve sorted 2-sum problem
      left, right = 0, len(nums) - 1
      while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == target:
          results.append(result + [nums[left], nums[right]])
          left += 1
          while left < right and nums[left] == nums[left - 1]:
            left += 1
        elif currentSum < target:
          left += 1
        else:
          right -= 1
    else: # recursively reduce N
      for i in range(len(nums) - size + 1):
        if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
          self.findNsum(nums[i + 1:], target - nums[i], size - 1, result + [nums[i]], results)

  def fourSum(self, nums, target):
    results = []
    size = 4
    self.findNsum(sorted(nums), target, size, [], results)
    return results