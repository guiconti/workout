A __transformation sequence__ from word `` beginWord `` to word `` endWord `` using a dictionary `` wordList `` is a sequence of words <code>beginWord -&gt; s<sub>1</sub> -&gt; s<sub>2</sub> -&gt; ... -&gt; s<sub>k</sub></code> such that:

*   Every adjacent pair of words differs by a single letter.
*   Every <code>s<sub>i</sub></code> for `` 1 &lt;= i &lt;= k `` is in `` wordList ``. Note that `` beginWord `` does not need to be in `` wordList ``.
*   <code>s<sub>k</sub> == endWord</code>

Given two words, `` beginWord `` and `` endWord ``, and a dictionary `` wordList ``, return _all the __shortest transformation sequences__ from_ `` beginWord `` _to_ `` endWord ``_, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words _<code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
<strong>Explanation:</strong>&nbsp;There are 2 shortest transformation sequences:
"hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; "cog"
"hit" -&gt; "hot" -&gt; "lot" -&gt; "log" -&gt; "cog"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> []
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= beginWord.length &lt;= 5 ``
*   `` endWord.length == beginWord.length ``
*   `` 1 &lt;= wordList.length &lt;= 1000 ``
*   `` wordList[i].length == beginWord.length ``
*   `` beginWord ``, `` endWord ``, and `` wordList[i] `` consist of lowercase English letters.
*   `` beginWord != endWord ``
*   All the words in `` wordList `` are __unique__.