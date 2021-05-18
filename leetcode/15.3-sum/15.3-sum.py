class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    hashMap = {}
    for i in range(0, len(nums)):
      for j in range(i + 1, len(nums)):
        hashMap[nums[i] + nums[j]] = [i, j]
    print(hashMap)
    for i in range(0, len(nums)):
      if not -nums[i] in hashMap:
        continue
      if i in hashMap[-nums[i]]:
        continue
      indexes = hashMap[-nums[i]]
      result.append([nums[i], nums[indexes[0]], nums[indexes[1]]])
    return result

