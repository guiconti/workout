Given the `` root `` of a binary tree, imagine yourself standing on the __right side__ of it, return _the values of the nodes you can see ordered from top to bottom_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/14/tree.jpg" style="width: 401px; height: 301px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,null,5,null,4]
<strong>Output:</strong> [1,3,4]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1,null,3]
<strong>Output:</strong> [1,3]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 100] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``