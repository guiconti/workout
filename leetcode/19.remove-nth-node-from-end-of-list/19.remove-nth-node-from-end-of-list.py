# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    slowNode = head
    fastNode = head

    i = 0
    while i < n and fastNode != None:
      fastNode = fastNode.next
      i += 1
    
    if fastNode == None:
      head = head.next
      return head

    while fastNode.next != None:
      slowNode = slowNode.next
      fastNode = fastNode.next
        
    slowNode.next = slowNode.next.next
    
    return head