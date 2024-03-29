Given a string `` S ``&nbsp;of digits, such as `` S = "123456579" ``, we can split it into a _Fibonacci-like sequence_&nbsp;`` [123, 456, 579]. ``

Formally, a Fibonacci-like sequence is a list&nbsp;`` F `` of non-negative integers such that:

*   `` 0 &lt;= F[i] &lt;= 2^31 - 1 ``, (that is,&nbsp;each integer fits a 32-bit signed integer type);
*   `` F.length &gt;= 3 ``;
*   and``  F[i] + F[i+1] = F[i+2]  ``for all `` 0 &lt;= i &lt; F.length - 2 ``.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `` S ``, or return `` [] `` if it cannot be done.

__Example 1:__

<pre>
<strong>Input: </strong>"123456579"
<strong>Output: </strong>[123,456,579]
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>"11235813"
<strong>Output: </strong>[1,1,2,3,5,8,13]
</pre>

__Example 3:__

<pre>
<strong>Input: </strong>"112358130"
<strong>Output: </strong>[]
<strong>Explanation: </strong>The task is impossible.
</pre>

__Example 4:__

<pre>
<strong>Input: </strong>"0123"
<strong>Output: </strong>[]
<strong>Explanation: </strong>Leading zeroes are not allowed, so "01", "2", "3" is not valid.
</pre>

__Example 5:__

<pre>
<strong>Input: </strong>"1101111"
<strong>Output: </strong>[110, 1, 111]
<strong>Explanation: </strong>The output [11, 0, 11, 11] would also be accepted.
</pre>

__Note: __

1.   `` 1 &lt;= S.length&nbsp;&lt;= 200 ``
2.   `` S `` contains only digits.