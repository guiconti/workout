
from .solution import Solution
import ast
import os

unknown_answer_token = '?'

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      sequence = file.readline()
      if not sequence:
        # End of tests
        return
      sequence = ast.literal_eval(sequence)
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result = Solution().isValid(sequence)
      print(f'Result given {result}')
      print(f'Correct answer {answer}')
          