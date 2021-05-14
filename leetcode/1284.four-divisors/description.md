Given an integer array `` nums ``, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [21,4,7]
<strong>Output:</strong> 32
<b>Explanation:</b>
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^4 ``
*   `` 1 &lt;= nums[i] &lt;= 10^5 ``