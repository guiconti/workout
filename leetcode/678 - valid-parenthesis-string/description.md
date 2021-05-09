Given a string `` s `` containing only three types of characters: `` '(' ``, `` ')' `` and `` '*' ``, return `` true `` _if_ `` s `` _is __valid___.

The following rules define a __valid__ string:

*   Any left parenthesis `` '(' `` must have a corresponding right parenthesis `` ')' ``.
*   Any right parenthesis `` ')' `` must have a corresponding left parenthesis `` '(' ``.
*   Left parenthesis `` '(' `` must go before the corresponding right parenthesis `` ')' ``.
*   `` '*' `` could be treated as a single right parenthesis `` ')' `` or a single left parenthesis `` '(' `` or an empty string `` "" ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre><strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s[i] `` is `` '(' ``, `` ')' `` or `` '*' ``.