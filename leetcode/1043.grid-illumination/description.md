There is a 2D `` grid `` of size `` N x N `` where each cell of this grid has a lamp that is initially __turned off__.

You are given a 2D array of lamp positions `` lamps ``, where <code>lamps[i] = [row<sub>i</sub>, col<sub>i</sub>]</code> indicates that the lamp at <code>grid[row<sub>i</sub>][col<sub>i</sub>]</code> is __turned on__. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it __illuminates its cell__ and __all other cells__ in the same __row, column, or diagonal__.

You are also given another 2D array `` queries ``, where <code>queries[j] = [row<sub>j</sub>, col<sub>j</sub>]</code>. For the <code>j<sup>th</sup></code> query, determine whether <code>grid[row<sub>j</sub>][col<sub>j</sub>]</code> is illuminated or not. After answering the <code>j<sup>th</sup></code> query, __turn off__ the lamp at <code>grid[row<sub>j</sub>][col<sub>j</sub>]</code> and its __8 adjacent lamps__ if they exist. A lamp is adjacent if its cell shares either a side or corner with <code>grid[row<sub>j</sub>][col<sub>j</sub>]</code>.

Return _an array of integers _`` ans ``_,__ where _`` ans[j] ``_ should be _`` 1 ``_ if the cell in the _<code>j<sup>th</sup></code>_ query was illuminated, or _`` 0 ``_ if the lamp was not._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg" style="width: 750px; height: 209px;"/>

<pre>
<strong>Input:</strong> N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0<sup>th</sup>&nbsp;query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg" style="width: 500px; height: 218px;"/>
The 1<sup>st</sup>&nbsp;query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg" style="width: 500px; height: 219px;"/>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
<strong>Output:</strong> [1,1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> N = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
<strong>Output:</strong> [1,1,0]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= N &lt;= 10<sup>9</sup></code>
*   `` 0 &lt;= lamps.length &lt;= 20000 ``
*   `` 0 &lt;= queries.length &lt;= 20000 ``
*   `` lamps[i].length == 2 ``
*   <code>0 &lt;= row<sub>i</sub>, col<sub>i</sub> &lt; N</code>
*   `` queries[j].length == 2 ``
*   <code>0 &lt;= row<sub>j</sub>, col<sub>j</sub> &lt; N</code>