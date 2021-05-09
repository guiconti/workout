Given a sentence&nbsp;`` text `` (A&nbsp;_sentence_&nbsp;is a string of space-separated words) in the following format:

*   First letter is in upper case.
*   Each word in `` text `` are separated by a single space.

Your task is to rearrange the words in text such that&nbsp;all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text&nbsp;following the format shown above.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text = "Leetcode is cool"
<strong>Output:</strong> "Is cool leetcode"
<strong>Explanation: </strong>There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text = "Keep calm and code on"
<strong>Output:</strong> "On and keep calm code"
<strong>Explanation: </strong>Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text = "To be or not to be"
<strong>Output:</strong> "To be or to be not"
</pre>

&nbsp;

__Constraints:__

*   `` text `` begins with a capital letter and then contains lowercase letters and single space between words.
*   `` 1 &lt;= text.length &lt;= 10^5 ``