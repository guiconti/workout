You have a `` grid `` of size `` n x 3 `` and you want to paint each cell of the grid with exactly one of the three colors: __Red__, __Yellow,__ or __Green__ while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given `` n `` the number of rows of the grid, return _the number of ways_ you can paint this `` grid ``. As the answer may grow large, the answer __must be__ computed modulo <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/03/26/e1.png" style="width: 400px; height: 257px;"/>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 12
<strong>Explanation:</strong> There are 12 possible way to paint the grid as shown.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 54
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 246
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 106494
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 5000
<strong>Output:</strong> 30228214
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` grid[i].length == 3 ``
*   `` 1 &lt;= n &lt;= 5000 ``