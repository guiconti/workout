# Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

# Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

# Note: p consists of only lowercase English letters and the size of p might be over 10000.

# Example 1:
# Input: "a"
# Output: 1

# Explanation: Only the substring "a" of string "a" is in the string s.
# Example 2:
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string s.
# Example 3:
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

from collections import defaultdict


class Solution(object):
  def findSubstringInWraproundString(self, p):
    """
    :type p: str
    :rtype: int
    """
    if len(p) <= 1:
      return len(p)
    count = defaultdict(int)
    max_length = 1
    count[p[0]] = 1
    lastCharCode = ord(p[0])
    for i in range(1, len(p)):
      currentCharCode = ord(p[i])
      if currentCharCode - lastCharCode == 1 or lastCharCode - currentCharCode  == 25:
        max_length += 1
      else:
        max_length = 1
      lastCharCode = currentCharCode
      count[p[i]] = max(count[p[i]], max_length)
    return sum(count.values())
