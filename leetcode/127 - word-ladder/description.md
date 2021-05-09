A __transformation sequence__ from word `` beginWord `` to word `` endWord `` using a dictionary `` wordList `` is a sequence of words <code>beginWord -&gt; s<sub>1</sub> -&gt; s<sub>2</sub> -&gt; ... -&gt; s<sub>k</sub></code> such that:

*   Every adjacent pair of words differs by a single letter.
*   Every <code>s<sub>i</sub></code> for `` 1 &lt;= i &lt;= k `` is in `` wordList ``. Note that `` beginWord `` does not need to be in `` wordList ``.
*   <code>s<sub>k</sub> == endWord</code>

Given two words, `` beginWord `` and `` endWord ``, and a dictionary `` wordList ``, return _the __number of words__ in the __shortest transformation sequence__ from_ `` beginWord `` _to_ `` endWord ``_, or _`` 0 ``_ if no such sequence exists._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> 5
<strong>Explanation:</strong> One shortest transformation sequence is "hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; cog", which is 5 words long.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= beginWord.length &lt;= 10 ``
*   `` endWord.length == beginWord.length ``
*   `` 1 &lt;= wordList.length &lt;= 5000 ``
*   `` wordList[i].length == beginWord.length ``
*   `` beginWord ``, `` endWord ``, and `` wordList[i] `` consist of lowercase English letters.
*   `` beginWord != endWord ``
*   All the words in `` wordList `` are __unique__.