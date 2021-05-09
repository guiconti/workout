You are given the `` root `` of a binary tree with `` n `` nodes where each `` node `` in the tree has `` node.val `` coins and there are `` n `` coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another. (A move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree1.png" style="width: 150px; height: 142px;"/>

<pre>
<strong>Input:</strong> root = [3,0,0]
<strong>Output:</strong> 2
<strong>Explanation: </strong>From the root of the tree, we move one coin to its left child, and one coin to its right child.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree2.png" style="width: 150px; height: 142px;"/>

<pre>
<strong>Input:</strong> root = [0,3,0]
<strong>Output:</strong> 3
<strong>Explanation: </strong>From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree3.png" style="width: 150px; height: 142px;"/>

<pre>
<strong>Input:</strong> root = [1,0,2]
<strong>Output:</strong> 2
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/18/tree4.png" style="width: 155px; height: 156px;"/>

<pre>
<strong>Input:</strong> root = [1,0,0,null,3]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is `` n ``.
*   `` 1 &lt;= n &lt;= 100 ``
*   `` 0 &lt;= Node.val &lt;= n ``
*   The sum of `` Node.val `` is `` n ``.