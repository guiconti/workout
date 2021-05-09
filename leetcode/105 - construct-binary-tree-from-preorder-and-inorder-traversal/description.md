Given two integer arrays `` preorder `` and `` inorder `` where `` preorder `` is the preorder traversal of a binary tree and `` inorder `` is the inorder traversal of the same tree, construct and return _the binary tree_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;"/>

<pre>
<strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= preorder.length &lt;= 3000 ``
*   `` inorder.length == preorder.length ``
*   `` -3000 &lt;= preorder[i], inorder[i] &lt;= 3000 ``
*   `` preorder `` and `` inorder `` consist of __unique__ values.
*   Each value of `` inorder `` also appears in `` preorder ``.
*   `` preorder `` is __guaranteed__ to be the preorder traversal of the tree.
*   `` inorder `` is __guaranteed__ to be the inorder traversal of the tree.