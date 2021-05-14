The demons had captured the princess and imprisoned her in __the bottom-right corner__ of a `` dungeon ``. The `` dungeon `` consists of `` m x n `` rooms laid out in a 2D grid. Our valiant knight was initially positioned in __the top-left room__ and must fight his way through `` dungeon `` to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to `` 0 `` or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only __rightward__ or __downward__ in each step.

Return _the knight's minimum initial health so that he can rescue the princess_.

__Note__ that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/13/dungeon-grid-1.jpg" style="width: 253px; height: 253px;"/>

<pre>
<strong>Input:</strong> dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-&gt; RIGHT -&gt; DOWN -&gt; DOWN.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> dungeon = [[0]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` m == dungeon.length ``
*   `` n == dungeon[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   `` -1000 &lt;= dungeon[i][j] &lt;= 1000 ``