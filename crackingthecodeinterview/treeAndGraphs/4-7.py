# Given a list of packages and a list of dependencies create a list of the build order

import queue

# Solution - Create a graph with every package as a node containing an array with it's dependencies and a state
# that will be used to control the build order. We then for each node inside the graph
# If the node is in a blank state (not initiated) we call DFS on this node
# On DFS on first check if this Node is not in progress, if it is we fell into a cycle and return False
# Then we set this node as being in progress and then for each dependency of this node we call DFS
# When there's no more dependecies we add it to a stack containing our build order
# Last element added to the stack, the one that we receive when calling pop(), would be the first in the build order
# And so on

BLANK = 0
IN_PROGRESS = 1
COMPLETED = 2

class Node:
  def __init__(self, data):
    self.data = data
    self.state = BLANK
    self.dependencies = []

def createGraph(size, connections):
  graph = [None] * size

  for i in range(size):
    graph[i] = Node(i + 1)

  for i in range(len(connections)):
    graph[connections[i][0] - 1].dependencies.append(graph[connections[i][1] - 1])

  return graph

def DFS(root, buildOrder):
  if root.state == IN_PROGRESS:
    # Cycle
    return False
  if root.state == BLANK:
    root.state = IN_PROGRESS
    for dependency in root.dependencies:
      if not DFS(dependency, buildOrder):
        return False
    root.state = COMPLETED
    buildOrder.append(root.data)

  return True

if __name__ == '__main__':
  amountOfPackages = 7
  dependencies = [[1, 2], [3, 1], [1, 5], [2, 4], [1, 4], [6, 7]]
  graph = createGraph(amountOfPackages, dependencies)
  # Stack (last element inserted will be the first to build)
  buildOrder = []
  for node in graph:
    if node.state == BLANK:
      if not DFS(node, buildOrder):
        print('IMPOSSIBLE')
        break
  # Empty stack to print order
  while len(buildOrder) > 0:
    print(buildOrder.pop())