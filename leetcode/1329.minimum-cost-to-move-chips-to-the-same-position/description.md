We have `` n `` chips, where the position of the <code>i<sup>th</sup></code> chip is `` position[i] ``.

We need to move all the chips to __the same position__. In one step, we can change the position of the <code>i<sup>th</sup></code> chip from `` position[i] `` to:

*   `` position[i] + 2 `` or `` position[i] - 2 `` with `` cost = 0 ``.
*   `` position[i] + 1 `` or `` position[i] - 1 `` with `` cost = 1 ``.

Return _the minimum cost_ needed to move all the chips to the same position.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg" style="width: 750px; height: 217px;"/>

<pre>
<strong>Input:</strong> position = [1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg" style="width: 750px; height: 306px;"/>

<pre>
<strong>Input:</strong> position = [2,2,2,3,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> position = [1,1000000000]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= position.length &lt;= 100 ``
*   `` 1 &lt;= position[i] &lt;= 10^9 ``