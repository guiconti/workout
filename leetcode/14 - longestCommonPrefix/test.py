from .solution import solution
import ast
import os

unknown_answer_token = '?'

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      first_input = file.readline()
      if not first_input:
        # End of tests
        return
      first_input = ast.literal_eval(first_input)
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result = solution(first_input)
      print(f'Input: {first_input}')
      print(f'Result given {result}')
      print(f'Correct answer {answer}\n')