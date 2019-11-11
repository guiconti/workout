# Suppose you have two numbers represented by linked lists. Sum these numbers and return
# a linkes list with the result. The lists are in the reverse order

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Solution 1 Goes through each element of the list, sum and mod 10. Get the remaning of the mod 10
# and add to the next number. Do it until you reach the end of both elements
def Solution1(firstNumber, secondNumber):
  headSolution = None
  currentSolution = None

  while firstNumber or secondNumber:
    if firstNumber and secondNumber:
      currentNumber = firstNumber.data + secondNumber.data
    elif firstNumber:
      currentNumber = firstNumber.data
    else:
      currentNumber = secondNumber.data

    if currentNumber > 10:
      if not headSolution:
        headSolution = Node(currentNumber % 10)
        currentSolution = headSolution
      else:
        currentSolution.next = Node(currentNumber % 10)
        currentSolution = currentSolution.next
      if not firstNumber.next:
        firstNumber.next = Node(0)
      firstNumber.next.data += currentNumber // 10
    else:
      if not headSolution:
        headSolution = Node(currentNumber)
        currentSolution = headSolution
      else:
        currentSolution.next = Node(currentNumber)
        currentSolution = currentSolution.next

    if firstNumber:
      firstNumber = firstNumber.next
    if secondNumber:
      secondNumber = secondNumber.next

  return headSolution


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  head = Node(1)
  head.next = Node(3)
  head.next.next = Node(1)
  head2 = Node(1)
  head2.next = Node(8)
  head2.next.next = Node(1)
  solution = Solution1(head, head2)
  current = solution
  while current:
    print(current.data)
    current = current.next