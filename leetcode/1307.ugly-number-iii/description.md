An __ugly number__ is a positive integer that is divisible by `` a ``, `` b ``, or `` c ``.

Given four integers `` n ``, `` a ``, `` b ``, and `` c ``, return the <code>n<sup>th</sup></code> __ugly number__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3, a = 2, b = 3, c = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong> The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 4, a = 2, b = 3, c = 4
<strong>Output:</strong> 6
<strong>Explanation:</strong> The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 5, a = 2, b = 11, c = 13
<strong>Output:</strong> 10
<strong>Explanation:</strong> The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 1000000000, a = 2, b = 217983653, c = 336916467
<strong>Output:</strong> 1999999984
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n, a, b, c &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= a * b * c &lt;= 10<sup>18</sup></code>
*   It is guaranteed that the result will be in range <code>[1, 2 * 10<sup>9</sup>]</code>.