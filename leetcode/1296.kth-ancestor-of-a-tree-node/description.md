You are given a tree with&nbsp;`` n ``&nbsp;nodes numbered from&nbsp;`` 0 ``&nbsp;to&nbsp;`` n-1 ``&nbsp;in the form of a parent array where `` parent[i] ``&nbsp;is the parent of node `` i ``. The root of the tree is node `` 0 ``.

Implement the function&nbsp;`` getKthAncestor ```` (int node, int k) ``&nbsp;to return the `` k ``-th ancestor of the given&nbsp;`` node ``. If there is no such ancestor, return&nbsp;`` -1 ``.

The&nbsp;_k-th&nbsp;__ancestor_&nbsp;of a tree node is the `` k ``-th node&nbsp;in the path&nbsp;from that node to the root.

&nbsp;

__Example:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/08/28/1528_ex1.png" style="width: 396px; height: 262px;"/></strong>

<pre>
<b>Input:</b>
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

<b>Output:</b>
[null,1,0,-1]

<b>Explanation:</b>
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;=&nbsp;n &lt;= 5*10^4 ``
*   `` parent[0] == -1 ``&nbsp;indicating that&nbsp;`` 0 ``&nbsp;is the root node.
*   `` 0 &lt;= parent[i] &lt; n ``&nbsp;for all&nbsp;`` 0 &lt;&nbsp;i &lt; n ``
*   `` 0 &lt;= node &lt; n ``
*   There will be at most `` 5*10^4 `` queries.