class Solution:
  def trailingZeroes(self, n: int) -> int:
    if n <= 1:
      return 0
    factorial = 1
    for i in range(2, n + 1):
      factorial *= i
    factorial = str(factorial)[::-1]
    result = 0
    for character in factorial:
      if character == '0':
        result += 1
        continue
      return result
    return result