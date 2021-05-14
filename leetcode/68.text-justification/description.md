Given an array of words and a width&nbsp;_maxWidth_, format the text such that each line has exactly _maxWidth_ characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `` ' ' `` when necessary so that each line has exactly _maxWidth_ characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no __extra__ space is inserted between words.

__Note:__

*   A word is defined as a character sequence consisting&nbsp;of non-space characters only.
*   Each word's length is&nbsp;guaranteed to be greater than 0 and not exceed _maxWidth_.
*   The input array `` words ``&nbsp;contains at least one word.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; &nbsp;"This &nbsp; &nbsp;is &nbsp; &nbsp;an",
&nbsp; &nbsp;"example &nbsp;of text",
&nbsp; &nbsp;"justification. &nbsp;"
]</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
<strong>Output:</strong>
[
&nbsp; "What &nbsp; must &nbsp; be",
&nbsp; "acknowledgment &nbsp;",
&nbsp; "shall be &nbsp; &nbsp; &nbsp; &nbsp;"
]
<strong>Explanation:</strong> Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
<strong>Output:</strong>
[
&nbsp; "Science &nbsp;is &nbsp;what we",
  "understand &nbsp; &nbsp; &nbsp;well",
&nbsp; "enough to explain to",
&nbsp; "a &nbsp;computer. &nbsp;Art is",
&nbsp; "everything &nbsp;else &nbsp;we",
&nbsp; "do &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"
]</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 300 ``
*   `` 1 &lt;= words[i].length &lt;= 20 ``
*   `` words[i] `` consists of only English letters and symbols.
*   `` 1 &lt;= maxWidth &lt;= 100 ``
*   `` words[i].length &lt;= maxWidth ``