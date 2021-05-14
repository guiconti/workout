Given a string `` s `` and a dictionary of strings `` wordDict ``, add spaces in `` s `` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in __any order__.

__Note__ that the same word in the dictionary may be reused multiple times in the segmentation.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
<strong>Output:</strong> ["cats and dog","cat sand dog"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
<strong>Output:</strong> ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 20 ``
*   `` 1 &lt;= wordDict.length &lt;= 1000 ``
*   `` 1 &lt;= wordDict[i].length &lt;= 10 ``
*   `` s `` and `` wordDict[i] `` consist of only lowercase English letters.
*   All the strings of `` wordDict `` are __unique__.