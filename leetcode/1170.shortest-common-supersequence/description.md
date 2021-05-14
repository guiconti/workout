Given two strings `` str1 `` and `` str2 ``,&nbsp;return the shortest string that has both `` str1 ``&nbsp;and `` str2 ``&nbsp;as subsequences.&nbsp;&nbsp;If multiple answers exist, you may return any of them.

_(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen <u>anywhere</u> from T) results in the string S.)_

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>str1 = <span id="example-input-1-1">"abac"</span>, str2 = <span id="example-input-1-2">"cab"</span>
<strong>Output: </strong><span id="example-output-1">"cabac"</span>
<strong>Explanation: </strong>
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= str1.length, str2.length &lt;= 1000 ``
2.   `` str1 `` and `` str2 `` consist of lowercase English letters.