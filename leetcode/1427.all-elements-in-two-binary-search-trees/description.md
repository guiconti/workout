Given two binary search trees `` root1 `` and `` root2 ``.

Return a list containing _all the integers_ from _both trees_ sorted in __ascending__ order.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/q2-e1.png" style="width: 457px; height: 207px;"/>

<pre>
<strong>Input:</strong> root1 = [2,1,4], root2 = [1,0,3]
<strong>Output:</strong> [0,1,1,2,3,4]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root1 = [0,-10,10], root2 = [5,1,7,0,2]
<strong>Output:</strong> [-10,0,0,1,2,5,7,10]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root1 = [], root2 = [5,1,7,0,2]
<strong>Output:</strong> [0,1,2,5,7]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root1 = [0,-10,10], root2 = []
<strong>Output:</strong> [-10,0,10]
</pre>

__Example 5:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/q2-e5-.png" style="width: 352px; height: 197px;"/>

<pre>
<strong>Input:</strong> root1 = [1,null,8], root2 = [8,1]
<strong>Output:</strong> [1,1,8,8]
</pre>

&nbsp;

__Constraints:__

*   Each tree has at most `` 5000 `` nodes.
*   Each node's value is between `` [-10^5, 10^5] ``.