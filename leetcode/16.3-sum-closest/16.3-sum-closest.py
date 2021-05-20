class Solution():
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = 10000000
    for i in range(0, len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      left = i + 1
      right = len(nums) - 1
      while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if abs(target - sum) < abs(target - result):
          result = sum
        if sum < target:
          left += 1
          continue
        if sum > target:
          right -= 1
          continue
        return sum
    return result