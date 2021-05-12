from typing import List
class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    # This problem is not very well written and it requires you to also change the nums list
    # So this solution, even though is correct, doesn't work
    # result = 0
    # for num in nums:
    #   if num != val:
    #     result += 1
    # return result
    i = 0
    while i < len(nums):
      if nums[i] == val:
        nums.pop(i)
        continue
      i += 1
    return len(nums)