You are given the `` root `` of a binary search tree (BST) and an integer `` val ``.

Find the node in the BST that the node's value equals `` val `` and return the subtree rooted with that node. If such a node does not exist, return `` null ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" style="width: 422px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 2
<strong>Output:</strong> [2,1,3]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" style="width: 422px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 5000] ``.
*   <code>1 &lt;= Node.val &lt;= 10<sup>7</sup></code>
*   `` root `` is a binary search tree.
*   <code>1 &lt;= val &lt;= 10<sup>7</sup></code>