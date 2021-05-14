Given two strings `` s `` and `` t ``, check if `` s `` is a __subsequence__ of `` t ``.

A __subsequence__ of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `` "ace" `` is a subsequence of `` "abcde" `` while `` "aec" `` is not).

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length &lt;= 100 ``
*   <code>0 &lt;= t.length &lt;= 10<sup>4</sup></code>
*   `` s `` and `` t ``&nbsp;consist&nbsp;only of lowercase English letters.

&nbsp;
__Follow up:__ If there are lots of incoming `` s ``, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if `` t `` has its subsequence. In this scenario, how would you change your code?