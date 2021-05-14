We are given an array `` asteroids `` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> asteroids = [5,10,-5]
<strong>Output:</strong> [5,10]
<b>Explanation:</b> The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> asteroids = [8,-8]
<strong>Output:</strong> []
<b>Explanation:</b> The 8 and -8 collide exploding each other.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> asteroids = [10,2,-5]
<strong>Output:</strong> [10]
<b>Explanation:</b> The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> asteroids = [-2,-1,1,2]
<strong>Output:</strong> [-2,-1,1,2]
<b>Explanation:</b> The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= asteroids.length&nbsp;&lt;= 10<sup>4</sup></code>
*   `` -1000 &lt;= asteroids[i] &lt;= 1000 ``
*   `` asteroids[i] != 0 ``