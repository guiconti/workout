# 64. Minimum Path Sum
# Medium

# 1980

# 47

# Add to List

# Share
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    answer = [None] * len(grid)
    for i in range(len(answer)):
      answer[i] = [0] * len(grid[0])
      
    answer[len(grid) - 1][len(grid[0]) - 1] = grid[len(grid) - 1][len(grid[0]) - 1]
    for row in range(len(grid) - 1, -1, -1):
      startingColumnPoint = len(grid[row]) - 1 if row < len(grid) - 1 else len(grid[row]) - 2
      for column in range(startingColumnPoint, -1, -1):
        rightValue = downValue = float('inf')
        if row < len(grid) - 1:
          downValue = answer[row + 1][column]
        if column < len(grid[row]) - 1:
          rightValue = answer[row][column + 1]
        answer[row][column] = min(rightValue, downValue) + grid[row][column]
    return answer[0][0]