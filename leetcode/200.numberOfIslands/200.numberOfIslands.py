# 200. Number of Islands
# Medium

# 3837

# 140

# Add to List

# Share
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.neighbours = []

class Solution:
  def createGraph(self, matrix):
    graph = [None] * len(matrix)
    for i in range(len(graph)):
      graph[i] = [None] * len(matrix[i])

    for i in range(len(matrix)):
      for j in range(len(matrix[i])):

        if matrix[i][j] == '1':
          if not graph[i][j]:
            graph[i][j] = Node(', '.join(str(x) for x in [i, j]))

          # Add connected islands
          if i > 0:
            if matrix[i - 1][j] == '1':
              if not graph[i - 1][j]:
                graph[i - 1][j] = Node(', '.join(str(x) for x in [i - 1, j]))
              graph[i][j].neighbours.append(graph[i - 1][j])

          if i < len(matrix) - 1:
            if matrix[i + 1][j] == '1':
              if not graph[i + 1][j]:
                graph[i + 1][j] = Node(', '.join(str(x) for x in [i + 1, j]))
              graph[i][j].neighbours.append(graph[i + 1][j])

          if j > 0:
            if matrix[i][j - 1] == '1':
              if not graph[i][j - 1]:
                graph[i][j - 1] = Node(', '.join(str(x) for x in [i, j - 1]))
              graph[i][j].neighbours.append(graph[i][j - 1])

          if j < len(matrix[i]) - 1:
            if matrix[i][j + 1] == '1':
              if not graph[i][j + 1]:
                graph[i][j + 1] = Node(', '.join(str(x) for x in [i, j + 1]))
              graph[i][j].neighbours.append(graph[i][j + 1])
    return graph
              
  def findIslandSize(self, root):
    if not root:
      return 1

    root.visited = True
    size = 1
    for neighbour in root.neighbours:
      if not neighbour.visited:
        size += self.findIslandSize(neighbour)
    return size
            
  def numIslands(self, grid: List[List[str]]) -> int:
    graph = self.createGraph(grid)
    answer = 0
    for row in graph:
      for node in row:
        if node and not node.visited:
          size = self.findIslandSize(node)
          if size > 0:
            answer += 1
    return answer