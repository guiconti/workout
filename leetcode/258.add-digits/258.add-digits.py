class Solution:
  def addDigits(self, num: int) -> int:
    while num / 10 >= 1:
      strNum = str(num)
      num = 0
      for character in strNum:
        num += int(character)
    return num