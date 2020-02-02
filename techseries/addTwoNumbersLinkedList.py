# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if not l1 and not l2:
      return None
    result = ListNode(0)
    currentNode = result
    leftover = 0
    while l1 or l2:
      currentSum = leftover
      leftover = 0
      if l1:
        currentSum += l1.val
        l1 = l1.next
      if l2:
        currentSum += l2.val
        l2 = l2.next
      leftover = currentSum // 10
      currentSum = currentSum % 10
      currentNode.val = currentSum
      if l1 or l2:
        currentNode.next = ListNode(0)
      elif leftover > 0:
        currentNode.next = ListNode(leftover)
      currentNode = currentNode.next
    return result

l1 = ListNode(9)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(6)
l2.next.next = ListNode(6)
l2.next.next.next = ListNode(9)
l2.next.next.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 8 1 0 0 0 1