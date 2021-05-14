Given the `` head `` of a singly linked list where elements are __sorted in ascending order__, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of _every_ node never differ by more than 1.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/linked.jpg" style="width: 600px; height: 466px;"/>

<pre>
<strong>Input:</strong> head = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [0]
<strong>Output:</strong> [0]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> head = [1,3]
<strong>Output:</strong> [3,1]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in `` head `` is in the range <code>[0, 2 * 10<sup>4</sup>]</code>.
*   `` -10^5 &lt;= Node.val &lt;= 10^5 ``