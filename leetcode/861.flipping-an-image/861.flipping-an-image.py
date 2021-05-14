# We have a two dimensional matrix A where each value is 0 or 1.

# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score.

# Example 1:

# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 
# Note:

# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.

class Solution:
  def toggle(self, value):
    return 0 if value == 1 else 1
  def matrixScore(self, A: List[List[int]]) -> int:
    for row in range(len(A)):
      if A[row][0] == 0:
        A[row] = list(map(self.toggle, A[row]))
    
    for col in range(1, len(A[0])):
      amountOfZeros = 0
      for row in range(len(A)):
        if A[row][col] == 0:
          amountOfZeros += 1
      if amountOfZeros > len(A) // 2:
        for row in range(len(A)):
          A[row][col] = self.toggle(A[row][col])
    
    answer = 0
    for row in range(len(A)):
      answer += int(''.join(map(str, A[row])), 2)
      
    return answer