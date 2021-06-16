class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    for i in range(n + 1):
      current = 2 ** i
      if current == n:
        return True
      if current > n:
        return False
    return False