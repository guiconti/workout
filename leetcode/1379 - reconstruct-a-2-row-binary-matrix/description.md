Given the following details of a matrix with `` n `` columns and `` 2 `` rows :

*   The matrix is a binary matrix, which means each element in the matrix can be `` 0 `` or `` 1 ``.
*   The sum of elements of the 0-th(upper) row is given as `` upper ``.
*   The sum of elements of the 1-st(lower) row is given as `` lower ``.
*   The sum of elements in the i-th column(0-indexed) is `` colsum[i] ``, where `` colsum `` is given as an integer array with length `` n ``.

Your task is to reconstruct the matrix with `` upper ``, `` lower `` and `` colsum ``.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> upper = 2, lower = 1, colsum = [1,1,1]
<strong>Output:</strong> [[1,1,0],[0,0,1]]
<strong>Explanation: </strong>[[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> upper = 2, lower = 3, colsum = [2,2,1,1]
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
<strong>Output:</strong> [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= colsum.length &lt;= 10^5 ``
*   `` 0 &lt;= upper, lower &lt;= colsum.length ``
*   `` 0 &lt;= colsum[i] &lt;= 2 ``