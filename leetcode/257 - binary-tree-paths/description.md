Given the `` root `` of a binary tree, return _all root-to-leaf paths in __any order___.

A __leaf__ is a node with no children.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,null,5]
<strong>Output:</strong> ["1-&gt;2-&gt;5","1-&gt;3"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> ["1"]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 100] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``