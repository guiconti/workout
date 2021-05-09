You are given a&nbsp;`` rows x cols ``&nbsp;matrix&nbsp;`` grid ``.&nbsp;Initially, you&nbsp;are located at the top-left&nbsp;corner `` (0, 0) ``,&nbsp;and in each step, you can only __move right&nbsp;or&nbsp;down__ in the matrix.

Among all possible paths starting from the top-left corner&nbsp;`` (0, 0) ``&nbsp;and ending in the bottom-right corner&nbsp;`` (rows - 1, cols - 1) ``, find the path with the&nbsp;__maximum non-negative product__. The product of a path is the product of all integers in the grid cells visited along the path.

Return the&nbsp;_maximum non-negative product&nbsp;__modulo__&nbsp;_<code>10<sup>9</sup>&nbsp;+ 7</code>.&nbsp;_If the maximum product is __negative__ return&nbsp;_`` -1 ``.

__Notice that the modulo is performed after getting the maximum product.__

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> grid = [[-1,-2,-3],
&nbsp;              [-2,-3,-3],
&nbsp;              [-3,-3,-2]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[<strong>1</strong>,-2,1],
&nbsp;              [<strong>1</strong>,<strong>-2</strong>,1],
&nbsp;              [3,<strong>-4</strong>,<strong>1</strong>]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[<strong>1</strong>, 3],
&nbsp;              [<strong>0</strong>,<strong>-4</strong>]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Maximum non-negative product is in bold (1 * 0 * -4 = 0).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[ <strong>1</strong>, 4,4,0],
&nbsp;              [<strong>-2</strong>, 0,0,1],
&nbsp;              [ <strong>1</strong>,<strong>-1</strong>,<strong>1</strong>,<strong>1</strong>]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= rows, cols &lt;= 15 ``
*   `` -4 &lt;= grid[i][j] &lt;= 4 ``