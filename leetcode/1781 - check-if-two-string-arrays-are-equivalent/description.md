Given two string arrays `` word1 `` and `` word2 ``, return_ _`` true ``_ if the two arrays __represent__ the same string, and _`` false ``_ otherwise._

A string is __represented__ by an array if the array elements concatenated __in order__ forms the string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = ["ab", "c"], word2 = ["a", "bc"]
<strong>Output:</strong> true
<strong>Explanation:</strong>
word1 represents string "ab" + "c" -&gt; "abc"
word2 represents string "a" + "bc" -&gt; "abc"
The strings are the same, so return true.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = ["a", "cb"], word2 = ["ab", "c"]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= word1.length, word2.length &lt;= 10<sup>3</sup></code>
*   <code>1 &lt;= word1[i].length, word2[i].length &lt;= 10<sup>3</sup></code>
*   <code>1 &lt;= sum(word1[i].length), sum(word2[i].length) &lt;= 10<sup>3</sup></code>
*   `` word1[i] `` and `` word2[i] `` consist of lowercase letters.