class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
      return

    for i in range(len(matrix) // 2):
      first = i
      last = len(matrix) - 1 - i
      for j in range(first, last):
        # Essentially the column
        offset = j - first
        
        # Save top
        top = matrix[first][j]
        # Left to top
        matrix[first][j] = matrix[last - offset][first]
        # Bottom to left
        matrix[last - offset][first] = matrix[last][last - offset]
        # Right to Bottom
        matrix[last][last - offset] = matrix[j][last]
        # Top to right
        matrix[j][last] = top