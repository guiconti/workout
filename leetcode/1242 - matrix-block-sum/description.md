Given a `` m x n `` matrix `` mat `` and an integer `` k ``, return _a matrix_ `` answer `` _where each_ `` answer[i][j] `` _is the sum of all elements_ `` mat[r][c] `` _for_:

*   `` i - k &lt;= r &lt;= i + k, ``
*   `` j - k &lt;= c &lt;= j + k ``, and
*   `` (r, c) `` is a valid position in the matrix.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>Output:</strong> [[12,21,16],[27,45,33],[24,39,28]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
<strong>Output:</strong> [[45,45,45],[45,45,45],[45,45,45]]
</pre>

&nbsp;

__Constraints:__

*   `` m ==&nbsp;mat.length ``
*   `` n ==&nbsp;mat[i].length ``
*   `` 1 &lt;= m, n, k &lt;= 100 ``
*   `` 1 &lt;= mat[i][j] &lt;= 100 ``