A __super ugly number__ is a positive integer whose prime factors are in the array `` primes ``.

Given an integer `` n `` and an array of integers `` primes ``, return _the_ <code>n<sup>th</sup></code> ___super ugly number___.

The <code>n<sup>th</sup></code> __super ugly number__ is __guaranteed__ to fit in a __32-bit__ signed integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 12, primes = [2,7,13,19]
<strong>Output:</strong> 32
<strong>Explanation:</strong> [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1, primes = [2,3,5]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>6</sup></code>
*   `` 1 &lt;= primes.length &lt;= 100 ``
*   `` 2 &lt;= primes[i] &lt;= 1000 ``
*   `` primes[i] `` is __guaranteed__ to be a prime number.
*   All the values of `` primes `` are __unique__ and sorted in __ascending order__.