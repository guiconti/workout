Given the `` root `` of a binary tree, return _the zigzag level order traversal of its nodes' values_. (i.e., from left to right, then right to left for the next level and alternate between).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[20,9],[15,7]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 2000] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``