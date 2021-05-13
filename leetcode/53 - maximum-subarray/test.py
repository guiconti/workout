
from .solution import Solution
import ast
import os

unknown_answer_token = '?'

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      nums = file.readline()
      if not nums:
        # End of tests
        return
      nums = ast.literal_eval(nums)
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result = Solution().maxSubArray(nums)
      print(f'Result given {result}')
      print(f'Correct answer {answer}')
          