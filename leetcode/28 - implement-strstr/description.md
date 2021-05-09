Implement <a href="http://www.cplusplus.com/reference/cstring/strstr/" target="_blank">strStr()</a>.

Return the index of the first occurrence of needle in haystack, or `` -1 `` if `` needle `` is not part of `` haystack ``.

__Clarification:__

What should we return when `` needle `` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `` needle `` is an empty string. This is consistent to C's&nbsp;<a href="http://www.cplusplus.com/reference/cstring/strstr/" target="_blank">strstr()</a> and Java's&nbsp;<a href="https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)" target="_blank">indexOf()</a>.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> haystack = "hello", needle = "ll"
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre><strong>Input:</strong> haystack = "aaaaa", needle = "bba"
<strong>Output:</strong> -1
</pre>

__Example 3:__

<pre><strong>Input:</strong> haystack = "", needle = ""
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= haystack.length, needle.length &lt;= 5 * 10<sup>4</sup></code>
*   `` haystack `` and&nbsp;`` needle `` consist of only lower-case English characters.