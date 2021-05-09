There is a room with `` n `` bulbs, numbered from `` 1 `` to `` n ``, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment _k_ (for _k_ from `` 0 `` to `` n - 1 ``), we turn on the `` light[k] `` bulb. A bulb __change&nbsp;color to blue__ only if it is on and all the previous bulbs (to the left)&nbsp;are turned on too.

Return the number of moments in&nbsp;which __all&nbsp;turned on__ bulbs&nbsp;__are blue.__

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/29/sample_2_1725.png" style="width: 575px; height: 300px;"/>

<pre>
<strong>Input:</strong> light = [2,1,3,5,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> All bulbs turned on, are blue at the moment 1, 2 and 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> light = [3,2,4,1,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> All bulbs turned on, are blue at the moment 3, and 4 (index-0).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> light = [4,1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> light = [2,1,4,3,6,5]
<strong>Output:</strong> 3
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> light = [1,2,3,4,5,6]
<strong>Output:</strong> 6
</pre>

&nbsp;

__Constraints:__

*   `` n ==&nbsp;light.length ``
*   `` 1 &lt;= n &lt;= 5 * 10^4 ``
*   `` light `` is a permutation of&nbsp;&nbsp;`` [1, 2, ..., n] ``