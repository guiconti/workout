Given the `` root `` of a binary tree and an integer `` targetSum ``, return `` true `` if the tree has a __root-to-leaf__ path such that adding up all the values along the path equals `` targetSum ``.

A __leaf__ is a node with no children.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;"/>

<pre>
<strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>Output:</strong> true
</pre>

__Example 2:__

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

<pre>
<strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1,2], targetSum = 0
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 5000] ``.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``
*   `` -1000 &lt;= targetSum &lt;= 1000 ``