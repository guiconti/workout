Given a binary string&nbsp;`` s ``&nbsp;(a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;10^9 + 7.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "0110111"
<strong>Output:</strong> 9
<strong>Explanation: </strong>There are 9 substring in total with only 1's characters.
"1" -&gt; 5 times.
"11" -&gt; 3 times.
"111" -&gt; 1 time.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "101"
<strong>Output:</strong> 2
<strong>Explanation: </strong>Substring "1" is shown 2 times in s.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "111111"
<strong>Output:</strong> 21
<strong>Explanation: </strong>Each substring contains only 1's characters.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "000"
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` s[i] == '0' `` or `` s[i] == '1' ``
*   `` 1 &lt;= s.length &lt;= 10^5 ``