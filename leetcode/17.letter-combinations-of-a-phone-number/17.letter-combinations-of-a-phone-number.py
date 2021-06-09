class Solution:
  PHONE_NUMBERS = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }
  def letterCombinations(self, digits: str) -> List[str]:
    result = []
    for digit in digits:
      new_result = []
      if len(result) == 0:
        for letter in self.PHONE_NUMBERS[digit]:
          new_result.append(letter)
      else:
        for letter in self.PHONE_NUMBERS[digit]:
          for combination in result:
            new_result.append(combination + letter)
      result = new_result
    return result