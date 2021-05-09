Given the `` root `` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a _binary search tree_ is a tree that satisfies these constraints:

*   The left subtree of a node contains only nodes with keys&nbsp;__less than__&nbsp;the node's key.
*   The right subtree of a node contains only nodes with keys&nbsp;__greater than__&nbsp;the node's key.
*   Both the left and right subtrees must also be binary search trees.

__Note:__ This question is the same as 538:&nbsp;<https://leetcode.com/problems/convert-bst-to-greater-tree/>

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/02/tree.png" style="width: 550px; height: 375px;"/>

<pre>
<strong>Input:</strong> root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
<strong>Output:</strong> [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [0,null,1]
<strong>Output:</strong> [1,null,1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1,0,2]
<strong>Output:</strong> [3,3,2]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [3,2,4,1]
<strong>Output:</strong> [7,9,4,10]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 100] ``.
*   `` 0 &lt;= Node.val &lt;= 100 ``
*   All the values in the tree are __unique__.
*   `` root `` is guaranteed to be a valid binary search tree.