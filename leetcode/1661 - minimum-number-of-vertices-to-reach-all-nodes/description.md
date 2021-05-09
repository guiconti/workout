Given a__&nbsp;directed acyclic graph__,&nbsp;with&nbsp;`` n ``&nbsp;vertices numbered from&nbsp;`` 0 ``&nbsp;to&nbsp;`` n-1 ``,&nbsp;and an array&nbsp;`` edges ``&nbsp;where&nbsp;<code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>]</code>&nbsp;represents a directed edge from node&nbsp;<code>from<sub>i</sub></code>&nbsp;to node&nbsp;<code>to<sub>i</sub></code>.

Find _the smallest set of vertices from which all nodes in the graph are reachable_. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/07/untitled22.png" style="width: 231px; height: 181px;"/>

<pre>
<strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
<strong>Output:</strong> [0,3]
<b>Explanation: </b>It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/07/untitled.png" style="width: 201px; height: 201px;"/>

<pre>
<strong>Input:</strong> n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
<strong>Output:</strong> [0,2,3]
<strong>Explanation: </strong>Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 10^5 ``
*   `` 1 &lt;= edges.length &lt;= min(10^5, n * (n - 1) / 2) ``
*   `` edges[i].length == 2 ``
*   <code>0 &lt;= from<sub>i,</sub>&nbsp;to<sub>i</sub> &lt; n</code>
*   All pairs <code>(from<sub>i</sub>, to<sub>i</sub>)</code> are distinct.