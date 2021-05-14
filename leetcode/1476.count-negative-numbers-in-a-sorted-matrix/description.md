Given a `` m x n `` matrix `` grid `` which is sorted in non-increasing order both row-wise and column-wise, return _the number of __negative__ numbers in_ `` grid ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 negatives number in the matrix.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[3,2],[1,0]]
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,-1],[-1,-1]]
<strong>Output:</strong> 3
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[-1]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m, n &lt;= 100 ``
*   `` -100 &lt;= grid[i][j] &lt;= 100 ``

&nbsp;
__Follow up:__ Could you find an `` O(n + m) `` solution?