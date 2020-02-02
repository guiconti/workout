# Given two strings find out if you can construct the first string
# with the letters of the second string

import collections

class Solution:
  def canConstruct(self, ransomNote, magazine):
    magazineDictionary = collections.defaultdict(int)
    for letter in magazine:
      magazineDictionary[letter] += 1
    for letter in ransomNote:
      if magazineDictionary[letter] <= 0:
        return False
      magazineDictionary[letter] -= 1
    return True

print(Solution().canConstruct('aa', 'ab'))
# True