class Solution:
  def titleToNumber(self, columnTitle: str) -> int: 
    result = 0
    columnTitle = columnTitle[::-1]
    for i in range(0, len(columnTitle)):
        result += (ord(columnTitle[i]) - 64) * (26 ** i)
    return result