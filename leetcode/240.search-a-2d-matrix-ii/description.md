Write an efficient algorithm that searches for a `` target `` value in an `` m x n `` integer `` matrix ``. The `` matrix `` has the following properties:

*   Integers in each row are sorted in ascending from left to right.
*   Integers in each column are sorted in ascending from top to bottom.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg" style="width: 300px; height: 300px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg" style="width: 300px; height: 300px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= n, m &lt;= 300 ``
*   <code>-10<sup>9</sup> &lt;= matix[i][j] &lt;= 10<sup>9</sup></code>
*   All the integers in each row are __sorted__ in ascending order.
*   All the integers in each column are __sorted__ in ascending order.
*   <code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code>