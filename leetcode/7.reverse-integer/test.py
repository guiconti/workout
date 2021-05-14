from .solution import solution
import ast
import os

unknown_answer_token = '?'

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      num = file.readline()
      if not num:
        # End of tests
        return
      num = ast.literal_eval(num)
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result = solution(num)
      print(f'Input: {num}')
      print(f'Result given {result}')
      print(f'Correct answer {answer}\n')