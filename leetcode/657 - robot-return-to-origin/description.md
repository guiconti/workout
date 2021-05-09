There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot __ends up at (0, 0)__ after it completes its moves.

The move sequence is represented by a string, and the character moves\[i\] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

__Note__: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> moves = "UD"
<strong>Output:</strong> true
<strong>Explanation</strong>: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> moves = "LL"
<strong>Output:</strong> false
<strong>Explanation</strong>: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> moves = "RRDD"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> moves = "LDRRLRUULR"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= moves.length &lt;= 2 * 10<sup>4</sup></code>
*   `` moves `` only contains the characters `` 'U' ``, `` 'D' ``, `` 'L' `` and `` 'R' ``.