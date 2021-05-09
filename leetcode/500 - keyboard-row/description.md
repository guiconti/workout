Given an array of strings `` words ``, return _the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below_.

In the __American keyboard__:

*   the first row consists of the characters `` "qwertyuiop" ``,
*   the second row consists of the characters `` "asdfghjkl" ``, and
*   the third row consists of the characters `` "zxcvbnm" ``.

<img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/keyboard.png" style="width: 800px; max-width: 600px; height: 267px;"/>

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["Hello","Alaska","Dad","Peace"]
<strong>Output:</strong> ["Alaska","Dad"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["omk"]
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["adsdf","sfd"]
<strong>Output:</strong> ["adsdf","sfd"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 20 ``
*   `` 1 &lt;= words[i].length &lt;= 100 ``
*   `` words[i] `` consists of English letters (both lowercase and uppercase).&nbsp;