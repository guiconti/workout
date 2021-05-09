Given an integer array of `` digits ``,&nbsp;return the largest multiple of __three__ that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> digits = [8,1,9]
<strong>Output:</strong> "981"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> digits = [8,6,7,1,0]
<strong>Output:</strong> "8760"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> digits = [1]
<strong>Output:</strong> ""
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> digits = [0,0,0,0,0,0]
<strong>Output:</strong> "0"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= digits.length &lt;= 10^4 ``
*   `` 0 &lt;= digits[i] &lt;= 9 ``
*   The returning answer must not contain unnecessary leading zeros.