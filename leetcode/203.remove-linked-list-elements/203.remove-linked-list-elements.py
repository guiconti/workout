# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    previous = None
    current = head
    while current != None:
      if current.val != val:
        previous = current
        current = current.next
        continue
      if previous is not None:
        previous.next = current.next
      if current == head:
        head = head.next
      current = current.next
    return head
        