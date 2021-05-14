Given two strings `` word1 `` and `` word2 ``, return _the minimum number of operations required to convert `` word1 `` to `` word2 ``_.

You have the following three operations permitted on a word:

*   Insert a character
*   Delete a character
*   Replace a character

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = "horse", word2 = "ros"
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace 'h' with 'r')
rorse -&gt; rose (remove 'r')
rose -&gt; ros (remove 'e')
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = "intention", word2 = "execution"
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove 't')
inention -&gt; enention (replace 'i' with 'e')
enention -&gt; exention (replace 'n' with 'x')
exention -&gt; exection (replace 'n' with 'c')
exection -&gt; execution (insert 'u')
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= word1.length, word2.length &lt;= 500 ``
*   `` word1 `` and `` word2 `` consist of lowercase English letters.