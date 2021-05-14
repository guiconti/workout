You are working in a ball factory where you have `` n `` balls numbered from `` lowLimit `` up to `` highLimit `` __inclusive__ (i.e., `` n == highLimit - lowLimit + 1 ``), and an infinite number of boxes numbered from `` 1 `` to `` infinity ``.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number `` 321 `` will be put in the box number `` 3 + 2 + 1 = 6 `` and the ball number `` 10 `` will be put in the box number `` 1 + 0 = 1 ``.

Given two integers `` lowLimit `` and `` highLimit ``, return_ the number of balls in the box with the most balls._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> lowLimit = 1, highLimit = 10
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> lowLimit = 5, highLimit = 15
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> lowLimit = 19, highLimit = 28
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= lowLimit &lt;= highLimit &lt;= 10<sup>5</sup></code>