Given a reference of a node in a __<a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a>__ undirected graph.

Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank">__deep copy__</a> (clone) of the graph.

Each node in the graph contains a value (`` int ``) and a list (`` List[Node] ``) of its neighbors.

<pre>
class Node {
    public int val;
    public List&lt;Node&gt; neighbors;
}
</pre>

&nbsp;

__Test case format:__

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `` val == 1 ``, the second node with `` val == 2 ``, and so on. The graph is represented in the test case using an adjacency list.

__An adjacency list__ is a collection of unordered __lists__ used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `` val = 1 ``. You must return the __copy of the given node__ as a reference to the cloned graph.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png" style="width: 500px; height: 550px;"/>

<pre>
<strong>Input:</strong> adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong>Output:</strong> [[2,4],[1,3],[2,4],[1,3]]
<strong>Explanation:</strong> There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/07/graph.png" style="width: 163px; height: 148px;"/>

<pre>
<strong>Input:</strong> adjList = [[]]
<strong>Output:</strong> [[]]
<strong>Explanation:</strong> Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> adjList = []
<strong>Output:</strong> []
<strong>Explanation:</strong> This an empty graph, it does not have any nodes.
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/07/graph-1.png" style="width: 272px; height: 133px;"/>

<pre>
<strong>Input:</strong> adjList = [[2],[1]]
<strong>Output:</strong> [[2],[1]]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the graph is in the range `` [0, 100] ``.
*   `` 1 &lt;= Node.val &lt;= 100 ``
*   `` Node.val `` is unique for each node.
*   There are no repeated edges and no self-loops in the graph.
*   The Graph is connected and all nodes can be visited starting from the given node.