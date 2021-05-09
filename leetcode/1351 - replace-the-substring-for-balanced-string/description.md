You are given a string containing only 4&nbsp;kinds of characters `` 'Q', `` `` 'W', 'E' `` and&nbsp;`` 'R' ``.

A string is said to be&nbsp;__balanced___&nbsp;_if each of its characters appears&nbsp;`` n/4 `` times where `` n `` is the length of the string.

Return the minimum length of the substring that can be replaced with __any__ other string of the same length to make the original string `` s ``&nbsp;__balanced__.

Return 0 if the string is already __balanced__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "QWER"
<strong>Output:</strong> 0
<strong>Explanation: </strong>s is already balanced.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "QQWE"
<strong>Output:</strong> 1
<strong>Explanation: </strong>We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "QQQW"
<strong>Output:</strong> 2
<strong>Explanation: </strong>We can replace the first "QQ" to "ER". 
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "QQQQ"
<strong>Output:</strong> 3
<strong>Explanation: </strong>We can replace the last 3 'Q' to make s = "QWER".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` s.length `` is a multiple of `` 4 ``
*   `` s&nbsp; ``contains only `` 'Q' ``, `` 'W' ``, `` 'E' `` and&nbsp;`` 'R' ``.