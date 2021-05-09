You are given a string `` text `` of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that `` text `` __contains at least one word__.

Rearrange the spaces so that there is an __equal__ number of spaces between every pair of adjacent words and that number is __maximized__. If you cannot redistribute all the spaces equally, place the __extra spaces at the end__, meaning the returned string should be the same length as `` text ``.

Return _the string after rearranging the spaces_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text = "  this   is  a sentence "
<strong>Output:</strong> "this   is   a   sentence"
<strong>Explanation: </strong>There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text = " practice   makes   perfect"
<strong>Output:</strong> "practice   makes   perfect "
<strong>Explanation:</strong>&nbsp;There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text = "hello   world"
<strong>Output:</strong> "hello   world"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> text = "  walks  udp package   into  bar a"
<strong>Output:</strong> "walks  udp  package  into  bar  a "
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> text = "a"
<strong>Output:</strong> "a"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= text.length &lt;= 100 ``
*   `` text ``&nbsp;consists of lowercase English letters and&nbsp;`` ' ' ``.
*   `` text ``&nbsp;contains at least one word.