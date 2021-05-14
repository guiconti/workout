Given an integer `` n ``, return _all the structurally unique __BST'__s (binary search trees), which has exactly _`` n ``_ nodes of unique values from_ `` 1 `` _to_ `` n ``. Return the answer in __any order__.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;"/>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[1]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 8 ``