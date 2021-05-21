class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    result = []
    for i in range(1, numRows + 1):
      result.append([])
      for j in range(i):
        if j == 0 or j == i - 1:
          result[i - 1].append(1)
          continue
        result[i - 1].append(result[i - 2][j - 1] + result[i - 2][j])
    return result