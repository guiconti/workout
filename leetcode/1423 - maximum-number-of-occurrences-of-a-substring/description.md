Given a string `` s ``, return the maximum number of ocurrences of __any__ substring&nbsp;under the following rules:

*   The number of unique characters in the substring must be less than or equal to `` maxLetters ``.
*   The substring size must be between `` minSize `` and `` maxSize ``&nbsp;inclusive.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring "aaa" occur 2 times in the string. It can overlap.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
<strong>Output:</strong> 3
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` 1 &lt;= maxLetters &lt;= 26 ``
*   `` 1 &lt;= minSize &lt;= maxSize &lt;= min(26, s.length) ``
*   `` s `` only contains lowercase English letters.