Given a `` m x n ``&nbsp;matrix `` mat `` and an integer `` threshold ``. Return the maximum side-length of a square with a sum less than or equal to `` threshold `` or return __0__ if there is no such square.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/05/e1.png" style="width: 335px; height: 186px;"/>

<pre>
<strong>Input:</strong> mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum side length of square with sum less than 4 is 2 as shown.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
<strong>Output:</strong> 3
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= m, n &lt;= 300 ``
*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   `` 0 &lt;= mat[i][j] &lt;= 10000 ``
*   `` 0 &lt;= threshold&nbsp;&lt;= 10^5 ``