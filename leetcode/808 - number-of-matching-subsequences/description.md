Given a string `` s `` and an array of strings `` words ``, return _the number of_ `` words[i] `` _that is a subsequence of_ `` s ``.

A __subsequence__ of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

*   For example, `` "ace" `` is a subsequence of `` "abcde" ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abcde", words = ["a","bb","acd","ace"]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three strings in words that are a subsequence of s: "a", "acd", "ace".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code>
*   `` 1 &lt;= words.length &lt;= 5000 ``
*   `` 1 &lt;= words[i].length &lt;= 50 ``
*   `` s `` and `` words[i] `` consist of only lowercase English letters.