import queue

class Node:
  def __init__(self, index):
    self.index = index
    self.visited = False
    self.distance = 0
    self.neighbours = []

def createGraph(size, connections):
    graph = [0] * size

    for i in range(size):
        graph[i] = Node(i + 1)

    for i in range(len(connections)):
        graph[connections[i][0] - 1].neighbours.append(graph[connections[i][1] - 1])
        graph[connections[i][1] - 1].neighbours.append(graph[connections[i][0] - 1])

    return graph

def BFS(graph, startPosition, value):
    graphQueue = queue.Queue(maxsize = 0)
    graphQueue.put(graph[startPosition - 1])

    while not graphQueue.empty():
        currentNode = graphQueue.get()
        currentNode.visited = True
        if (currentNode.index == value):
          return currentNode.distance
        for neighbour in currentNode.neighbours:
            if not neighbour.visited:
                neighbour.distance = currentNode.distance + 1
                graphQueue.put(neighbour)
    return -1

if __name__ == '__main__':
  graph = createGraph(5, [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [3, 5], [2, 4]])
  print(BFS(graph, 1, 5))