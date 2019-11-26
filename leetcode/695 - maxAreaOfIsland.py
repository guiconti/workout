# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.neighbours = []

class Solution:
  
  def buildGraph(self, matrix):
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
            # if j > 0:
            #   if matrix[i - 1][j - 1] == 1:
            #     if not graph[i - 1][j - 1]:
            #       graph[i - 1][j - 1] = Node(', '.join(str(x) for x in [i - 1, j - 1]))
            #     graph[i][j].neighbours.append(graph[i - 1][j - 1])
            # if j < len(matrix[i]) - 1:
            #   if matrix[i - 1][j + 1] == 1:
            #     if not graph[i - 1][j + 1]:
            #       graph[i - 1][j + 1] = Node(', '.join(str(x) for x in [i - 1, j + 1]))
            #     graph[i][j].neighbours.append(graph[i - 1][j + 1])

          if i < len(matrix) - 1:
            if matrix[i + 1][j] == 1:
              if not graph[i + 1][j]:
                graph[i + 1][j] = Node(', '.join(str(x) for x in [i + 1, j]))
              graph[i][j].neighbours.append(graph[i + 1][j])
            # if j > 0:
            #   if matrix[i + 1][j - 1] == 1:
            #     if not graph[i + 1][j - 1]:
            #       graph[i + 1][j - 1] = Node(', '.join(str(x) for x in [i + 1, j - 1]))
            #     graph[i][j].neighbours.append(graph[i + 1][j - 1])
            # if j < len(matrix[i]) - 1:
            #   if matrix[i + 1][j + 1] == 1:
            #     if not graph[i + 1][j + 1]:
            #       graph[i + 1][j + 1] = Node(', '.join(str(x) for x in [i + 1, j + 1]))
            #     graph[i][j].neighbours.append(graph[i + 1][j + 1])

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
  
  def DFS(self, root):
    if not root:
      return 1
  
    root.visited = True
    size = 1
    for neighbour in root.neighbours:
      if not neighbour.visited:
        size += self.DFS(neighbour)
    return size

  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    graph = self.buildGraph(grid)
    maxSize = 0
    for row in graph:
      for island in row:
        if island and not island.visited:
          size = self.DFS(island)
          if size > maxSize:
            maxSize = size
    return maxSize
          