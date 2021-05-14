Given an `` m x n `` `` matrix ``, return&nbsp;_`` true ``&nbsp;if the matrix is Toeplitz. Otherwise, return `` false ``._

A matrix is __Toeplitz__ if every diagonal from top-left to bottom-right has the same elements.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg" style="width: 322px; height: 242px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong>
In the above grid, the&nbsp;diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg" style="width: 162px; height: 162px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,2],[2,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong>
The diagonal "[1, 2]" has different elements.
</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= m, n &lt;= 20 ``
*   `` 0 &lt;= matrix[i][j] &lt;= 99 ``

&nbsp;

__Follow up:__

*   What if the `` matrix `` is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
*   What if the `` matrix `` is so large that you can only load up a partial row into the memory at once?