Given a 2D array of characters&nbsp;`` grid ``&nbsp;of size `` m x n ``, you need to find if there exists any cycle consisting of the __same value__&nbsp;in&nbsp;`` grid ``.

A cycle is a path of __length 4&nbsp;or more__&nbsp;in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the __same value__ of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle&nbsp;`` (1, 1) -&gt; (1, 2) -&gt; (1, 1) ``&nbsp;is invalid because from&nbsp;`` (1, 2) ``&nbsp;we visited&nbsp;`` (1, 1) ``&nbsp;which was the last visited cell.

Return&nbsp;`` true ``&nbsp;if any cycle of the same value exists in&nbsp;`` grid ``, otherwise, return&nbsp;`` false ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/1.png" style="width: 231px; height: 152px;"/></strong>

<pre>
<strong>Input:</strong> grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
<strong>Output:</strong> true
<strong>Explanation: </strong>There are two valid cycles shown in different colors in the image below:
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/11.png" style="width: 225px; height: 163px;"/>
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/22.png" style="width: 236px; height: 154px;"/></strong>

<pre>
<strong>Input:</strong> grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
<strong>Output:</strong> true
<strong>Explanation: </strong>There is only one valid cycle highlighted in the image below:
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/2.png" style="width: 229px; height: 157px;"/>
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/3.png" style="width: 183px; height: 120px;"/></strong>

<pre>
<strong>Input:</strong> grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m &lt;= 500 ``
*   `` 1 &lt;= n &lt;= 500 ``
*   `` grid ``&nbsp;consists only of lowercase&nbsp;English letters.