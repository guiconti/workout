# 39. Combination Sum
# Medium

# 2832

# 87

# Add to List

# Share
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# Solution 1 test every possibility with backtracking
class Solution:
  
  def backtrack(self, answer, tempList, nums, remain, start):
    if remain < 0:
      return answer
    elif remain == 0:
      answer.append(tempList.copy())
    else:
      for i in range(start, len(nums)):
        tempList.append(nums[i])
        answer = self.backtrack(answer, tempList, nums, remain - nums[i], i)
        tempList.pop(len(tempList) - 1)
    return answer
  
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    self.backtrack(answer, [], candidates, target, 0)
    return answer

# Solution 2 (better) Sort the candidates and breaks the backtrack loops when finds an solution 
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
        tempList.append(nums[i])
        shouldContinue = self.backtrack(answer, tempList, nums, remain - nums[i], i)
        tempList.pop(len(tempList) - 1)
        if not shouldContinue:
          break
    return True
  
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    candidates = sorted(candidates)
    self.backtrack(answer, [], candidates, target, 0)
    return answer
