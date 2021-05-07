# 245. Shortest Word Distance III
# Medium

# 172

# 65

# Add to List

# Share
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# word1 and word2 may be the same and they represent two individual words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “makes”, word2 = “coding”
# Output: 1
# Input: word1 = "makes", word2 = "makes"
# Output: 3
# Note:
# You may assume word1 and word2 are both in the list.

class Solution:
  def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
    word1Index = -1
    word2Index = -1
    minDistance = 100000
    for i in range(len(words)):
      if words[i] == word1 and (word1 != word2 or word1Index == -1):
        if word2Index >= 0:
          if i - word2Index < minDistance:
            minDistance = i - word2Index
            word2Index = -1
          else:
            word2Index = -1
        word1Index = i
      elif words[i] == word2:
        if word1Index >= 0:
          if i - word1Index < minDistance:
            minDistance = i - word1Index
            word1Index = -1
          else:
            word1Index = -1
        word2Index = i
    return minDistance