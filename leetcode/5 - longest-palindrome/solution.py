# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"

# My solution O(n2)


class Solution:
  def longestPalindrome(self, s: str) -> str:
    longestPalindromeString = ''
    for i in range(len(s)):
      for j in range(len(s), i, -1):
        if len(longestPalindromeString) >= j - i:
          break
        if s[i:j] == s[i:j][::-1]:
          longestPalindromeString = s[i:j]
          break
    return longestPalindromeString


# Optimal solution (There's one better but it's impossible to implement in a coding session)
class Solution:
  def longestPalindrome(self, s: 'str') -> 'str':
    if len(s) <= 1:
      return s
    start = end = 0
    length = len(s)
    for i in range(length):
      max_len_1 = self.get_max_len(s, i, i + 1)
      max_len_2 = self.get_max_len(s, i, i)
      max_len = max(max_len_1, max_len_2)
      if max_len > end - start:
        start = i - (max_len - 1) // 2
        end = i + max_len // 2
    return s[start: end+1]

  def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':
    length = len(s)
    i = 1
    max_len = 0
    while left >= 0 and right < length and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1

# Manacher's solution O(N) not viable to implement in a coding session
class Solution:
	def longestPalindrome(self, s):
		_str = '$#' + '#'.join(s) + '#@'
		_id,mx = 0,0
		p = [0 for i in range(len(_str) + 1)]
		for i in range(1,len(_str) - 1):
			if i < mx:
				p[i] = min(mx - i,p[2 * _id - i])
			else:
				p[i] = 1
			while _str[i - p[i]] == _str[i + p[i]]:
				p[i] += 1
			if mx < i + p[i]:
				_id = i
				mx = i + p[i]
		_id,mx = 0,0
		for i in range(len(_str)):
			if mx < p[i]:
				_id = i
				mx = p[i]
		return _str[_id - p[_id] + 1:_id + p[_id]].replace('#','')
