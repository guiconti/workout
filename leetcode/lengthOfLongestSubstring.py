# Given a string, find the length of the longest substring without repeating characters.
# Example
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    dicts = {}
    maxlength = start = 0
    for i, value in enumerate(s):
      if value in dicts:
        sums = dicts[value] + 1
        if sums > start:
          start = sums
      num = i - start + 1
      if num > maxlength:
        maxlength = num
      dicts[value] = i
    return maxlength
