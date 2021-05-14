Given the `` root `` of a binary tree and an integer `` targetSum ``, return all __root-to-leaf__ paths where each path's sum equals `` targetSum ``.

A __leaf__ is a node with no children.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;"/>

<pre>
<strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>Output:</strong> [[5,4,11,2],[5,8,4,5]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1,2], targetSum = 0
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 5000] ``.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``
*   `` -1000 &lt;= targetSum &lt;= 1000 ``