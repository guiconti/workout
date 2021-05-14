Given two strings `` text1 `` and `` text2 ``, return _the length of their longest __common subsequence__. _If there is no __common subsequence__, return `` 0 ``.

A __subsequence__ of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

*   For example, `` "ace" `` is a subsequence of `` "abcde" ``.

A __common subsequence__ of two strings is a subsequence that is common to both strings.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text1 = "abcde", text2 = "ace" 
<strong>Output:</strong> 3  
<strong>Explanation:</strong> The longest common subsequence is "ace" and its length is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text1 = "abc", text2 = "abc"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest common subsequence is "abc" and its length is 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text1 = "abc", text2 = "def"
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no such common subsequence, so the result is 0.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= text1.length, text2.length &lt;= 1000 ``
*   `` text1 `` and `` text2 `` consist of only lowercase English characters.