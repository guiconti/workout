from collections import deque
class MyStack:
  def __init__(self):
    self.stack = deque()
    self.tmp = deque()
      

  def push(self, x: int) -> None:
    self.tmp.append(x)
    while len(self.stack) != 0:
      self.tmp.append(self.stack.popleft())
    self.stack = self.tmp 
    self.tmp = deque()
      

  def pop(self) -> int:
    return self.stack.popleft()
      

  def top(self) -> int:
    return self.stack[0]
      

  def empty(self) -> bool:
    return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()