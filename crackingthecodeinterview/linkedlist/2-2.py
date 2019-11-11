# Write code to remove duplicates from an unsorted linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Create two pointers to run the array. Run the first point k time
# Then start running each pointer together. When the first pointer reach the end
# The second point would be length - k O(n)
def Solution1(head, k):

  current = head
  runner = head
  for i in range(k):
    if not runner.next:
      return False
    runner = runner.next

  while runner.next:
    current = current.next
    runner = runner.next
  
  return current.data


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  head = Node(5)
  head.next = Node(1)
  head.next.next = Node(3)
  head.next.next.next = Node(5)
  head.next.next.next.next = Node(8)
  head.next.next.next.next.next = Node(9)
  print(Solution1(head, 6))