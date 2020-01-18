# 616. Add Bold Tag in String
# Medium

# 393

# 49

# Add to List

# Share
# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
# Example 1:
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].

class Solution:
  def addBoldTag(self, s, dict):
    status = [False] * len(s)
    answer = ''
    for word in dict:
      start = s.find(word)
      while start != -1:
        for i in range(start, start + len(word)):
          status[i] = True
        start = s.find(word, start + 1)
    i = 0
    i = 0
    while i < len(s):
      if status[i]:
        answer += '<b>'
        while i < len(s) and status[i]:
          answer += s[i]
          i += 1
        answer += '</b>'
      else:
        answer += s[i]
        i += 1
    return answer
