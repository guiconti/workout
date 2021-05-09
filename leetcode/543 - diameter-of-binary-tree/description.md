Given the `` root `` of a binary tree, return _the length of the __diameter__ of the tree_.

The __diameter__ of a binary tree is the __length__ of the longest path between any two nodes in a tree. This path may or may not pass through the `` root ``.

The __length__ of a path between two nodes is represented by the number of edges between them.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   `` -100 &lt;= Node.val &lt;= 100 ``