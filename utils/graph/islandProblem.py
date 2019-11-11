class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.neighbours = []

def createGraph(matrix):
  graph = [None] * len(matrix)
  for i in range(len(graph)):
      graph[i] = [None] * len(matrix[i])

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      
      if matrix[i][j] == 1:
        if not graph[i][j]:
          graph[i][j] = Node(', '.join(str(x) for x in [i, j]))
        
        # Add connected islands
        if i > 0:
          if matrix[i - 1][j] == 1:
            if not graph[i - 1][j]:
              graph[i - 1][j] = Node(', '.join(str(x) for x in [i - 1, j]))
            graph[i][j].neighbours.append(graph[i - 1][j])
          if j > 0:
            if matrix[i - 1][j - 1] == 1:
              if not graph[i - 1][j - 1]:
                graph[i - 1][j - 1] = Node(', '.join(str(x) for x in [i - 1, j - 1]))
              graph[i][j].neighbours.append(graph[i - 1][j - 1])
          if j < len(matrix[i]) - 1:
            if matrix[i - 1][j + 1] == 1:
              if not graph[i - 1][j + 1]:
                graph[i - 1][j + 1] = Node(', '.join(str(x) for x in [i - 1, j + 1]))
              graph[i][j].neighbours.append(graph[i - 1][j + 1])

        if i < len(matrix) - 1:
          if matrix[i + 1][j] == 1:
            if not graph[i + 1][j]:
              graph[i + 1][j] = Node(', '.join(str(x) for x in [i + 1, j]))
            graph[i][j].neighbours.append(graph[i + 1][j])
          if j > 0:
            if matrix[i + 1][j - 1] == 1:
              if not graph[i + 1][j - 1]:
                graph[i + 1][j - 1] = Node(', '.join(str(x) for x in [i + 1, j - 1]))
              graph[i][j].neighbours.append(graph[i + 1][j - 1])
          if j < len(matrix[i]) - 1:
            if matrix[i + 1][j + 1] == 1:
              if not graph[i + 1][j + 1]:
                graph[i + 1][j + 1] = Node(', '.join(str(x) for x in [i + 1, j + 1]))
              graph[i][j].neighbours.append(graph[i + 1][j + 1])

        if j > 0:
          if matrix[i][j - 1] == 1:
            if not graph[i][j - 1]:
              graph[i][j - 1] = Node(', '.join(str(x) for x in [i, j - 1]))
            graph[i][j].neighbours.append(graph[i][j - 1])

        if j < len(matrix[i]) - 1:
          if matrix[i][j + 1] == 1:
            if not graph[i][j + 1]:
              graph[i][j + 1] = Node(', '.join(str(x) for x in [i, j + 1]))
            graph[i][j].neighbours.append(graph[i][j + 1])

  return graph

def findIslandSize(root):
  if not root:
    return 1
  
  root.visited = True
  size = 1
  for neighbour in root.neighbours:
    if not neighbour.visited:
      size += findIslandSize(neighbour)
  return size

if __name__ == "__main__":
  ocean = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
          ]
  graph = createGraph(ocean)
  for row in graph:
    for node in row:
      if node and not node.visited:
        size = findIslandSize(node)
        print (size)
  
