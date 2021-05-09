Given two integer arrays `` inorder `` and `` postorder `` where `` inorder `` is the inorder traversal of a binary tree and `` postorder `` is the postorder traversal of the same tree, construct and return _the binary tree_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;"/>

<pre>
<strong>Input:</strong> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> inorder = [-1], postorder = [-1]
<strong>Output:</strong> [-1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= inorder.length &lt;= 3000 ``
*   `` postorder.length == inorder.length ``
*   `` -3000 &lt;= inorder[i], postorder[i] &lt;= 3000 ``
*   `` inorder `` and `` postorder `` consist of __unique__ values.
*   Each value of `` postorder `` also appears in `` inorder ``.
*   `` inorder `` is __guaranteed__ to be the inorder traversal of the tree.
*   `` postorder `` is __guaranteed__ to be the postorder traversal of the tree.