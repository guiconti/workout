# Implement a MyQueue class which implements a queue using two stacks

class MyQueue:
  firstStack = []
  secondStack = []

  def add(self, value):
    self.firstStack.append(value)

  def remove(self):
    if len(self.secondStack) == 0:
      while len(self.firstStack) > 0:
        self.secondStack.append(self.firstStack.pop())
    return self.secondStack.pop()

  def peek(self):
    if len(self.secondStack) == 0:
      while len(self.firstStack) > 0:
        self.secondStack.append(self.firstStack.pop())
    return self.secondStack[len(self.secondStack) - 1]

  def isEmpty(self):
    return len(self.firstStack) == 0 and len(self.secondStack) == 0

if __name__ == '__main__':
  stackQueue = MyQueue()
  stackQueue.add(1)
  stackQueue.add(2)
  stackQueue.add(3)
  stackQueue.add(4)
  stackQueue.add(5)
  print(stackQueue.remove())
  print(stackQueue.peek())
  stackQueue.add(6)
  print(stackQueue.peek())
  print(stackQueue.remove())