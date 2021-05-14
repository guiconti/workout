Given the `` root `` of a binary tree, return _the length of the longest path, where each node in the path has the same value_. This path may or may not pass through the root.

__The length of the path__ between two nodes is represented by the number of edges between them.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg" style="width: 571px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [5,4,5,1,1,5]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg" style="width: 571px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [1,4,5,4,4,5]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``
*   The depth of the tree will not exceed `` 1000 ``.