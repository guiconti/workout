There is a __3 lane road__ of length `` n `` that consists of `` n + 1 `` __points__ labeled from `` 0 `` to `` n ``. A frog __starts__ at point `` 0 `` in the __second __lane__ __and wants to jump to point `` n ``. However, there could be obstacles along the way.

You are given an array `` obstacles `` of length `` n + 1 `` where each `` obstacles[i] `` (__ranging from 0 to 3__) describes an obstacle on the lane `` obstacles[i] `` at point `` i ``. If `` obstacles[i] == 0 ``, there are no obstacles at point `` i ``. There will be __at most one__ obstacle in the 3 lanes at each point.

*   For example, if `` obstacles[2] == 1 ``, then there is an obstacle on lane 1 at point 2.

The frog can only travel from point `` i `` to point `` i + 1 `` on the same lane if there is not an obstacle on the lane at point `` i + 1 ``. To avoid obstacles, the frog can also perform a __side jump__ to jump to __another__ lane (even if they are not adjacent) at the __same__ point if there is no obstacle on the new lane.

*   For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.

Return_ the __minimum number of side jumps__ the frog needs to reach __any lane__ at point n starting from lane `` 2 `` at point 0._

__Note:__ There will be no obstacles on points `` 0 `` and `` n ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex1.png" style="width: 500px; height: 244px;"/>

<pre>
<strong>Input:</strong> obstacles = [0,1,2,3,0]
<strong>Output:</strong> 2 
<strong>Explanation:</strong> The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex2.png" style="width: 500px; height: 196px;"/>

<pre>
<strong>Input:</strong> obstacles = [0,1,1,3,3,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no obstacles on lane 2. No side jumps are required.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex3.png" style="width: 500px; height: 196px;"/>

<pre>
<strong>Input:</strong> obstacles = [0,2,1,0,3,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The optimal solution is shown by the arrows above. There are 2 side jumps.
</pre>

&nbsp;

__Constraints:__

*   `` obstacles.length == n + 1 ``
*   <code>1 &lt;= n &lt;= 5 * 10<sup>5</sup></code>
*   `` 0 &lt;= obstacles[i] &lt;= 3 ``
*   `` obstacles[0] == obstacles[n] == 0 ``