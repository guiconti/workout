
# Solution 1
# First we check for base cases which are different lengths and 1 letter length
# Then we store the original s and move the first character to the end
# Until we either reach the original s again or match the goal.
class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
      return False
    if len(s) == 1:
      return s == goal

    originalS = s
    while s != goal:
      s = s[1:] + s[0]
      # Back to the original
      if s == originalS:
        return False

    return True