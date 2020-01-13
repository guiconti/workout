# 49. Group Anagrams
# Medium

# 2408

# 140

# Add to List

# Share
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    answer = []
    hashmap = collections.defaultdict(list)
    for word in strs:
      sortedWord = ''.join(sorted(word))
      hashmap[sortedWord].append(word)
    for key in hashmap.keys():
      answer.append(hashmap[key])
    return answer