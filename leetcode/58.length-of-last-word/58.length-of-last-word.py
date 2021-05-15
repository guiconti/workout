class Solution:
  def lengthOfLastWord(self, s: str):
    s = s.strip().split(' ')
    return len(s[len(s) - 1])