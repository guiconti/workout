Given two strings `` s `` and `` t ``, _determine if they are isomorphic_.

Two strings `` s `` and `` t `` are isomorphic if the characters in `` s `` can be replaced to get `` t ``.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "egg", t = "add"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "foo", t = "bar"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre><strong>Input:</strong> s = "paper", t = "title"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code>
*   `` t.length == s.length ``
*   `` s `` and `` t `` consist of any valid ascii character.