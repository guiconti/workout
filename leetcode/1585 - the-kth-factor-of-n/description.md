Given two positive integers `` n `` and `` k ``.

A factor of an integer `` n `` is defined as an integer `` i `` where `` n % i == 0 ``.

Consider a list of all factors of `` n ``&nbsp;sorted in __ascending order__, return _the _`` kth ``_ factor_ in this list or return __-1__ if `` n `` has less than&nbsp;`` k `` factors.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 12, k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 7, k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Factors list is [1, 7], the 2nd factor is 7.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4, k = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> Factors list is [1], the 1st factor is 1.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 1000, k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= n &lt;= 1000 ``