class Solution:
  def isHappy(self, n: int) -> bool:
    cache = set()

    while n != 1:
      if n in cache:
        return False
      cache.add(n)
      array = [int(digit) for digit in str(n)]
      n = 0
      for digit in array:
        n += digit * digit
    return True