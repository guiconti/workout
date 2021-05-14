Given a `` pattern `` and a string `` s ``, find if `` s ``&nbsp;follows the same pattern.

Here __follow__ means a full match, such that there is a bijection between a letter in `` pattern `` and a __non-empty__ word in `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> pattern = "abba", s = "dog cat cat dog"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> pattern = "abba", s = "dog cat cat fish"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> pattern = "aaaa", s = "dog cat cat dog"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> pattern = "abba", s = "dog dog dog dog"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= pattern.length &lt;= 300 ``
*   `` pattern `` contains only lower-case English letters.
*   `` 1 &lt;= s.length &lt;= 3000 ``
*   `` s `` contains only lower-case English letters and spaces `` ' ' ``.
*   `` s `` __does not contain__ any leading or trailing spaces.
*   All the words in `` s `` are separated by a __single space__.