# 1189. Maximum Number of Balloons
# Easy

# 133

# 19

# Add to List

# Share
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 10^4
# text consists of lower case English letters only.

class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    hashmap = collections.defaultdict(int)
    for letter in text:
      hashmap[letter] += 1
    amountOfB = hashmap['b']
    amountOfA = hashmap['a']
    amountOfL = int(hashmap['l'] // 2)
    amountOfO = int(hashmap['o'] // 2)
    amountOfN = hashmap['n']
    
    return min(amountOfB, amountOfA, amountOfL, amountOfO, amountOfN)
    