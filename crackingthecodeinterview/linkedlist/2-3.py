# Delete a node in the middle point if you receive a middle node

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Create two pointers to run the array. Run the first point k time
# Then start running each pointer together. When the first pointer reach the end
# The second point would be length - k O(n)
def Solution1(current):

  current.data = current.next.data
  current.next = current.next.next


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  head = Node(5)
  head.next = Node(1)
  head.next.next = Node(3)
  head.next.next.next = Node(5)
  head.next.next.next.next = Node(8)
  head.next.next.next.next.next = Node(9)
  Solution1(head.next.next.next)
  current = head
  while current:
    print(current.data)
    current = current.next