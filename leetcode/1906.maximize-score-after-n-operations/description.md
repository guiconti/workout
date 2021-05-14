You are given `` nums ``, an array of positive integers of size `` 2 * n ``. You must perform `` n `` operations on this array.

In the <code>i<sup>th</sup></code> operation __(1-indexed)__, you will:

*   Choose two elements, `` x `` and `` y ``.
*   Receive a score of `` i * gcd(x, y) ``.
*   Remove `` x `` and `` y `` from `` nums ``.

Return _the maximum score you can receive after performing _`` n ``_ operations._

The function `` gcd(x, y) `` is the greatest common divisor of `` x `` and `` y ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,4,6,8]
<strong>Output:</strong> 11
<strong>Explanation:</strong>&nbsp;The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6]
<strong>Output:</strong> 14
<strong>Explanation:</strong>&nbsp;The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 7 ``
*   `` nums.length == 2 * n ``
*   <code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code>