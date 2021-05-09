Given a string `` s `` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return _all the possible results_. You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "()())()"
<strong>Output:</strong> ["(())()","()()()"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "(a)())()"
<strong>Output:</strong> ["(a())()","(a)()()"]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = ")("
<strong>Output:</strong> [""]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 25 ``
*   `` s `` consists of lowercase English letters and parentheses `` '(' `` and `` ')' ``.
*   There will be at most `` 20 `` parentheses in `` s ``.