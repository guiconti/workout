# Find if a linkedlist contains a loop

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Create a slow and a faster pointer. Faster runs twice as fast as slow
# If they meet before faster point reaches null then there's a loop
def Solution1(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True

  return False


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  head = Node(5)
  head.next = Node(1)
  head.next.next = Node(3)
  head.next.next.next = Node(5)
  head.next.next.next.next = Node(8)
  head.next.next.next.next.next = Node(9)
  head.next.next.next.next.next.next = Node(3)
  head.next.next.next.next.next.next.next = head.next.next.next
  print(Solution1(head))