Given a `` rows x cols ``&nbsp;binary `` matrix `` filled with `` 0 ``'s and `` 1 ``'s, find the largest rectangle containing only `` 1 ``'s and return _its area_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;"/>

<pre>
<strong>Input:</strong> matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The maximal rectangle is shown in the above picture.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = []
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [["0"]]
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> matrix = [["1"]]
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> matrix = [["0","0"]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` rows == matrix.length ``
*   `` cols == matrix[i].length ``
*   `` 0 &lt;= row, cols &lt;= 200 ``
*   `` matrix[i][j] `` is `` '0' `` or `` '1' ``.