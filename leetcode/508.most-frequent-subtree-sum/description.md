Given the `` root `` of a binary tree, return the most frequent __subtree sum__. If there is a tie, return all the values with the highest frequency in any order.

The __subtree sum__ of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg" style="width: 207px; height: 183px;"/>

<pre>
<strong>Input:</strong> root = [5,2,-3]
<strong>Output:</strong> [2,-3,4]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg" style="width: 207px; height: 183px;"/>

<pre>
<strong>Input:</strong> root = [5,2,-5]
<strong>Output:</strong> [2]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code>