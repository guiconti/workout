Given the `` root `` of a binary tree, _determine if it is a valid binary search tree (BST)_.

A __valid BST__ is defined as follows:

*   The left subtree of a node contains only nodes with keys __less than__ the node's key.
*   The right subtree of a node contains only nodes with keys __greater than__ the node's key.
*   Both the left and right subtrees must also be binary search trees.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;"/>

<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;"/>

<pre>
<strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code>