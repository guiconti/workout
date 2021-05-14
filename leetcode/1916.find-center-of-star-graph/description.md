There is an undirected __star__ graph consisting of `` n `` nodes labeled from `` 1 `` to `` n ``. A star graph is a graph where there is one __center__ node and __exactly__ `` n - 1 `` edges that connect the center node with every other node.

You are given a 2D integer array `` edges `` where each <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that there is an edge between the nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>. Return the center of the given star graph.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/24/star_graph.png" style="width: 331px; height: 321px;"/>

<pre>
<strong>Input:</strong> edges = [[1,2],[2,3],[4,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> edges = [[1,2],[5,1],[1,3],[1,4]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` edges.length == n - 1 ``
*   `` edges[i].length == 2 ``
*   <code>1 &lt;= u<sub>i,</sub> v<sub>i</sub> &lt;= n</code>
*   <code>u<sub>i</sub> != v<sub>i</sub></code>
*   The given `` edges `` represent a valid star graph.