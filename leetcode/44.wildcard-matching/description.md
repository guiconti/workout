Given an input string (`` s ``) and a pattern (`` p ``), implement wildcard pattern matching with support for `` '?' `` and `` '*' `` where:

*   `` '?' `` Matches any single character.
*   `` '*' `` Matches any sequence of characters (including the empty sequence).

The matching should cover the __entire__ input string (not partial).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aa", p = "a"
<strong>Output:</strong> false
<strong>Explanation:</strong> "a" does not match the entire string "aa".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aa", p = "*"
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;'*' matches any sequence.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "cb", p = "?a"
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;'?' matches 'c', but the second letter is 'a', which does not match 'b'.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "adceb", p = "*a*b"
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "acdcb", p = "a*c?b"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length, p.length &lt;= 2000 ``
*   `` s `` contains only lowercase English letters.
*   `` p `` contains only lowercase English letters, `` '?' `` or `` '*' ``.