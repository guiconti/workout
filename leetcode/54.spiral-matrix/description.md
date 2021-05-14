Given an `` m x n `` `` matrix ``, return _all elements of the_ `` matrix `` _in spiral order_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= m, n &lt;= 10 ``
*   `` -100 &lt;= matrix[i][j] &lt;= 100 ``