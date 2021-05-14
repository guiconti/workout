Given a weighted undirected connected graph with `` n ``&nbsp;vertices numbered from `` 0 `` to `` n - 1 ``,&nbsp;and an array `` edges ``&nbsp;where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>, weight<sub>i</sub>]</code> represents a bidirectional and weighted edge between nodes&nbsp;<code>a<sub>i</sub></code>&nbsp;and <code>b<sub>i</sub></code>. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles&nbsp;and with the minimum possible total edge weight.

Find _all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST)_. An MST edge whose deletion from the graph would cause the MST weight to increase is called a&nbsp;_critical edge_. On&nbsp;the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/04/ex1.png" style="width: 259px; height: 262px;"/>

<pre>
<strong>Input:</strong> n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
<strong>Output:</strong> [[0,1],[2,3,4,5]]
<strong>Explanation:</strong> The figure above describes the graph.
The following figure shows all the possible MSTs:
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/04/msts.png" style="width: 540px; height: 553px;"/>
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/04/ex2.png" style="width: 247px; height: 253px;"/>

<pre>
<strong>Input:</strong> n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
<strong>Output:</strong> [[],[0,1,2,3]]
<strong>Explanation:</strong> We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= edges.length &lt;= min(200, n * (n - 1) / 2) ``
*   `` edges[i].length == 3 ``
*   <code>0 &lt;= a<sub>i</sub> &lt; b<sub>i</sub> &lt; n</code>
*   <code>1 &lt;= weight<sub>i</sub>&nbsp;&lt;= 1000</code>
*   All pairs <code>(a<sub>i</sub>, b<sub>i</sub>)</code> are __distinct__.