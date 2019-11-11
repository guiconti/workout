# Check if a linked list is a palindrome

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Run through the list and add each value to a hash table
# Iterate through the hash table to check if there's more than 1 odd occurrence O(N)
def Solution1(nodeA):
  dictionary = {}

  while nodeA:
    if nodeA.data in dictionary:
      dictionary[nodeA.data] += 1
    else:
      dictionary[nodeA.data] = 1
    nodeA = nodeA.next

  foundOdd = False
  for key in dictionary:
    if dictionary[key] % 2 != 0:
      if foundOdd:
        return False
      foundOdd = True

  return True

# Solution 2 If you have the size of the list create two pointers where one pointer runs twice
# as fast as the first pointer. When the second pointer reaches the end your first pointer would be at
# the middle. Then just comes back and check if they are equivalent O(N)


# Solution 3 If we don't know the size if the list and can't use another structure we can
# create a clone of the linked list, reverse it and the go char by char O(2n)
def Solution3(current):
  reversedList = cloneAndReverse(current)

  while current:
    if current != reversedList:
      return False
    current = current.next
    reversedList = reversedList.next
  
  return True

def cloneAndReverse(head):
  original = head
  clonedHead = Node(head.data)
  newNode = clonedHead
  original = original.next

  while original:
    newNode = Node(original.data)
    newNode.next = clonedHead
    clonedHead = newNode
    original = original.next
  
  return newNode

if __name__ == '__main__':
  head = Node(3)
  head.next = Node(2)
  head.next.next = Node(3)
  print(Solution1(head))
  print(Solution3(head))