
from .solution import Solution
import ast
import os

unknown_answer_token = '?'

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      a = file.readline()
      if not a:
        # End of tests
        return
      a = ast.literal_eval(a)
      first_parameter = None
      previous_node = None
      for num in a:
        new_node = ListNode(num)
        if not first_parameter:
          first_parameter = new_node
        if previous_node:
          previous_node.next = new_node
        previous_node = new_node
      b = ast.literal_eval(file.readline())
      second_parameter = None
      previous_node = None
      for num in b:
        new_node = ListNode(num)
        if not second_parameter:
          second_parameter = new_node
        if previous_node:
          previous_node.next = new_node
        previous_node = new_node
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result: ListNode = Solution().addTwoNumbers(first_parameter, second_parameter)
      result_text = []
      while not result is None:
        result_text.append(result.val)
        result = result.next
      print(f'Result given {result_text}')
      print(f'Correct answer {answer}')
          