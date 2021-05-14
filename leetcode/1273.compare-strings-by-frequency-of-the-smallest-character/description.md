Let the function `` f(s) `` be the __frequency of the lexicographically smallest character__ in a non-empty string `` s ``. For example, if `` s = "dcce" `` then `` f(s) = 2 `` because the lexicographically smallest character is `` 'c' ``, which has a frequency of 2.

You are given an array of strings `` words `` and another array of query strings `` queries ``. For each query `` queries[i] ``, count the __number of words__ in `` words `` such that `` f(queries[i]) `` &lt; `` f(W) `` for each `` W `` in `` words ``.

Return _an integer array _`` answer ``_, where each _`` answer[i] ``_ is the answer to the _<code>i<sup>th</sup></code>_ query_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> queries = ["cbd"], words = ["zaaaz"]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") &lt; f("zaaaz").
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> On the first query only f("bbb") &lt; f("aaaa"). On the second query both f("aaa") and f("aaaa") are both &gt; f("cc").
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= queries.length &lt;= 2000 ``
*   `` 1 &lt;= words.length &lt;= 2000 ``
*   `` 1 &lt;= queries[i].length, words[i].length &lt;= 10 ``
*   `` queries[i][j] ``, `` words[i][j] `` consist of lowercase English letters.