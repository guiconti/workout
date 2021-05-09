We start at some node in a directed graph, and every turn, we walk along a directed edge of the graph. If we reach a terminal node (that is, it has no outgoing directed edges), we stop.

We define a starting node to be __safe__ if we must eventually walk to a terminal node. More specifically, there is a natural number `` k ``, so that we must have stopped at a terminal node in less than `` k `` steps for __any choice of where to walk__.

Return _an array containing all the safe nodes of the graph_. The answer should be sorted in __ascending__ order.

The directed graph has `` n `` nodes with labels from `` 0 `` to `` n - 1 ``, where `` n `` is the length of `` graph ``. The graph is given in the following form: `` graph[i] `` is a list of labels `` j `` such that `` (i, j) `` is a directed edge of the graph, going from node `` i `` to node `` j ``.

&nbsp;

__Example 1:__

<img alt="Illustration of graph" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" style="height: 171px; width: 600px;"/>

<pre>
<strong>Input:</strong> graph = [[1,2],[2,3],[5],[0],[5],[],[]]
<strong>Output:</strong> [2,4,5,6]
<strong>Explanation:</strong> The given graph is shown above.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
<strong>Output:</strong> [4]
</pre>

&nbsp;

__Constraints:__

*   `` n == graph.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   `` 0 &lt;= graph[i].legnth &lt;= n ``
*   `` graph[i] `` is sorted in a strictly increasing order.
*   The graph may contain self-loops.
*   The number of edges in the graph will be in the range <code>[1, 4 * 10<sup>4</sup>]</code>.