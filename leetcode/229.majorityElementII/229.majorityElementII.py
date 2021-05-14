# 229. Majority Element II
# Medium

# 1171

# 136

# Add to List

# Share
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    hashmap = {}
    answer = []
    for num in nums:
      if not num in hashmap:
        hashmap[num] = [0, False]
      hashmap[num][0] += 1
      if not hashmap[num][1] and hashmap[num][0] > len(nums) / 3:
        hashmap[num][1] = True
        answer.append(num)
    return answer
      