You are given an integer array `` matchsticks `` where `` matchsticks[i] `` is the length of the <code>i<sup>th</sup></code> matchstick. You want to use __all the matchsticks__ to make one square. You __should not break__ any stick, but you can link them up, and each matchstick must be used __exactly one time__.

Return `` true `` if you can make this square and `` false `` otherwise.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg" style="width: 253px; height: 253px;"/>

<pre>
<strong>Input:</strong> matchsticks = [1,1,2,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can form a square with length 2, one side of the square came two sticks with length 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matchsticks = [3,3,3,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot find a way to form a square with all the matchsticks.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= matchsticks.length &lt;= 15 ``
*   <code>0 &lt;= matchsticks[i] &lt;= 10<sup>9</sup></code>