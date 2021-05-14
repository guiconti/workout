Given a binary string `` S `` (a string consisting only of '0' and '1's) and a positive integer `` N ``, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">"0110"</span>, N = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">"0110"</span>, N = <span id="example-input-2-2">4</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= S.length &lt;= 1000 ``
2.   `` 1 &lt;= N &lt;= 10^9 ``