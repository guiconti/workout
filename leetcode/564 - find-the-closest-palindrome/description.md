Given a string `` n `` representing an integer, return _the closest integer (not including itself), which is a palindrome_. If there is a tie, return ___the smaller one___.

The closest is defined as the absolute difference minimized between two integers.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = "123"
<strong>Output:</strong> "121"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = "1"
<strong>Output:</strong> "0"
<strong>Explanation:</strong> 0 and 2 are the closest palindromes but we return the smallest which is 0.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n.length &lt;= 18 ``
*   `` n `` consists of only digits.
*   `` n `` does not have leading zeros.
*   `` n `` is representing an integer in the range <code>[1, 10<sup>18</sup> - 1]</code>.