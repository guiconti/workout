You are given a binary matrix `` matrix `` of size `` m x n ``, and you are allowed to rearrange the __columns__ of the `` matrix `` in any order.

Return _the area of the largest submatrix within _`` matrix ``_ where __every__ element of the submatrix is _`` 1 ``_ after reordering the columns optimally._

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png" style="width: 300px; height: 144px;"/></strong>

<pre>
<strong>Input:</strong> matrix = [[0,0,1],[1,1,1],[1,0,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png" style="width: 500px; height: 62px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,0,1,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[1,1,0],[1,0,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> matrix = [[0,0],[0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> As there are no 1s, no submatrix of 1s can be formed and the area is 0.</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   <code>1 &lt;= m * n &lt;= 10<sup>5</sup></code>
*   `` matrix[i][j] `` is `` 0 `` or `` 1 ``.