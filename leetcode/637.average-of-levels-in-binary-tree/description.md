Given the `` root `` of a binary tree, return _the average value of the nodes on each level in the form of an array_. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.
&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg" style="width: 277px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,null,15,7]
<strong>Output:</strong> [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg" style="width: 292px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,15,7]
<strong>Output:</strong> [3.00000,14.50000,11.00000]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code>