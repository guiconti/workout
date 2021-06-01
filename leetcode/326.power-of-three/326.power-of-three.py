class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    if n == 0:
      return False
    elif n == 1:
      return True
    while (n != 1):
      n = (float(n)/3)
      if n < 1:
        return False
      elif n == 1:
        return True