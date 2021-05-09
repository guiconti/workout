You are given four integers, `` m ``, `` n ``, `` introvertsCount ``, and `` extrovertsCount ``. You have an `` m x n `` grid, and there are two types of people: introverts and extroverts. There are `` introvertsCount `` introverts and `` extrovertsCount `` extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you __do not__ have to have all the people living in the grid.

The __happiness__ of each person is calculated as follows:

*   Introverts __start__ with `` 120 `` happiness and __lose__ `` 30 `` happiness for each neighbor (introvert or extrovert).
*   Extroverts __start__ with `` 40 `` happiness and __gain__ `` 20 `` happiness for each neighbor (introvert or extrovert).

Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The __grid happiness__ is the __sum__ of each person's happiness. Return_ the __maximum possible grid happiness__._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/grid_happiness.png" style="width: 261px; height: 121px;"/>

<pre>
<strong>Input:</strong> m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
<strong>Output:</strong> 240
<strong>Explanation:</strong> Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
<strong>Output:</strong> 260
<strong>Explanation:</strong> Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
- Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
- Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
- Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
The grid happiness is 90 + 80 + 90 = 260.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
<strong>Output:</strong> 240
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= m, n &lt;= 5 ``
*   `` 0 &lt;= introvertsCount, extrovertsCount &lt;= min(m * n, 6) ``