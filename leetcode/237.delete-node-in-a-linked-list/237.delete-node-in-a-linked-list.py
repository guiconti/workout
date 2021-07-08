# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def deleteNode(self, node):
    previous = node
    node = node.next
    while node.next != None:
        previous.val = node.val
        node = node.next
        previous = previous.next
    previous.val = node.val
    previous.next = None
        