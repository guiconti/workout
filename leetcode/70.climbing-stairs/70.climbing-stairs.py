class Solution:
  memoization = {}
  def fibonacci(self, n):
    if n in self.memoization:
      return self.memoization[n]
    if n <= 1:
      return n
    if not n - 1 in self.memoization:
      self.memoization[n - 1] = self.fibonacci(n - 1)
    if not n - 2 in self.memoization:
      self.memoization[n - 2] = self.fibonacci(n - 2)
    return self.memoization[n - 1] + self.memoization[n - 2]

  def climbStairs(self, n: int) -> int:
    return self.fibonacci(n + 1)
  