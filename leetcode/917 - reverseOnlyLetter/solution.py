# 917. Reverse Only Letters
# Easy

# 372

# 30

# Add to List

# Share
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 

# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "

class Solution:
  def reverseOnlyLetters(self, S: str) -> str:
    answer = []
    letters = [c for c in S if c.isalpha()]
    for i in range(len(S)):
      if S[i].isalpha():
        answer.append(letters.pop())
      else:
        answer.append(S[i])
    return ''.join(answer)