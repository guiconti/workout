# Design a stack that also contains a min function with O(1)

class SetOfStacks():
  amountOfStacks = 1
  stacks = [[]] * 5
  stackThreshold = 4
  currentStackSize = 0
  
  def push(self, value):
    if self.currentStackSize == self.stackThreshold:
      self.amountOfStacks += 1
      self.currentStackSize = 0
    if not self.stacks[self.amountOfStacks - 1]:
      self.stacks[self.amountOfStacks - 1] = []
    self.stacks[self.amountOfStacks - 1].append(value)
    self.currentStackSize += 1

  def pop(self):
    if self.currentStackSize == 0:
      if self.amountOfStacks == 1:
        return False
      self.currentStackSize = self.stackThreshold
      self.amountOfStacks -= 1
    self.currentStackSize -= 1
    return self.stacks[self.amountOfStacks - 1].pop()

  def peek(self):
    if self.currentStackSize == 0:
      if self.amountOfStacks == 1:
        return False
      return self.stacks[self.amountOfStacks - 2]
    return self.stacks[self.amountOfStacks - 1]

  def isEmpty(self):
    return self.currentStackSize == 0 and self.amountOfStacks == 1


# Solution 2 if no buffer is allowed we could for each element create a runner pointer
# That will go through the remaining elements looking for duplicates O(n^2)

if __name__ == '__main__':
  stack = SetOfStacks()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.push(4)
  stack.push(5)
  stack.push(6)
  stack.push(7)
  stack.push(8)
  stack.pop()
  stack.push(8)
  stack.push(9)
  stack.pop()
  print(stack.stacks)