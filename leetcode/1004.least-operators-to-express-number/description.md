Given a single positive integer `` x ``, we will write an expression of the form `` x (op1) x (op2) x (op3) x ... `` where each operator `` op1 ``, `` op2 ``, etc. is either addition, subtraction, multiplication, or division (`` + ``, `` - ``, `` * ``, or `` /) ``. For example, with `` x = 3 ``, we might write `` 3 * 3 / 3 + 3 - 3 `` which is a value of 

<font face="monospace">3</font>

.

When writing such an expression, we adhere to the following conventions:

*   The division operator (`` / ``) returns rational numbers.
*   There are no parentheses placed anywhere.
*   We use the usual order of operations: multiplication and division happen before addition and subtraction.
*   It is not allowed to use the unary negation operator (`` - ``). For example, "`` x - x ``" is a valid expression as it only uses subtraction, but "`` -x + x ``" is not because it uses negation.

We would like to write an expression with the least number of operators such that the expression equals the given `` target ``. Return the least number of operators used.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> x = 3, target = 19
<strong>Output:</strong> 5
<strong>Explanation:</strong> 3 * 3 + 3 * 3 + 3 / 3.
The expression contains 5 operations.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> x = 5, target = 501
<strong>Output:</strong> 8
<strong>Explanation:</strong> 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
The expression contains 8 operations.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> x = 100, target = 100000000
<strong>Output:</strong> 3
<strong>Explanation:</strong> 100 * 100 * 100 * 100.
The expression contains 3 operations.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= x &lt;= 100 ``
*   <code>1 &lt;= target &lt;= 2 * 10<sup>8</sup></code>