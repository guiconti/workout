# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    slow, fast = head, head
    stack = []
    
    while fast != None and fast.next != None:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next

    #     Odd length
    if fast != None:
        slow = slow.next
        
    while slow != None:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True