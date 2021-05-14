Given a string containing just the characters `` '(' `` and `` ')' ``, find the length of the longest valid (well-formed) parentheses substring.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "(()"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is "()".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = ")()())"
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is "()()".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code>
*   `` s[i] `` is `` '(' ``, or `` ')' ``.