# 387. First Unique Character in a String
# Easy

# 1396

# 97

# Add to List

# Share
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
  def firstUniqChar(self, s: str) -> int:
    hashmap = collections.defaultdict(int)
    for letter in s:
      hashmap[letter] += 1
    for i in range(len(s)):
      if hashmap[s[i]] == 1:
        return i
    return -1