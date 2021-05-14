Given a string `` s `` which represents an expression, _evaluate this expression and return its value_.&nbsp;

The integer division should truncate toward zero.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "3+2*2"
<strong>Output:</strong> 7
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = " 3/2 "
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre><strong>Input:</strong> s = " 3+5 / 2 "
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code>
*   `` s `` consists of integers and operators `` ('+', '-', '*', '/') `` separated by some number of spaces.
*   `` s `` represents __a valid expression__.
*   All the integers in the expression are non-negative integers in the range <code>[0, 2<sup>31</sup> - 1]</code>.
*   The answer is __guaranteed__ to fit in a __32-bit integer__.