Alice and Bob have an undirected graph of&nbsp;`` n ``&nbsp;nodes&nbsp;and 3 types of edges:

*   Type 1: Can be traversed by Alice only.
*   Type 2: Can be traversed by Bob only.
*   Type 3: Can by traversed by both Alice and Bob.

Given an array&nbsp;`` edges ``&nbsp;where&nbsp;<code>edges[i] = [type<sub>i</sub>, u<sub>i</sub>, v<sub>i</sub>]</code>&nbsp;represents a bidirectional edge of type&nbsp;<code>type<sub>i</sub></code>&nbsp;between nodes&nbsp;<code>u<sub>i</sub></code>&nbsp;and&nbsp;<code>v<sub>i</sub></code>, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return _the maximum number of edges you can remove, or return_ `` -1 `` _if it's impossible for the graph to be fully traversed by Alice and Bob._

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/ex1.png" style="width: 179px; height: 191px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
<strong>Output:</strong> 2
<strong>Explanation: </strong>If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/ex2.png" style="width: 178px; height: 190px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
<strong>Output:</strong> 0
<strong>Explanation: </strong>Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/ex3.png" style="width: 178px; height: 190px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
<strong>Output:</strong> -1
<b>Explanation: </b>In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.</pre>

&nbsp;
&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^5 ``
*   `` 1 &lt;= edges.length &lt;= min(10^5, 3 * n * (n-1) / 2) ``
*   `` edges[i].length == 3 ``
*   `` 1 &lt;= edges[i][0] &lt;= 3 ``
*   `` 1 &lt;= edges[i][1] &lt; edges[i][2] &lt;= n ``
*   All tuples&nbsp;<code>(type<sub>i</sub>, u<sub>i</sub>, v<sub>i</sub>)</code>&nbsp;are distinct.