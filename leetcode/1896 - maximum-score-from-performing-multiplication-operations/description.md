You are given two integer arrays `` nums `` and `` multipliers ``__ __of size `` n `` and `` m `` respectively, where `` n &gt;= m ``. The arrays are __1-indexed__.

You begin with a score of `` 0 ``. You want to perform __exactly__ `` m `` operations. On the <code>i<sup>th</sup></code> operation __(1-indexed)__, you will:

*   Choose one integer `` x `` from __either the start or the end __of the array `` nums ``.
*   Add `` multipliers[i] * x `` to your score.
*   Remove `` x `` from the array `` nums ``.

Return _the __maximum__ score after performing _`` m `` _operations._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3], multipliers = [3,2,1]
<strong>Output:</strong> 14
<strong>Explanation:</strong>&nbsp;An optimal solution is as follows:
- Choose from the end, [1,2,<strong><u>3</u></strong>], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,<strong><u>2</u></strong>], adding 2 * 2 = 4 to the score.
- Choose from the end, [<strong><u>1</u></strong>], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
<strong>Output:</strong> 102
<strong>Explanation: </strong>An optimal solution is as follows:
- Choose from the start, [<u><strong>-5</strong></u>,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [<strong><u>-3</u></strong>,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [<strong><u>-3</u></strong>,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,<strong><u>1</u></strong>], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,<strong><u>7</u></strong>], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   `` m == multipliers.length ``
*   <code>1 &lt;= m &lt;= 10<sup>3</sup></code>
*   <code>m &lt;= n &lt;= 10<sup>5</sup></code>``   ``
*   `` -1000 &lt;= nums[i], multipliers[i] &lt;= 1000 ``