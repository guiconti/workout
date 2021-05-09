There is a room with `` n `` bulbs labeled from `` 1 `` to `` n `` that all are turned on initially, and __four buttons__ on the wall. Each of the four buttons has a different functionality where:

*   __Button 1:__ Flips the status of all the bulbs.
*   __Button 2:__ Flips the status of all the bulbs with even labels (i.e., `` 2, 4, ... ``).
*   __Button 3:__ Flips the status of all the bulbs with odd labels (i.e., `` 1, 3, ... ``).
*   __Button 4:__ Flips the status of all the bulbs with a label `` j = 3k + 1 `` where `` k = 0, 1, 2, ... `` (i.e., `` 1, 4, 7, 10, ... ``).

You will press one of the four mentioned buttons exactly `` presses `` times.

Given the two integers `` n `` and `` presses ``, return _the number of __different statuses__ after pressing the four buttons __exactly__ _`` presses ``_ times_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1, presses = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> Status can be: [on], [off].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, presses = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> Status can be: [on, off], [off, on], [off, off].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3, presses = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 1000 ``
*   `` 0 &lt;= presses &lt;= 1000 ``