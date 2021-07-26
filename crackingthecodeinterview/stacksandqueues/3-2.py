# Design a stack that also contains a min function with O(1)

# Solution 1 Create two stacks. One that holds every value and another that holds the min
# If a value is popped check if it is the top of your stack, if so pop as well
def insert(stack, minStack, value):
  stack.append(value)
  if len(minStack) == 0 or minStack[len(minStack) - 1] >= value:
    minStack.append(value)

def remove(stack, minStack):
  if minStack[len(minStack) - 1] == stack.pop():
    minStack.pop()

def getMin(stack, minStack):
  return minStack[len(minStack) - 1]


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  stack = []
  minStack = []
  insert(stack, minStack, 10)
  insert(stack, minStack, 13)
  insert(stack, minStack, 8)
  insert(stack, minStack, 5)
  insert(stack, minStack, 8)
  insert(stack, minStack, 5)
  insert(stack, minStack, 13)
  insert(stack, minStack, 11)
  print(stack, minStack)
  print(getMin(stack, minStack))
  remove(stack, minStack)
  remove(stack, minStack)
  remove(stack, minStack)
  print(stack, minStack)
  remove(stack, minStack)
  remove(stack, minStack)
  print(getMin(stack, minStack))
  remove(stack, minStack)
  print(getMin(stack, minStack))

class MinStack:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []
    self.minStack = []
      

  def push(self, val: int) -> None:
    self.stack.append(val)
    if len(self.minStack) == 0 or self.minStack[len(self.minStack) - 1] >= val:
      self.minStack.append(val)
    return

  def pop(self) -> None:
    removed = self.stack.pop()
    if len(self.minStack) > 0 and removed == self.minStack[len(self.minStack) - 1]:
      self.minStack.pop()
    return

  def top(self) -> int:
    return self.stack[len(self.stack) - 1]

  def getMin(self) -> int:
    if len(self.minStack) == 0:
      return 999
    return self.minStack[len(self.minStack) - 1]
