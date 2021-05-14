Given an integer `` num ``, find the closest two integers in absolute difference whose product equals&nbsp;`` num + 1 ``&nbsp;or `` num + 2 ``.

Return the two integers in any order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 8
<strong>Output:</strong> [3,3]
<strong>Explanation:</strong> For num + 1 = 9, the closest divisors are 3 &amp; 3, for num + 2 = 10, the closest divisors are 2 &amp; 5, hence 3 &amp; 3 is chosen.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 123
<strong>Output:</strong> [5,25]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = 999
<strong>Output:</strong> [40,25]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= num &lt;= 10^9 ``