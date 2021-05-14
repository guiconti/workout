Given a binary tree `` root `` and a&nbsp;linked list with&nbsp;`` head ``&nbsp;as the first node.&nbsp;

Return True if all the elements in the linked list starting from the `` head `` correspond to some _downward path_ connected in the binary tree&nbsp;otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png" style="width: 220px; height: 280px;"/></strong>

<pre>
<strong>Input:</strong> head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> Nodes in blue form a subpath in the binary Tree.  
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/sample_2_1720.png" style="width: 220px; height: 280px;"/></strong>

<pre>
<strong>Input:</strong> head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong>Output:</strong> true
</pre>

__Example 3:__

<strong>Input:</strong> head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    <strong>Output:</strong> false
    <strong>Explanation:</strong> There is no path in the binary tree that contains all the elements of the linked list from head.

&nbsp;

__Constraints:__

*   The number of nodes in the tree will be in the range `` [1, 2500] ``.
*   The number of nodes in the list will be in the range `` [1, 100] ``.
*   `` 1 &lt;= Node.val&nbsp;&lt;= 100 ``&nbsp;for each node in the linked list and binary tree.