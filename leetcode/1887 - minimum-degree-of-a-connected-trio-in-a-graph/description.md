You are given an undirected graph. You are given an integer `` n `` which is the number of nodes in the graph and an array `` edges ``, where each <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that there is an undirected edge between <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.

A __connected trio__ is a set of __three__ nodes where there is an edge between __every__ pair of them.

The __degree of a connected trio__ is the number of edges where one endpoint is in the trio, and the other is not.

Return _the __minimum__ degree of a connected trio in the graph, or_ `` -1 `` _if the graph has no connected trios._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/26/trios1.png" style="width: 388px; height: 164px;"/>

<pre>
<strong>Input:</strong> n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/26/trios2.png" style="width: 388px; height: 164px;"/>

<pre>
<strong>Input:</strong> n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 400 ``
*   `` edges[i].length == 2 ``
*   `` 1 &lt;= edges.length &lt;= n * (n-1) / 2 ``
*   <code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code>
*   <code>u<sub>i </sub>!= v<sub>i</sub></code>
*   There are no repeated edges.