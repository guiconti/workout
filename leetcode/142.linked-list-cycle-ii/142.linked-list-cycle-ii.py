# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    slow, fast = head, head

    while fast != None and fast.next != None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        break
    
    if fast == None or fast.next == None:
      return None

    # Finding beginning of loop
    slow = head
    while slow != fast:
      slow = slow.next
      fast = fast.next
    return fast