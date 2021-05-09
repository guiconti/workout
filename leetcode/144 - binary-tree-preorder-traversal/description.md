Given the `` root `` of a binary tree, return _the preorder traversal of its nodes' values_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,2,3]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg" style="width: 202px; height: 202px;"/>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> [1,2]
</pre>

__Example 5:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg" style="width: 202px; height: 202px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> [1,2]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 100] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``

&nbsp;

__Follow up:__ Recursive solution is trivial, could you do it iteratively?