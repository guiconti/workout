On an infinite plane, a robot initially stands at `` (0, 0) `` and faces north. The robot can receive one of three instructions:

*   `` "G" ``: go straight 1 unit;
*   `` "L" ``: turn 90 degrees to the left;
*   `` "R" ``: turn 90 degrees to the right.

The robot performs the `` instructions `` given in order, and repeats them forever.

Return `` true `` if and only if there exists a circle in the plane such that the robot never leaves the circle.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> instructions = "GGLLGG"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> instructions = "GG"
<strong>Output:</strong> false
<strong>Explanation:</strong> The robot moves north indefinitely.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> instructions = "GL"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves from (0, 0) -&gt; (0, 1) -&gt; (-1, 1) -&gt; (-1, 0) -&gt; (0, 0) -&gt; ...</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= instructions.length &lt;= 100 ``
*   `` instructions[i] ``&nbsp;is&nbsp;`` 'G' ``, `` 'L' `` or, `` 'R' ``.