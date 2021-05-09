Given the `` root `` of a binary tree, return the sum of all left leaves.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" style="width: 277px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 24
<strong>Explanation:</strong> There are two left leaves in the binary tree, with values 9 and 15 respectively.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 1000] ``.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``