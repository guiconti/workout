Given an `` m x n `` matrix `` mat ``, return _an array of all the elements of the array in a diagonal order_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;"/>

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,4,7,5,3,6,8,9]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[1,2],[3,4]]
<strong>Output:</strong> [1,2,3,4]
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   <code>1 &lt;= m, n &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= m * n &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>5</sup> &lt;= mat[i][j] &lt;= 10<sup>5</sup></code>