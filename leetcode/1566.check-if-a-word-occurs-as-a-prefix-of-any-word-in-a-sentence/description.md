Given a `` sentence ``&nbsp;that consists of some words separated by a&nbsp;__single space__, and a `` searchWord ``.

You have to check if `` searchWord `` is a prefix of any word in `` sentence ``.

Return _the index of the word_ in `` sentence `` where `` searchWord `` is a prefix of this word (__1-indexed__).

If `` searchWord `` is&nbsp;a prefix of more than one word, return the index of the first word __(minimum index)__. If there is no such word return __-1__.

A __prefix__ of a string&nbsp;`` S `` is any leading contiguous substring of `` S ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> sentence = "i love eating burger", searchWord = "burg"
<strong>Output:</strong> 4
<strong>Explanation:</strong> "burg" is prefix of "burger" which is the 4th word in the sentence.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> sentence = "this problem is an easy problem", searchWord = "pro"
<strong>Output:</strong> 2
<strong>Explanation:</strong> "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> sentence = "i am tired", searchWord = "you"
<strong>Output:</strong> -1
<strong>Explanation:</strong> "you" is not a prefix of any word in the sentence.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> sentence = "i use triple pillow", searchWord = "pill"
<strong>Output:</strong> 4
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> sentence = "hello from the other side", searchWord = "they"
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= sentence.length &lt;= 100 ``
*   `` 1 &lt;= searchWord.length &lt;= 10 ``
*   `` sentence `` consists of lowercase English letters and spaces.
*   `` searchWord ``&nbsp;consists of lowercase English letters.