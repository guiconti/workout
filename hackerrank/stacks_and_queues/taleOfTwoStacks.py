class MyQueue(object):

    firstStack = []
    secondStack = []

    def __init__(self):
        self.firstStack = []
        self.secondStack = []
    
    def peek(self):
        if len(self.secondStack) == 0:
            while len(self.firstStack) > 0:
                self.secondStack.append(self.firstStack.pop())
        return self.secondStack[-1]
        
    def pop(self):
        if len(self.secondStack) == 0:
            while len(self.firstStack) > 0:
                self.secondStack.append(self.firstStack.pop())
        return self.secondStack.pop()
        
    def put(self, value):
        self.firstStack.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

