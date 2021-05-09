# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
 

# Constraints:

# -231 <= x <= 231 - 1
import math

def solution(x: int) -> int:
  stringified_number = str(x)
  isNegative = stringified_number[0] == '-'
  stringified_number = stringified_number[::-1]
  if isNegative:
    stringified_number = '-' + stringified_number[:-1]
  try:
    result = int(stringified_number)
  except:
    return 0
  # Python max int is base-64 not base 32 so we have to manually check for this
  if abs(result) > math.pow(2, 31) - 1:
    result = 0
  return result