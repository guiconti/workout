class Solution: 
  def longestPalindrome(self, s):
    maxLength = 1
    start = low = high = 0

    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, len(s)): 
      # Find the longest even length palindrome with center 
      # points as i-1 and i. 
      low = i - 1
      high = i 
      while low >= 0 and high < len(s) and s[low] == s[high]: 
        if high - low + 1 > maxLength: 
          start = low 
          maxLength = high - low + 1
        low -= 1
        high += 1

      # Find the longest odd length palindrome with center  
      # point as i 
      low = i - 1
      high = i + 1
      while low >= 0 and high < len(s) and s[low] == s[high]: 
        if high - low + 1 > maxLength: 
          start = low 
          maxLength = high - low + 1
        low -= 1
        high += 1
  
    return s[start:start + maxLength] 

# Test program
s = "geeksskeeg"
print(str(Solution().longestPalindrome(s)))
# geeksskeeg