Given the `` root `` of a Binary Search Tree and a target number `` k ``, return _`` true `` if there exist two elements in the BST such that their sum is equal to the given target_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="width: 562px; height: 322px;"/>

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 9
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="width: 562px; height: 322px;"/>

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 28
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [2,1,3], k = 4
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [2,1,3], k = 1
<strong>Output:</strong> false
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> root = [2,1,3], k = 3
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>4</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>4</sup></code>
*   `` root `` is guaranteed to be a __valid__ binary search tree.
*   <code>-10<sup>5</sup>&nbsp;&lt;= k &lt;= 10<sup>5</sup></code>