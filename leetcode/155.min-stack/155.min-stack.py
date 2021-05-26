class MinStack:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []
      

  def push(self, val: int) -> None:
    self.stack.append(val)
    return

  def pop(self) -> None:
    self.stack.pop()
    return

  def top(self) -> int:
    return self.stack[len(self.stack) - 1]

  def getMin(self) -> int:
    if len(self.stack) == 0:
      return None
    result = self.stack[0]
    for i in range(1, len(self.stack)):
      if self.stack[i] < result:
        result = self.stack[i]
    return result
