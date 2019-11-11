import queue

if __name__ == '__main__':
  a = queue.Queue(maxsize = 0)
  a.put(5)
  a.put(6)
  print(a.get())
  print(a.get())
  print(a)