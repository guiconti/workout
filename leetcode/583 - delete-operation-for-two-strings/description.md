Given two strings `` word1 `` and `` word2 ``, return _the minimum number of __steps__ required to make_ `` word1 `` _and_ `` word2 `` _the same_.

In one __step__, you can delete exactly one character in either string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = "sea", word2 = "eat"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = "leetcode", word2 = "etco"
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word1.length, word2.length &lt;= 500 ``
*   `` word1 `` and `` word2 `` consist of only lowercase English letters.