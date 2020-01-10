# 347. Top K Frequent Elements
# Medium

# 2194

# 144

# Add to List

# Share
# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from operator import itemgetter

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hashMap = collections.defaultdict(int)
    for num in nums:
      hashMap[num] += 1
    items = hashMap.items()
    items = sorted(items, key = itemgetter(1))
    answer = []
    for i in range(len(items) - 1, len(items) - k - 1, -1):
      answer.append(items[i][0])
    return answer