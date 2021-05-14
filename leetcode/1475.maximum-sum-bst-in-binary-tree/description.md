Given a __binary tree__ `` root ``, the task is to return the maximum sum of all keys of __any__&nbsp;sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

*   The left subtree of a node contains only nodes with keys&nbsp;__less than__&nbsp;the node's key.
*   The right subtree of a node contains only nodes with keys&nbsp;__greater than__&nbsp;the node's key.
*   Both the left and right subtrees must also be binary search trees.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/30/sample_1_1709.png" style="width: 320px; height: 250px;"/>

<pre>
<strong>Input:</strong> root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
<strong>Output:</strong> 20
<strong>Explanation:</strong> Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/30/sample_2_1709.png" style="width: 134px; height: 180px;"/>

<pre>
<strong>Input:</strong> root = [4,3,null,1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [-4,-2,-5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All values are negatives. Return an empty BST.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> 6
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> root = [5,4,8,3,null,6,3]
<strong>Output:</strong> 7
</pre>

&nbsp;

__Constraints:__

*   The&nbsp;given binary tree will have between&nbsp;`` 1 ``&nbsp;and&nbsp;`` 40000 ``&nbsp;nodes.
*   Each node's value is between `` [-4 * 10^4&nbsp;, 4 * 10^4] ``.