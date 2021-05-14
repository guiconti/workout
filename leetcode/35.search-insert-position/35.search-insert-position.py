from typing import List
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    first = 0
    last = len(nums) - 1
    while first <= last:
      middle = (last + first) // 2
      if nums[middle] == target:
        return middle
      if nums[middle] < target:
        first = middle + 1
        continue
      last = middle - 1
    return first