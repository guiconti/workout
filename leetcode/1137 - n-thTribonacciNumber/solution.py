# 1137. N-th Tribonacci Number
# Easy

# 123

# 24

# Add to List

# Share
# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

class Memoization:
  def __init__(self):
    def helper(n):
      if n == 0:
        return 0

      if answers[n]:
        return answers[n]

      answers[n] = helper(n - 1) + helper(n - 2) + helper(n - 3) 
      return answers[n]
    maxAmountOfNumbers = 38
    self.answers = answers = [0] * maxAmountOfNumbers
    answers[1] = answers[2] = 1
    helper(maxAmountOfNumbers - 1)
                    
class Solution:
  memoization = Memoization()
  def tribonacci(self, n: int) -> int:
    return self.memoization.answers[n]