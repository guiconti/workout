class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    hashMap = {}
    for i in range(len(numbers)):
      hashMap[numbers[i]] = i 
    for i in range(len(numbers)):
      matchingNumber = target - numbers[i]
      if matchingNumber in hashMap:
        return [i + 1, hashMap[matchingNumber] + 1]
    return [-1, -1]