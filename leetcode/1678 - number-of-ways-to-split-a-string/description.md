Given a binary string `` s `` (a string consisting only of '0's and '1's),&nbsp;we can split `` s ``&nbsp;into 3 __non-empty__ strings s1, s2, s3 (s1+ s2+ s3 = s).

Return the number of ways `` s `` can be split such that the number of&nbsp;characters '1' is the same in s1, s2, and s3.

Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;10^9 + 7.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "10101"
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "1001"
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "0000"
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "100100010100110"
<strong>Output:</strong> 12
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= s.length &lt;= 10^5 ``
*   `` s[i] `` is `` '0' ``&nbsp;or&nbsp;`` '1' ``.