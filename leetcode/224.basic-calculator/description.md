Given a string `` s `` representing an expression, implement a basic calculator to evaluate it.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "1 + 1"
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = " 2-1 + 2 "
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "(1+(4+5+2)-3)+(6+8)"
<strong>Output:</strong> 23
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 3&nbsp;* 10<sup>5</sup></code>
*   `` s `` consists of digits, `` '+' ``, `` '-' ``, `` '(' ``, `` ')' ``, and `` ' ' ``.
*   `` s `` represents a valid expression.