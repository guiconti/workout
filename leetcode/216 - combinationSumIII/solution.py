# 216. Combination Sum III
# Medium

# 817

# 45

# Add to List

# Share
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

# Solution Create our nums range (1 to 9) and breaks the backtrack loops when finds an solution 
# or the sum surpass the target. This improves the average complexity
class Solution:
  def backtrack(self, answer, tempList, nums, remain, size, start):
    if remain < 0:
      return False
    elif remain == 0:
      if len(tempList) == size:
        answer.append(tempList.copy())
      return False
    else:
      for i in range(start, len(nums)):
        tempList.append(nums[i])
        shouldContinue = self.backtrack(answer, tempList, nums, remain - nums[i], size, i + 1)
        tempList.pop(len(tempList) - 1)
        if not shouldContinue:
          break
    return True
  
  def combinationSum3(self, size: int, target: int) -> List[List[int]]:
    answer = []
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.backtrack(answer, [], nums, target, size, 0)
    return answer
    