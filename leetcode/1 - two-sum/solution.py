from typing import List

class Solution():
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i in range(len(nums)):
      numToBeFound = target - nums[i]
      if numToBeFound in hashMap and hashMap[numToBeFound] != i:
        return [i, hashMap[numToBeFound]]
      hashMap[nums[i]] = i