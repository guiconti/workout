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
