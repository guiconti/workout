A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank">__perfect number__</a> is a __positive integer__ that is equal to the sum of its __positive divisors__, excluding the number itself. A __divisor__ of an integer `` x `` is an integer that can divide `` x `` evenly.

Given an integer `` n ``, return `` true ``_ if _`` n ``_ is a perfect number, otherwise return _`` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 28
<strong>Output:</strong> true
<strong>Explanation:</strong> 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 6
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = 496
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> num = 8128
<strong>Output:</strong> true
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> num = 2
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= num &lt;= 10<sup>8</sup></code>