# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
from typing import List
def solution(strs: List[str]) -> str:
  smallest_string = "a" * 201
  smallest_string_index = -1
  for i in range(0, len(strs)):
    if len(strs[i]) < len(smallest_string):
      smallest_string = strs[i]
      smallest_string_index = i
  del strs[smallest_string_index]
  answer_candidate = smallest_string
  for i in range(0, len(strs)):
    while answer_candidate != strs[i][:len(answer_candidate)] and len(answer_candidate) > 0:
      answer_candidate = answer_candidate[:-1]
    # Even though this should improve the average time it doesn't for leetcode tests
    if len(answer_candidate) == 0:
      return ""
  return answer_candidate