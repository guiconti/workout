A tree is an undirected graph in which any two vertices are connected by&nbsp;_exactly_&nbsp;one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `` n `` nodes&nbsp;labelled from `` 0 `` to `` n - 1 ``, and an array of&nbsp;`` n - 1 ``&nbsp;`` edges `` where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an undirected edge between the two nodes&nbsp;<code>a<sub>i</sub></code> and&nbsp;<code>b<sub>i</sub></code> in the tree,&nbsp;you can choose any node of the tree as the root. When you select a node `` x `` as the root, the result tree has height `` h ``. Among all possible rooted trees, those with minimum height (i.e. `` min(h) ``)&nbsp; are called __minimum height trees__ (MHTs).

Return _a list of all __MHTs'__ root labels_.&nbsp;You can return the answer in __any order__.

The __height__ of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e1.jpg" style="width: 800px; height: 213px;"/>

<pre>
<strong>Input:</strong> n = 4, edges = [[1,0],[1,2],[1,3]]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e2.jpg" style="width: 800px; height: 321px;"/>

<pre>
<strong>Input:</strong> n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
<strong>Output:</strong> [3,4]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 1, edges = []
<strong>Output:</strong> [0]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 2, edges = [[0,1]]
<strong>Output:</strong> [0,1]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code>
*   `` edges.length == n - 1 ``
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   All the pairs <code>(a<sub>i</sub>, b<sub>i</sub>)</code> are distinct.
*   The given input is __guaranteed__ to be a tree and there will be __no repeated__ edges.