A string is a _valid parentheses string_&nbsp;(denoted VPS) if and only if it consists of `` "(" `` and `` ")" `` characters only, and:

*   It is the empty string, or
*   It can be written as&nbsp;`` AB ``&nbsp;(`` A ``&nbsp;concatenated with&nbsp;`` B ``), where&nbsp;`` A ``&nbsp;and&nbsp;`` B ``&nbsp;are VPS's, or
*   It can be written as&nbsp;`` (A) ``, where&nbsp;`` A ``&nbsp;is a VPS.

We can&nbsp;similarly define the _nesting depth_ `` depth(S) `` of any VPS `` S `` as follows:

*   `` depth("") = 0 ``
*   `` depth(A + B) = max(depth(A), depth(B)) ``, where `` A `` and `` B `` are VPS's
*   `` depth("(" + A + ")") = 1 + depth(A) ``, where `` A `` is a VPS.

For example,&nbsp; `` "" ``,&nbsp;`` "()()" ``, and&nbsp;`` "()(()())" ``&nbsp;are VPS's (with nesting depths 0, 1, and 2), and `` ")(" `` and `` "(()" `` are not VPS's.

&nbsp;

Given a VPS 

<font face="monospace">seq</font>

, split it into two disjoint subsequences `` A `` and `` B ``, such that&nbsp;`` A `` and `` B `` are VPS's (and&nbsp;`` A.length + B.length = seq.length ``).

Now choose __any__ such `` A `` and `` B `` such that&nbsp;`` max(depth(A), depth(B)) `` is the minimum possible value.

Return an `` answer `` array (of length `` seq.length ``) that encodes such a&nbsp;choice of `` A `` and `` B ``:&nbsp; `` answer[i] = 0 `` if `` seq[i] `` is part of `` A ``, else `` answer[i] = 1 ``.&nbsp; Note that even though multiple answers may exist, you may return any of them.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> seq = "(()())"
<strong>Output:</strong> [0,1,1,1,1,0]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> seq = "()(())()"
<strong>Output:</strong> [0,0,0,1,1,0,1,1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= seq.size &lt;= 10000 ``