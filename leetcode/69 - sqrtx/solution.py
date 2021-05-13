# Binary search
class Solution:
  def mySqrt(self, x: int) -> int:
    left = 0
    # Biggest square root, which is sqrt(2^31 - 1)
    right = 46340

    while left <= right:
      # print(left, right)
      middle = (left + right) // 2
      middle_powered = middle * middle
      if middle_powered == x:
        return middle
      if middle_powered < x:
        left = middle + 1
        continue
      right = middle - 1

    return left - 1

