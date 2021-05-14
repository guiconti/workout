Given a list of words, each word consists of English lowercase letters.

Let's say `` word1 `` is a predecessor of `` word2 `` if and only if we can add exactly one letter anywhere in `` word1 `` to make it equal to `` word2 ``. For example, `` "abc" `` is a predecessor of `` "abac" ``.

A _word chain _is a sequence of words `` [word_1, word_2, ..., word_k] `` with `` k &gt;= 1 ``, where `` word_1 `` is a predecessor of `` word_2 ``, `` word_2 `` is a predecessor of `` word_3 ``, and so on.

Return the longest possible length of a word chain with words chosen from the given list of `` words ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["a","b","ba","bca","bda","bdca"]
<strong>Output:</strong> 4
<strong>Explanation</strong>: One of the longest word chain is "a","ba","bda","bdca".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 1000 ``
*   `` 1 &lt;= words[i].length &lt;= 16 ``
*   `` words[i] `` only consists of English lowercase letters.