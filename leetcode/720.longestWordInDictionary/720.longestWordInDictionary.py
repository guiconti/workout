# 720. Longest Word in Dictionary
# Easy

# 462

# 568

# Add to List

# Share
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

# If there is no answer, return the empty string.
# Example 1:
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Note:

# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].

class Solution:
  def merge(self, left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
      if len(left[left_index]) < len(right[right_index]):
        result.append(left[left_index])
        left_index += 1
      elif len(right[right_index]) < len(left[left_index]):
        result.append(right[right_index])
        right_index += 1
      elif left[left_index] > right[right_index]:
        result.append(left[left_index])
        left_index += 1
      else:
        result.append(right[right_index])
        right_index += 1
        
    result += left[left_index:]
    result += right[right_index:]
    return result


  def merge_sort(self, array):
    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = self.merge_sort(array[:half])
    right = self.merge_sort(array[half:])

    return self.merge(left, right)
  
  def longestWord(self, words: List[str]) -> str:
    words = self.merge_sort(words)
    hashset = set()
    for word in words:
      if not word in hashset:
        hashset.add(word)
    for i in range(len(words) - 1, -1, -1):
      found = True
      print(words[i])
      for j in range(1, len(words[i])):
        if not words[i][:j] in hashset:
          found = False
          break
      if found:
        return words[i]
    return ''