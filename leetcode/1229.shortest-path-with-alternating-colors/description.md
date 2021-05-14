Consider a directed graph, with nodes labelled `` 0, 1, ..., n-1 ``.&nbsp; In this graph, each edge is either red or blue, and there could&nbsp;be self-edges or parallel edges.

Each `` [i, j] `` in `` red_edges `` denotes a red directed edge from node `` i `` to node `` j ``.&nbsp; Similarly, each `` [i, j] `` in `` blue_edges `` denotes a blue directed edge from node `` i `` to node `` j ``.

Return an array `` answer ``&nbsp;of length `` n ``,&nbsp;where each&nbsp;`` answer[X] ``&nbsp;is&nbsp;the length of the shortest path from node `` 0 ``&nbsp;to node `` X ``&nbsp;such that the edge colors alternate along the path (or `` -1 `` if such a path doesn't exist).

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
<strong>Output:</strong> [0,1,-1]
</pre>

__Example 2:__

<pre><strong>Input:</strong> n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
<strong>Output:</strong> [0,1,-1]
</pre>

__Example 3:__

<pre><strong>Input:</strong> n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
<strong>Output:</strong> [0,-1,-1]
</pre>

__Example 4:__

<pre><strong>Input:</strong> n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
<strong>Output:</strong> [0,1,2]
</pre>

__Example 5:__

<pre><strong>Input:</strong> n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
<strong>Output:</strong> [0,1,1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``
*   `` red_edges.length &lt;= 400 ``
*   `` blue_edges.length &lt;= 400 ``
*   `` red_edges[i].length == blue_edges[i].length == 2 ``
*   `` 0 &lt;= red_edges[i][j], blue_edges[i][j] &lt; n ``