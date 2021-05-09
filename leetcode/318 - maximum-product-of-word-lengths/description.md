Given a string array `` words ``, return _the maximum value of_ `` length(word[i]) * length(word[j]) `` _where the two words do not share common letters_. If no such two words exist, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["abcw","baz","foo","bar","xtfn","abcdef"]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The two words can be "abcw", "xtfn".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["a","ab","abc","d","cd","bcd","abcd"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The two words can be "ab", "cd".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["a","aa","aaa","aaaa"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> No such pair of words.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= words.length &lt;= 1000 ``
*   `` 1 &lt;= words[i].length &lt;= 1000 ``
*   `` words[i] `` consists only of lowercase English letters.