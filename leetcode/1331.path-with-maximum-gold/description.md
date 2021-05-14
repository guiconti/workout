In a gold mine `` grid `` of size `` m x n ``, each cell in this mine has an integer representing the amount of gold in that cell, `` 0 `` if it is empty.

Return the maximum amount of gold you can collect under the conditions:

*   Every time you are located in a cell you will collect all the gold in that cell.
*   From your position, you can walk one step to the left, right, up, or down.
*   You can't visit the same cell more than once.
*   Never visit a cell with `` 0 `` gold.
*   You can start and stop collecting gold from __any __position in the grid that has some gold.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> grid = [[0,6,0],[5,8,7],[0,9,0]]
<strong>Output:</strong> 24
<strong>Explanation:</strong>
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -&gt; 8 -&gt; 7.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
<strong>Output:</strong> 28
<strong>Explanation:</strong>
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 7.
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m, n &lt;= 15 ``
*   `` 0 &lt;= grid[i][j] &lt;= 100 ``
*   There are at most __25 __cells containing gold.