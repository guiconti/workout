# 40. Combination Sum II
# Medium

# 1262

# 54

# Add to List

# Share
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

# Solution Sort the candidates and breaks the backtrack loops when finds an solution 
# or the sum surpass the target. This improves the average complexity
class Solution:
  def backtrack(self, answer, tempList, nums, remain, start):
    if remain < 0:
      return False
    elif remain == 0:
      answer.append(tempList.copy())
      return False
    else:
      for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]: # This only works because we ordered it first
          continue
        tempList.append(nums[i])
        shouldContinue = self.backtrack(answer, tempList, nums, remain - nums[i], i + 1) # We add i + 1 so we don't use the same element more than once
        tempList.pop(len(tempList) - 1)
        if not shouldContinue:
          break
    return True
  
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    candidates = sorted(candidates)
    self.backtrack(answer, [], candidates, target, 0)
    return answer
