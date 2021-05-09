Normally, the factorial of a positive integer `` n ``&nbsp;is the product of all positive integers less than or equal to `` n ``.&nbsp; For example, `` factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 ``.

We instead make a _clumsy factorial:_&nbsp;using the integers in decreasing order, we&nbsp;swap out the multiply operations for a fixed rotation of operations:&nbsp;multiply (\*), divide (/), add (+) and subtract (-) in this order.

For example, `` clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1 ``.&nbsp; However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is _floor division_&nbsp;such that&nbsp;`` 10 * 9 / 8 ``&nbsp;equals&nbsp;`` 11 ``.&nbsp; This guarantees the result is&nbsp;an integer.

<code><font face="sans-serif, Arial, Verdana, Trebuchet MS">Implement the&nbsp;</font>clumsy</code>&nbsp;function&nbsp;as defined above: given an integer `` N ``, it returns the clumsy factorial of `` N ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>4
<strong>Output:</strong>&nbsp;7
<strong>Explanation:</strong> 7 = 4 * 3 / 2 + 1
</pre>

__Example 2:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">10
</span><strong>Output: </strong><span id="example-output-1">12
</span><strong>Explanation: </strong>12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= N &lt;= 10000 ``
2.   `` -2^31 &lt;= answer &lt;= 2^31 - 1 ``&nbsp; (The answer is guaranteed to fit within a 32-bit integer.)