# Validate if a string containing parentheses is balanced

from collections import deque 

# Solution O(n)
class Solution:
  parenthesesMap = {
    ')': '(',
    ']': '[',
    '}': '{'
  }
  def isValid(self, s):
    stack = deque()
    for letter in s:
      if letter not in self.parenthesesMap:
        stack.append(letter)
      elif len(stack) > 0 and stack[len(stack) - 1] == self.parenthesesMap[letter]:
        stack.pop()
      else:
        return False
    return len(stack) == 0

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
s = "([{}])(()"
# should return False
print(Solution().isValid(s))

s = "([{)}])(()"
# should return False
print(Solution().isValid(s))