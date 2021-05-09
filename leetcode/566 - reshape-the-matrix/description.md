In MATLAB, there is a handy function called `` reshape ``&nbsp;which can reshape an `` m x n `` matrix into a new one with a different size `` r x c ``&nbsp;keeping its original data.

You are given an `` m x n ``&nbsp;matrix `` mat `` and two integers `` r `` and `` c `` representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the `` reshape ``&nbsp;operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg" style="width: 613px; height: 173px;"/>

<pre>
<strong>Input:</strong> mat = [[1,2],[3,4]], r = 1, c = 4
<strong>Output:</strong> [[1,2,3,4]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg" style="width: 453px; height: 173px;"/>

<pre>
<strong>Input:</strong> mat = [[1,2],[3,4]], r = 2, c = 4
<strong>Output:</strong> [[1,2],[3,4]]
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   `` 1 &lt;= m, n &lt;= 100 ``
*   `` -1000 &lt;= mat[i][j] &lt;= 1000 ``
*   `` 1 &lt;= r, c &lt;= 300 ``