# 148. Sort List
# Medium

# 2038

# 102

# Add to List

# Share
# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def sortedMerge(self, a, b): 
    result = None

    # Base cases 
    if not a: 
      return b 
    if not b: 
      return a 

    # pick either a or b and recur.. 
    if a.val <= b.val: 
      result = a 
      result.next = self.sortedMerge(a.next, b) 
    else: 
      result = b 
      result.next = self.sortedMerge(a, b.next) 
    return result 
      
  def mergeSort(self, head): 

      # Base case if head is None 
      if not head or not head.next: 
        return head

      # get the middle of the list  
      middle = self.getMiddle(head) 
      nextToMiddle = middle.next

      # set the next of middle node to None 
      middle.next = None

      # Apply mergeSort on left list  
      left = self.mergeSort(head) 

      # Apply mergeSort on right list 
      right = self.mergeSort(nextToMiddle) 

      # Merge the left and right lists  
      sortedList = self.sortedMerge(left, right) 
      return sortedList 
      
  # Utility function to get the middle  
  # of the linked list  
  def getMiddle(self, head): 
    if not head: 
      return head 

    slow = head 
    fast = head 

    while fast.next and fast.next.next: 
      slow = slow.next
      fast = fast.next.next

    return slow 
      
  def sortList(self, head: ListNode) -> ListNode:
    head = self.mergeSort(head) 
    return head
        