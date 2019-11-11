# Design a stack that also contains a min function with O(1)

class SetOfStacks():
  stack = []
  tempStack = []
  
  def push(self, value):
    while len(self.stack) > 0 and self.stack[len(self.stack) - 1] < value:
      self.tempStack.append(self.stack.pop())
    self.stack.append(value)
    while len(self.tempStack) > 0:
      self.stack.append(self.tempStack.pop())

  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[len(self.stack) - 1]

  def isEmpty(self):
    return len(self.stack) == 0


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  stack = SetOfStacks()
  stack.push(4)
  stack.push(8)
  stack.push(2)
  stack.push(4)
  stack.push(1)
  stack.push(3)
  stack.push(1)
  stack.push(10)
  stack.pop()
  stack.push(11)
  stack.push(0)
  stack.pop()
  print(stack.stack)