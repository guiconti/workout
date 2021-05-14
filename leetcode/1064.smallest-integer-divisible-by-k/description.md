Given a positive integer `` K ``, you need to find the __length__ of the __smallest__ positive integer `` N `` such that `` N `` is divisible by `` K ``, and `` N `` only contains the digit `` 1 ``.

Return _the __length__ of _`` N ``. If there is no such `` N ``, return -1.

__Note:__ `` N `` may not fit in a 64-bit signed integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> K = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest answer is N = 1, which has length 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> K = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no such positive integer N divisible by 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> K = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The smallest answer is N = 111, which has length 3.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= K &lt;= 10<sup>5</sup></code>