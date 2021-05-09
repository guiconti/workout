You are given an `` m x n `` binary matrix `` matrix ``.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from `` 0 `` to `` 1 `` or vice versa).

Return _the maximum number of rows that have all values equal after some number of flips_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> matrix = [[0,1],[1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After flipping no values, 1 row has all values equal.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = [[0,1],[1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> After flipping values in the first column, both rows have equal values.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[0,0,0],[0,0,1],[1,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> After flipping values in the first two columns, the last two rows have equal values.
</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= m, n &lt;= 300 ``
*   `` matrix[i][j] `` is either&nbsp;`` 0 `` or `` 1 ``.