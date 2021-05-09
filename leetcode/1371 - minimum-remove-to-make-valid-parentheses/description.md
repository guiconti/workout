Given a string 

<font face="monospace">s</font>

&nbsp;of&nbsp;`` '(' ``&nbsp;,&nbsp;`` ')' ``&nbsp;and lowercase English characters.&nbsp;

Your task is to remove the minimum number of parentheses (&nbsp;`` '(' ``&nbsp;or&nbsp;`` ')' ``,&nbsp;in any positions ) so that the resulting _parentheses string_ is valid and return __any__ valid string.

Formally, a _parentheses string_ is valid if and only if:

*   It is the empty string, contains only lowercase characters, or
*   It can be written as&nbsp;`` AB ``&nbsp;(`` A ``&nbsp;concatenated with&nbsp;`` B ``), where&nbsp;`` A ``&nbsp;and&nbsp;`` B ``&nbsp;are valid strings, or
*   It can be written as&nbsp;`` (A) ``, where&nbsp;`` A ``&nbsp;is a valid string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "lee(t(c)o)de)"
<strong>Output:</strong> "lee(t(c)o)de"
<strong>Explanation:</strong> "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "a)b(c)d"
<strong>Output:</strong> "ab(c)d"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "))(("
<strong>Output:</strong> ""
<strong>Explanation:</strong> An empty string is also valid.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "(a(b(c)d)"
<strong>Output:</strong> "a(b(c)d)"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` s[i] ``&nbsp;is one&nbsp;of&nbsp;&nbsp;`` '(' `` , `` ')' `` and&nbsp;lowercase English letters`` . ``