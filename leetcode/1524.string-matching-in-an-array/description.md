Given an array of string `` words ``. Return all strings in `` words `` which is substring of another word in __any__ order.&nbsp;

String `` words[i] `` is substring of `` words[j] ``,&nbsp;if&nbsp;can be obtained removing some characters to left and/or right side of `` words[j] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["mass","as","hero","superhero"]
<strong>Output:</strong> ["as","hero"]
<strong>Explanation:</strong> "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["leetcode","et","code"]
<strong>Output:</strong> ["et","code"]
<strong>Explanation:</strong> "et", "code" are substring of "leetcode".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["blue","green","bu"]
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 100 ``
*   `` 1 &lt;= words[i].length &lt;= 30 ``
*   `` words[i] `` contains only lowercase English letters.
*   It's __guaranteed__&nbsp;that `` words[i] ``&nbsp;will be unique.