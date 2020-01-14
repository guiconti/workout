# 409. Longest Palindrome
# Easy

# 724

# 69

# Add to List

# Share
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
  def longestPalindrome(self, s: str) -> int:
    hashmap = collections.defaultdict(int)
    for letter in s:
      hashmap[letter] += 1
    
    pairs = 0
    hasOdd = False
    for letter in hashmap.keys():
      pairs += (hashmap[letter] // 2) * 2
      if not hasOdd and hashmap[letter] % 2 != 0:
        hasOdd = True
    pairs += 1 if hasOdd else 0
    return pairs