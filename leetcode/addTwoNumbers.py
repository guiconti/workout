# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode(0)
        currentAnswerNode = answer
        exceededSum = 0
        
        while l1 or l2 or exceededSum > 0:
          if l1:
            currentAnswerNode.val += l1.val
          if l2:
            currentAnswerNode.val += l2.val
          currentAnswerNode.val += exceededSum
          exceededSum = 0
          if currentAnswerNode.val // 10 > 0:
            exceededSum = currentAnswerNode.val // 10
            currentAnswerNode.val = currentAnswerNode.val % 10
          if l1:
            l1 = l1.next
          if l2:
            l2 = l2.next
          if l1 or l2 or exceededSum > 0:
            currentAnswerNode.next = ListNode(0)
            currentAnswerNode = currentAnswerNode.next
        
        return answer