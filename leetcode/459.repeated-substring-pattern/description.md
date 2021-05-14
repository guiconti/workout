Given a string `` s ``, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abab"
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring "ab" twice.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aba"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "abcabcabcabc"
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring "abc" four times or the substring "abcabc" twice.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s `` consists of lowercase English letters.