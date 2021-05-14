class Solution:
  MATCHING_CHARACTERS = {
    ')': '(',
    '}': '{',
    ']': '['
  }
  def isValid(self, s: str) -> bool:
    stack = []
    for character in s:
      if not character in self.MATCHING_CHARACTERS:
        stack.append(character)
        continue
      if len(stack) == 0 or stack[len(stack) - 1] != self.MATCHING_CHARACTERS[character]:
        return False
      stack.pop()
    return len(stack) == 0
        