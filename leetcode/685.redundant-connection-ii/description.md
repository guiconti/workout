In this problem, a rooted tree is a __directed__ graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with `` n `` nodes (with distinct values from `` 1 `` to `` n ``), with one additional directed edge added. The added edge has two different vertices chosen from `` 1 `` to `` n ``, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `` edges ``. Each element of `` edges `` is a pair <code>[u<sub>i</sub>, v<sub>i</sub>]</code> that represents a __directed__ edge connecting nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>, where <code>u<sub>i</sub></code> is a parent of child <code>v<sub>i</sub></code>.

Return _an edge that can be removed so that the resulting graph is a rooted tree of_ `` n `` _nodes_. If there are multiple answers, return the answer that occurs last in the given 2D-array.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg" style="width: 222px; height: 222px;"/>

<pre>
<strong>Input:</strong> edges = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> [2,3]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg" style="width: 222px; height: 382px;"/>

<pre>
<strong>Input:</strong> edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
<strong>Output:</strong> [4,1]
</pre>

&nbsp;

__Constraints:__

*   `` n == edges.length ``
*   `` 3 &lt;= n &lt;= 1000 ``
*   `` edges[i].length == 2 ``
*   <code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code>
*   <code>u<sub>i</sub> != v<sub>i</sub></code>