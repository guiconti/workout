Given a string `` num `` representing __the digits__ of&nbsp;a very large integer and an integer `` k ``.

You are allowed to swap any two adjacent digits of the integer __at most__ `` k `` times.

Return _the minimum integer_ you can obtain also as a string.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg" style="width: 500px; height: 40px;"/>

<pre>
<strong>Input:</strong> num = "4321", k = 4
<strong>Output:</strong> "1342"
<strong>Explanation:</strong> The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = "100", k = 1
<strong>Output:</strong> "010"
<strong>Explanation:</strong> It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = "36789", k = 1000
<strong>Output:</strong> "36789"
<strong>Explanation:</strong> We can keep the number without any swaps.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> num = "22", k = 22
<strong>Output:</strong> "22"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> num = "9438957234785635408", k = 23
<strong>Output:</strong> "0345989723478563548"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= num.length &lt;= 30000 ``
*   `` num `` contains __digits__ only and doesn't have __leading zeros__.
*   `` 1 &lt;= k &lt;= 10^9 ``