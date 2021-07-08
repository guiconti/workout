# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        rightHead = None
        currentRight = None
        current = head
        leftTail = head

        while current != None:
            if current.val < x:
                leftTail = current
                current = current.next
                continue
            
            movedHead = False
            if current == head:
                if current.next == None and rightHead == None:
                    return head
                head = current.next
                leftTail = head
                movedHead = True

            if rightHead == None:
                rightHead = current
                currentRight = rightHead
            else:
                currentRight.next = current
                currentRight = current
            if not movedHead:
                leftTail.next = current.next
            current = current.next

        if leftTail == None:
            return rightHead          
        leftTail.next = rightHead
        if currentRight != None:
            currentRight.next = None
        return head