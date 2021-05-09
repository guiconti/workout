Given a parentheses string `` s `` containing only the characters `` '(' `` and `` ')' ``. A parentheses string is __balanced__ if:

*   Any left parenthesis&nbsp;`` '(' ``&nbsp;must have a corresponding two consecutive right parenthesis&nbsp;`` '))' ``.
*   Left parenthesis&nbsp;`` '(' ``&nbsp;must go before the corresponding two&nbsp;consecutive right parenthesis&nbsp;`` '))' ``.

In other words, we treat `` '(' `` as openning parenthesis and `` '))' `` as closing parenthesis.

For example, `` "())" ``, `` "())(())))" `` and `` "(())())))" `` are&nbsp;balanced, `` ")()" ``, `` "()))" `` and `` "(()))" `` are not balanced.

You can insert the characters `` '(' `` and `` ')' `` at any position of the string to balance it if needed.

Return _the minimum number of insertions_ needed to make `` s `` balanced.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "(()))"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "())"
<strong>Output:</strong> 0
<strong>Explanation:</strong> The string is already balanced.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "))())("
<strong>Output:</strong> 3
<strong>Explanation:</strong> Add '(' to match the first '))', Add '))' to match the last '('.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "(((((("
<strong>Output:</strong> 12
<strong>Explanation:</strong> Add 12 ')' to balance the string.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = ")))))))"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Add 4 '(' at the beginning of the string and one ')' at the end. The string becomes "(((())))))))".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` s `` consists of `` '(' `` and `` ')' `` only.