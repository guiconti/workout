class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    exceededSum = 0
    for i in range(len(digits) - 1, -1, -1):
      if exceededSum > 0:
        digits[i] += exceededSum
        exceededSum = 0
      else:
        digits[i] += 1

      if digits[i] >= 10:
        exceededSum = digits[i] // 10
        digits[i] = digits[i] % 10
        continue
      return digits
    if exceededSum > 0:
      return [exceededSum] + digits
    return digits