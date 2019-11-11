# Write code to remove duplicates from an unsorted linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Iterate through the linked list, add each data to a hash table
# If we found a hit remove it O(n)
def Solution1(head):
  dictionary = {}

  current = head
  previous = None
  while current:
    if current.data in dictionary:
      previous.next = current.next if current.next else None
      current = previous.next
    else:
      dictionary[current.data] = True
      previous = current
      current = current.next
  return head

# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  head = Node(5)
  head.next = Node(1)
  head.next.next = Node(3)
  head.next.next.next = Node(5)
  head.next.next.next.next = Node(8)
  head.next.next.next.next.next = Node(9)
  Solution1(head)
  current = head
  while current:
    print(current.data)
    current = current.next