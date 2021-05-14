Given a 2D matrix `` matrix ``, handle multiple queries of the following type:

1.   Calculate the __sum__ of the elements of `` matrix `` inside the rectangle defined by its __upper left corner__ `` (row1, col1) `` and __lower right corner__ `` (row2, col2) ``.

Implement the NumMatrix class:

*   `` NumMatrix(int[][] matrix) `` Initializes the object with the integer matrix `` matrix ``.
*   `` int sumRegion(int row1, int col1, int row2, int col2) `` Returns the __sum__ of the elements of `` matrix `` inside the rectangle defined by its __upper left corner__ `` (row1, col1) `` and __lower right corner__ `` (row2, col2) ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg" style="width: 415px; height: 415px;"/>

<pre>
<strong>Input</strong>
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
<strong>Output</strong>
[null, 8, 11, 12]

<strong>Explanation</strong>
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   <code>-10<sup>5</sup> &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= row1 &lt;= row2 &lt; m ``
*   `` 0 &lt;= col1 &lt;= col2 &lt; n ``
*   At most <code>10<sup>4</sup></code> calls will be made to `` sumRegion ``.