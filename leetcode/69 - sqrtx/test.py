
from .solution import Solution
import ast
import os

unknown_answer_token = '?'

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      a = file.readline()
      if not a:
        # End of tests
        return
      a = ast.literal_eval(a)
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result = Solution().mySqrt(a)
      print(f'Result given {result}')
      print(f'Correct answer {answer}')
          