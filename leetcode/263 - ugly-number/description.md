An __ugly number__ is a positive integer whose prime factors are limited to `` 2 ``, `` 3 ``, and `` 5 ``.

Given an integer `` n ``, return `` true `` _if_ `` n `` _is an __ugly number___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> 6 = 2 × 3</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> true
<strong>Explanation:</strong> 8 = 2 × 2 × 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> 14 is not ugly since it includes the prime factor 7.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
</pre>

&nbsp;

__Constraints:__

*   <code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code>