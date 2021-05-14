Given an array of strings `` words `` representing an English Dictionary, return _the longest word in_ `` words `` _that can be built one character at a time by other words in_ `` words ``.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["w","wo","wor","worl","world"]
<strong>Output:</strong> "world"
<strong>Explanation:</strong> The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["a","banana","app","appl","ap","apply","apple"]
<strong>Output:</strong> "apple"
<strong>Explanation:</strong> Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 1000 ``
*   `` 1 &lt;= words[i].length &lt;= 30 ``
*   `` words[i] `` consists of lowercase English letters.