Given a _m_ x _n_ `` grid ``. Each cell of the `` grid `` has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of `` grid[i][j] `` can be:

*   __1__ which means go to the cell to the right. (i.e go from `` grid[i][j] `` to `` grid[i][j + 1] ``)
*   __2__ which means go to the cell to the left. (i.e go from `` grid[i][j] `` to `` grid[i][j - 1] ``)
*   __3__ which means go to the lower cell. (i.e go from `` grid[i][j] `` to `` grid[i + 1][j] ``)
*   __4__ which means go to the upper cell. (i.e go from `` grid[i][j] `` to `` grid[i - 1][j] ``)

Notice&nbsp;that there could be some __invalid signs__ on the cells of the `` grid `` which points outside the `` grid ``.

You will initially start at the upper left cell `` (0,0) ``. A valid path in the grid is a path which starts from the upper left&nbsp;cell `` (0,0) `` and ends at the bottom-right&nbsp;cell `` (m - 1, n - 1) `` following the signs on the grid. The valid path __doesn't have to be the shortest__.

You can modify the sign on a cell with `` cost = 1 ``. You can modify the sign on a cell __one time only__.

Return _the minimum cost_ to make the grid have at least one valid path.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/13/grid1.png" style="width: 542px; height: 528px;"/>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --&gt; (0, 1) --&gt; (0, 2) --&gt; (0, 3) change the arrow to down with cost = 1 --&gt; (1, 3) --&gt; (1, 2) --&gt; (1, 1) --&gt; (1, 0) change the arrow to down with cost = 1 --&gt; (2, 0) --&gt; (2, 1) --&gt; (2, 2) --&gt; (2, 3) change the arrow to down with cost = 1 --&gt; (3, 3)
The total cost = 3.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/13/grid2.png" style="width: 419px; height: 408px;"/>

<pre>
<strong>Input:</strong> grid = [[1,1,3],[3,2,2],[1,1,4]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You can follow the path from (0, 0) to (2, 2).
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/13/grid3.png" style="width: 314px; height: 302px;"/>

<pre>
<strong>Input:</strong> grid = [[1,2],[4,3]]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[2,2,2],[2,2,2]]
<strong>Output:</strong> 3
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> grid = [[4]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m, n &lt;= 100 ``