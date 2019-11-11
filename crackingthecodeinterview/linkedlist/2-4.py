# Sort a list where all values less than x should be on the left and all elements bigger than x
# should be on the right

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Create another list to keep our smaller values while keeping the greater values on the current list
# Then merge the two lists
def Solution1(head, value):
  headSmallestList = None
  endSmallestList = None
  headBiggerList = head
  endBiggerList = head
  previous = None

  while endBiggerList:
    if endBiggerList.data < value:
      if headSmallestList:
        endSmallestList.next = endBiggerList
        endSmallestList = endBiggerList
      else:
        headSmallestList = endBiggerList
        endSmallestList = headSmallestList
      if previous:
        previous.next = endBiggerList.next
      current = current.next
      current.next = None
    else:


  currentSmallestList.next = 


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  head = Node(5)
  head.next = Node(1)
  head.next.next = Node(3)
  head.next.next.next = Node(5)
  head.next.next.next.next = Node(8)
  head.next.next.next.next.next = Node(9)
  Solution1(head, 5)
  current = head
  while current:
    print(current.data)
    current = current.next