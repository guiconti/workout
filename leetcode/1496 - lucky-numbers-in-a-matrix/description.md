Given a `` m * n `` matrix of __distinct __numbers, return all lucky numbers in the&nbsp;matrix in __any __order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> matrix = [[3,7,8],[9,11,13],[15,16,17]]
<strong>Output:</strong> [15]
<strong>Explanation:</strong> 15 is the only lucky number since it is the minimum in its row and the maximum in its column
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
<strong>Output:</strong> [12]
<strong>Explanation:</strong> 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[7,8],[1,2]]
<strong>Output:</strong> [7]
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   `` 1 &lt;= n, m &lt;= 50 ``
*   `` 1 &lt;=&nbsp;matrix[i][j]&nbsp;&lt;= 10^5 ``.
*   All elements in the matrix are distinct.