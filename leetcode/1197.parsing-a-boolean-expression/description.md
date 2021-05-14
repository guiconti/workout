Return the result of evaluating a given boolean `` expression ``, represented as a string.

An expression can either be:

*   `` "t" ``, evaluating to `` True ``;
*   `` "f" ``, evaluating to `` False ``;
*   `` "!(expr)" ``, evaluating to the logical NOT of the inner expression `` expr ``;
*   `` "&amp;(expr1,expr2,...)" ``, evaluating to the logical AND of 2 or more inner expressions `` expr1, expr2, ... ``;
*   `` "|(expr1,expr2,...)" ``, evaluating to the logical OR of 2 or more inner expressions `` expr1, expr2, ... ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> expression = "!(f)"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> expression = "|(f,t)"
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> expression = "&amp;(t,f)"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> expression = "|(&amp;(t,f,t),!(t))"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= expression.length &lt;= 20000 ``
*   `` expression[i] ``&nbsp;consists of characters in `` {'(', ')', '&amp;', '|', '!', 't', 'f', ','} ``.
*   `` expression `` is a valid expression representing a boolean, as given in the description.