# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    answer = ListNode(0)
    current_answer_node = answer
    exceeded_sum = 0

    while l1 or l2 or exceeded_sum > 0:
      if l1:
        current_answer_node.val += l1.val
        l1 = l1.next
      if l2:
        current_answer_node.val += l2.val
        l2 = l2.next
      current_answer_node.val += exceeded_sum
      exceeded_sum = 0
      if current_answer_node.val >= 10:
        exceeded_sum = current_answer_node.val // 10
        current_answer_node.val = current_answer_node.val % 10
      if l1 or l2 or exceeded_sum > 0:
        current_answer_node.next = ListNode(0)
        current_answer_node = current_answer_node.next

    return answer