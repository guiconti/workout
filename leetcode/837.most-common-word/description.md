Given a string `` paragraph `` and a string array of the banned words `` banned ``, return _the most frequent word that is not banned_. It is __guaranteed__ there is __at least one word__ that is not banned, and that the answer is __unique__.

The words in `` paragraph `` are __case-insensitive__ and the answer should be returned in __lowercase__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
<strong>Output:</strong> "ball"
<strong>Explanation:</strong> 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> paragraph = "a.", banned = []
<strong>Output:</strong> "a"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= paragraph.length &lt;= 1000 ``
*   paragraph consists of English letters, space `` ' ' ``, or one of the symbols: `` "!?',;." ``.
*   `` 0 &lt;= banned.length &lt;= 100 ``
*   `` 1 &lt;= banned[i].length &lt;= 10 ``
*   `` banned[i] `` consists of only lowercase English letters.