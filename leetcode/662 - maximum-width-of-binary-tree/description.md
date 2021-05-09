Given the `` root `` of a binary tree, return _the __maximum width__ of the given tree_.

The __maximum width__ of a tree is the maximum __width__ among all levels.

The __width__ of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is __guaranteed__ that the answer will in the range of __32-bit__ signed integer.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg" style="width: 359px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [1,3,2,5,3,null,9]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The maximum width existing in the third level with the length 4 (5,3,null,9).
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width2-tree.jpg" style="width: 224px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [1,3,null,5,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum width existing in the third level with the length 2 (5,3).
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg" style="width: 289px; height: 299px;"/>

<pre>
<strong>Input:</strong> root = [1,3,2,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum width existing in the second level with the length 2 (3,2).
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width4-tree.jpg" style="width: 500px; height: 244px;"/>

<pre>
<strong>Input:</strong> root = [1,3,2,5,null,null,9,6,null,null,7]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 3000] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``