class Solution:
  def convert(self, s: str, numRows: int) -> str:
    zigZag = []
    for i in range(numRows):
      zigZag.append([])
    
    goingDown = True
    i = 0
    for character in s:
      zigZag[i].append(character)
      if i >= len(zigZag) - 1:
        goingDown = False
      elif i <= 0:
        goingDown = True
      i += 1 if goingDown else -1
    result = ""
    for substring in zigZag:
      result += ''.join(substring)
    return result
    