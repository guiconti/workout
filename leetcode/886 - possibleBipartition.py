# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group. 

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

 

# Example 1:

# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:

# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:

# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 

# Note:

# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

class Node:
  def __init__(self, value):
    self.value = value
    self.neighbours = []
    self.group = None

class Solution:
  GROUPS = {
    'A': 'B',
    'B': 'A'
  }
  def buildGraph(self, matrix, size):
    graph = [None] * size
    
    for i in range(size):
      graph[i] = Node(i + 1)
      
    for dislike in matrix:
      graph[dislike[0] - 1].neighbours.append(graph[dislike[1] - 1])
      graph[dislike[1] - 1].neighbours.append(graph[dislike[0] - 1])
      
    return graph
  
  def DFS(self, root):
    for node in root.neighbours:
      if node.group:
        if node.group != self.GROUPS[root.group]:
          return False
      else:
        node.group = self.GROUPS[root.group]
        validSoFar = self.DFS(node)
        if not validSoFar:
          return False
    return True
  
  def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
    graph = self.buildGraph(dislikes, N)
    for node in graph:
      if not node.group:
        node.group = 'A'
        validSoFar = self.DFS(node)
      if not validSoFar:
        return False
    return True
    
        