There is a strange printer with the following two special requirements:

*   On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
*   Once the printer has used a color for the above operation, __the same color cannot be used again__.

You are given a `` m x n `` matrix `` targetGrid ``, where `` targetGrid[row][col] `` is the color in the position `` (row, col) `` of the grid.

Return `` true ``_ if it is possible to print the matrix _`` targetGrid ``_,__ otherwise, return _`` false ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/sample_1_1929.png" style="width: 483px; height: 138px;"/>

<pre>
<strong>Input:</strong> targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/sample_2_1929.png" style="width: 483px; height: 290px;"/>

<pre>
<strong>Input:</strong> targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to form targetGrid because it is not allowed to print the same color in different turns.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> targetGrid = [[1,1,1],[3,1,3]]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` m == targetGrid.length ``
*   `` n == targetGrid[i].length ``
*   `` 1 &lt;= m, n &lt;= 60 ``
*   `` 1 &lt;= targetGrid[row][col] &lt;= 60 ``