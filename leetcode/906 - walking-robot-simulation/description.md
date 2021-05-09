A robot on an infinite XY-plane starts at point `` (0, 0) `` and faces north. The robot can receive one of three possible types of `` commands ``:

*   `` -2 ``: turn left `` 90 `` degrees,
*   `` -1 ``: turn right `` 90 `` degrees, or
*   `` 1 &lt;= k &lt;= 9 ``: move forward `` k `` units.

Some of the grid squares are `` obstacles ``. The <code>i<sup>th</sup></code> obstacle is at grid point <code>obstacles[i] = (x<sub>i</sub>, y<sub>i</sub>)</code>.

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return _the maximum Euclidean distance that the robot will be from the origin __squared__ (i.e. if the distance is _`` 5 ``_, return _`` 25 ``_)_.

__Note:__

*   North means +Y direction.
*   East means +X direction.
*   South means -Y direction.
*   West means -X direction.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> commands = [4,-1,3], obstacles = []
<strong>Output:</strong> 25
<strong>Explanation:</strong> The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point away from the origin is (3, 4), which is 3<sup>2</sup> + 4<sup>2</sup> = 25 units away.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> commands = [4,-1,4,-2,4], obstacles = [[2,4]]
<strong>Output:</strong> 65
<strong>Explanation:</strong> The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point away from the origin is (1, 8), which is 1<sup>2</sup> + 8<sup>2</sup> = 65 units away.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= commands.length &lt;= 10<sup>4</sup></code>
*   `` commands[i] `` is one of the values in the list `` [-2,-1,1,2,3,4,5,6,7,8,9] ``.
*   <code>0 &lt;= obstacles.length &lt;= 10<sup>4</sup></code>
*   <code>-3 * 10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 3 * 10<sup>4</sup></code>
*   The answer is guaranteed to be less than <code>2<sup>31</sup></code>.