# Given a graph find if there is a route between two nodes

import queue

class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.neighbours = []

def createGraph(size, connections):
  graph = [None] * size

  for i in range(size):
    graph[i] = Node(i + 1)

  for i in range(len(connections)):
    graph[connections[i][0] - 1].neighbours.append(graph[connections[i][1] - 1])
    graph[connections[i][1] - 1].neighbours.append(graph[connections[i][0] - 1])

  return graph

def BFS(nodeA, goal):
  myQueue = queue.Queue(maxsize = 0)
  myQueue.put(nodeA)

  while not myQueue.empty():
    current = myQueue.get()
    current.visited = True
    if current == goal:
      return True
    for neighbour in current.neighbours:
      if not neighbour.visited:
        myQueue.put(neighbour)
        
  return False

if __name__ == '__main__':
  amountOfNodes = 5
  connections = [[1, 2], [1, 5], [4, 5], [4, 2], [2, 3]]
  graph = createGraph(amountOfNodes, connections)
  print(BFS(graph[0], graph[2]))

