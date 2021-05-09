Given a _m_ x _n_ `` grid ``. Each cell of the `` grid `` represents a street. The street of&nbsp;`` grid[i][j] `` can be:

*   __1__ which means a street connecting the left cell and the right cell.
*   __2__ which means a street connecting the upper cell and the lower cell.
*   __3__&nbsp;which means a street connecting the left cell and the lower cell.
*   __4__ which means a street connecting the right cell and the lower cell.
*   __5__ which means a street connecting the left cell and the upper cell.
*   __6__ which means a street connecting the right cell and the upper cell.

<img alt="" src="https://assets.leetcode.com/uploads/2020/03/05/main.png" style="width: 450px; height: 708px;"/>

You will initially start at the street of the&nbsp;upper-left cell `` (0,0) ``. A valid path in the grid is a path which starts from the upper left&nbsp;cell `` (0,0) `` and ends at the bottom-right&nbsp;cell `` (m - 1, n - 1) ``. __The path should only follow the streets__.

__Notice__ that you are __not allowed__ to change any street.

Return _true_&nbsp;if there is a valid path in the grid or _false_ otherwise.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/03/05/e1.png" style="width: 455px; height: 311px;"/>

<pre>
<strong>Input:</strong> grid = [[2,4,3],[6,5,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong> As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/03/05/e2.png" style="width: 455px; height: 293px;"/>

<pre>
<strong>Input:</strong> grid = [[1,2,1],[1,2,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,1,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,3]]
<strong>Output:</strong> true
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> grid = [[2],[2],[2],[2],[2],[2],[6]]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m, n &lt;= 300 ``
*   `` 1 &lt;= grid[i][j] &lt;= 6 ``