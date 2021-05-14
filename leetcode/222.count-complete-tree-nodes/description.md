Given the `` root `` of a __complete__ binary tree, return the number of the nodes in the tree.

According to __<a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>__, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `` 1 `` and <code>2<sup>h</sup></code> nodes inclusive at the last level `` h ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> 6
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.
*   <code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code>
*   The tree is guaranteed to be __complete__.

&nbsp;
__Follow up:__ Traversing the tree to count the number of nodes in the tree is an easy solution but with `` O(n) `` complexity. Could you find a faster algorithm?