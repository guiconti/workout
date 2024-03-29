Given an integer array `` nums `` where the elements are sorted in __ascending order__, convert _it to a __height-balanced__ binary search tree_.

A __height-balanced__ binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;"/>

<pre>
<strong>Input:</strong> nums = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> [0,-10,5,null,-3,null,9] is also accepted:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;"/>
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;"/>

<pre>
<strong>Input:</strong> nums = [1,3]
<strong>Output:</strong> [3,1]
<strong>Explanation:</strong> [1,3] and [3,1] are both a height-balanced BSTs.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` nums `` is sorted in a __strictly increasing__ order.