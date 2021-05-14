An undirected, connected graph of N nodes (labeled&nbsp;`` 0, 1, 2, ..., N-1 ``) is given as `` graph ``.

`` graph.length = N ``, and `` j != i ``&nbsp;is in the list&nbsp;`` graph[i] ``&nbsp;exactly once, if and only if nodes `` i `` and `` j `` are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>[[1,2,3],[0],[0],[0]]
<strong>Output: </strong>4
<strong>Explanation</strong>: One possible path is [1,0,2,0,3]</pre>

__Example 2:__

<pre>
<strong>Input: </strong>[[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>Output: </strong>4
<strong>Explanation</strong>: One possible path is [0,1,4,2,3]
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= graph.length &lt;= 12 ``
2.   `` 0 &lt;= graph[i].length &lt;&nbsp;graph.length ``