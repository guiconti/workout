# 155. Min Stack
# Easy

# 2509

# 267

# Add to List

# Share
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:

  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, x: int) -> None:
    self.stack.append(x)
    if len(self.minStack) == 0:
      self.minStack.append(x)
    elif x <= self.minStack[len(self.minStack) - 1]:
      self.minStack.append(x)
    return

  def pop(self) -> None:
    if len(self.stack) > 0 and self.stack.pop() == self.minStack[len(self.minStack) - 1]:
      self.minStack.pop()
    return

  def top(self) -> int:
    if len(self.stack) > 0:
      return self.stack[len(self.stack) - 1]
    return None

  def getMin(self) -> int:
    return self.minStack[len(self.minStack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()