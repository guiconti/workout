You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point `` [0, 0] ``, and you are given a destination point <code>target = [x<sub>target</sub>, y<sub>target</sub>]</code>, which you are trying to get to. There are several ghosts on the map with their starting positions given as an array `` ghosts ``, where <code>ghosts[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the starting position of the <code>i<sup>th</sup></code> ghost. All inputs are __integral coordinates__.

Each turn, you and all the ghosts may independently choose to either __move 1 unit__ in any of the four cardinal directions: north, east, south, or west or __stay still__. All actions happen __simultaneously__.

You escape if and only if you can reach the target __before__ any ghost reaches you. If you reach any square (including the target) at the __same time__ as a ghost, it __does not__ count as an escape.

Return `` true ``_ if it is possible to escape, otherwise return _`` false ``_._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> ghosts = [[1,0],[0,3]], target = [0,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> ghosts = [[1,0]], target = [2,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> ghosts = [[2,0]], target = [1,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The ghost can reach the target at the same time as you.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]], target = [7,7]
<strong>Output:</strong> false
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> ghosts = [[-1,0],[0,1],[-1,0],[0,1],[-1,0]], target = [0,0]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= ghosts.length &lt;= 100 ``
*   `` ghosts[i].length == 2 ``
*   <code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code>
*   There can be __multiple ghosts__ in the same location.
*   `` target.length == 2 ``
*   <code>-10<sup>4</sup> &lt;= x<sub>target</sub>, y<sub>target</sub> &lt;= 10<sup>4</sup></code>