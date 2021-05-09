Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

__Note:__&nbsp;A leaf is a node with no children.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [2,null,3,null,4,null,5,null,6]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 10<sup>5</sup>]</code>.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``