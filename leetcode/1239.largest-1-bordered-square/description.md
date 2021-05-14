Given a 2D `` grid `` of `` 0 ``s and `` 1 ``s, return the number of elements in&nbsp;the largest __square__&nbsp;subgrid that has all `` 1 ``s on its __border__, or `` 0 `` if such a subgrid&nbsp;doesn't exist in the `` grid ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> 9
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[1,1,0,0]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= grid.length &lt;= 100 ``
*   `` 1 &lt;= grid[0].length &lt;= 100 ``
*   `` grid[i][j] `` is `` 0 `` or `` 1 ``