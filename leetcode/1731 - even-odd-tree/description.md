A binary tree is named __Even-Odd__ if it meets the following conditions:

*   The root of the binary tree is at level index `` 0 ``, its children are at level index `` 1 ``, their children are at level index `` 2 ``, etc.
*   For every __even-indexed__ level, all nodes at the level have __odd__ integer values in __strictly increasing__ order (from left to right).
*   For every __odd-indexed__ level, all nodes at the level have __even__ integer values in __strictly decreasing__ order (from left to right).

Given the `` root `` of a binary tree, _return _`` true ``_ if the binary tree is __Even-Odd__, otherwise return _`` false ``_._

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/sample_1_1966.png" style="width: 362px; height: 229px;"/></strong>

<pre>
<strong>Input:</strong> root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/sample_2_1966.png" style="width: 363px; height: 167px;"/></strong>

<pre>
<strong>Input:</strong> root = [5,4,2,3,3,7]
<strong>Output:</strong> false
<strong>Explanation:</strong> The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in the level 2 must be in strictly increasing order, so the tree is not Even-Odd.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/22/sample_1_333_1966.png" style="width: 363px; height: 167px;"/>

<pre>
<strong>Input:</strong> root = [5,9,1,3,5,7]
<strong>Output:</strong> false
<strong>Explanation:</strong> Node values in the level 1 should be even integers.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> true
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.
*   <code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code>