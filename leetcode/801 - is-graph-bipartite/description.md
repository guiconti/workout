There is an __undirected__ graph with `` n `` nodes, where each node is numbered between `` 0 `` and `` n - 1 ``. You are given a 2D array `` graph ``, where `` graph[u] `` is an array of nodes that node `` u `` is adjacent to. More formally, for each `` v `` in `` graph[u] ``, there is an undirected edge between node `` u `` and node `` v ``. The graph has the following properties:

*   There are no self-edges (`` graph[u] `` does not contain `` u ``).
*   There are no parallel edges (`` graph[u] `` does not contain duplicate values).
*   If `` v `` is in `` graph[u] ``, then `` u `` is in `` graph[v] `` (the graph is undirected).
*   The graph may not be connected, meaning there may be two nodes `` u `` and `` v `` such that there is no path between them.

A graph is __bipartite__ if the nodes can be partitioned into two independent sets `` A `` and `` B `` such that __every__ edge in the graph connects a node in set `` A `` and a node in set `` B ``.

Return `` true ``_ if and only if it is __bipartite___.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg" style="width: 222px; height: 222px;"/>

<pre>
<strong>Input:</strong> graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg" style="width: 222px; height: 222px;"/>

<pre>
<strong>Input:</strong> graph = [[1,3],[0,2],[1,3],[0,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can partition the nodes into two sets: {0, 2} and {1, 3}.</pre>

&nbsp;

__Constraints:__

*   `` graph.length == n ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` 0 &lt;= graph[u].length &lt; n ``
*   `` 0 &lt;= graph[u][i] &lt;= n - 1 ``
*   `` graph[u] ``&nbsp;does not contain&nbsp;`` u ``.
*   All the values of `` graph[u] `` are __unique__.
*   If `` graph[u] `` contains `` v ``, then `` graph[v] `` contains `` u ``.