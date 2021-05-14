Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `` n `` nodes numbered from `` 0 `` to `` n - 1 `` and exactly `` n - 1 `` `` edges ``. The __root__ of the tree is the node `` 0 ``, and each node of the tree has __a label__ which is a lower-case character given in the string `` labels `` (i.e. The node with the number `` i `` has the label `` labels[i] ``).

The `` edges `` array is given on the form <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>, which means there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.

Return _an array of size `` n ``_ where `` ans[i] `` is the number of nodes in the subtree of the&nbsp;<code>i<sup>th</sup></code>&nbsp;node which have the same label as node `` i ``.

A&nbsp;subtree&nbsp;of a tree&nbsp;`` T `` is the tree consisting of a node in `` T `` and all of its descendant&nbsp;nodes.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/q3e1.jpg" style="width: 441px; height: 321px;"/>

<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
<strong>Output:</strong> [2,1,1,1,1,1,1]
<strong>Explanation:</strong> Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/q3e2.jpg" style="width: 381px; height: 321px;"/>

<pre>
<strong>Input:</strong> n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
<strong>Output:</strong> [4,2,1,1]
<strong>Explanation:</strong> The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/q3e3.jpg" style="width: 381px; height: 321px;"/>

<pre>
<strong>Input:</strong> n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
<strong>Output:</strong> [3,2,1,1,1]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
<strong>Output:</strong> [1,2,1,1,2,1]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
<strong>Output:</strong> [6,5,4,1,3,2,1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^5 ``
*   `` edges.length == n - 1 ``
*   `` edges[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub>,&nbsp;b<sub>i</sub> &lt; n</code>
*   <code>a<sub>i</sub> !=&nbsp;b<sub>i</sub></code>
*   `` labels.length == n ``
*   `` labels `` is consisting of only of lower-case English letters.