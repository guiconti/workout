For two strings `` s `` and `` t ``, we say "`` t `` divides `` s ``" if and only if `` s = t + ... + t ``&nbsp; (`` t `` concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string `` x `` such that `` x `` divides both&nbsp;<code><font face="monospace">str1</font></code>&nbsp;and <code><font face="monospace">str2</font></code>.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> str1 = "ABCABC", str2 = "ABC"
<strong>Output:</strong> "ABC"
</pre>

__Example 2:__

<pre><strong>Input:</strong> str1 = "ABABAB", str2 = "ABAB"
<strong>Output:</strong> "AB"
</pre>

__Example 3:__

<pre><strong>Input:</strong> str1 = "LEET", str2 = "CODE"
<strong>Output:</strong> ""
</pre>

__Example 4:__

<pre><strong>Input:</strong> str1 = "ABCDEF", str2 = "ABC"
<strong>Output:</strong> ""
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= str1.length &lt;= 1000 ``
*   `` 1 &lt;= str2.length &lt;= 1000 ``
*   `` str1 ``&nbsp;and `` str2 ``&nbsp;consist of&nbsp;English uppercase letters.