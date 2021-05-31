class Solution:
  def trailingZeroes(self, n: int) -> int:
    #the no. of trailing zeroes increases by 1 per increment of 5. 25 is worth two zeroes, 125 is worth 3 and so on
    #since n<10^4, we only need to evaluate up to 3125
    return n//5 + n//25 + n//125 + n//625 + n//3125
    # if n <= 1:
    #   return 0
    # factorial = 1
    # for i in range(2, n + 1):
    #   factorial *= i
    # factorial = str(factorial)[::-1]
    # result = 0
    # for character in factorial:
    #   if character == '0':
    #     result += 1
    #     continue
    #   return result
    # return result