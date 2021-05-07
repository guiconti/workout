# 118. Pascal's Triangle
# Easy

# 1000

# 88

# Add to List

# Share
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 0:
      return []
    pascalTriangle = [[1]]
    for i in range(1, numRows):
      row = []
      for j in range(i + 1):
        leftValue = rightValue = 0
        if j > 0:
          leftValue = pascalTriangle[i - 1][j - 1]
        if j < len(pascalTriangle[i - 1]):
          rightValue = pascalTriangle[i - 1][j]
        row.append(leftValue + rightValue)
      pascalTriangle.append(row)
    return pascalTriangle