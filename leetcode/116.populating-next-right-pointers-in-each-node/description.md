You are given a __perfect binary tree__&nbsp;where&nbsp;all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

<pre>
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `` NULL ``.

Initially, all next pointers are set to `` NULL ``.

&nbsp;

__Follow up:__

*   You may only use constant extra space.
*   Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="width: 640px; height: 218px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7]
<strong>Output:</strong> [1,#,2,3,#,4,5,6,7,#]
<strong>Explanation: </strong>Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the given tree is less than `` 4096 ``.
*   `` -1000 &lt;= node.val &lt;= 1000 ``