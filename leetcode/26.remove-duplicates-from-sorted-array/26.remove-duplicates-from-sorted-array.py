# Iterate through the array counting the unique numbers
class Solution:
  def removeDuplicates(self, nums) -> int:
    if len(nums) == 0:
      return 0
    result = 1
    for i in range(1, len(nums)):
      if nums[i] == nums[i - 1]:
        continue
      result += 1
    return result