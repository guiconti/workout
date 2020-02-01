# Given a string, find the length of the longest substring without repeating characters.


# Solution O(n)
class Solution:
  def lengthOfLongestSubstring(self, s):
    longestSubstring = ''
    currentSubstring = ''
    foundWords = set()

    for letter in s:
      if letter in foundWords:
        foundWords = set()
        if len(currentSubstring) > len(longestSubstring):
          longestSubstring = currentSubstring
        currentSubstring = ''
      currentSubstring += letter
      foundWords.add(letter)
    if len(currentSubstring) > len(longestSubstring):
      longestSubstring = currentSubstring
    
    return len(longestSubstring)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))