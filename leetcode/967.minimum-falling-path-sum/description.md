Given an `` n x n `` array of integers `` matrix ``, return _the __minimum sum__ of any __falling path__ through_ `` matrix ``.

A __falling path__ starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `` (row, col) `` will be `` (row + 1, col - 1) ``, `` (row + 1, col) ``, or `` (row + 1, col + 1) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> There are two falling paths with a minimum sum underlined below:
[[2,<u>1</u>,3],      [[2,<u>1</u>,3],
 [6,<u>5</u>,4],       [6,5,<u>4</u>],
 [<u>7</u>,8,9]]       [7,<u>8</u>,9]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = [[-19,57],[-40,-5]]
<strong>Output:</strong> -59
<strong>Explanation:</strong> The falling path with a minimum sum is underlined below:
[[<u>-19</u>,57],
 [<u>-40</u>,-5]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[-48]]
<strong>Output:</strong> -48
</pre>

&nbsp;

__Constraints:__

*   `` n == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` -100 &lt;= matrix[i][j] &lt;= 100 ``