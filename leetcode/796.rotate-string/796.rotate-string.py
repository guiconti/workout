
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