class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    # Store the rows and columns that will be 0
    # Then DO IT!
    if len(matrix) == 0:
      return
    rows = [False] * len(matrix)
    columns = [False] * len(matrix[0])

    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
          rows[i] = True
          columns[j] = True

    for i in range(len(rows)):
      if not rows[i]:
        continue
      for j in range(len(matrix[i])):
        matrix[i][j] = 0

    for i in range(len(columns)):
      if not columns[i]:
        continue
      for j in range(len(matrix)):
        matrix[j][i] = 0
        